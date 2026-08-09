#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vault-Inventar fuer LLMWiki_V4
===============================
Erzeugt aus dem Obsidian-Vault eine einzige Markdown-Datei, die alle
relevanten Markdown-Dateien des Vaults mit Pfad, Dateiname, Typ und einer
Kurzbeschreibung auflistet. Die Datei kann NotebookLM zur Verfuegung
gestellt werden, damit NotebookLM den Inhalt des Vaults kennt. Enthaelt
zusaetzlich einen Anweisungsblock fuer NotebookLM.

Ablage des Skripts: 60-PARA/Resources/Skripte/vault-inventar.py
Ausgabe (Standard): 60-PARA/Resources/Vault-Inventar.md

Verwendung:
    python vault-inventar.py                  # Standard-Vault und -Ausgabe
    python vault-inventar.py --vault <PFAD>   # anderer Vault
    python vault-inventar.py --out <PFAD>     # andere Ausgabedatei
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_VAULT = SCRIPT_DIR.parents[2]            # 60-PARA/Resources/Skripte -> Vault-Wurzel
DEFAULT_OUT = SCRIPT_DIR.parents[0] / "Vault-Inventar.md"  # 60-PARA/Resources/Vault-Inventar.md

# Inhalts-Ordner in gewuenschter Reihenfolge
INCLUDE_DIRS = ["20-Literature", "30-Narrative", "40-Permanent", "50-MOC", "60-PARA", "70-Meta"]
HOME_FILE = "Home.md"

# Ordnernamen, die nicht zum Wiki gehoeren (Loose-Folder, System, Assets)
EXCLUDE_DIRS = {
    ".obsidian", ".git", ".tmp.driveupload", "80-Assets", "ObsidianTest",
    "merged", "Nadja goes Austria", "Hochbehälter Reith", "FA Fruchtgenuss 2026",
    "Literatur", "Unterrichtsmaterialien", "Vova Mathe",
}

# Unterordner, die inhaltlich nicht in das Inventar gehoeren
EXCLUDE_SUBDIRS = {"Alte_KI-Anweisungen", "Templates", "Skripte"}

FOLDER_LABELS = {
    "20-Literature": "Experten-Exzerpte je Quelle",
    "30-Narrative": "Argumentationsstraenge",
    "40-Permanent": "Atomare Wissenseinheiten",
    "50-MOC": "Maps of Content",
    "60-PARA": "Projekte / Areas / Resources",
    "70-Meta": "KI-Anweisungen, Skills, Dokumentation",
}

NOTEBOOKLM_INSTRUCTIONS = """## Anweisungen an NotebookLM

Du erhaeltst den Inhalt einer persoenlichen Wissensdatenbank (Obsidian-Zettelkasten) in Form einer kuratierten, einzeldateibasierten Inventarliste. Beantworte Fragen zu diesem Vault ausschliesslich anhand der folgenden Informationen.

Hinweise:
- Jeder Listeneintrag entspricht einer Datei des Vaults; Pfad und Dateiname sind in Klammern bzw. als Code angegeben.
- Der Vault ist ein "molekularer Zettelkasten": Permanent Notes enthalten je genau eine Idee, Narrative Notes verbinden Argumentationsstraenge, MOCs (Maps of Content) sind Navigations-Hubs.
- Wenn du gebeten wirst, Erkenntnisse fuer den Vault zu produzieren, liefere diese als zusammenhaengenden Fliesstext. Versuche NICHT, strukturiertes Markdown (Frontmatter, Wikilinks, Ueberschriften-Hierarchien) zu erzeugen -- der Text wird anschliessend von einem spezialisierten Ingest-Prozess automatisch in die Vault-Struktur ueberfuehrt.
- Falls der gesamte Erkenntnisstand nicht in eine einzelne Ausgabe passt, brich an einer sinnvollen Stelle ab und kennzeichne das Ende mit "(Fortsetzung folgt -- bitte 'continue' eingeben)". Setze in der naechsten Ausgabe an genau dieser Stelle fort, bis alles vollstaendig ausgegeben ist.
- Wichtig: Der finale Fliesstext muss in sich vollstaendig und selbsterklaerend sein -- er wird als eigenstaendige Rohquelle im Vault gespeichert und ohne den urspruenglichen Chat-Kontext ingestiert.
"""


def parse_frontmatter(text: str) -> dict:
    """Liefert die Frontmatter-Felder als dict (einfache key: value-Paare)."""
    text = text.lstrip("\ufeff")
    fields = {}
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    if not m:
        return fields
    for line in m.group(1).splitlines():
        fm = re.match(r"^([A-Za-z_-][A-Za-z0-9_-]*):\s*(.*)$", line)
        if fm:
            key = fm.group(1).strip().lower()
            value = fm.group(2).strip().strip('"').strip("'")
            fields[key] = value
    return fields


