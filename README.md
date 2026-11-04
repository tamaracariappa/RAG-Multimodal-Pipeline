# Multimodal RAG

A retrieval-augmented generation pipeline for PDFs that indexes text, tables and figures, then answers questions from the indexed evidence with page-level citations. When none of the retrieved evidence bears on a question, it declines to answer.

Extraction and embedding run locally on the CPU. Gemini is used only to describe figures at ingest, to grade retrieved evidence and to write answers.

## Key features

- **PDF extraction with PyMuPDF**: text blocks, table grids, embedded raster images and vector drawings (clustered drawing paths rendered as figures). No OCR, Poppler or layout model is required.
- **Figure descriptions**: each figure is sent once to a Gemini vision model, and the description is embedded so that questions about a figure's contents can match it. Set `IMAGE_SUMMARIES=0` to index figures by their surrounding text instead.
- **Table indexing**: flattened table cells are embedded together with the text that introduces the table, and passed to the answer model as HTML.
- **Retrieval**: a LangChain `MultiVectorRetriever` searches embedded chunks in Chroma and returns the full parent records from SQLite.
- **Grounded answers and abstention**: Gemini first grades which retrieved blocks are relevant (corrective RAG), then answers only from those blocks and cites document and page. If no block is kept, the pipeline returns a fixed abstention message.
- **Incremental ingestion**: an unchanged PDF under an unchanged configuration is skipped, and only new or modified records are re-embedded. Several PDFs can share one index.

## Architecture

```
PDF
 └─ PyMuPDF extraction (local)
     ├─ text   → 1000-char chunks
     ├─ tables → cells + lead-in text
     └─ figures (raster + vector) → Gemini vision description
          │
          ▼
 all-MiniLM-L6-v2 embeddings (local CPU)
          │
          ▼
 Chroma (child vectors)  +  SQLite (parent records, ingestion manifest)
          │
          ▼
 Question → MultiVectorRetriever → Gemini relevance grader
          → Gemini answer with citations, or abstain
```

## Tech stack

