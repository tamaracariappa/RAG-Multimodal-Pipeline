"""Lightweight multimodal RAG pipeline over PyMuPDF.

Importing this module is side-effect free: nothing is parsed, embedded or sent
to an API at import time, and ``pymupdf`` is imported inside the one function
that needs it.

Extraction is local and fast. PyMuPDF reads text blocks, table grids and image
positions straight out of the structures the PDF already carries - no page is
rasterised, no layout model is loaded and no OCR binary is required.

Text and tables are embedded raw - the chunk is the vector, with no summariser
between the document and the index. Figures are the exception: their labels
are pixels, so each one costs a single Gemini vision call at ingest and is
indexed by the description that comes back. Gemini's free tier is 1M TPM,
which is what makes a per-figure call affordable where Groq's 8k did not.

Answering costs two calls: Gemini grades the retrieved evidence for relevance
(corrective RAG) and then answers from whatever survived, or abstains.

State persists next to this file - Chroma in ``chroma_db/`` and the parent
documents plus the ingestion manifest in ``rag_state.sqlite3``. Ingestion is
incremental: an unchanged PDF under an unchanged configuration is skipped
entirely, and a changed one only embeds the records that actually changed.

Command line:
    python rag_pipeline.py              # print the resolved configuration only
    python rag_pipeline.py --run        # parse a PDF and call the Gemini API
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import uuid
from base64 import b64encode
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Iterable, Iterator, NamedTuple, Sequence

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_classic.retrievers.multi_vector import MultiVectorRetriever
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.stores import BaseStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

#: State lives next to this file, never next to the caller's working directory,
#: so a notebook launched from anywhere reopens the same index.
PROJECT_DIR = Path(__file__).resolve().parent
CHROMA_DIR = PROJECT_DIR / "chroma_db"
STATE_DB = PROJECT_DIR / "rag_state.sqlite3"
COLLECTION_NAME = "multi_modal_rag"

# Reads the project's .env if there is one. Variables already set in the
# environment win, and nothing is printed or logged.
load_dotenv(PROJECT_DIR / ".env", override=False)

#: Metadata key that tells text, table and image records apart.
CONTENT_TYPE_KEY = "content_type"

#: Metadata key linking a child vector to its parent record.
ID_KEY = "doc_id"

#: Local sentence-transformers model. Runs on the CPU, needs no API key and
#: costs nothing per call; 384 dimensions against text-embedding-3-small's
#: 1536, so a Chroma collection built with the old model cannot be reused.
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
)

#: The one model the pipeline calls, for figure summaries, relevance grading
#: and answers alike. Google retired gemini-1.5-flash and the 2.x aliases on
#: this tier (404 NOT_FOUND), so the name is one of the -latest aliases.
#:
#: Lite rather than Flash for two measured reasons. The free tier caps daily
#: *requests* per model, not just tokens, and gemini-flash-latest resolves to
#: a thinking model with 20 a day - one evaluation run exhausts it. That model
#: also spent 256s on a single graded question, against 1.4s for lite.
ANSWER_MODEL = os.getenv("GEMINI_ANSWER_MODEL", "gemini-flash-lite-latest")

#: Gemini answers a 429 with a retry delay and the SDK sleeps for it. A daily
#: quota refuses for the rest of the day instead (retryDelay in the tens of
#: thousands of seconds), so retries cannot rescue an exhausted key: budget the
#: calls instead - one per figure at ingest, two per question at answer time.
GEMINI_MAX_RETRIES = 10

#: Vision summaries for figures at ingest: one call each, the description is
#: what gets embedded. Set IMAGE_SUMMARIES=0 to fall back to indexing a figure
#: by the text printed around it, which costs nothing but cannot answer a
#: question about what the figure itself shows.
IMAGE_SUMMARIES = os.getenv("IMAGE_SUMMARIES", "1") != "0"

#: Chunking, sized for the embedding model rather than for a summariser.
#: all-MiniLM-L6-v2 truncates at 256 word pieces, roughly 1000 characters:
#: anything past that never reaches the vector. The old 10000 was safe only
#: because a short summary was embedded in the chunk's place. Embedding raw
#: text means the chunk itself has to fit the window, with enough overlap that
#: a sentence split across the boundary stays searchable from both sides.
#: Kept as module constants so config_fingerprint can hash them: a change here
#: changes what a record contains, so cached records must rebuild.
CHUNK_CHARS = int(os.getenv("CHUNK_CHARS", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "150"))

#: Characters of surrounding page text attached to a figure or a table.
#: A figure takes this much from each side: its own "Figure n: ..." line sits
#: directly under it and lands in the trailing half, while the leading half
#: catches the paragraph that refers to it. A table takes it from above only,
#: which is where both its "Table n: ..." line and the sentence introducing it
#: sit. Flattened cells ("Model | BLEU EN DE | ...") embed badly against a
#: question asked in prose, so for a table the lead-in is most of what makes
#: it findable at all.
CAPTION_CHARS = int(os.getenv("CAPTION_CHARS", "400"))

#: Name of the extraction stack, hashed into the fingerprint so that switching
#: extractors invalidates every record the old one produced.
EXTRACTOR = "pymupdf"

# Vector-drawing extraction settings
VECTOR_DRAWING_VERSION = "clustered-vector-v1"

#: Bumped so already-ingested PDFs are re-extracted without their blank images.
RASTER_FILTER_VERSION = "skip-blank-v1"

VECTOR_DRAWING_DPI = int(os.getenv("VECTOR_DRAWING_DPI", "180"))

# Ignore very small decorative paths and isolated lines.
VECTOR_MIN_WIDTH = float(os.getenv("VECTOR_MIN_WIDTH", "40"))
VECTOR_MIN_HEIGHT = float(os.getenv("VECTOR_MIN_HEIGHT", "30"))
VECTOR_MIN_PATHS = int(os.getenv("VECTOR_MIN_PATHS", "3"))

# Expand the detected drawing region to include nearby graph labels and axes.
VECTOR_PADDING_X = float(os.getenv("VECTOR_PADDING_X", "20"))
VECTOR_PADDING_Y = float(os.getenv("VECTOR_PADDING_Y", "25"))

#: Whether to look for tables. Set FIND_TABLES=0 for a prose-only document.
#: ponytail: find_tables scans every page for ruling lines and is by far the
#: most expensive thing left - measured at 43.8s of a 45.2s parse over a
#: 152-page book, to recover 4 tables. Everything else (text blocks, image
#: positions) totals under 4s. Pre-filtering on get_cdrawings only nets about
#: 5s, and strategy="text" is no faster, so the honest lever is the switch:
#: off, that book parses in roughly 4 seconds. Revisit if PyMuPDF speeds up
#: detection, or add a page range if only part of a document holds tables.
FIND_TABLES = os.getenv("FIND_TABLES", "1") != "0"

IMAGE_PROMPT = """Describe this figure from a technical paper so that it can be found by search and read without the picture.

