"""Live evaluation of the multimodal RAG pipeline against a source PDF.

Eval-driven: every question carries the patterns its answer must contain
(``expect``) and the patterns that mark a known wrong answer (``reject``), so a
run produces a scorecard rather than a wall of prose to read by hand. Ground
truth comes from the paper itself, not from the pipeline's output.

The pipeline is used exactly as it ships - ``ingest_pdf`` then ``build_chain``
- and nothing in ``rag_pipeline`` is monkey-patched or reconfigured beyond the
documented environment overrides.

Command line:
    python evaluate_rag.py              # ingest if needed, then run all 5 (Gemini calls)
    python evaluate_rag.py --dry-run    # grader self-check only, no API calls
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parent

# .env is loaded before rag_pipeline is imported: that module resolves its
# environment overrides once, at import time, so anything set afterwards would
# be silently ignored.
load_dotenv(PROJECT_DIR / ".env", override=False)

import rag_pipeline as rp  # noqa: E402  (import order is load-bearing, see above)

DEFAULT_PDF = PROJECT_DIR / "attention.pdf"
DEFAULT_OUT = PROJECT_DIR / "eval_results.json"

#: Refusal wording the abstention policy may produce. The answer prompt says
#: "If the evidence does not contain the answer, say so", so any of these
#: counts as the policy firing.
ABSTAIN = (
    r"(does not|doesn'?t|do not|don'?t|cannot|can'?t|could not|couldn'?t|"
    r"is not|isn'?t|was not|wasn'?t|no |not )\s*\w*\s*"
    r"(contain|provide|specify|state|mention|include|report|give|given|"
    r"available|present|found|information|data|figure|cost)"
)

QUESTIONS: list[dict[str, Any]] = [
    {
        "id": "Q1",
        "scenario": "Exact fact (body text)",
        "question": (
            "What BLEU score does the big transformer model achieve on the "
            "WMT 2014 English-to-German translation task?"
        ),
        "truth": "28.4 (page 8, Table 2 and surrounding text)",
        "expect": [r"28\.4"],
        "reject": [],
    },
    {
        "id": "Q2",
        "scenario": "Table 3 row alignment (OCR stress test)",
        "question": (
            "According to Table 3, what is the BLEU (dev) score for the base "
            "model where dk is reduced to 16?"
        ),
        "truth": "25.1 - Table 3 row (B), dk=16, PPL 5.16, 58M params (page 9)",
        "expect": [r"25\.1"],
        # 25.4 is row (A) h=32, which also carries dk=16: the classic
        # row-alignment failure when the table grid is lost to OCR.
        "reject": [r"25\.4"],
    },
    {
        "id": "Q3",
        "scenario": "Figure 1 (image evidence)",
        "question": (
            "Based on Figure 1, what component immediately follows the "
            "Multi-Head Attention layer in the encoder stack?"
        ),
        "truth": "Add & Norm (residual connection followed by layer normalisation)",
        "expect": [r"add\s*&\s*norm|add\s+and\s+norm|layer\s*norm|residual"],
        "reject": [],
    },
    {
        "id": "Q4",
        "scenario": "Missing information (abstention)",
        "question": (
            "What was the total cost in US dollars to train the big "
            "transformer model on the 8 P100 GPUs?"
        ),
        "truth": "Not in the paper. Correct behaviour is to abstain.",
        "expect": [ABSTAIN],
        # Any dollar figure is a hallucination: the paper quotes FLOPs and
        # 3.5 days on 8 P100s, never a price.
        "reject": [r"\$\s?\d|\d+\s*(US )?dollars|USD\s?\d"],
    },
    {
        "id": "Q5",
        "scenario": "Multi-part extraction (formula generalisation)",
        "question": (
            "What optimizer and specific learning rate schedule formula were "
            "used for training?"
        ),
        "truth": (
            "Adam (beta1=0.9, beta2=0.98, eps=1e-9); "
            "lrate = d_model^-0.5 * min(step_num^-0.5, step_num * warmup_steps^-1.5), "
            "warmup_steps = 4000"
        ),
        # The answer model writes the formula as LaTeX, so these match the
        # names rather than the ASCII punctuation around them: d_model arrives
        # as d_{\text{model}} and min( as \min\!\big( .
        "expect": [
            r"\badam\b",
            r"warm[\s-]?up",
            r"4[,.]?000\b",
            r"\bd[\s_{-]*\\?(?:text|mathrm)?\{?model",
            r"\bmin\b|inverse square root",
        ],
        "reject": [],
    },
]


def grade(answer: str, case: dict[str, Any]) -> dict[str, Any]:
    """Rule grader: every ``expect`` must hit, no ``reject`` may hit."""
    matched = [p for p in case["expect"] if re.search(p, answer, re.I)]
    missed = [p for p in case["expect"] if p not in matched]
    tripped = [p for p in case["reject"] if re.search(p, answer, re.I)]
    return {
        "passed": not missed and not tripped,
        "matched": matched,
        "missed": missed,
        "tripped": tripped,
    }


def sources_of(context: dict[str, list[Any]]) -> list[dict[str, Any]]:
    """Flatten retrieved evidence to (content type, source, page) rows."""
    rows = []
    for bucket, docs in context.items():
        for doc in docs:
            meta = doc.metadata or {}
            rows.append(
                {
                    "bucket": bucket,
                    "content_type": meta.get(rp.CONTENT_TYPE_KEY),
                    "source": meta.get("source"),
                    "page_number": meta.get("page_number"),
                    "chars": len(doc.page_content or ""),
                    "has_html_grid": bool(meta.get("text_as_html")),
                }
            )
    return rows


def _self_check() -> None:
    """The graders are the only logic here, so they are what gets checked."""
    q2 = next(q for q in QUESTIONS if q["id"] == "Q2")
    assert grade("Table 3 gives a BLEU (dev) of 25.1.", q2)["passed"]
    assert not grade("The BLEU (dev) score is 25.4.", q2)["passed"]
    assert not grade("The table does not show it.", q2)["passed"]

    q4 = next(q for q in QUESTIONS if q["id"] == "Q4")
    assert grade("The evidence does not contain the training cost.", q4)["passed"]
    assert not grade("Roughly $300,000 based on P100 pricing.", q4)["passed"]
    # Abstention wording plus an invented figure must still fail.
    assert not grade(
        "The paper does not provide a cost, but it is about $150,000.", q4
    )["passed"]

    q5 = next(q for q in QUESTIONS if q["id"] == "Q5")
    assert grade(
        "Adam with lrate = d_model^-0.5 * min(step^-0.5, ...), warmup_steps = 4000",
        q5,
    )["passed"]
    assert not grade("They used Adam.", q5)["passed"]
    # The live answer model emits LaTeX, which the old ASCII patterns missed.
    assert grade(
        r"Adam, lrate = d_{\text{model}}^{-0.5}\;\min\!\big("
        r"\text{step\_num}^{-0.5}\big), warmup_steps = 4000",
        q5,
    )["passed"]


def run(pdf: Path, out: Path) -> int:
    started = time.perf_counter()
    retriever = rp.build_retriever()
    report = rp.ingest_pdf(pdf, retriever)
    print(
        f"ingest: source={report.source_id} indexed={report.indexed} "
        f"reused={report.reused} deleted={report.deleted} "
        f"orphans_removed={report.orphans_removed} skipped={report.skipped} "
        f"({time.perf_counter() - started:.1f}s)",
        flush=True,
    )

    chain = rp.build_chain(retriever, with_sources=True)
    results = []
    for case in QUESTIONS:
        t0 = time.perf_counter()
        result = chain.invoke(case["question"])
        answer = result["response"]
        row = {
            **{k: case[k] for k in ("id", "scenario", "question", "truth")},
            "answer": answer,
            "grade": grade(answer, case),
            "sources": sources_of(result["context"]),
            "seconds": round(time.perf_counter() - t0, 1),
        }
        results.append(row)
        verdict = "PASS" if row["grade"]["passed"] else "FAIL"
        print(f"{row['id']} {verdict} ({row['seconds']}s)", flush=True)

    payload = {
        "pdf": str(pdf),
        "models": {
            "embedding": rp.EMBEDDING_MODEL,
            "answer": rp.ANSWER_MODEL,
        },
        "extraction": {
            "extractor": rp.EXTRACTOR,
            "chunk_chars": rp.CHUNK_CHARS,
            "chunk_overlap": rp.CHUNK_OVERLAP,
            "caption_chars": rp.CAPTION_CHARS,
        },
        "fingerprint": rp.config_fingerprint(),
        "ingest": {k: v for k, v in report._asdict().items() if k != "retriever"},
        "results": results,
    }
    out.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")

    passed = sum(r["grade"]["passed"] for r in results)
    print("\n" + "=" * 78)
    print(f"SCORECARD  {passed}/{len(results)} passed")
    print("=" * 78)
    for row in results:
        verdict = "PASS" if row["grade"]["passed"] else "FAIL"
        print(f"\n[{row['id']}] {verdict}  {row['scenario']}")
        print(f"  expected : {row['truth']}")
        print(f"  answer   : {' '.join(row['answer'].split())[:400]}")
        if row["grade"]["missed"]:
            print(f"  missed   : {row['grade']['missed']}")
        if row["grade"]["tripped"]:
            print(f"  tripped  : {row['grade']['tripped']}")
        print("  evidence :")
        for src in row["sources"]:
            print(
                f"    {str(src['content_type']):6} source={src['source']} "
                f"page={src['page_number']} chars={src['chars']} "
                f"html_grid={src['has_html_grid']}"
            )
    print(f"\nwrote {out}")
    return 0 if passed == len(results) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="run the grader self-check only; no parsing, no API calls",
    )
    args = parser.parse_args()

    # Answers come back with non-breaking hyphens, Greek letters and
    # subscripts, none of which the Windows console's cp1252 default can
    # encode: printing the scorecard died on a single U+2011 after a complete
    # run. The results are worth more than the exact glyph.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    _self_check()
    if args.dry_run:
        print("grader self-check passed; no API calls made.")
        return 0
    return run(args.pdf.resolve(), args.out)


if __name__ == "__main__":
    raise SystemExit(main())
