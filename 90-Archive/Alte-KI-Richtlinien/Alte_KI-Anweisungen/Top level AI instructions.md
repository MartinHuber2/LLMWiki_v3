---
type: ai_instruction
created: 2026-05-19 08:30:00
updated: 2026-05-19 08:30:00
tags:
  - "AI_Instruction"
---

Diese Notiz legt die verbindliche Hierarchie und Priorität für alle KI-Anweisungen in diesem Vault fest. Jede KI ist angewiesen, Instruktionen in der folgenden Reihenfolge zu priorisieren:

1. **Höchste Priorität:** Inhalte dieser Notiz ([[Top level AI instructions]])
2. Inhalte im Ordner: Current AI Instructions
3. Inhalte im Ordner: Previous AI instructions


### Warnmeldung bei Nutzung veralteter Instruktionen
Falls eine Anweisung basierend auf Inhalten aus dem Ordner `Previous AI instructions` (Priorität 4) ausgeführt wird, weil keine aktuelleren Instruktionen in den Prioritäten 1 bis 3 vorhanden sind, muss die KI zwingend folgende Warnmeldung ausgeben:

> "AI ist nach previous AI instructions vorgegangen, weil keine aktuelleren vorhanden sind"

### Umgang mit Widersprüchen
Sollten innerhalb der Instruktionen widersprüchliche oder unklare Anweisungen festgestellt werden, ist die KI angewiesen:
1. Den Widerspruch bzw. die Unklarheit deutlich aufzuzeigen, sowohl allgemein als auch im konkreten Anwendungsfall.
2. Drei konkrete Lösungsvorschläge zu präsentieren, wie mit dem Widerspruch bzw. der Unklarheit verfahren werden soll und wie gegebenenfalls die AI Instructions umzuformulieren sind.

## Umgang mit Vault-Inkonsistenzen

In Fällen, in denen der historische Bestand des Vaults (Altnotizen) nicht den aktuellen Instruktionen entspricht, ist nach folgender Hierarchie und Logik vorzugehen:

1. **Priorität der Instruktionen:** Bestehende Notizen, die den Vorgaben in den [[AI Instructions]] widersprechen, sind als rein historisch bedingt zu betrachten. Aktuelle Anweisungen haben bei der Erstellung _neuer_ Inhalte grundsätzlich Vorrang vor der Struktur oder Logik alter Dokumente.
2. **Verlinkung und Benennung:** Beim Setzen von WikiLinks auf bestehende Altnotizen ist zwingend deren **aktueller Dateiname** zu verwenden, um das Protokoll zur Vermeidung von „Broken Links“ einzuhalten, auch wenn dieser Name nicht den aktuellen Benennungsregeln entspricht.
3. **Verzicht auf automatische Korrektur:** Die KI soll **keine** automatischen Updates (z. B. `_Update.md`) für alte Notizen erstellen, nur weil deren Metadaten-Schema (z. B. `Rel_source_ki` statt `Rel_KI`) veraltet ist. Eine Bereinigung erfolgt nur bei inhaltlichen Überarbeitungen.
4. **Bestandslogik als Fallback mit Rückfragepflicht:** Existiert für einen spezifischen Aspekt keine ausdrückliche Regel in den aktuellen Instruktionen, ist die neue Notiz orientiert an der Logik der Altnotizen zu erstellen. Erscheint diese Alt-Logik jedoch unklar, widersprüchlich oder qualitativ minderwertig, hat die KI **aktiv den Benutzer um Klärung zu bitten**, anstatt veraltete Muster blind zu kopieren.
5. **Zwingende Mindeststandards (Schutz der Systemintegrität):** Auch im Fallback-Modus (Punkt 4) dürfen folgende Mindeststandards **niemals** unterschritten werden:
    - **No Broken Links:** Es dürfen niemals WikiLinks auf nicht-existente Dateien erstellt werden.
    - **Striktes YAML-Protokoll:** Jede Notiz muss zwingend die Pflichtfelder `created`, `status`, `up` und `source_type` im Frontmatter enthalten.
    - **ISO 8601:** Datums- und Zeitangaben müssen ausnahmslos im Format `YYYY-MM-DD` bzw. `HH:mm:ss` erfolgen.
    - **Video-Zitierweise:** Bei Videoquellen ist zwingend das HTML-Anker-Format für Zeitstempel `<a href="..." title="..."> (V) </a>` unmittelbar nach der extrahierten Aussage zu verwenden.
    - **Konzeptionelle Einheit:** Jede atomare Konzept-Notiz darf nur genau ein eigenständiges Prinzip oder Gedanken beschreiben (Atomarität).