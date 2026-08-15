#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF -> Markdown fuer LLMWiki_V4
==============================
Extrahiert den Text aus einem PDF mit pypdf, schreibt ihn als Markdown-Datei
mit Seitenueberschriften und setzt die Seitenzahlen als explizite Information.

Ziel: Jede Ausgabe ist eine einmalige, wiederverwendbare Rohquelle mit
Seitenstruktur, damit Q-Anker wie [[10-Raw/datei.md#Seite 4|Q1]] sauber moeglich sind.

Ablage: 60-PARA/Resources/Skripte/pdf_to_markdown.py
Standard-Ausgabe: Im selben Ordner wie die PDF-Datei, mit gleichem Basisnamen und .md

Verwendung:
    python pdf_to_markdown.py "10-Raw/Quelldatei.pdf"
    python pdf_to_markdown.py "10-Raw/Quelldatei.pdf" --out "10-Raw/Quelldatei.md"
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

try:
    from pypdf import PdfReader
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"pypdf fehlt. Bitte installieren: pip install pypdf\nFehler: {exc}") from exc


def default_raw_root() -> Path:
    return Path(__file__).resolve().parents[3] / "10-Raw"


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\xa0", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{2,}", "\n\n", text)
    text = text.strip()
    return text


def page_to_markdown(page_no: int, text: str) -> str:
    clean = normalize_text(text)
    if not clean:
        clean = "(Keine Textzeilen konnten aus dieser Seite extrahiert werden.)"
    return f"\n## Seite {page_no}\n\n{clean}\n"


def pdf_to_markdown(pdf_path: Path, out_path: Path) -> Path:
    reader = PdfReader(str(pdf_path))
    chunks = [f"# {pdf_path.stem}", "", f"_Quelle: {pdf_path.name}_", ""]

    for idx, page in enumerate(reader.pages, start=1):
        try:
            page_text = page.extract_text() or ""
        except Exception:
            page_text = ""
        chunks.append(page_to_markdown(idx, page_text))

    markdown = "\n".join(chunks).strip() + "\n"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown, encoding="utf-8")
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Extrahiert ein PDF als Markdown mit Seitenzahlen.")
    parser.add_argument("input", type=Path, help="Pfad zur PDF-Datei")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Zielpfad der Markdown-Datei (optional). Standard: im selben Waiting-Ordner, gleicher Basisname mit .md",
    )
    parser.add_argument(
        "--raw-root",
        type=Path,
        default=default_raw_root(),
        help="Pfad zum Raw-Archiv (Standard: <Vault>/10-Raw)",
    )
    parser.add_argument(
        "--archive-pdf",
        action="store_true",
        help="Verschiebt die PDF nach der Konvertierung aus dem Waiting-Ordner in das Raw-Archiv.",
    )
    parser.add_argument(
        "--finalize",
        action="store_true",
        help="Verschiebt die Markdown-Datei nach dem Ingest aus dem Waiting-Ordner endgültig in das Raw-Archiv.",
    )
    args = parser.parse_args()

    src = args.input.expanduser().resolve()
    if not src.exists():
        raise SystemExit(f"Datei nicht gefunden: {src}")
    if src.suffix.lower() != ".pdf":
        raise SystemExit(f"Keine PDF-Datei: {src}")

    raw_root = args.raw_root.expanduser().resolve()
    raw_root.mkdir(parents=True, exist_ok=True)

    if args.out is None:
        dst = src.with_suffix(".md")
    else:
        dst = args.out.expanduser().resolve()

    if src.parent.name == "Waiting_For_Ingestion":
        stale_md = src.with_suffix(".md")
        if stale_md.exists() and stale_md.resolve() != dst.resolve():
            stale_md.unlink()

    if src.parent.name == "Waiting_For_Ingestion" and dst.name != f"{src.stem}.md":
        dst = src.with_suffix(".md")

    result = pdf_to_markdown(src, dst)

    if src.parent.name == "Waiting_For_Ingestion" and args.archive_pdf:
        archive_pdf = raw_root / src.name
        if archive_pdf.exists() and archive_pdf.resolve() != src.resolve():
            archive_pdf.unlink()
        if src.resolve() != archive_pdf.resolve():
            shutil.move(str(src), str(archive_pdf))
        print(f"PDF aus Waiting-Ordner nach Raw verschoben: {archive_pdf}")

    if src.parent.name == "Waiting_For_Ingestion" and args.finalize:
        archive_md = raw_root / dst.name
        if archive_md.exists() and archive_md.resolve() != dst.resolve():
            archive_md.unlink()
        if dst.resolve() != archive_md.resolve():
            shutil.move(str(dst), str(archive_md))
        print(f"Markdown aus Waiting-Ordner nach Raw verschoben: {archive_md}")

    print(f"PDF -> Markdown: {src}")
    print(f"Ausgabe: {result}")
    print(f"Raw-Archiv: {raw_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