Name every labelled box, axis, arrow and legend entry using the exact wording printed inside the image, and say what connects or leads to what. State the order of components in any stack or pipeline. No preamble, no interpretation.

Text printed around the figure: {caption}
"""

GRADE_PROMPT = """You are grading retrieved evidence before it is used to answer a question.

Question: {question}

{blocks}

Reply with the numbers of the blocks that could contribute to the answer, separated by commas. Judge generously: a block holding part of the answer, or the table or figure the question names, counts. Reply NONE only if no block bears on the question at all.
"""

#: What the chain answers with when the grader keeps nothing. Worded so that it
#: reads as a refusal rather than as an answer.
ABSTAIN_ANSWER = (
    "The retrieved evidence does not contain the answer to this question."
)

ANSWER_PROMPT = """Answer the question using only the evidence below. The \
evidence can include text passages, tables (given as HTML) and figures (given
as the text printed around them).

Each block is delimited and labelled with the document it came from and its
page number. Cite those sources in your answer. If the evidence does not
contain the answer, say so.

Evidence:
{context}

Question: {question}
"""

# --------------------------------------------------------------------------
# 0. Identity and persistence
# --------------------------------------------------------------------------


def chat_model(**kwargs: Any) -> Any:
    """The Gemini client, built fresh so a changed key or model takes effect.

    One model serves every call the pipeline makes - figure summaries,
    relevance grading and answers - so there is one place to change it.
    """
    return ChatGoogleGenerativeAI(
        model=ANSWER_MODEL,
        temperature=0,
        max_retries=GEMINI_MAX_RETRIES,
        # The SDK looks for GOOGLE_API_KEY; the project's .env names it
        # GEMINI_API_KEY, so both are accepted rather than renamed.
        google_api_key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"),
        **kwargs,
    )


def _sha256(data: str | bytes) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8", "replace")
    return hashlib.sha256(data).hexdigest()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def file_hash(path: str | Path) -> str:
    """SHA-256 of a file's bytes, read in blocks so a large PDF stays off the heap."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def config_fingerprint() -> str:
    """Hash of every setting that changes what ends up in the index.

    The answer prompt is deliberately excluded: it shapes the reply, not the
    stored records. The answer model is excluded too - except while
    IMAGE_SUMMARIES is on, because then the same model writes the figure
    descriptions that are stored and embedded, and a different model would
    write different ones.
    """
    payload = json.dumps(
        {
            "embedding_model": EMBEDDING_MODEL,
            "extractor": EXTRACTOR,
            "chunking": [CHUNK_CHARS, CHUNK_OVERLAP],
            "caption_chars": CAPTION_CHARS,
            "find_tables": FIND_TABLES,
            "image_summaries": IMAGE_SUMMARIES,
            "vision_model": ANSWER_MODEL if IMAGE_SUMMARIES else None,
        },
        sort_keys=True,
    )
    return _sha256(payload)[:16]

def ingestion_fingerprint() -> str:
    """Version the extraction process without changing existing record IDs."""
    payload = {
        "record_config": config_fingerprint(),
        "vector_drawing_version": VECTOR_DRAWING_VERSION,
        "raster_filter_version": RASTER_FILTER_VERSION,
    }
    return _sha256(json.dumps(payload, sort_keys=True))[:16]

def record_id(locator: str, payload_hash: str, fingerprint: str) -> str:
    """Stable identifier for one extracted record.

    The fingerprint is part of the hash on purpose. When the embedding model,
    the extractor or the chunking changes, every id changes, the old ids are
    no longer planned, and the ordinary obsolete-record sweep removes them -
    one mechanism covers both re-ingestion and config invalidation.
    """
    return _sha256("\x1f".join([locator, payload_hash, fingerprint]))


_SCHEMA = """
CREATE TABLE IF NOT EXISTS parents (
    id       TEXT PRIMARY KEY,
    document TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS records (
    id           TEXT PRIMARY KEY,
    source_id    TEXT NOT NULL,
    locator      TEXT NOT NULL,
    payload_hash TEXT NOT NULL,
    content_type TEXT,
    page_number  INTEGER,
    fingerprint  TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS records_by_source ON records (source_id);
CREATE TABLE IF NOT EXISTS sources (
    source_id   TEXT PRIMARY KEY,
    source_hash TEXT NOT NULL,
    fingerprint TEXT NOT NULL,
    status      TEXT NOT NULL,
    updated_at  TEXT NOT NULL
);
"""

#: SQLite caps host parameters per statement; stay well under the limit.
_BATCH = 400


def _batched(items: Sequence[Any]) -> Iterator[Sequence[Any]]:
    for start in range(0, len(items), _BATCH):
        yield items[start : start + _BATCH]