| Component | Used for |
|---|---|
| [PyMuPDF](https://pymupdf.readthedocs.io/) | Text, table, image and vector-drawing extraction; figure rendering |
| LangChain (`langchain-classic`, `langchain-chroma`, `langchain-text-splitters`, `langchain-huggingface`, `langchain-google-genai`) | Retriever, vector store integration, chunking, model clients |
| `sentence-transformers/all-MiniLM-L6-v2` | Local embeddings (no API key) |
| Google Gemini (`gemini-flash-lite-latest` by default) | Figure descriptions, relevance grading, answer generation |
| Chroma | Persistent vector store |
| SQLite (Python standard library) | Parent document store and ingestion manifest |
| `python-dotenv` | Loads API keys from `.env` |

## Project structure

```
.
├── rag_pipeline.py              # Extraction, indexing, retrieval, grading and answering
├── langchain_multimodal.ipynb   # Staged walkthrough: extraction review → indexing → Q&A
├── evaluate_rag.py              # Scored evaluation against a PDF (live Gemini calls)
├── eval_results.json            # Output of the last evaluation run
├── requirements.txt
├── SETUP.md                     # Detailed Windows setup and tuning reference
└── .gitignore
```

Created at runtime and git-ignored: `.env`, `.venv/`, `chroma_db/`, `rag_state.sqlite3`.

Input PDFs are not included in the repository. Put your own PDF in the project root.

## Setup

Requires Python 3.11 (64-bit). The steps below use Windows PowerShell; see [SETUP.md](SETUP.md) for details.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`requirements.txt` does not include a Jupyter frontend. To run the notebook, also install one, for example:

```powershell
pip install notebook      # or: pip install ipykernel  (for VS Code's Jupyter extension)
```

The first ingestion downloads the embedding model (about 90 MB) into the Hugging Face cache. `sentence-transformers` also installs PyTorch (CPU build, about 1 GB).

## API configuration

Create a `.env` file in the project root. It is git-ignored and must never be committed.

```
GEMINI_API_KEY=your-key-here
```

The pipeline reads `GEMINI_API_KEY` and falls back to `GOOGLE_API_KEY`. No other API key is used.

Optional settings, also read from the environment or `.env`:

| Variable | Default | Effect |
|---|---|---|
| `GEMINI_ANSWER_MODEL` | `gemini-flash-lite-latest` | Model for figure descriptions, grading and answers |
| `IMAGE_SUMMARIES` | `1` | `0` disables Gemini figure descriptions at ingest |
| `FIND_TABLES` | `1` | `0` skips table detection (the slowest extraction step) |
| `CHUNK_CHARS` / `CHUNK_OVERLAP` | `1000` / `150` | Text chunk size and overlap |
| `CAPTION_CHARS` | `400` | Surrounding text attached to figures and tables |
| `EMBEDDING_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Local embedding model |

Changing extraction or model settings changes the configuration fingerprint, and the affected records are rebuilt on the next ingestion.

## Running

### Notebook

1. Open `langchain_multimodal.ipynb` in Jupyter or VS Code and select the `.venv` kernel.
2. In section A, set `PDF_PATH` to your PDF and `QUESTION` to a question about it.
3. Run sections A–F. They extract and display text, tables and figures locally, without API calls, so you can review extraction quality first.
4. To enable Gemini calls, set both flags in section A to `True` and re-run it:

   ```python
   RUN_MODEL_CALLS = True
   EXTRACTION_REVIEW_APPROVED = True
   ```

   Sections G–J then describe a sample figure, ingest the PDF into Chroma and SQLite, retrieve evidence, and answer `QUESTION` plus a set of demo questions. When either flag is `False`, these sections print a skip message.

Check both flags before using *Run All*: the notebook as saved may have them set to `True`.

### Command line

```powershell
python rag_pipeline.py                                   # print configuration only; no parsing or API calls
python rag_pipeline.py --run --pdf my.pdf --question "..."  # ingest the PDF and answer one question
```

Without `--pdf`, `--run` uses `attention.pdf` in the project root.

### Evaluation

`evaluate_rag.py` ingests a PDF (default `attention.pdf`), asks five fixed questions about the *Attention Is All You Need* paper and scores each answer against expected patterns. It writes `eval_results.json`.

```powershell
python evaluate_rag.py --dry-run   # grader self-check, no API calls
python evaluate_rag.py             # full run, calls Gemini
```

## Persistence

All state is stored next to `rag_pipeline.py`:

- **`chroma_db/`**: Chroma collection `multi_modal_rag` holding the embedded chunks, table text and figure descriptions.
- **`rag_state.sqlite3`**: the full parent records returned to the answer model, plus a per-PDF manifest (file hash, configuration fingerprint, record IDs) used for incremental ingestion.

Records are scoped by PDF file name, so re-ingesting one PDF never touches another's records. To start from an empty index, delete both `chroma_db/` and `rag_state.sqlite3`.

## Important notes

- **Local vs. API work**: PDF parsing and embeddings run locally at no per-call cost. Only Gemini calls leave the machine.
- **Gemini usage**: ingestion makes one vision call per new or changed figure (none when `IMAGE_SUMMARIES=0`). Each question makes two calls: one to grade evidence and one to answer.
- **Costs and quotas**: on the free tier, Gemini limits requests per day per model, and a full notebook or evaluation run can use a large share of that limit. On a paid tier, these calls are billed.
- **Approval flags**: in the notebook, `RUN_MODEL_CALLS` and `EXTRACTION_REVIEW_APPROVED` must both be `True` before any section sends requests to Gemini.
- **Data sent to Gemini**: figure images, retrieved text excerpts and your questions are sent to Google's API. Do not index documents you are not permitted to share with that service.
