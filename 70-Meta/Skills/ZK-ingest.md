---
type: ai_instruction
tags:
  - meta
  - skill
created: 2026-08-08
updated: 2026-08-09
---

# Skill: ZK-ingest (Zettelkasten Ingestion)

> **Hinweis**: Diese Datei ist die verbindliche und einzige Skill-Anweisung für die Zettelkasten-Ingestion in diesem Vault. Die KI nutzt diese Anweisung zur automatischen Verarbeitung von Rohquellen aus `10-Raw/Waiting_For_Ingestion/`.

---

## Zweck
Verarbeitung von Quelldateien (PDF, Markdown-Clipping, DOCX, KI-Chatlog, Video-Transkript) aus dem Ordner `10-Raw/Waiting_For_Ingestion/` in den molekularen Zettelkasten (`20-Literature/`, `30-Narrative/`, `40-Permanent/`, `50-MOC/`). Nach erfolgreicher Ingestierung wird die Quelldatei nach `10-Raw/` verschoben.

**Es werden ausschließlich Dateien aus `10-Raw/Waiting_For_Ingestion/` ingestiert.** Dateien, die direkt in `10-Raw/` liegen, gelten als bereits verarbeitet und werden nicht (erneut) ingestiert.

---

## Ablaufschritte (Workflow)

### 1. Pre-Output Validation & Kontext-Check
1. Alle Quelldateien im Ordner `10-Raw/Waiting_For_Ingestion/` auflisten und jede einzeln verarbeiten.
2. Die rohe Quelldatei lesen.
3. Kernideen, Argumentationsstränge, Kausalitätsketten und Entitäten identifizieren.
4. Bestehende Notizen in `20-Literature/`, `30-Narrative/`, `40-Permanent/` und `50-MOC/` durchsuchen:
   - Duplikate vermeiden.
   - Passende Zieldateien für `[[Wikilinks]]` finden.

### 2. Literature Note erstellen (`20-Literature/`)
Erstellung einer strukturierten Notiz unter `20-Literature/<slug.md>`:

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
- **Belege**: Bei Textquellen verweist der Q-Link **direkt auf die exakte Stelle in der Rohdatei** unter `10-Raw/` — bei Markdown über den Überschriften-Anker `([[10-Raw/dateiname.md#Überschrift|Q]])`, bei PDF über den Seiten-Anker `([[10-Raw/dateiname.pdf#page=N|Q]])`. Bei Videoquellen `<a href="URL&t=Ns" title="HH:mm:ss">(V)</a>`.
- **Belegpflicht**: Gilt für alle KI-erzeugten Aussagen in allen Notiztypen (Literature, Narrative, Permanent, MOC) — jede Aussage, die aus einer bestimmten Quellenstelle hergeleitet wird, einschließlich Synthesen in eigenen Worten, erhält den passenden (Q)- bzw. (V)-Anker. `Qn` nummeriert die Rohquelle (erste zitierte = Q1, zweite = Q2, bleibt auch bei wechselnder Ankerstelle erhalten).

### 3. Narrative Notes extrahieren (`30-Narrative/`)
Falls die Quelle einen oder mehrere eigenständige Argumentationsstränge enthält, wird `30-Narrative/<slug.md>` erstellt:

```yaml
---
type: narrative
tags: []
sources: ["[[20-Literature/quellenname]]"]
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: auto
---
```

- **Inhalt**: Verlinkte Argumentationskette in eigenen Worten, die auf die atomaren Permanent Notes verweist.

### 4. Permanent Notes erstellen (`40-Permanent/`)
Extraktion atomarer Wissenseinheiten in `40-Permanent/<slug.md>`:

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

### 5. MOC-Genese & Aktualisierung (`50-MOC/`)
- Prüfen, ob ≥ 5 Permanent Notes unter einem gemeinsamen Überbegriff existieren.
- Falls ja und noch kein MOC existiert: `50-MOC/<thema-moc.md>` anlegen und in `50-MOC/_Index MOC.md` eintragen.

### 6. Quelle nach der Ingestierung verschieben
- Nach erfolgreichem Abschluss der Schritte 2–5 wird die Quelldatei von `10-Raw/Waiting_For_Ingestion/` nach `10-Raw/` verschoben — nur die Quelldatei selbst, nicht die erzeugten Notizen.
- Erzeugte Notizen werden dabei nicht verändert; die Q-/V-Anker zeigen weiterhin auf die nun in `10-Raw/` liegende Quelldatei.
- Erst durch das Verschieben gilt die Datei als verarbeitet. Beim nächsten Ingest-Lauf liegt sie nicht mehr in `Waiting_For_Ingestion/` und wird daher nicht erneut verarbeitet.

---

## Qualitätsregeln & Einschränkungen
- **No Broken Links**: Keine Wikilinks auf nicht-existierende Dateien setzen.
- **ISO 8601**: Datumsangaben immer im Format `YYYY-MM-DD`.
- **Status-Handling**: Neue Notizen erhalten `status: auto`. Bestehende Notizen mit `confirmed` oder `review` werden von der KI nicht verändert.
- **Experten-Standard**: Kausalität und Tiefe statt oberflächlicher Zusammenfassungen.
- **Kollisionsfreiheit der Dateinamen**: Basisnamen von Dateien müssen im gesamten Vault eindeutig sein, damit bare `[[Wikilinks]]` eindeutig auflösen. Kollidiert der Basisname einer Rohquelle mit einer bestehenden Inhaltsseite (`20-Literature/`, `30-Narrative/`, `40-Permanent/`, `50-MOC/`), erhält die Rohquelle das Suffix ` (Quelle)` (z.B. `10-Raw/Trilobiten (Quelle).md`). Kollidiert der Basisname einer Literature Note mit einem MOC, erhält die Literature Note ein Herkunfts-Suffix (z.B. ` (Wikipedia)`). Bei jedem Ingest: Basisnamen der neuen Dateien gegen den Bestand prüfen.