class SQLiteStore(BaseStore[str, Document]):
    """Parent documents and the ingestion manifest in one SQLite file.

    Implements the ``BaseStore[str, Document]`` interface that
    ``MultiVectorRetriever.docstore`` is typed against, so it drops into the
    existing retriever in place of ``InMemoryStore`` and survives a restart.
    """

    def __init__(self, path: str | Path = STATE_DB) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        # ponytail: one connection, no pool - ingestion is single threaded.
        # Switch to a connection per thread if ingestion is ever parallelised.
        self.db = sqlite3.connect(self.path, check_same_thread=False)
        self.db.executescript(_SCHEMA)
        self.db.commit()

    def close(self) -> None:
        self.db.close()

    # -- BaseStore ---------------------------------------------------------

    def mget(self, keys: Sequence[str]) -> list[Document | None]:
        keys = list(keys)
        found: dict[str, str] = {}
        for batch in _batched(keys):
            marks = ",".join("?" * len(batch))
            found.update(
                self.db.execute(
                    f"SELECT id, document FROM parents WHERE id IN ({marks})",
                    list(batch),
                )
            )
        return [
            Document(**json.loads(found[key])) if key in found else None for key in keys
        ]

    def mset(self, key_value_pairs: Sequence[tuple[str, Document]]) -> None:
        self.db.executemany(
            "INSERT OR REPLACE INTO parents (id, document) VALUES (?, ?)",
            [
                (
                    key,
                    json.dumps(
                        {"page_content": doc.page_content, "metadata": doc.metadata}
                    ),
                )
                for key, doc in key_value_pairs
            ],
        )
        self.db.commit()

    def mdelete(self, keys: Sequence[str]) -> None:
        for batch in _batched(list(keys)):
            marks = ",".join("?" * len(batch))
            self.db.execute(f"DELETE FROM parents WHERE id IN ({marks})", list(batch))
        self.db.commit()

    def yield_keys(self, prefix: str | None = None) -> Iterator[str]:
        sql, args = "SELECT id FROM parents", ()
        if prefix:
            sql, args = sql + " WHERE id LIKE ?", (f"{prefix}%",)
        for (key,) in self.db.execute(sql, args):
            yield key

    # -- Ingestion manifest ------------------------------------------------

    def manifest(self, source_id: str) -> dict[str, str]:
        """``{record_id: payload_hash}`` for everything recorded for one source."""
        return dict(
            self.db.execute(
                "SELECT id, payload_hash FROM records WHERE source_id = ?",
                (source_id,),
            )
        )

    def source_state(self, source_id: str) -> tuple[str, str, str] | None:
        """``(source_hash, fingerprint, status)`` of the last ingestion, if any."""
        row = self.db.execute(
            "SELECT source_hash, fingerprint, status FROM sources WHERE source_id = ?",
            (source_id,),
        ).fetchone()
        return tuple(row) if row else None

    def begin_source(self, source_id: str, source_hash: str, fingerprint: str) -> None:
        """Mark a source in progress. Nothing counts as done until finish_source."""
        self.db.execute(
            "INSERT OR REPLACE INTO sources "
            "(source_id, source_hash, fingerprint, status, updated_at) "
            "VALUES (?, ?, ?, 'pending', ?)",
            (source_id, source_hash, fingerprint, _now()),
        )
        self.db.commit()

    def finish_source(self, source_id: str) -> None:
        self.db.execute(
            "UPDATE sources SET status = 'complete', updated_at = ? WHERE source_id = ?",
            (_now(), source_id),
        )
        self.db.commit()

    def add_records(self, source_id: str, records: Sequence[dict[str, Any]]) -> None:
        self.db.executemany(
            "INSERT OR REPLACE INTO records (id, source_id, locator, payload_hash, "
            "content_type, page_number, fingerprint) VALUES (?, ?, ?, ?, ?, ?, ?)",
            [
                (
                    record["id"],
                    source_id,
                    record["locator"],
                    record["payload_hash"],
                    record["content_type"],
                    record["page_number"],
                    record["fingerprint"],
                )
                for record in records
            ],
        )
        self.db.commit()

    def drop_records(self, ids: Sequence[str]) -> None:
        for batch in _batched(list(ids)):
            marks = ",".join("?" * len(batch))
            self.db.execute(f"DELETE FROM records WHERE id IN ({marks})", list(batch))
        self.db.commit()


# --------------------------------------------------------------------------
# 1. Extraction
# --------------------------------------------------------------------------


#: Layout of a PyMuPDF text block tuple: (x0, y0, x1, y1, text, no, type).
_BLOCK_Y0, _BLOCK_TEXT, _BLOCK_TYPE = 1, 4, 6
_TEXT_BLOCK = 0


def _squash(text: str) -> str:
    """Collapse the newlines and padding PDF text blocks carry."""
    return re.sub(r"\s+", " ", text).strip()


def _element(
    text: str, *, source: str | None, page_number: int, html: str | None = None
) -> Any:
    """One extracted text or table chunk.

    An attribute bag rather than a class: the rest of the module reads
    ``.text``, ``.metadata.filename``, ``.metadata.page_number`` and
    ``.metadata.text_as_html``, and nothing else.
    """
    return SimpleNamespace(
        text=text,
        metadata=SimpleNamespace(
            filename=source, page_number=page_number, text_as_html=html
        ),
    )


def _table_text(rows: Sequence[Sequence[str | None]]) -> str:
    """Extracted cells as plain text - this is what gets embedded."""
    return "\n".join(" | ".join(_squash(cell or "") for cell in row) for row in rows)


def _table_html(rows: Sequence[Sequence[str | None]]) -> str:
    """The same cells as HTML, first row as the header.

    The answer model reads tables from this, so the grid has to survive: a
    flattened row of numbers loses which column each one came from.
    """

    def cells(row: Sequence[str | None], tag: str) -> str:
        return "".join(f"<{tag}>{escape(_squash(cell or ''))}</{tag}>" for cell in row)

    header, *body = rows
    grid = [f"<tr>{cells(header, 'th')}</tr>"]
    grid += [f"<tr>{cells(row, 'td')}</tr>" for row in body]
    return "<table>" + "".join(grid) + "</table>"


def _inside(block: Sequence[Any], boxes: Sequence[Sequence[float]]) -> bool:
    """True when a block's centre falls inside one of the table rectangles.

    Table cell text comes back from ``get_text("blocks")`` as well. Without
    this every table is indexed twice - once as a grid, once as loose prose -
    and the two copies compete for the same query.
    """
    centre_x = (block[0] + block[2]) / 2
    centre_y = (block[1] + block[3]) / 2
    return any(
        x0 <= centre_x <= x1 and y0 <= centre_y <= y1 for x0, y0, x1, y1 in boxes
    )


def _lead_in(blocks: Sequence[Any], y: float, caption_chars: int) -> str:
    """The last ``caption_chars`` of page text printed above ``y``.

    Blocks stay in the PDF's own content order, so this is what a reader meets
    just before reaching ``y``: the caption line and the sentence introducing
    whatever sits there.
    """
    return "".join(b[_BLOCK_TEXT] for b in blocks if b[_BLOCK_Y0] < y)[-caption_chars:]


