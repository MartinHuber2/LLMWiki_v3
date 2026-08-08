---
type: ai_instruction
tags:
  - meta
  - skill
created: 2026-08-08
updated: 2026-08-08
---

# Skill: ZK-ingest (Zettelkasten Ingestion)

> **Hinweis**: Diese Datei ist die in Obsidian sichtbare und editierbare Version des **`ZK-ingest`**-Skills. Die KI nutzt diese Anweisung zur automatischen Verarbeitung von Rohquellen aus `Raw/`.

---

## Zweck
Verarbeitung von Quelldateien (PDF, Markdown-Clipping, DOCX, KI-Chatlog, Video-Transkript) aus dem Ordner `Raw/` in den molekularen Zettelkasten (`Literature/`, `Narrative/`, `Permanent/`, `MOC/`).

---

## Ablaufschritte (Workflow)

### 1. Pre-Output Validation & Kontext-Check
1. Rohe Quelldatei im Ordner `Raw/` lesen.
2. Kernideen, Argumentationsstränge, Kausalitätsketten und Entitäten identifizieren.
3. Bestehende Notizen in `Literature/`, `Narrative/`, `Permanent/` und `MOC/` durchsuchen:
   - Duplikate vermeiden.
   - Passende Zieldateien für `[[Wikilinks]]` finden.

### 2. Literature Note erstellen (`Literature/`)
Erstellung einer strukturierten Notiz unter `Literature/<slug.md>`:

```yaml
---
type: literature
tags: []
source-type: pdf | video | buch | ai-chat | artikel | sonstiges
source-ref: ""
author: ""
year: ""
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: auto
---
```

- **Inhalt**: Vollständiges Experten-Exzerpt. Kausalitätsketten explizit ausformulieren (Warum X? Was folgte daraus?). Fachbegriffe bei Ersterwähnung präzise definieren.
- **Verlinkung**: Alle bekannten Konzepte als Wikilinks setzen.
- **Belege**: Bei Textquellen `([[Literature/quellenname|Q]])`, bei Videoquellen `<a href="URL&t=Ns" title="HH:mm:ss">(V)</a>`.

### 3. Narrative Notes extrahieren (`Narrative/`)
Falls die Quelle einen oder mehrere eigenständige Argumentationsstränge enthält, wird `Narrative/<slug.md>` erstellt:

```yaml
---
type: narrative
tags: []
sources: ["[[Literature/quellenname]]"]
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: auto
---
```

- **Inhalt**: Verlinkte Argumentationskette in eigenen Worten, die auf die atomaren Permanent Notes verweist.

### 4. Permanent Notes erstellen (`Permanent/`)
Extraktion atomarer Wissenseinheiten in `Permanent/<slug.md>`:

```yaml
---
type: permanent
tags: []
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: auto
---
```

- **Inhalt**: Eine Idee pro Note, in eigenen Worten, maximal mit anderen Permanent Notes verlinkt.

### 5. MOC-Genese & Aktualisierung (`MOC/`)
- Prüfen, ob ≥ 5 Permanent Notes unter einem gemeinsamen Überbegriff existieren.
- Falls ja und noch kein MOC existiert: `MOC/<thema-moc.md>` anlegen und in `MOC/_Index MOC.md` eintragen.

---

## Qualitätsregeln & Einschränkungen
- **No Broken Links**: Keine Wikilinks auf nicht-existierende Dateien setzen.
- **ISO 8601**: Datumsangaben immer im Format `YYYY-MM-DD`.
- **Status-Handling**: Neue Notizen erhalten `status: auto`. Bestehende Notizen mit `confirmed` oder `review` werden von der KI nicht verändert.
- **Experten-Standard**: Kausalität und Tiefe statt oberflächlicher Zusammenfassungen.
