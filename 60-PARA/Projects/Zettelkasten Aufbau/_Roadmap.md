---
type: project
status: aktiv
ziel: Aufbau eines molekularen Zettelkastens mit PARA-Projektverwaltung in Obsidian sowie Vorbereitung der Master-Vault-Struktur
deadline: 2026-08-31
tags:
  - meta/zettelkasten
created: 2026-08-08
updated: 2026-08-17 13:41:00
---

# 🚀 Zettelkasten Aufbau — Project Roadmap

Zentrale Roadmap für das PARA-Projekt `Zettelkasten Aufbau`: Aufsetzen, Befüllen und Systematisieren der Verzeichnis-, Regel- und Multi-Vault-Architektur für `LLMWiki_V4` (basierend auf dem Template [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki)).

> **Projekt-Logbuch**: Alle zeitlich abgeschlossenen Änderungsschritte und Commits sind chronologisch im [[Log|Projekt-Logbuch]] dokumentiert.

---

## Status & Checkliste

Das Projekt bleibt **aktiv**: Der Grundaufbau ist abgeschlossen, konkrete Ausbau-Ideen und System-Architekturen liegen vor.

- [x] Grundlegende Ordnerstruktur anlegen (`10-Raw/`, `20-Literature/`, `30-Narrative/`, `40-Permanent/`, `50-MOC/`, `60-PARA/`, `70-Meta/`)
- [x] Dashboards und Systemseiten erstellen (`Home.md`, `_Index MOC.md`)
- [x] Templates für alle Notiztypen anlegen
- [x] Dokumentation (`Vault Guide.md`) erstellen
- [x] Verbindliche `KI-Anweisungen.md` im Vault verankern
- [x] Alte KI-Anweisungen nach `60-PARA/Resources/Alte_KI-Anweisungen/` verschieben
- [x] Erste Quelldatei in `10-Raw/` ablegen und Testlauf durchführen
- [x] Nutzerprofil (`70-Meta/Nutzerprofil.md`) als eigene Datei ausgliedern und in `KI-Anweisungen.md` verankern
- [x] Hierarchische Tag-Taxonomie und `u/`-Nutzer-Tag-System verankern ([`70-Meta/Tag-Taxonomie.md`](file:///g:/Meine%20Ablage/Hidden/Synch/Obsidian/LLMWiki_V4/70-Meta/Tag-Taxonomie.md))
- [ ] Master- & Kinder-Vault Architektur einrichten (Details siehe [[Master-Kinder-Vault-Architektur]])
- [ ] Aufteilung & Entkopplung aller Initial-Skills im Master-Vault (Details siehe [[Master-Kinder-Vault-Architektur]])
- [ ] Täglichen Wartungszyklus einrichten (Quellen-Frische prüfen, Index aktualisieren, `hot.md` regenerieren) — inkl. Adaption auf Windows (kein macOS-launchd)

---

## Nächste Schritte

1. Quelldateien (PDF, Clippings, KI-Chatlogs, Transkripte) in den Ordner `10-Raw/` legen.
2. KI beauftragen, aus einer Quelldatei eine `Literature Note` und ggf. erste `Narrative` oder `Permanent Notes` zu erzeugen.
3. Master-Vault Sync-Skript (`sync_master.py`) gemaß [[Master-Kinder-Vault-Architektur]] erstellen.
4. Multimodale Ingest-Pipeline und NotebookLM-Erweiterungen umsetzen.

---

## Ausbau-Ideen

Konkretisierte Weiterentwicklungs-Ideen des Nutzers (System-Architekturen & Ingest-Pipelines):

- [ ] **Master- & Kinder-Vault Architektur:** Technische Umsetzung der Vererbung von Plugins (`main.js`, `manifest.json`, `styles.css`) und System-Skills (`70-Meta/Skills/`) bei gleichzeitiger Isolierung lokaler Einstellungen (`data.json`) und lokaler Tag-Taxonomien. Siehe ausführliche Spezifikation: [[Master-Kinder-Vault-Architektur]].
- [ ] **Aufteilung & Entkopplung aller Initial-Skills:** Systematische Modularisierung und Aufteilung aller vordefinierten KI-Skills (z. B. `ZK-ingest.md`, Linting-, Ingest- & Taxonomie-Skills) zur zentralen Pflege im Master-Vault. Siehe [[Master-Kinder-Vault-Architektur]].
- [ ] **Foto-Ingestierung & OCR-Text-Extraktion:** Workflow/Skript zur Ingestierung von Bilddateien (Fotos von Skripten, Infotafeln, Whiteboards, Buchseiten). Das Originalfoto wandert nach `80-Assets/`, der per OCR (oder Multimodal-LLM) extrahierte Text wird als Raw-Markdown in `10-Raw/Waiting_For_Ingestion/` abgelegt.
- [ ] **PDF-Foto-Extraktion:** Erweiterung des Skripts `60-PARA/Resources/Skripte/pdf_to_markdown.py` zur automatischen Extraktion eingebetteter Abbildungen aus PDFs. Bilder werden nach `80-Assets/` gespeichert und im Raw-Markdown direkt an der jeweiligen Position referenziert.
- [ ] **Automatische Abbildungsbeschreibung (Multimodale KI):** Generierung strukturierter Inhalts- und Kontextbeschreibungen für alle extrahierten oder hochgeladenen Bilder (`80-Assets/`), damit die KI während des ZK-Ingests den fachlichen Inhalt der Abbildungen versteht und in Literature-/Permanent-Notes einbinden kann.
- [ ] **NotebookLM-Ingest großer Datenquellen:** Erweiterter Ingest-Prozess für umfangreiche Quellsammlungen via NotebookLM. Nutzung kapitelweiser/thematischer Synthese-Prompts in NotebookLM, Übernahme des synthetisierten Fließtexts mit `($"..."`)`-Markern in `10-Raw/` und automatischer ZK-Ingest mit Konvertierung in Beleg-Fußnoten (`[^n]`).
- [ ] **NotebookLM-Audio-Ingest:** Pipeline zur Verarbeitung von Audiodateien (Vorlesungs-Mitschnitte, Sprachnotizen, Audio-Podcasts) über NotebookLM. Ablage der Audiodatei in `80-Assets/` (oder extern), Konvertierung des Audio-Transkripts/Chatlogs nach `10-Raw/` mit Belegpflicht über Zeitstempel.
- [x] **NotebookLM-Übernahme:** Inhalte aus NotebookLM in den Vault übernehmen — Behandlung als `source-type: ai-chat`. Workflow: Setup-Prompt zu Sessionsbeginn → Thema diskutieren → `/produce` → NotebookLM liefert Fließtext mit Quellenangaben als `($"..."`)`-Marker → Ablage in `10-Raw/Waiting_For_Ingestion/` → ZK-Ingest (Q-Refs auf die ai-chat-Rohdatei, `($"..."`)`-Marker werden in Fußnoten konvertiert). *Ersttest 2026-08-09: Schmirn Podcasts → 16 Permanent, 3 Narrative, MOC Schmirntal.*
- [ ] **Vault-Inventar-Skript für NotebookLM:** Skript, das alle relevanten Markdown-Dateien des Vaults (mit Pfad und Dateiname) in einer einzigen Markdown-Datei zusammenfasst, die NotebookLM zur Verfügung gestellt wird, damit NotebookLM den Vault-Inhalt kennt. Kann zusätzlich Anweisungen an NotebookLM enthalten.
- [ ] **Buch-Ingestion über Kapitel-Splitter:** Ingestion von Büchern über einen **Kapitel-Splitter** (Buch → einzelne `10-Raw`-Kapitel-Dateien), den die Ingest-Pipeline abschnittsweise verarbeitet. Bewusst **nicht** über NotebookLM als Hauptquelle — Kapitelzusammenfassungen wären eine zweite Destillation (Informationsverlust + Belegpflicht-Problem). NotebookLM remains reserved for overview/synthesis.