def _is_blank(document: Any, xref: int) -> bool:
    """True when an image and its soft mask are each a single flat value.

    Such an image is a spacer or overlay, not a figure: BCS703 places a black,
    fully transparent 1009x166 one on every page, and each placement was
    indexed under the caption of the real figure beside it. The soft mask is
    checked on its own because ``Pixmap(document, xref)`` does not apply it,
    and black ink whose shape lives only in the mask is a real figure. Images
    with a hard /Mask, or that cannot be decoded here, are kept, as before.

    ponytail: exact match only, so a near-blank JPEG (compression noise) still
    gets indexed. Compare against a tolerance if those show up.
    """
    import pymupdf

    def flat(image_xref: int) -> bool:
        pixmap = pymupdf.Pixmap(document, image_xref)
        samples = pixmap.samples
        return samples == samples[: pixmap.n] * (pixmap.width * pixmap.height)

    try:
        if document.xref_get_key(xref, "Mask")[0] != "null":
            return False
        kind, smask = document.xref_get_key(xref, "SMask")
        return flat(xref) and (kind == "null" or flat(int(smask.split()[0])))
    except Exception:
        return False


def _page_images(
    page: Any,
    blocks: Sequence[Any],
    *,
    source: str,
    page_number: int,
    caption_chars: int,
) -> list[dict[str, Any]]:
    """Describe each image on a page by the text printed around it.

    No vision model and no OCR: the caption is ``caption_chars`` of page text
    ending above the figure plus the same amount starting below it, which is
    where a figure's own "Figure n: ..." line lives.

    The pixels are not stored. ``xref`` and ``image_hash`` identify the image
    inside the PDF, so it can be pulled out again on demand, and the hash is
    what tells the manifest a figure changed.
    """
    records: list[dict[str, Any]] = []
    seen: set[Any] = set()
    for info in page.get_image_info(xrefs=True):
        xref = info.get("xref")
        if xref in seen:
            continue
        seen.add(xref)
        if _is_blank(page.parent, xref):
            continue
        top, bottom = info["bbox"][1], info["bbox"][3]
        after = "".join(b[_BLOCK_TEXT] for b in blocks if b[_BLOCK_Y0] >= bottom)
        caption = _squash(
            f"{_lead_in(blocks, top, caption_chars)} {after[:caption_chars]}"
        )
        records.append(
            {
                "source": source,
                "page_number": page_number,
                "xref": xref,
                "image_hash": info.get("digest", b"").hex(),
                # An unlabelled figure on a wordless page still gets indexed,
                # and still retrieves by page, rather than carrying the vector
                # of the empty string, which no query ever matches.
                "caption": caption or f"figure on page {page_number} of {source}",
            }
        )
    return records

def _overlap_fraction(rect: Any, box: Sequence[float]) -> float:
    """Fraction of a drawing rectangle covered by another bounding box."""
    x0 = max(float(rect.x0), float(box[0]))
    y0 = max(float(rect.y0), float(box[1]))
    x1 = min(float(rect.x1), float(box[2]))
    y1 = min(float(rect.y1), float(box[3]))

    intersection = max(0.0, x1 - x0) * max(0.0, y1 - y0)
    area = max(float(rect.width) * float(rect.height), 1.0)
    return intersection / area


def _page_vector_drawings(
    page: Any,
    blocks: Sequence[Any],
    *,
    source: str,
    page_number: int,
    caption_chars: int,
    excluded_boxes: Sequence[Sequence[float]] = (),
) -> list[dict[str, Any]]:
    """Extract vector-drawn figure regions as searchable PNG records.

    The PNG is rendered locally for hashing and later vision summarisation.
    Only the bounding box and hash are kept in the record.
    """
    drawings = page.get_drawings()
    if not drawings:
        return []

    clusters = page.cluster_drawings(drawings=drawings)

    # Stable ordering matters because plan_records assigns position-based IDs.
    clusters = sorted(clusters, key=lambda r: (round(r.y0, 2), round(r.x0, 2)))

    records: list[dict[str, Any]] = []

    for cluster_index, rect in enumerate(clusters):
        paths = [
            path for path in drawings
            if path.get("rect") is not None
            and rect.intersects(path["rect"])
        ]

        if len(paths) < VECTOR_MIN_PATHS:
            continue

        if rect.width < VECTOR_MIN_WIDTH or rect.height < VECTOR_MIN_HEIGHT:
            continue

        page_area = max(page.rect.width * page.rect.height, 1.0)
        if rect.width * rect.height > page_area * 0.80:
            continue

        # Avoid treating ruled tables or existing raster-image boundaries
        # as separate vector figures.
        if any(
            _overlap_fraction(rect, box) >= 0.50
            for box in excluded_boxes
        ):
            continue

        # Expand the crop to capture nearby axis labels and graph text.
        bbox = [
            max(float(page.rect.x0), float(rect.x0) - VECTOR_PADDING_X),
            max(float(page.rect.y0), float(rect.y0) - VECTOR_PADDING_Y),
            min(float(page.rect.x1), float(rect.x1) + VECTOR_PADDING_X),
            min(float(page.rect.y1), float(rect.y1) + VECTOR_PADDING_Y),
        ]

        if bbox[2] <= bbox[0] or bbox[3] <= bbox[1]:
            continue

        # Local PNG rendering. No Gemini/API call occurs here.
        png_bytes = page.get_pixmap(
            dpi=VECTOR_DRAWING_DPI,
            clip=bbox,
            alpha=False,
        ).tobytes("png")

        top, bottom = bbox[1], bbox[3]
        after = "".join(
            block[_BLOCK_TEXT]
            for block in blocks
            if block[_BLOCK_Y0] >= bottom
        )

        caption = _squash(
            f"{_lead_in(blocks, top, caption_chars)} "
            f"{after[:caption_chars]}"
        )

        records.append(
            {
                "source": source,
                "page_number": page_number,
                "extraction_method": "vector_drawing",
                "bbox": bbox,
                "cluster_index": cluster_index,
                "drawing_count": len(paths),
                "render_dpi": VECTOR_DRAWING_DPI,
                "image_hash": _sha256(png_bytes),
                "caption": caption
                or f"vector figure on page {page_number} of {source}",
            }
        )

    return records


