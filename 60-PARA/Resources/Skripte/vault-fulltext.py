#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vault-Fulltext fuer NotebookLM (LLMWiki_V4)
===========================================
Erzeugt aus dem Obsidian-Vault eine einzige grosse Markdown-Datei, die die
Volltexte aller Wissens-Notizen (20-Literature, 30-Narrative, 40-Permanent,
50-MOC) samt Pfad- und Dateinamen-Header enthaelt. Die Datei wird NotebookLM
als Quelle zur Verfuegung gestellt, damit NotebookLM im Fliesstext seiner
Ausgaben mit `[[Kanonischer Name]]` auf bestehende Notizen verlinken kann.

Rohquellen (10-Raw), Archive (90-Archive) und Systemordner werden nicht
exportiert. 60-PARA und 70-Meta werden nur als Kurzbeschreibungen
aufgelistet (Anweisungen/Resources, keine Wissens-Notizen).

Ablage des Skripts: 60-PARA/Resources/Skripte/vault-fulltext.py
Ausgabe (Standard): 60-PARA/Resources/Vault-Fulltext.md

Verwendung:
    python vault-fulltext.py                  # Standard-Vault und -Ausgabe
    python vault-fulltext.py --vault <PFAD>   # anderer Vault
    python vault-fulltext.py --out <PFAD>     # andere Ausgabedatei
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_VAULT = SCRIPT_DIR.parents[2]            # 60-PARA/Resources/Skripte -> Vault-Wurzel
DEFAULT_OUT = SCRIPT_DIR.parents[0] / "Vault-Fulltext.md"  # 60-PARA/Resources/Vault-Fulltext.md

# Ordner, deren Volltext exportiert wird (Wissens-Notizen)
FULL_DIRS = ["20-Literature", "30-Narrative", "40-Permanent", "50-MOC"]
HOME_FILE = "Home.md"

# Ordner, die nur als Kurzbeschreibung aufgelistet werden
SUMMARY_DIRS = ["60-PARA", "70-Meta"]

# Ordnernamen, die nicht zum Wiki gehoeren (Loose-Folder, System, Assets)
EXCLUDE_DIRS = {
    ".obsidian", ".git", ".tmp.driveupload", "80-Assets", "ObsidianTest",
    "merged", "Nadja goes Austria", "Hochbehälter Reith", "FA Fruchtgenuss 2026",
    "Literatur", "Unterrichtsmaterialien", "Vova Mathe",
}

# Unterordner, die inhaltlich nicht exportiert werden
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

Du erhaeltst den Inhalt einer persoenlichen Wissensdatenbank (Obsidian-Zettelkasten) als Volltext. Jede Notiz ist durch drei Marker eindeutig abgegrenzt:
- `--- FILENAME: <Pfad>/<Dateiname>.md` — kennzeichnet Notizbeginn und Dateinamen als Pfadangabe
- `--- BEGIN NOTE ---` — Beginn des Notiztextes
- `--- END NOTE ---` — Ende des Notiztextes

Der Vault ist ein "molekularer Zettelkasten": Permanent Notes enthalten je genau eine Idee, Narrative Notes verbinden Argumentationsstraenge, MOCs (Maps of Content) sind Navigations-Hubs.

Verlinkungsregel fuer deine Ausgaben:
- Wenn du im Fliesstext deiner Ausgabe auf eine bestehende Notiz verweisen willst, setze einen **Alias-Wikilink** aus exaktem Dateinamen ohne Endung und grammatikalisch korrektem Anzeigetext: `[[Dateiname|Anzeigetext]]`. Der Anzeigetext ist die Form, die im Satz semantisch und grammatikalisch passt (z.B. `[[Reissenschuh-Rutschung|der Reissenschuh]]` oder `[[Tauernfenster|im Tauernfenster]]`), sodass der Fliesstext korrekt lesbar bleibt. Der Ingest-Prozess wandelt diese Verweise in echte Links um.
- Verwende ausschliesslich Dateinamen, die in diesem Dokument als `--- FILENAME:`-Eintrag vorkommen (oder aus dem Anhang "Kurzbeschreibungen" stammen).
- Erfinde keine Notiznamen. Existiert keine passende Notiz, belasse den Begriff im Klartext (ohne Klammern).
- Versuche NICHT, selbst strukturiertes Markdown (Frontmatter, Ueberschriften-Hierarchien) zu erzeugen -- der Text wird anschliessend von einem spezialisierten Ingest-Prozess in die Vault-Struktur ueberfuehrt.
- Falls der gesamte Erkenntnisstand nicht in eine einzelne Ausgabe passt, brich an einer sinnvollen Stelle ab und kennzeichne das Ende mit "(Fortsetzung folgt -- bitte 'continue' eingeben)".
- Wichtig: Der finale Fliesstext muss in sich vollstaendig und selbsterklaerend sein -- er wird als eigenstaendige Rohquelle im Vault gespeichert.
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


def strip_frontmatter(text: str) -> str:
    """Entfernt den Frontmatter-Block, liefert den reinen Notiztext."""
    text = text.lstrip("\ufeff")
    m = re.match(r"^---\r?\n.*?\r?\n---\r?\n?", text, re.DOTALL)
    if m:
        return text[m.end():].strip()
    return text.strip()


