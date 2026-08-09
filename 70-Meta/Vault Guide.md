---
type: meta
tags:
  - meta
created: 2026-08-08
updated: 2026-08-09
---

# Vault Guide — LLMWiki_V4

## Was ist dieses Wiki?

Ein **molekularer Zettelkasten** für gemischte Wissensquellen (PDFs, Videos, Bücher, KI-Chats, Urlaubs-Notizen, Transkripte), kombiniert mit PARA-Projektverwaltung. Alle Notizen werden **KI-generiert** und vom Nutzer nach Bedarf überarbeitet oder ergänzt.

---

## Ordnerstruktur

| Ordner | Inhalt |
|---|---|
| `10-Raw/Waiting_For_Ingestion/` | Eingangsordner für neue Rohquellen (PDF, Markdown-Clippings, DOCX, Transkripte). **Nur Dateien hier werden von der KI ingestiert.** |
| `10-Raw/` | Verarbeitete Rohquellen: Nach der Ingestierung werden Quelldateien hierher verschoben. Liegen hier auch die Ziele der Q-Beleglinks. |
| `20-Literature/` | Je Quelle eine KI-generierte Notiz: strukturiertes Experten-Exzerpt mit expliziten Kausalitätsketten. |
| `30-Narrative/` | Argumentationsstrang einer oder mehrerer Quellen, verlinkt auf Permanent Notes. Ermöglicht mehrere unabhängig verlinkbare Narrative pro Quelle. |
| `40-Permanent/` | Atomare Wissenseinheiten in eigenen Worten — das Herzstück des Zettelkastens. Dienen auch als synthetisierende (molekulare) Notizen. |
| `50-MOC/` | Maps of Content — reine Navigations-Hubs, entstehen emergent ab ≥5 Permanent Notes zu einem Thema. |
| `60-PARA/Projects/` | Zeitgebundene Projekte (Diplomarbeiten, Vault-Aufbau, ...). |
| `60-PARA/Areas/` | Dauerhaft relevante Lebensbereiche (HTL-Unterricht, Forschungsinteressen, ...). |
| `60-PARA/Resources/` | Referenzmaterial, KI-Anweisungen, Vorlagen-Ideen. |
| `60-PARA/Archive/` | Abgeschlossene Projekte und inaktive Notizen. |
| `70-Meta/` | `Templates/`, `Skills/`, Vault Guide und KI-Anweisungen. |
| `80-Assets/` | Bilder, Anhänge, exportierte Dateien. |

---

## Workflow

```
10-Raw/Waiting_For_Ingestion/  ←  Quelldatei ablegen (PDF, Clipping, Transkript, ...)
  │
  ▼  KI liest Rohquelle, erzeugt Notizen und verschiebt die Datei nach 10-Raw/
20-Literature/     Experten-Exzerpt: Was steht drin? Kausalitäten explizit.
  │
  ├──▶ 30-Narrative/    Argumentationsstrang → verlinkt auf Permanent Notes
  │
  └──▶ 40-Permanent/    Eine Idee, in eigenen Worten, maximal verlinkt
            │
            │  ab ≥5 Notes zum selben Thema (emergent)
            ▼
          50-MOC/       Navigations-Hub für ein Themenfeld
```

---

## Note-Typen

### Literature Note (`type: literature`)
Beantwortet: *Was steht in der Quelle?*
- Strukturiertes Experten-Exzerpt, keine oberflächliche Zusammenfassung
- Kausalitätsketten explizit ausformulieren (Warum X? Was folgte daraus?)
- Fachbegriffe bei Ersterwähnung präzise definieren
- Alle bekannten Konzepte/Entitäten als Wikilinks setzen

### Narrative Note (`type: narrative`)
Beantwortet: *Wie argumentiert die Quelle? Was ist der rote Faden?*
- Kein Fließtext über Quellinhalte — verlinkte Argumentationskette in eigenen Worten
- Verlinkt auf Permanent Notes für einzelne Behauptungen
- Eine Quelle kann mehrere Narrative-Notizen bekommen (je Argumentationsstrang eine)

### Permanent Note (`type: permanent`)
Beantwortet: *Was denke ich darüber?*
- Eine Note = eine Idee, in eigenen Worten
- Maximal mit anderen Permanent Notes verlinkt
- Dient auch als synthetisierende Notiz (mehrere Ideen zusammenführend) — kein eigener Typ nötig

### MOC — Map of Content (`type: moc`)
- Reiner Navigations-Hub, kein eigener Inhalt
- Listet und gruppiert Permanent Notes zu einem Themenfeld
- Entsteht emergent wenn ≥5 Notes sinnvoll zusammengefasst werden können

### AI Instruction (`type: ai_instruction`)
- Beinhaltet Verhaltensregeln, Prompts und Handlungsanweisungen für KI-Modelle im Vault (z. B. `70-Meta/KI-Anweisungen.md` sowie archivierte KI-Anweisungsdateien in `60-PARA/Resources/Alte_KI-Anweisungen/`).

---

## Status-Werte

| Wert | Bedeutung |
|---|---|
| `auto` | KI-generiert, noch nicht vom Nutzer geprüft |
| `confirmed` | Vom Nutzer geprüft und freigegeben |
| `review` | Muss überarbeitet werden |

> `confirmed` und `review` werden **ausschließlich vom Nutzer** vergeben. Die KI setzt niemals einen bestehenden `confirmed`- oder `review`-Status zurück auf `auto`.

---

## Verlinkungskonventionen

- **Wikilinks**: `[[Dateiname]]` oder `[[Dateiname|Anzeigetext]]`
- **Video-Zitate**: `<a href="URL&t=Ns" title="HH:mm:ss">(V)</a>` direkt nach der Aussage
- **Keine Broken Links**: KI verlinkt nur auf tatsächlich existierende Dateien