def figure_image_bytes(document, record):
    """Return image bytes and MIME type for raster or vector figures."""
    import pymupdf

    if record.get("extraction_method") == "vector_drawing":
        page = document[int(record["page_number"]) - 1]

        png_bytes = page.get_pixmap(
            dpi=int(record.get("render_dpi", VECTOR_DRAWING_DPI)),
            clip=record["bbox"],
            alpha=False,
        ).tobytes("png")

        return png_bytes, "image/png"

    # Extract raster image
    xref = record.get("xref")
    if xref is None:
        raise ValueError(f"Raster figure record has no xref: {record}")

    extracted = document.extract_image(xref)
    image_bytes = extracted["image"]

    # Apply transparency mask if present
    smask = extracted.get("smask", 0)

    if smask:
        base = pymupdf.Pixmap(image_bytes)
        mask_data = document.extract_image(smask)["image"]
        mask = pymupdf.Pixmap(mask_data)

        # Remove existing alpha channels before combining
        if base.alpha:
            base = pymupdf.Pixmap(base, 0)

        if mask.alpha:
            mask = pymupdf.Pixmap(mask, 0)

        # Ensure mask is grayscale
        if mask.colorspace != pymupdf.csGRAY:
            mask = pymupdf.Pixmap(pymupdf.csGRAY, mask)

        # A PDF /SMask may have its own resolution; both map onto the same
        # image square, so scale the mask, never the image.
        if (mask.width, mask.height) != (base.width, base.height):
            mask = pymupdf.Pixmap(mask, base.width, base.height)

        image = pymupdf.Pixmap(base, mask)

        return image.tobytes("png"), "image/png"

    ext = extracted["ext"].lower()
    mime_type = "image/jpeg" if ext in {"jpg", "jpeg"} else f"image/{ext}"

    return image_bytes, mime_type

def _summarise_images(
    document: Any,
    images: Sequence[dict[str, Any]],
    model: Any = None,
) -> None:
    """Attach a Gemini vision summary to each image record, in place.

    A figure's labels are pixels: nothing printed inside it reaches the index
    through text extraction, which is why the surrounding prose cannot answer a
    question about what the figure shows. One call per figure turns those
    pixels into words both the embedding model and the answer model can read.

    Best effort by design: a figure that cannot be extracted or summarised
    keeps its surrounding-text caption and ingestion continues. Losing one
    description is worth less than failing a whole book on one bad image.
    """
    model = model or chat_model()
    for record in images:
        try:
            image_bytes, mime_type = figure_image_bytes(document, record)
            payload = b64encode(image_bytes).decode("ascii")
            reply = model.invoke(
                [
                    HumanMessage(
                        content=[
                            {
                                "type": "text",
                                "text": IMAGE_PROMPT.format(caption=record["caption"]),
                            },
                            {
                                "type": "image_url",
                                "image_url": f"data:{mime_type};base64,{payload}",
                            },
                        ]
                    )
                ]
            )
            record["summary"] = _squash(reply.text)
        except Exception as error:
            record["summary"] = ""
            location = (
                f"bbox={record.get('bbox')}"
                if record.get("extraction_method") == "vector_drawing"
                else f"xref={record.get('xref')}"
            )
            print(
                f"  figure summary failed "
                f"(page {record['page_number']}, {location}): {error}",
                flush=True,
            )


def partition_document(
    file_path: str,
    *,
    chunk_chars: int = CHUNK_CHARS,
    chunk_overlap: int = CHUNK_OVERLAP,
    caption_chars: int = CAPTION_CHARS,
    find_tables: bool | None = None,
    summarise_images: bool | None = None,
) -> tuple[list[Any], list[Any], list[dict[str, Any]]]:
    """Extract ``(texts, tables, images)`` from a PDF with PyMuPDF.

    Extraction is local and in-process: no page is rasterised, no layout model
    is loaded and no external binary is needed, so a hundred-page book parses
    in under a minute rather than the half hour the hi_res OCR stack took - and
    in a few seconds with ``find_tables=False``.

    The one call out is the figure summaries, which need the pixels and so have
    to happen while the document is still open. Pass ``summarise_images=False``
    to keep the whole function offline.

    ponytail: blocks are kept in the content order the PDF itself stores,
    which tracks reading order for generated PDFs but can interleave the
    columns of a scanned two-column page. Sort blocks per column if that
    shows up.
    """
    # Imported here, not at module level, so importing this module stays free.
    import pymupdf
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_chars, chunk_overlap=chunk_overlap
    )
    find_tables = FIND_TABLES if find_tables is None else find_tables
    summarise = IMAGE_SUMMARIES if summarise_images is None else summarise_images
    source = Path(file_path).name
    texts: list[Any] = []
    tables: list[Any] = []
    images: list[dict[str, Any]] = []

    with pymupdf.open(file_path) as document:
        for page_number, page in enumerate(document, start=1):
            found = page.find_tables().tables if find_tables else []
            boxes = [table.bbox for table in found]
            blocks = [
                block
                for block in page.get_text("blocks")
                if block[_BLOCK_TYPE] == _TEXT_BLOCK and not _inside(block, boxes)
            ]
            for table in found:
                rows = table.extract()
                if not rows:
                    continue
                # The grid on its own embeds badly against a question asked in
                # prose. Prepending the text above it - the "Table n: ..." line
                # and the sentence introducing it - gives the vector the words
                # the question is actually likely to use.
                lead = _squash(_lead_in(blocks, table.bbox[1], caption_chars))
                tables.append(
                    _element(
                        f"{lead}\n{_table_text(rows)}".strip(),
                        source=source,
                        page_number=page_number,
                        html=_table_html(rows),
                    )
                )
            body = "".join(block[_BLOCK_TEXT] for block in blocks)
            texts.extend(
                _element(chunk, source=source, page_number=page_number)
                for chunk in splitter.split_text(body)
                if chunk.strip()
            )

            # 1. Extract existing embedded raster images first.
            raster_records = _page_images(
                page,
                blocks,
                source=source,
                page_number=page_number,
                caption_chars=caption_chars,
            )

            images.extend(raster_records)

            # 2. Exclude detected tables and existing raster-image regions
            #    when looking for vector-drawn figures.
            raster_boxes = [
                info["bbox"]
                for info in page.get_image_info(xrefs=True)
            ]

            excluded_boxes = [*boxes, *raster_boxes]

            # 3. Extract vector-drawn graphs, diagrams and plots.
            #    Keep these AFTER raster_records so existing raster record positions
            #    remain stable for deterministic ID generation.
            vector_records = _page_vector_drawings(
                page,
                blocks,
                source=source,
                page_number=page_number,
                caption_chars=caption_chars,
                excluded_boxes=excluded_boxes,
            )

            images.extend(vector_records)
            
        if summarise and images:
            _summarise_images(document, images)
    return texts, tables, images


