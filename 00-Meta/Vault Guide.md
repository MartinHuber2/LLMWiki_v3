# Vault Guide — LLMWiki_V3

## Was ist dieses Wiki?

Ein **molekularer Zettelkasten** für gemischte Wissensquellen (PDFs, Videos, Bücher, KI-Chats, Urlaubs-Notizen, Transkripte), kombiniert mit PARA-Projektverwaltung. Alle Notizen werden **KI-generiert** und vom Nutzer nach Bedarf überarbeitet oder ergänzt.

---

## Ordnerstruktur

| Ordner | Inhalt |
|---|---|
| `Raw/` | Rohe Quelldateien — PDF, Markdown-Clippings, DOCX, Transkripte. Hier landet alles, bevor die KI es verarbeitet. |
| `Literature/` | Je Quelle eine KI-generierte Notiz: strukturiertes Experten-Exzerpt mit expliziten Kausalitätsketten. |
| `Narrative/` | Argumentationsstrang einer oder mehrerer Quellen, verlinkt auf Permanent Notes. Ermöglicht mehrere unabhängig verlinkbare Narrative pro Quelle. |
| `Permanent/` | Atomare Wissenseinheiten in eigenen Worten — das Herzstück des Zettelkastens. Dienen auch als synthetisierende (molekulare) Notizen. |
| `MOC/` | Maps of Content — reine Navigations-Hubs, entstehen emergent ab ≥5 Permanent Notes zu einem Thema. |
| `PARA/Projects/` | Zeitgebundene Projekte (Diplomarbeiten, Vault-Aufbau, ...). |
| `PARA/Areas/` | Dauerhaft relevante Lebensbereiche (HTL-Unterricht, Forschungsinteressen, ...). |
| `PARA/Resources/` | Referenzmaterial, KI-Anweisungen, Vorlagen-Ideen. |
| `PARA/Archive/` | Abgeschlossene Projekte und inaktive Notizen. |
| `Assets/` | Bilder, Anhänge, exportierte Dateien. |

---

## Workflow

```
Raw/  ←  Quelldatei ablegen (PDF, Clipping, Transkript, ...)
  │
  ▼  KI liest Rohquelle
Literature/     Experten-Exzerpt: Was steht drin? Kausalitäten explizit.
  │
  ├──▶ Narrative/    Argumentationsstrang → verlinkt auf Permanent Notes
  │
  └──▶ Permanent/    Eine Idee, in eigenen Worten, maximal verlinkt
            │
            │  ab ≥5 Notes zum selben Thema (emergent)
            ▼
          MOC/       Navigations-Hub für ein Themenfeld
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
- Beinhaltet Verhaltensregeln, Prompts und Handlungsanweisungen für KI-Modelle im Vault (z. B. `00-Meta/KI-Anweisungen.md` sowie archivierte KI-Anweisungsdateien in `PARA/Resources/Alte_KI-Anweisungen/`).

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
