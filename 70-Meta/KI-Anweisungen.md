---
type: ai_instruction
created: 2026-08-08
updated: 2026-08-08
---

# KI-Anweisungen — LLMWiki_V3

Diese Datei ist die **verbindliche und höchstpriorisierte** Anweisung für alle KI-Interaktionen in diesem Vault. Sie hat Vorrang vor allen anderen Quellen, Notizen oder früheren Anweisungen.

---

## Prioritätshierarchie

1. **Diese Datei** (`70-Meta/KI-Anweisungen.md`) — höchste Priorität
2. Spezifische Anweisungen in 60-PARA/Resources/
3. Kontext aus bestehenden Notizen des Vaults

Bei **Widersprüchen** zwischen Anweisungen: Widerspruch dem Nutzer klar benennen und drei konkrete Lösungsvorschläge präsentieren. Nicht eigenständig entscheiden.

---

## Grundprinzipien

### Experten-Skript-Standard
Notizen sind **keine oberflächlichen Zusammenfassungen**. Sie müssen:
- **Kausalitätsketten** explizit ausformulieren: Warum geschah X? Was folgte daraus?
- **Fachbegriffe** bei Ersterwähnung präzise definieren und konsistent verwenden
- Querverbindungen zu anderen Inhalten des Vaults aufzeigen
- Inhalte so aufbereiten, dass sie eigenständig lesbar und lehrbar sind

### Atomarität
Jede Permanent Note beschreibt **genau eine Idee**. Wenn aus einer Quelle mehrere unabhängige Ideen entstehen, entstehen mehrere Permanent Notes.

### Sprache
Deutsch, außer bei Eigennamen und etablierten Fachbegriffen ohne gängige deutsche Entsprechung.

---

## Vor dem Schreiben: Pre-Output-Validierung

Bevor die KI eine Note erstellt, muss sie intern prüfen und bei Bedarf bestätigen:
1. **Entitäten-Check**: Welche zentralen Entitäten/Konzepte kommen vor?
2. **Bestandscheck**: Existiert für diese Entität/dieses Konzept bereits eine Notiz im Vault?
3. **Link-Check**: Werden nur tatsächlich existierende Dateien verlinkt?
4. **Duplikat-Check**: Würde eine neue Note inhaltlich mit einer bestehenden überlappen?

---

## Verlinkungsregeln

- **Vernetzungspflicht**: Jedes bekannte Konzept und jede bekannte Entität, die im Fließtext vorkommt, wird als Wikilink gesetzt: `[[dateiname|grammatikalisch angepasster Anzeigetext]]`
- **No Broken Links**: Es werden **ausschließlich** Links auf tatsächlich existierende Dateien gesetzt. Ist eine Zieldatei noch nicht vorhanden, bleibt der Begriff Klartext (kein Link)
- **Entitäten-Schwelle**: Eine eigene Permanent Note für eine Entität entsteht nur, wenn ausreichend Substanz vorhanden ist (Richtwert: ~150 Wörter eigenständiger Inhalt). Beiläufige Erwähnungen bleiben Klartext

---

## Frontmatter-Regeln

- **`status`**: Immer `auto` bei KI-Erstellung. `confirmed` und `review` werden **ausschließlich vom Nutzer** vergeben. Ein bestehender `confirmed`- oder `review`-Status darf von der KI **niemals** auf `auto` zurückgesetzt werden
- **Datumsformat**: Ausnahmslos ISO 8601: `YYYY-MM-DD`
- **`tags`**: Ohne `#`-Zeichen (z.B. `- Geologie`, nicht `- #Geologie`)
- **`related`**: Nur Links auf existierende Dateien

---

## Note-Typen & Felder

### Literature Note
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

### Narrative Note
```yaml
---
type: narrative
tags: []
sources: []
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: auto
---
```

### Permanent Note
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

