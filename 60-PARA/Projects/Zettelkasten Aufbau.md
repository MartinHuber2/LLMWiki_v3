---
type: project
status: aktiv
ziel: Aufbau eines molekularen Zettelkastens mit PARA-Projektverwaltung in Obsidian
deadline: 2026-08-31
tags:
  - meta
  - zettelkasten
created: 2026-08-08
updated: 2026-08-09
---

# 🚀 Zettelkasten Aufbau

Erstes aktives PARA-Projekt: Aufsetzen und Befüllen der Verzeichnis- und Regelstruktur für `LLMWiki_V4`.

## Status

Das Projekt bleibt **aktiv**: Der Grundaufbau ist abgeschlossen, konkrete Ausbau-Ideen liegen vor. Siehe **Ausbau-Ideen** und **Nächste Schritte**.

- [x] Grundlegende Ordnerstruktur anlegen (`10-Raw/`, `20-Literature/`, `30-Narrative/`, `40-Permanent/`, `50-MOC/`, `60-PARA/`, `70-Meta/`)
- [x] Dashboards und Systemseiten erstellen (`Home.md`, `_Index MOC.md`)
- [x] Templates für alle Notiztypen anlegen
- [x] Dokumentation (`Vault Guide.md`) erstellen
- [x] Verbindliche `KI-Anweisungen.md` im Vault verankern
- [x] Alte KI-Anweisungen nach `60-PARA/Resources/Alte_KI-Anweisungen/` verschieben
- [x] Erste Quelldatei in `10-Raw/` ablegen und Testlauf durchführen
- [x] Nutzerprofil (`70-Meta/Nutzerprofil.md`) als eigene Datei ausgliedern und in `KI-Anweisungen.md` verankern
- [ ] Täglichen Wartungszyklus einrichten (Quellen-Frische prüfen, Index aktualisieren, `hot.md` regenerieren) — inkl. Adaption auf Windows (kein macOS-launchd)

## Nächste Schritte

1. Quelldateien (PDF, Clippings, KI-Chatlogs, Transkripte) in den Ordner `10-Raw/` legen.
2. KI beauftragen, aus einer Quelldatei eine `Literature Note` und ggf. erste `Narrative` oder `Permanent Notes` zu erzeugen.
3. Täglichen Wartungszyklus einrichten (siehe offene Checkliste oben).
4. Ausbau-Ideen umsetzen (siehe unten) — Start mit **PDF-Extraktions-Skript** (Bild-Extraktion + Bildbeschreibungen).

## Ausbau-Ideen

Konkretisierte Weiterentwicklungs-Ideen des Nutzers (noch nicht priorisiert):

- [ ] **PDF-Extraktions-Skript:** Skript, das Bilder und Text aus einem vorgegebenen PDF extrahiert und im Notfall auf OCR zurückgreift. Die Bilder werden nach `80-Assets/` extrahiert; zu jedem Bild wird eine kurze Beschreibung verfasst, damit die KI den Bildinhalt beim Ingest schneller erkennt und gezielt in die Notizen einfügen kann. Ein gescanntes PDF liegt aktuell nicht vor — der Hauptnutzen ist die bislang fehlende Bild-Extraktion.
- [x] **NotebookLM-Übernahme:** Inhalte aus NotebookLM in den Vault übernehmen — Behandlung als `source-type: ai-chat`. Workflow: Setup-Prompt zu Sessionsbeginn → Thema diskutieren → `/produce` → NotebookLM liefert Fließtext mit Quellenangaben als `($"..."`)`-Marker → Ablage in `10-Raw/Waiting_For_Ingestion/` → ZK-Ingest (Q-Refs auf die ai-chat-Rohdatei, `($"..."`)`-Marker werden in Fußnoten konvertiert). *Ersttest 2026-08-09: Schmirn Podcasts → 16 Permanent, 3 Narrative, MOC Schmirntal.*
- [ ] **Vault-Inventar-Skript für NotebookLM:** Skript, das alle relevanten Markdown-Dateien des Vaults (mit Pfad und Dateiname) in einer einzigen Markdown-Datei zusammenfasst, die NotebookLM zur Verfügung gestellt wird, damit NotebookLM den Vault-Inhalt kennt. Kann zusätzlich Anweisungen an NotebookLM enthalten.
- [ ] **Buch-Ingestion über Kapitel-Splitter:** Ingestion von Büchern über einen **Kapitel-Splitter** (Buch → einzelne `10-Raw`-Kapitel-Dateien), den die Ingest-Pipeline abschnittsweise verarbeitet. Bewusst **nicht** über NotebookLM als Hauptquelle — Kapitelzusammenfassungen wären eine zweite Destillation (Informationsverlust + Belegpflicht-Problem). NotebookLM bleibt für Übersicht/Synthese reserviert.