def _source_of(element: Any) -> tuple[str | None, int | None]:
    """Return ``(filename, page_number)`` for one extracted element."""
    metadata = getattr(element, "metadata", None)
    return getattr(metadata, "filename", None), getattr(metadata, "page_number", None)


# --------------------------------------------------------------------------
# 2. Indexing
# --------------------------------------------------------------------------


def build_retriever(
    *,
    collection_name: str = COLLECTION_NAME,
    persist_directory: str | Path | None = CHROMA_DIR,
    state_db: str | Path = STATE_DB,
    embeddings: Any = None,
    docstore: Any = None,
) -> MultiVectorRetriever:
    """Persistent Chroma over the child vectors, SQLite for the parent records.

    Reopening with the same paths reuses the existing index instead of
    silently starting an empty one.
    """
    embeddings = embeddings or HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=str(persist_directory) if persist_directory else None,
    )
    return MultiVectorRetriever(
        vectorstore=vectorstore,
        docstore=docstore if docstore is not None else SQLiteStore(state_db),
        id_key=ID_KEY,
    )


def plan_records(
    texts: Sequence[Any],
    tables: Sequence[Any],
    images: Sequence[dict[str, Any]],
    *,
    source_id: str,
    fingerprint: str | None = None,
) -> list[dict[str, Any]]:
    """Describe every extractable record without embedding it.

    Each record gets a locator - source, content type, page, and position
    within that page - and an id derived from the locator, the SHA-256 of its
    payload and the configuration fingerprint. Two identical tables on two
    pages get different locators, so their ids differ. The same table
    extracted again from an unchanged PDF gets the same id and is reused.

    An image's payload is its pixel digest joined to its caption: either one
    changing changes what is stored or what is searched, so either one has to
    invalidate the record. A table's payload is its text for the same reason -
    that text carries the lead-in as well as the cells, so a table whose grid
    is unchanged but whose introduction was reworded still re-indexes.

    Position is counted per page rather than per document so that editing one
    page does not shift the locators of every record after it.
    """
    fingerprint = fingerprint or config_fingerprint()
    seen: dict[tuple[str, Any], int] = {}
    plan: list[dict[str, Any]] = []
    items: list[tuple[str, Any, str]] = (
        [("text", chunk, getattr(chunk, "text", "")) for chunk in texts]
        + [("table", table, getattr(table, "text", "")) for table in tables]
        + [
            ("image", image, f"{image.get('image_hash', '')}|{image.get('caption', '')}")
            for image in images
        ]
    )
    for content_type, item, payload in items:
        page = (
            item.get("page_number") if isinstance(item, dict) else _source_of(item)[1]
        )
        position = seen.get((content_type, page), 0)
        seen[(content_type, page)] = position + 1
        locator = f"{source_id}|{content_type}|p{page}|#{position}"
        payload_hash = _sha256(payload or "")
        plan.append(
            {
                "id": record_id(locator, payload_hash, fingerprint),
                "locator": locator,
                "payload_hash": payload_hash,
                "content_type": content_type,
                "page_number": page,
                "fingerprint": fingerprint,
                "item": item,
            }
        )
    return plan


def _parent_document(
    content_type: str,
    item: Any,
    source: str | None = None,
) -> Document:
    """One parent record as a Document, whatever its content type.

    ``page_content`` is the record's own text in every case - the chunk, the
    flattened table, the figure's caption - because that text is both what a
    reader sees and what gets embedded.
    """
    if content_type == "image":
        metadata = {CONTENT_TYPE_KEY: "image", **item}
        if source:
            metadata["source"] = source
        # Vision summary first, surrounding text second. The child vector is
        # truncated at the embedding model's window, so whatever leads is what
        # retrieval sees; the answer model reads the parent in full either way.
        body = "\n\n".join(
            part for part in (item.get("summary"), item.get("caption")) if part
        )
        return Document(page_content=body, metadata=metadata)

    element_source, page = _source_of(item)
    metadata = {
        CONTENT_TYPE_KEY: content_type,
        "source": source or element_source,
        "page_number": page,
    }
    if content_type == "table":
        metadata["text_as_html"] = getattr(
            getattr(item, "metadata", None), "text_as_html", None
        )
    return Document(page_content=getattr(item, "text", ""), metadata=metadata)


def collect_records(
    records: Sequence[dict[str, Any]],
    *,
    source: str | None = None,
) -> list[Document]:
    """Parent Documents for planned records, in plan order.

    ``MultiVectorRetriever.docstore`` is typed ``BaseStore[str, Document]``, so
    every parent record is a Document; the raw extracted elements and bare
    dicts the extractor produces do not satisfy that contract.

    ``source`` overrides the filename the extractor reported, so every record
    of one PDF carries the same source identity.
    """
    return [
        _parent_document(record["content_type"], record["item"], source)
        for record in records
    ]


