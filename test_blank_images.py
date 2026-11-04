"""Regression: blank raster images must not be indexed as figures.

Offline - no Gemini call, fake embeddings, a throwaway index. Runs under
pytest or directly:

    .venv\\Scripts\\python.exe test_blank_images.py
"""

import tempfile
from pathlib import Path

import pymupdf
from langchain_core.embeddings import DeterministicFakeEmbedding

import rag_pipeline as rp

PDF = rp.PROJECT_DIR / "BCS703_module_1.pdf"


def test_page33_indexes_des_diagram_not_blank_overlay():
    rp.IMAGE_SUMMARIES = False
    with tempfile.TemporaryDirectory() as tmp:
        retriever = rp.build_retriever(
            collection_name="test_blank_images",
            persist_directory=None,
            state_db=Path(tmp) / "state.sqlite3",
            embeddings=DeterministicFakeEmbedding(size=16),
        )
        rp.ingest_pdf(PDF, retriever)
        where = {"$and": [{"page_number": 33}, {"content_type": "image"}]}
        ids = retriever.vectorstore.get(where=where)["ids"]
        figures = [doc.metadata for doc in retriever.docstore.mget(ids)]
        retriever.docstore.close()

    with pymupdf.open(PDF) as document:
        images = [document.extract_image(m["xref"]) for m in figures if "xref" in m]
    # Figure 3.4 (the DES diagram) is indexed; the 1009x166 blank overlay
    # placed on the same page is not.
    assert [(i["width"], i["height"]) for i in images] == [(901, 1083)]


def test_soft_mask_shape_is_kept_flat_image_dropped():
    # Black ink whose shape lives only in the soft mask is a real figure.
    w = h = 8
    alpha = [255 if 2 <= i % w < 6 else 0 for i in range(w * h)]
    samples = b"".join(bytes((0, 0, 0, a)) for a in alpha)
    ink = pymupdf.Pixmap(pymupdf.csRGB, w, h, samples, 1)
    # White, not black: get_image_info matches xrefs by pixel digest, so two
    # identical black bases would both report the same xref.
    flat = pymupdf.Pixmap(pymupdf.csRGB, w, h, b"\xff" * (w * h * 3), 0)
    document = pymupdf.open()
    page = document.new_page()
    page.insert_image(pymupdf.Rect(0, 0, 100, 100), pixmap=ink)
    page.insert_image(pymupdf.Rect(0, 200, 100, 300), pixmap=flat)
    records = rp._page_images(page, [], source="t.pdf", page_number=1, caption_chars=0)
    assert [document.xref_get_key(r["xref"], "SMask")[0] for r in records] == ["xref"]


if __name__ == "__main__":
    test_soft_mask_shape_is_kept_flat_image_dropped()
    test_page33_indexes_des_diagram_not_blank_overlay()
    print("ok")