def _clean_line(s: str) -> str:
    """Entfernt Markdown-Struktur aus einer Zeile fuer die Kurzbeschreibung."""
    s = s.lstrip("> ").strip()
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*_`~]", "", s)
    return s.strip()


def extract_summary(text: str) -> str:
    """Prioritaet: summary-Frontmatter > erster Textabsatz > erste H1-UEberschrift."""
    text = text.lstrip("\ufeff")
    fm = parse_frontmatter(text)
    if fm.get("summary"):
        return fm["summary"].strip()
    m = re.match(r"^---\r?\n.*?\r?\n---\r?\n(.*)$", text, re.DOTALL)
    body = m.group(1).strip() if m else text.strip()
    candidates = []
    for line in body.splitlines():
        s = _clean_line(line)
        if not s or s.startswith("#"):
            continue
        candidates.append(s)
    for s in candidates:
        if len(s) >= 40:
            return s[:200]
    if candidates:
        return candidates[0][:200]
    heading = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if heading:
        return heading.group(1).strip()[:200]
    return "(keine Beschreibung)"


def collect_pages(vault: Path) -> list:
    """Sammelt alle relevanten Markdown-Dateien als Dict-Liste."""
    pages = []
    for folder in INCLUDE_DIRS:
        base = vault / folder
        if not base.is_dir():
            continue
        for md in sorted(base.rglob("*.md")):
            rel = md.relative_to(vault).as_posix()
            parts = md.parts
            if any(p in EXCLUDE_DIRS or p in EXCLUDE_SUBDIRS for p in parts):
                continue
            if md.name == "Vault-Inventar.md":
                continue
            text = md.read_text(encoding="utf-8", errors="replace")
            fm = parse_frontmatter(text)
            pages.append({
                "path": rel,
                "name": md.name,
                "type": fm.get("type", ""),
                "summary": extract_summary(text),
            })
    return pages


def collect_raw(vault: Path) -> list:
    """Liefert die Dateinamen der Rohquellen (ohne Inhalte)."""
    raw = vault / "10-Raw"
    if not raw.is_dir():
        return []
    names = []
    for f in sorted(raw.iterdir()):
        if f.is_file() and f.name != ".gitkeep":
            names.append(f.name)
    return names


def build_report(vault: Path, pages: list, raw: list, now: str) -> str:
    lines = []
    lines.append("# Vault-Inventar — LLMWiki_V4")
    lines.append("")
    lines.append(f"_Automatisch erzeugt am {now} aus `{vault}`._")
    lines.append("")
    lines.append("Diese Datei fasst den Inhalt des Vaults (Pfad, Dateiname, Typ, Kurzbeschreibung) zusammen.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(NOTEBOOKLM_INSTRUCTIONS.strip())
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Startseite")
    lines.append("")
    home = vault / HOME_FILE
    if home.is_file():
        text = home.read_text(encoding="utf-8", errors="replace")
        lines.append(f"- **`{HOME_FILE}`** — {extract_summary(text)}")
    else:
        lines.append("- (keine Home.md)")
    lines.append("")

    for folder in INCLUDE_DIRS:
        group = [p for p in pages if p["path"].startswith(folder + "/")]
        label = FOLDER_LABELS.get(folder, "")
        lines.append(f"## {folder} — {label} ({len(group)})")
        lines.append("")
        if not group:
            lines.append("- (leer)")
        for p in group:
            type_part = f" ({p['type']})" if p["type"] else ""
            lines.append(f"- **`{p['path']}`**{type_part} — {p['summary']}")
        lines.append("")

    lines.append("## 10-Raw — Rohquellen (nur Dateinamen)")
    lines.append("")
    if raw:
        for name in raw:
            lines.append(f"- `{name}`")
    else:
        lines.append("- (leer)")
    lines.append("")

    total = len(pages)
    lines.append("---")
    lines.append("")
    lines.append(f"_Inventar-Summe: {total} Notizen aus {len(INCLUDE_DIRS)} Ordnern, {len(raw)} Rohquellen._")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Vault-Inventar fuer LLMWiki erzeugen")
    parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT, help="Pfad zum Vault-Root")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Ausgabedatei")
    args = parser.parse_args()

    vault: Path = args.vault.resolve()
    out: Path = args.out.resolve()
    if not vault.is_dir():
        print(f"FEHLER: Vault nicht gefunden: {vault}", file=sys.stderr)
        return 1

    pages = collect_pages(vault)
    raw = collect_raw(vault)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    report = build_report(vault, pages, raw, now)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8", newline="\n")
    print(f"Inventar geschrieben: {out}")
    print(f"  Notizen: {len(pages)} | Rohquellen: {len(raw)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