def index_records(
    retriever: Any,
    parents: Sequence[Document],
    ids: Sequence[str] | None = None,
) -> list[str]:
    """Embed each parent's own text as its child vector, under the same id.

    No summarisation step stands between the document and the index: the text
    that was extracted is the text that is embedded, which is why the chunk
    size has to fit the embedding model's window (see ``CHUNK_CHARS``).

    ``ids`` are the deterministic record ids when ingesting a source; without
    them one random id is minted per record.
    """
    if not parents:
        return []

    ids = list(ids) if ids is not None else [str(uuid.uuid4()) for _ in parents]
    if len(ids) != len(parents):
        msg = f"ids ({len(ids)}) and parents ({len(parents)}) must align"
        raise ValueError(msg)
    children = []
    for doc_id, parent in zip(ids, parents):
        # The vector of the empty string matches no query, so a record with no
        # text would be stored and never retrievable. Label it by source and
        # page instead, which at least answers a question about that page.
        content = parent.page_content.strip() or _source_label(parent.metadata)
        metadata = {
            retriever.id_key: doc_id,
            CONTENT_TYPE_KEY: parent.metadata.get(CONTENT_TYPE_KEY),
            "source": parent.metadata.get("source"),
            "page_number": parent.metadata.get("page_number"),
        }
        # Chroma rejects None metadata values.
        children.append(
            Document(
                page_content=content,
                metadata={k: v for k, v in metadata.items() if v is not None},
            )
        )

    # Chroma upserts by id, so re-indexing a known record is idempotent.
    retriever.vectorstore.add_documents(children, ids=ids)
    retriever.docstore.mset(list(zip(ids, parents)))
    return ids


class IngestReport(NamedTuple):
    """What one ``ingest_pdf`` call actually did."""

    retriever: Any
    source_id: str
    indexed: int  # embedded in this run
    reused: int  # already present, not embedded again
    deleted: int  # gone from the PDF or invalidated, removed from both stores
    orphans_removed: int  # left behind by an interrupted earlier run
    skipped: bool  # source unchanged, not even reparsed


def _remove_orphans(retriever: Any, source_id: str) -> list[str]:
    """Delete child vectors for this source that the manifest never recorded.

    A run that dies between indexing a record and writing its manifest row
    leaves a record that nothing will ever delete but retrieval can still
    return. The manifest is the authority, so anything indexed under this
    source and absent from it goes.
    """
    known = set(retriever.docstore.manifest(source_id))
    indexed = retriever.vectorstore.get(where={"source": source_id}).get("ids", [])
    orphans = [key for key in indexed if key not in known]
    if orphans:
        retriever.vectorstore.delete(ids=orphans)
        retriever.docstore.mdelete(orphans)
    return orphans


def ingest_pdf(file_path: str | Path, retriever: Any = None) -> IngestReport:
    """Parse and index one PDF, reusing whatever is already stored.

    Every step is local: parsing is PyMuPDF, embedding is a CPU
    sentence-transformers model, and no API is called at any point.

    An unchanged PDF under an unchanged configuration is not reparsed at all.
    A changed PDF is reparsed, but only new or modified records are embedded;
    records that disappeared are deleted from both stores so they can no
    longer be retrieved. Records belonging to other PDFs are never touched -
    every query is scoped by ``source_id``.
    """
    path = Path(file_path).resolve()
    source_id = path.name
    retriever = retriever if retriever is not None else build_retriever()
    store = retriever.docstore
    if not isinstance(store, SQLiteStore):
        msg = "incremental ingestion needs a SQLiteStore docstore"
        raise TypeError(msg)

    # Keep record IDs compatible with the existing index.
    record_fingerprint = config_fingerprint()

    # Change the source-level fingerprint once so existing PDFs are
    # re-extracted to discover vector drawings.
    source_fingerprint = ingestion_fingerprint()

    source_hash = file_hash(path)
    previous = store.source_state(source_id)

    if previous == (source_hash, source_fingerprint, "complete"):
        # The source row saying "complete" is not proof the index still holds
        # what that run produced: a record can be dropped by a crash, a manual
        # delete or a vector store rebuilt from scratch. Skipping on the row
        # alone leaves those records permanently unretrievable, because the
        # fast path returns before the manifest diff that would notice. Count
        # both stores first, and forget whatever is damaged so the diff below
        # treats it as new and rebuilds it.
        known = list(store.manifest(source_id))
        present = {k for k, doc in zip(known, store.mget(known)) if doc is not None}
        present &= set(retriever.vectorstore.get(ids=known)["ids"])
        damaged = [key for key in known if key not in present]
        if not damaged:
            return IngestReport(retriever, source_id, 0, 0, 0, 0, True)
        store.drop_records(damaged)

    orphans = (
        _remove_orphans(retriever, source_id)
        if previous and previous[2] != "complete"
        else []
    )
    store.begin_source(source_id, source_hash, source_fingerprint)
    # Extraction only. Do not spend Gemini calls before checking which
    # figure records are actually new.
    texts, tables, images = partition_document(
        str(path),
        summarise_images=False,
    )
    plan = plan_records(
        texts,
        tables,
        images,
        source_id=source_id,
        fingerprint=record_fingerprint,
    )
    known = store.manifest(source_id)
    planned = {record["id"] for record in plan}
    obsolete = [key for key in known if key not in planned]
    fresh = [record for record in plan if record["id"] not in known]

    # Only summarise new or modified figures.
    # Unchanged raster images reuse their previously stored descriptions.
    fresh_images = [
        record["item"]
        for record in fresh
        if record["content_type"] == "image"
    ]

    if IMAGE_SUMMARIES and fresh_images:
        import pymupdf

        with pymupdf.open(path) as document:
            _summarise_images(document, fresh_images)

    if fresh:
        parents = collect_records(fresh, source=source_id)
        index_records(retriever, parents, [r["id"] for r in fresh])
        store.add_records(source_id, fresh)

    if obsolete:
        retriever.vectorstore.delete(ids=obsolete)
        store.mdelete(obsolete)
        store.drop_records(obsolete)

    store.finish_source(source_id)
    return IngestReport(
        retriever,
        source_id,
        len(fresh),
        len(plan) - len(fresh),
        len(obsolete),
        len(orphans),
        False,
    )


# --------------------------------------------------------------------------
# 3. Retrieval and answer generation
# --------------------------------------------------------------------------

_BUCKETS = {"text": "texts", "table": "tables", "image": "images"}


def parse_docs(docs: Iterable[Any]) -> dict[str, list[Document]]:
    """Group retrieved parent records by content type.

    Classification reads ``metadata[CONTENT_TYPE_KEY]``. The notebook guessed by
    calling ``base64.b64decode`` on each record, which misfires: b64decode is
    lenient and happily decodes ordinary prose, filing text as an image.
    """
    grouped: dict[str, list[Document]] = {"texts": [], "tables": [], "images": []}
    for doc in docs:
        metadata = getattr(doc, "metadata", None) or {}
        bucket = _BUCKETS.get(metadata.get(CONTENT_TYPE_KEY), "texts")
        grouped[bucket].append(doc)
    return grouped