### MOC
```yaml
---
type: moc
tags: []
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

---

## Zitierregeln

Die **Belegpflicht** gilt für **alle KI-erzeugten Aussagen in allen Notiztypen** — Literature, Narrative, Permanent und MOC. Nicht nur das Exzerpt der Literature Note ist zu belegen: Wann immer die KI in einer beliebigen Notiz eine Aussage macht, die aus einer bestimmten Text- oder Videostelle einer Quelle hergeleitet wird, folgt unmittelbar hinter der Aussage der entsprechende Beleg. Synthesen in eigenen Worten befreien nicht von der Belegpflicht.

### Textzitate aus Quellen
Nach jeder belegten Aussage wird ein **Q-Alias-Wikilink** gesetzt, der **direkt auf die exakte Stelle in der Rohdatei** unter `10-Raw/` verweist — nicht auf die Literature Note:
- **Markdown-Rohdateien** (Transkripte, Clippings): über den Überschriften-Anker der betreffenden Stelle, z.B. `([[10-Raw/dateiname.md#Passende Überschrift|Q]])`
- **PDF-Rohdateien**: über den Seiten-Anker, z.B. `([[10-Raw/dateiname.pdf#page=12|Q]])`
- **Andere Formate** (DOCX u.ä.): so präzise wie möglich (z.B. über Abschnitt oder Seite), ansonsten auf die Rohdatei insgesamt

**Nummerierung:** Die Zahl in `Qn` bezeichnet die **Rohquelle**, nicht die Aussage. Auf einer Notiz wird jede eigenständig zitierte Rohquelle bei ihrem ersten Auftreten durchnummeriert (erste zitierte Rohquelle = Q1, zweite = Q2, usw.) und behält diese Nummer bei jeder weiteren Aussage aus derselben Rohquelle bei — auch wenn sich die Ankerstelle innerhalb der Rohquelle ändert. Wird eine Aussage durch mehrere Rohquellen belegt, stehen deren Verweise in einem einzigen Klammernpaar, durch Kommas getrennt, jeweils mit eigener Quellennummer: `([[10-Raw/datei1.md#Abschnitt|Q1]], [[10-Raw/datei2.pdf#page=5|Q2]])`.

Diese Q-Konvention gilt **in allen Notiztypen** (Literature, Narrative, Permanent, MOC). Die Belegpflicht aus dem Abschnitt oben umfasst damit ausdrücklich auch Textquellen.

### Videoquellen
Nach **jeder Aussage**, die aus einer bestimmten Aussage in einem Video hergeleitet wird — in **jedem** Notiztyp —, setzt die KI direkt den Zeitstempel-Anker:
```html
<a href="VIDEO_URL&t=Ns" title="HH:mm:ss">(V)</a>
```
- `N` = Sekunden (z.B. `t=754s` für 00:12:34)
- `title` zeigt den Zeitstempel beim Hover
- Gilt auch in Narrative- und Permanent Notes: Syntheseaussagen, die sich auf eine konkrete Stelle derselben Videoquelle stützen, erhalten den Anker dieser Stelle.

---

## MOC-Entstehung

Die KI legt **eigenständig kein neues MOC** an, solange nicht mindestens **5 Permanent Notes** unter einem einheitlichen Überbegriff sinnvoll zusammengefasst werden können. Bis dahin bleiben Notizen ohne MOC-Zuweisung — das `related:`-Feld und Obsidians Backlinks-Panel übernehmen die Navigation.

---

## Umgang mit Inkonsistenzen

- Bestehende `confirmed`- oder `review`-Notizen werden **nicht automatisch korrigiert**, auch wenn ihr Schema veraltet ist. Korrekturen nur bei expliziter Anfrage oder inhaltlicher Überarbeitung
- Existiert für einen Aspekt keine Regel in dieser Datei: Nutzer aktiv fragen, anstatt veraltete Muster zu übernehmen
- Links auf bestehende Altnotizen verwenden deren **aktuellen Dateinamen**, auch wenn dieser nicht den aktuellen Namenskonventionen entspricht

---

## Extraktions-Richtwert

- Permanent Notes: **150–300 Wörter** als Orientierung. Kein striktes Limit — Inhalt entscheidet
- Deutlich längere Inhalte werden auf mehrere Permanent Notes aufgeteilt
- Deutlich kürzere Inhalte werden mit inhaltlich verwandten Notes zusammengeführt
