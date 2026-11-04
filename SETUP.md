# Local Setup — Multimodal RAG on Windows 11

Target machine: Windows 11, Intel i5 (4 cores), 12 GB RAM, Python 3.11 (64-bit).

`requirements.txt` covers everything. There are no native binaries to install:
PyMuPDF carries its own renderer, so the Poppler and Tesseract installs the
old `unstructured` `hi_res` stack needed are gone, along with the layout-model
weights it downloaded on first run.

---

## 1. Python environment

```powershell
# from D:\MultimodalRAG
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip check
```

If PowerShell blocks `Activate.ps1`, allow local scripts once per user:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

---

## 2. Embedding model weights (automatic, needs a first online run)

The first ingestion downloads `sentence-transformers/all-MiniLM-L6-v2` (about
90 MB) into `%USERPROFILE%\.cache\huggingface`. This happens once; afterwards
the pipeline runs offline. To keep the model inside the project instead, set
`HF_HOME` before importing `rag_pipeline`:

```powershell
$env:HF_HOME = "D:\MultimodalRAG\.hf_cache"
```

`.hf_cache/` is already in `.gitignore`.

---

## 3. API keys

Create a `.env` file in the project root (it is git-ignored):

```
GEMINI_API_KEY=AIza...
```

Gemini is the only API the pipeline calls. Parsing is PyMuPDF and embeddings
run locally through `sentence-transformers`, so neither needs a key.

Budget the calls, because the free tier caps **requests per day per model**,
not only tokens per minute:

| When | Calls |
|---|---|
| Ingestion | one vision call per figure, once per figure that changes |
| Each question | two - the relevance grader, then the answer |

`gemini-flash-latest` allows 20 requests a day, which a single five-question
evaluation run exhausts; `gemini-flash-lite-latest` is the default for that
reason, and because the thinking Flash model spent 256s on one graded question
against 1.4s for lite. Set `IMAGE_SUMMARIES=0` to make ingestion free again at
the cost of answering questions about what a figure shows.

---

## 4. Verify the whole environment

```powershell
.\.venv\Scripts\python.exe smoke_test_imports.py
```

The script imports every critical component. It makes no API calls and embeds
nothing.

Then check extraction against a real PDF — still no API calls, no embeddings:

```powershell
.\.venv\Scripts\python.exe test_pdf_extraction.py --pdf attention.pdf
```

Unit tests (offline, synthetic data only):

```powershell
.\.venv\Scripts\python.exe -m unittest test_rag_pipeline -v
```

---

## 5. Tuning

All of these are environment variables, read once at import:

| Variable | Default | What it does |
|---|---|---|
| `CHUNK_CHARS` | `1000` | Characters per text chunk. Raw chunks are embedded, so anything past the embedding model's window (256 word pieces for MiniLM, roughly 1000 characters) never reaches the vector. Raise it only alongside a model with a bigger window. |
| `CHUNK_OVERLAP` | `150` | Characters shared between neighbouring chunks, so a sentence split across the boundary stays searchable from both sides. |
| `CAPTION_CHARS` | `400` | Characters of surrounding page text attached to a figure or a table. A figure takes this much from each side; a table takes it from above only, where its `Table n: ...` line sits. Flattened cells embed badly against a question asked in prose, so for a table the lead-in is most of what makes it findable. |
| `FIND_TABLES` | `1` | Set to `0` for a prose-only document. Table detection scans every page for ruling lines and is by far the slowest pass: 43.8s of a 45.2s parse over a 152-page book, to recover 4 tables. With it off that book parses in 4.8s. |
| `EMBEDDING_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Local CPU embeddings. |
| `IMAGE_SUMMARIES` | `1` | Set to `0` to index a figure by the text printed around it instead of by a Gemini description of its pixels. A figure's labels never reach the index as text, so with this off no question about the inside of a figure can be answered. |
| `GEMINI_ANSWER_MODEL` | `gemini-flash-lite-latest` | The model that grades the evidence, writes the figure summaries and writes the answer. |

Changing any of the first five changes the configuration fingerprint, which
invalidates every stored record and rebuilds the index on the next ingestion.
So does `IMAGE_SUMMARIES`, and so does the model name while summaries are on -
that model wrote the figure descriptions that are stored and embedded, so a
different one has to rewrite them.

---

## Notes on resource use

* No PyTorch is needed for parsing. `sentence-transformers` still pulls it in
  for embeddings (CPU build on Windows, ~1 GB on disk).
* A hundred-page book parses in seconds and embeds on the CPU, so there is no
  longer a reason to split long PDFs into page ranges.