def _clean_line(s: str) -> str:
    """Entfernt Markdown-Struktur aus einer Zeile fuer die Kurzbeschreibung."""
    s = s.lstrip("> ").strip()
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*_`~]", "", s)
    return s.strip()


def extract_summary(text: str) -> str:
    """Prioritaet: summary-Frontmatter > erster Textabsatz > erste H1-Ueberschrift."""
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


def should_skip(rel: str, name: str, parts) -> bool:
    """Prueft, ob eine Datei ausgeschlossen wird."""
    if any(p in EXCLUDE_DIRS or p in EXCLUDE_SUBDIRS for p in parts):
        return True
    if name in ("Vault-Inventar.md", "Vault-Fulltext.md"):
        return True
    return False


def collect_full(vault: Path) -> list:
    """Sammelt die Volltexte aller Wissens-Notizen (mit Pfad + Dateiname)."""
    notes = []
    for folder in FULL_DIRS:
        base = vault / folder
        if not base.is_dir():
            continue
        for md in sorted(base.rglob("*.md")):
            rel = md.relative_to(vault).as_posix()
            if should_skip(rel, md.name, md.parts):
                continue
            text = md.read_text(encoding="utf-8", errors="replace")
            notes.append({"path": rel, "name": md.name, "body": strip_frontmatter(text)})
    return notes


def collect_summaries(vault: Path) -> list:
    """Sammelt Kurzbeschreibungen fuer 60-PARA und 70-Meta."""
    pages = []
    for folder in SUMMARY_DIRS:
        base = vault / folder
        if not base.is_dir():
            continue
        for md in sorted(base.rglob("*.md")):
            rel = md.relative_to(vault).as_posix()
            if should_skip(rel, md.name, md.parts):
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


def build_report(vault: Path, notes: list, summaries: list, now: str) -> str:
    lines = []
    lines.append("# Vault-Fulltext — LLMWiki_V4")
    lines.append("")
    lines.append(f"_Automatisch erzeugt am {now} aus `{vault}`._")
    lines.append("")
    lines.append("Diese Datei enthaelt den Volltext aller Wissens-Notizen des Vaults (20-Literature, 30-Narrative, 40-Permanent, 50-MOC) sowie die Startseite. Jede Notiz ist durch die Marker `--- FILENAME: <Pfad>/<Dateiname>.md`, `--- BEGIN NOTE ---` und `--- END NOTE ---` abgegrenzt.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(NOTEBOOKLM_INSTRUCTIONS.strip())
    lines.append("")
    lines.append("---")
    lines.append("")

    home = vault / HOME_FILE
    if home.is_file():
        text = home.read_text(encoding="utf-8", errors="replace")
        lines.append(f"--- FILENAME: {HOME_FILE}")
        lines.append("--- BEGIN NOTE ---")
        lines.append("")
        lines.append(strip_frontmatter(text))
        lines.append("")
        lines.append("--- END NOTE ---")
        lines.append("")

    for folder in FULL_DIRS:
        group = [n for n in notes if n["path"].startswith(folder + "/")]
        label = FOLDER_LABELS.get(folder, "")
        lines.append(f"# {folder} — {label} ({len(group)} Notizen)")
        lines.append("")
        if not group:
            lines.append("(leer)")
        for n in group:
            lines.append(f"--- FILENAME: {n['path']}")
            lines.append("--- BEGIN NOTE ---")
            lines.append("")
            lines.append(n["body"])
            lines.append("")
            lines.append("--- END NOTE ---")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("# Anhang: Kurzbeschreibungen (60-PARA, 70-Meta)")
    lines.append("")
    lines.append("Diese Dateien sind Anweisungen und Resources, keine Wissens-Notizen. Sie werden nur zur Orientierung aufgelistet und sind KEINE gueltigen Link-Ziele.")
    lines.append("")
    for folder in SUMMARY_DIRS:
        group = [p for p in summaries if p["path"].startswith(folder + "/")]
        label = FOLDER_LABELS.get(folder, "")
        lines.append(f"## {folder} — {label} ({len(group)})")
        lines.append("")
        if not group:
            lines.append("- (leer)")
        for p in group:
            type_part = f" ({p['type']})" if p["type"] else ""
            lines.append(f"- **`{p['path']}`**{type_part} — {p['summary']}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"_Fulltext-Summe: {len(notes)} Notizen im Volltext, {len(summaries)} Kurzbeschreibungen._")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Vault-Fulltext fuer NotebookLM erzeugen")
    parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT, help="Pfad zum Vault-Root")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Ausgabedatei")
    args = parser.parse_args()

    vault: Path = args.vault.resolve()
    out: Path = args.out.resolve()
    if not vault.is_dir():
        print(f"FEHLER: Vault nicht gefunden: {vault}", file=sys.stderr)
        return 1

    notes = collect_full(vault)
    summaries = collect_summaries(vault)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    report = build_report(vault, notes, summaries, now)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8", newline="\n")
    print(f"Fulltext geschrieben: {out}")
    print(f"  Notizen im Volltext: {len(notes)} | Kurzbeschreibungen: {len(summaries)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