def _source_label(metadata: dict[str, Any]) -> str:
    parts = []
    if metadata.get("source"):
        parts.append(f"source={metadata['source']}")
    if metadata.get("page_number") is not None:
        parts.append(f"page={metadata['page_number']}")
    return " | ".join(parts) or "source=unknown"


def format_evidence(doc: Document) -> str:
    """Render one retrieved record with explicit boundaries and its source."""
    metadata = doc.metadata or {}
    kind = metadata.get(CONTENT_TYPE_KEY, "text")
    body = doc.page_content
    if kind == "table":
        # Keep the grid: the HTML preserves rows, columns and headers that the
        # flattened text version loses.
        body = metadata.get("text_as_html") or doc.page_content
    return f"--- BEGIN {kind} | {_source_label(metadata)} ---\n{body}\n--- END {kind} ---"


def build_prompt(kwargs: dict[str, Any]) -> list[HumanMessage]:
    """Build the model input for one question.

    Returns a list of messages, which a chat model accepts. The notebook
    returned an uninvoked ``ChatPromptTemplate``, which a chat model cannot
    take as input.

    The answer model is text-only, and the pixels are never stored anyway, so
    a retrieved figure contributes the caption held as its parent's
    ``page_content``: the text the document printed around it.
    """
    grouped = kwargs["context"]
    question = kwargs["question"]

    docs = [*grouped["texts"], *grouped["tables"], *grouped["images"]]
    blocks = [format_evidence(doc) for doc in docs]
    context = "\n\n".join(blocks) if blocks else "(no evidence retrieved)"
    return [
        HumanMessage(content=ANSWER_PROMPT.format(context=context, question=question))
    ]


def grade_context(kwargs: dict[str, Any], model: Any) -> dict[str, Any]:
    """Corrective RAG: drop retrieved records the model judges irrelevant.

    One extra call per question, grading the whole retrieved set at once rather
    than one call per record. Returned in the shape ``build_prompt`` expects,
    so an empty result is the signal to abstain instead of generating an answer
    from evidence that does not bear on the question.

    ponytail: the kept blocks are read back as the integers in the reply. A
    grader that quoted a number out of a block would be misread; the prompt
    asks for numbers only, and a stricter contract (structured output) is the
    upgrade path if that ever shows up.
    """
    grouped = kwargs["context"]
    docs = [*grouped["texts"], *grouped["tables"], *grouped["images"]]
    if not docs:
        return kwargs
    blocks = "\n\n".join(
        f"[{number}]\n{format_evidence(doc)}"
        for number, doc in enumerate(docs, start=1)
    )
    reply = model.invoke(
        [
            HumanMessage(
                content=GRADE_PROMPT.format(question=kwargs["question"], blocks=blocks)
            )
        ]
    ).text
    keep = {int(number) for number in re.findall(r"\d+", reply)}
    kept: dict[str, list[Document]] = {bucket: [] for bucket in grouped}
    for number, doc in enumerate(docs, start=1):
        if number in keep:
            bucket = _BUCKETS.get((doc.metadata or {}).get(CONTENT_TYPE_KEY), "texts")
            kept[bucket].append(doc)
    return {"context": kept, "question": kwargs["question"]}


def answer_question(kwargs: dict[str, Any], model: Any) -> str:
    """Grade the retrieved evidence, then answer from what survived."""
    graded = grade_context(kwargs, model)
    if not any(graded["context"].values()):
        return ABSTAIN_ANSWER
    return model.invoke(build_prompt(graded)).text


def build_chain(retriever: Any, *, model: Any = None, with_sources: bool = False):
    """Question string in, answer string out (or ``{context, question, response}``).

    ``context`` is reported as retrieved, before grading, so a scorecard still
    shows what the index actually returned for the question.
    """
    model = model or chat_model()
    context = {
        "context": retriever | RunnableLambda(parse_docs),
        "question": RunnablePassthrough(),
    }
    answer = RunnableLambda(lambda kwargs: answer_question(kwargs, model))
    if with_sources:
        return context | RunnablePassthrough.assign(response=answer)
    return context | answer


# --------------------------------------------------------------------------
# Demo - never runs on import, and never on a bare `python rag_pipeline.py`
# --------------------------------------------------------------------------


def _main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Multimodal RAG pipeline")
    parser.add_argument(
        "--run",
        action="store_true",
        help="parse the PDF and call the Gemini API",
    )
    parser.add_argument("--pdf", default=str(PROJECT_DIR / "attention.pdf"))
    parser.add_argument("--question", default="What is the attention mechanism?")
    args = parser.parse_args()

    if not args.run:
        print("Dry run: nothing parsed, embedded or sent to any API.")
        print(f"  extractor       : {EXTRACTOR} (local, no OCR, no layout model)")
        print(f"  embedding model : {EMBEDDING_MODEL} (local, no API)")
        print(f"  answer model    : {ANSWER_MODEL} (Gemini, grade + answer)")
        print(
            f"  figure summary  : {'on' if IMAGE_SUMMARIES else 'off'} "
            "(IMAGE_SUMMARIES, one vision call per figure at ingest)"
        )
        print(f"  chunking        : {CHUNK_CHARS} chars, {CHUNK_OVERLAP} overlap")
        print(f"  figure caption  : {CAPTION_CHARS} chars each side")
        print(f"  table lead-in   : {CAPTION_CHARS} chars above the grid")
        print(f"  table detection : {'on' if FIND_TABLES else 'off'} (FIND_TABLES)")
        print(f"  chroma dir      : {CHROMA_DIR}")
        print(f"  state database  : {STATE_DB}")
        print(f"  fingerprint     : {config_fingerprint()}")
        print("Pass --run to execute the pipeline for real.")
        return 0

    report = ingest_pdf(args.pdf)
    print(
        f"{report.source_id}: indexed={report.indexed} reused={report.reused} "
        f"deleted={report.deleted} orphans_removed={report.orphans_removed} "
        f"skipped={report.skipped}"
    )
    print(build_chain(report.retriever).invoke(args.question))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
