#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF-OCR fuer LLMWiki_V4
=======================
Rendert jede Seite eines gescannten PDFs als Bild (300 dpi) und erkennt den
Text per Tesseract OCR (deutsch). Ausgabe ist eine Markdown-Datei mit
Seiten-Ueberschriften (## Seite N), die als Rohquelle in
10-Raw/Waiting_For_Ingestion/ ingestiert werden kann und exakte
Q-Anker ([[10-Raw/datei.md#Seite N|Qn]]) ermoeglicht.

Voraussetzungen:
    pip install pdfplumber pillow
    Tesseract OCR installiert (z.B. UB-Mannheim-Build), tessdata mit
    deu.traineddata. Liegen die Sprachdaten nicht im Installationsordner,
    TESSDATA_PREFIX auf das Verzeichnis mit deu.traineddata setzen.

Ablage des Skripts: 60-PARA/Resources/Skripte/pdf-ocr.py
Ablage der Ausgabe: 10-Raw/Waiting_For_Ingestion/<name>.md

Verwendung:
    python pdf-ocr.py <eingabe.pdf> [--out <ausgabe.md>] [--dpi 300]
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_OUT = SCRIPT_DIR.parents[1] / "10-Raw" / "Waiting_For_Ingestion"

TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSDATA = Path.home() / "AppData/Local/Tesseract-OCR/tessdata"


def ocr_page(img_path: Path, page_no: int) -> str:
    env = None
    if TESSDATA.exists():
        env = {"TESSDATA_PREFIX": str(TESSDATA)}
    result = subprocess.run(
        [TESSERACT, str(img_path), "stdout", "-l", "deu", "--psm", "3"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        shell=False,
    )
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        raise RuntimeError(f"Tesseract fehlgeschlagen auf Seite {page_no}")
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description="OCR eines gescannten PDFs")
    parser.add_argument("input", type=Path, help="Pfad zum PDF")
    parser.add_argument("--out", type=Path, default=None, help="Ausgabe-Markdown")
    parser.add_argument("--dpi", type=int, default=300, help="Aufloesung (Standard 300)")
    args = parser.parse_args()

    import pdfplumber

    src = args.input.resolve()
    if args.out is None:
        dst = DEFAULT_OUT / f"{src.stem}.md"
    else:
        dst = args.out.resolve()

    dst.parent.mkdir(parents=True, exist_ok=True)
    print(f"OCR {src} -> {dst}")

    chunks = []
    with pdfplumber.open(src) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages, 1):
            print(f"  Seite {i}/{total} ...", end=" ", flush=True)
            img = page.to_image(resolution=args.dpi)
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
                tmp_name = tmp.name
            img.save(tmp_name, format="PNG")
            text = ocr_page(Path(tmp_name), i)
            Path(tmp_name).unlink(missing_ok=True)
            chunks.append(f"\n\n## Seite {i}\n\n{text}")
            print(f"{len(text.splitlines())} Zeilen")

    with open(dst, "w", encoding="utf-8") as f:
        f.write("".join(chunks))
    print(f"Fertig: {dst}")


if __name__ == "__main__":
    main()
