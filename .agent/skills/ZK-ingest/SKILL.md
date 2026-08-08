---
name: ZK-ingest
description: >-
  Ingests raw source files (PDFs, web clippings, DOCX, AI chat logs, video transcripts) from Raw/
  into the molecular Zettelkasten according to LLMWiki_V3 guidelines. Generates Literature Notes,
  Narrative Notes, Permanent Notes, and updates MOCs.
---

# ZK-ingest — Zettelkasten Ingestion Skill

## Purpose
Use this skill whenever asked to process, ingest, or convert a raw file from `Raw/` into the molecular Zettelkasten (`Literature/`, `Narrative/`, `Permanent/`, `MOC/`).

---

## Workflow Steps

### Step 1: Pre-Output Validation & Context Check
1. Read the raw source file in `Raw/`.
2. Extract key concepts, central argument/narrative, explicit causality chains, and entities.
3. Search existing notes in `Literature/`, `Narrative/`, `Permanent/`, and `MOC/` to:
   - Avoid creating duplicate notes.
   - Find existing notes to link via `[[Wikilinks]]`.

### Step 2: Create Literature Note (`Literature/`)
Create a structured expert note in `Literature/<slug.md>`:
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
- **Content**: Complete expert excerpt. Formulate cause-and-effect chains explicitly (Why did X happen? What followed?). Define technical terms precisely on first mention.
- **Links**: Link all known concepts to existing notes.
- **Citations**: For text, use `([[Literature/quellenname|Q]])`. For videos, use `<a href="URL&t=Ns" title="HH:mm:ss">(V)</a>`.

### Step 3: Extract Narrative Notes (`Narrative/`)
If the source contains one or more distinct argumentation threads, create `Narrative/<slug.md>`:
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
- **Content**: Linked reasoning chain in your own words, referencing atomized Permanent Notes.

### Step 4: Generate Permanent Notes (`Permanent/`)
Extract distinct atomic ideas into `Permanent/<slug.md>`:
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
- **Content**: One idea per note, written in your own words, maximally linked to other Permanent Notes.

### Step 5: Update or Generate MOCs (`MOC/`)
- Check if 5 or more Permanent Notes exist under a common topic.
- If threshold is reached and no MOC exists, create `MOC/<thema-moc.md>` and register it in `MOC/_Index MOC.md`.

---

## Core Rules & Constraints
- **No Broken Links**: Never create a Wikilink to a non-existent file.
- **ISO 8601**: All dates must be `YYYY-MM-DD`.
- **Status Handling**: Set `status: auto` for new notes. Never revert `confirmed` or `review` status on existing notes.
- **Expert Quality**: No superficial summaries; focus on depth, causality, and precise definitions.
