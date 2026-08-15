---
type: ai_instruction
created: 2026-08-08
updated: 2026-08-10
---

# KI-Anweisungen — LLMWiki_V4

Diese Datei ist die **verbindliche und höchstpriorisierte** Anweisung für alle KI-Interaktionen in diesem Vault. Sie hat Vorrang vor allen anderen Quellen, Notizen oder früheren Anweisungen.

---

## Prioritätshierarchie

1. **Diese Datei** (`70-Meta/KI-Anweisungen.md`) — höchste Priorität
2. **`70-Meta/Nutzerprofil.md`** — verbindliches Nutzerprofil (von Priorität 1 referenziert)
3. Spezifische Anweisungen in 60-PARA/Resources/
4. Kontext aus bestehenden Notizen des Vaults

Bei **Widersprüchen** zwischen Anweisungen: Widerspruch dem Nutzer klar benennen und drei konkrete Lösungsvorschläge präsentieren. Nicht eigenständig entscheiden.

---

## Grundprinzipien

### Experten-Skript-Standard
Notizen sind **keine oberflächlichen Zusammenfassungen**. Sie müssen:
- **Kausalitätsketten** explizit ausformulieren: Warum geschah X? Was folgte daraus?
- **Fachbegriffe** bei Ersterwähnung präzise definieren und konsistent verwenden
- Querverbindungen zu anderen Inhalten des Vaults aufzeigen
- Inhalte so aufbereiten, dass sie eigenständig lesbar und lehrbar sind

### Prüfungslern-Standard
Notizen müssen nicht nur wichtige Kernaussagen, sondern den **vollen Stoffumfang** einer Quelle über einen abgestuften Lernpfad abbilden. Dafür gilt:
- `Rel_AI = 1` deckt den ersten groben Überblick über die wichtigsten Inhalte ab; diese Notizen sind der Einstieg, nicht das gesamte Prüfungswissen.
- `Rel_AI = 2` erweitert den Überblick mit den wichtigsten Verbindungen, Zusammenhängen und Interpretationsebenen.
- `Rel_AI = 3` vertieft die systematische Wiederholung, Kausalitäten und die fachliche Struktur.
- `Rel_AI = 4` ergänzt Detailwissen und Spezialaspekte, die nach dem Verständnis der Kernlogik relevant werden.
- `Rel_AI = 5` erfasst die weniger relevanten, aber stofflich vollständigen Detailpunkte und Randaspekte der Quelle.
- Der gesamte Stoff einer Quelle muss in den Notizen abgebildet sein: Es ist **nicht erlaubt**, nur die `1`- und `2`-Notizen zu erzeugen, weil so Stofflücken für die Prüfung entstehen.
- Die KI erzeugt beim Ingest bewusst auch die weniger relevanten `4`- und `5`-Notizen, damit man allein durch die Notizen das gesamte Quellenmaterial für die Prüfung lernen kann.
- Im Frontmatter gibt es **keine `rel_KI`- oder `Rel_KI`-Felder mehr**. Das einzige kanonische Relevanzfeld ist `Rel_AI`.

### Atomarität
Jede Permanent Note beschreibt **genau eine Idee**. Wenn aus einer Quelle mehrere unabhängige Ideen entstehen, entstehen mehrere Permanent Notes.

### Sprache
Deutsch, außer bei Eigennamen und etablierten Fachbegriffen ohne gängige deutsche Entsprechung.

---

## Kommunikation mit dem Nutzer

### Keine Höflichkeitsfloskeln
Die KI kommuniziert sachlich, direkt und auf den Punkt. Unnötige Höflichkeitsfloskeln und Füllsel ("gerne", "sehr gerne", "vielen Dank", "kein Problem", "ich helfe dir gerne dabei" u.ä.) werden vermieden. Dazu zählt auch eine nichtssagende Einleitung/Verabschiedung ohne Informationsgehalt.

### Kritische Prüfung von Nutzervorschlägen
Die KI übernimmt Vorschläge des Nutzers **nicht ungeprüft**. Sie prüft sie kritisch auf Umsetzbarkeit, Konsistenz mit dem Vault und Zielerreichung. Hält sie einen Vorschlag für suboptimal oder fehlerhaft, macht sie einen **konkreten Gegen- bzw. Alternativvorschlag** und benennt dabei die jeweiligen **Vor- und Nachteile beider Optionen**. Die Entscheidung trifft der Nutzer; die KI führt nach der Entscheidung aus, auch wenn sie anders empfohlen hätte.

### Kritische Analyse neuer Projektaufgaben
Reicht der Nutzer neue Aufgaben, Ideen oder Anforderungen für ein Projekt ein (z.B. Ausbau-Ideen im Projekt `Zettelkasten Aufbau`), führt die KI **automatisch und ohne gesonderte Aufforderung** eine kritische Analyse durch, **bevor** sie die Aufgabe dokumentiert oder übernimmt:
- **Machbarkeit & Bedarf** prüfen: Löst die Aufgabe ein reales Problem? Besteht aktuell überhaupt ein Bedarf?
- **Konsistenz** mit Vault-Struktur, `KI-Anweisungen.md` und bestehenden Konventionen prüfen (z.B. Belegpflicht, Namenskonventionen, Link-Regeln).
- Bei erkennbaren Schwächen einen **konkreten Alternativ- oder Gegenvorschlag** mit Vor-/Nachteilen beider Optionen benennen.
- Die Aufgabe wird erst nach dieser Analyse aufgenommen; die Entscheidung trifft der Nutzer.

### Aktives Nachfragen bei Unklarheiten
Bei Unklarheiten oder offenen Punkten, deren Klärung zu einer **verbesserten Erfüllung der Aufgabe** führt, fragt die KI **selbstständig nach** — ohne dass der Nutzer sie dazu auffordert. Entscheidungskritische Unklarheiten klärt sie frühzeitig (idealerweise vor aufwändiger Arbeit), nicht erst am Ende.

### Modell-Fitness-Meldung
Die KI meldet **selbstständig**, wenn das aktuell gewählte Modell für die Aufgabe nicht geeignet ist. Indikatoren sind u.a.:
- Die Aufgabe ist für das Modell **zu komplex** (Wissensstand, Reasoning oder Anweisungstreue reichen nicht aus)
- Für die Aufgabe wurde ein **unnötig komplexes** (und damit unnötig teures) Modell gewählt
- Der **Kontextrahmen** (Kontextfenster/Input-Limit) ist für den Umfang der Aufgabe unzureichend

In allen diesen Fällen macht die KI einen konkreten Vorschlag, welches **andere, möglichst kostengünstige Modell** für die Aufgabe geeignet wäre, und begründet die Empfehlung knapp.

### Commit- und Push-Vorschläge
Die KI schlägt einen Git-Commit (und — sofern ein Remote konfiguriert ist — einen Push) **selten und nur zu passenden Zeitpunkten** vor. Zwischen zwei Commit-Vorschlägen müssen deutlich mehr Arbeitsschritte liegen — Richtwert: mindestens ~5 Arbeitsschritte oder ein klar abgeschlossener, zusammenhängender Arbeitsblock. Nach jedem einzelnen kleinen Arbeitsschritt (z.B. eine einzelne Dateiänderung, eine einzelne Regeländerung) wird **kein** Commit vorgeschlagen.

Passende Zeitpunkte sind z.B.:
- Ein **abgeschlossener Arbeitsblock** (z.B. Ingest einer Quelle, abgeschlossener Health-Check mit Fixes, größeres Refactoring).
- Mindestens ~5 Arbeitsschritte seit dem letzten Commit oder seit dem letzten abgelehnten Commit-Vorschlag.

**Vor riskanten Schritten** schlägt die KI **selbstständig und proaktiv** einen Commit (und Push) vor — unabhängig von der Anzahl der Arbeitsschritte seit dem letzten Commit. Ein riskanter Schritt liegt vor, wenn durch den Schritt der Vault potenziell korrumpiert werden könnte, z.B.:
- Ausprobieren eines neuen, ungetesteten Workflows oder Skripts
- Massenänderungen an vielen Dateien (z.B. Suchen-Ersetzen über den gesamten Vault)
- Strukturänderungen (Ordner umbenennen, Dateien verschieben)
- Experimentelle Ingestierungen mit ungewissem Ergebnis

Der Vorschlag benennt den Umfang (betroffene Dateien) und eine konkrete Commit-Message. Ausgeführt wird erst **nach expliziter Zustimmung** des Nutzers. Lehnt der Nutzer ab, wird der Vorschlag erst nach weiteren Arbeitsschritten erneut unterbreitet.

---

## Nutzerprofil

Das Nutzerprofil liegt als eigene Datei unter [[70-Meta/Nutzerprofil|`70-Meta/Nutzerprofil.md`]] und ist **verbindlicher Bestandteil dieser Anweisungen** (Priorität 1). Es speichert dauerhaft alle Informationen über den Nutzer, die für die weitere Zusammenarbeit von Bedeutung sein können.

### Lese- und Anwendungspflicht

Vor jeder inhaltsbezogenen Arbeit — insbesondere vor Notizen-Erstellung, Inhaltsaufbereitung und Datenextraktion aus Quellen — liest die KI `70-Meta/Nutzerprofil.md` und richtet Darstellung, Tiefe und Terminologie an den dort gespeicherten Informationen aus (z.B. Nutzung physikalisch/mathematisch vertrauter Anker).

### Aufnahmeregel

Teilt der Nutzer in einer Sitzung neue Informationen über sich mit, die für die Zusammenarbeit relevant sind (Hintergrund, Konventionen, Präferenzen, Kontext), ergänzt die KI diese in `70-Meta/Nutzerprofil.md` unter **Bekannte Informationen** und aktualisiert dort sowie hier das Datumsfeld `updated` im Frontmatter.

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
- **Zusätzliche Kontext-Verlinkungen im Fließtext**: Zusätzlich zu den Q- und V-Verweisen müssen thematisch passende Verknüpfungen zu anderen Notizen im Fließtext mit passenden Alias-Wikilinks erfolgen, sofern der Satzfluss dies sinnvoll erlaubt. Das gilt für alle Notiztypen: Literature, Narrative, Permanent und MOC. Die Verknüpfung dient der inhaltlichen Vernetzung und muss im Text nicht künstlich wirken; sie ist dann erforderlich, wenn ein bereits bekannter Fachbegriff, ein Thema oder eine inhaltliche Referenz im Fließtext erwähnt wird und ein passender interner Zusammenhang besteht.
- **No Broken Links**: Es werden **ausschließlich** Links auf tatsächlich existierende Dateien gesetzt. Ist eine Zieldatei noch nicht vorhanden, bleibt der Begriff Klartext (kein Link)
- **Entitäten-Schwelle**: Eine eigene Permanent Note für eine Entität entsteht nur, wenn ausreichend Substanz vorhanden ist (Richtwert: ~150 Wörter eigenständiger Inhalt). Beiläufige Erwähnungen bleiben Klartext
- **Kollisionsfreiheit der Dateinamen**: Basisnamen von Dateien müssen im gesamten Vault eindeutig sein, damit bare `[[Wikilinks]]` eindeutig auflösen. Kollidiert der Basisname einer Rohquelle mit einer bestehenden Inhaltsseite (`20-Literature/`, `30-Narrative/`, `40-Permanent/`, `50-MOC/`), erhält die Rohquelle das Suffix ` (Quelle)`. Kollidiert der Basisname einer Literature Note mit einem MOC, erhält die Literature Note ein Herkunfts-Suffix (z.B. ` (Wikipedia)`). Bestehende Kollisionen werden bei einer Lint-Lauf behoben

---

## Frontmatter-Regeln

- **`status`**: Immer `auto` bei KI-Erstellung. `confirmed` und `review` werden **ausschließlich vom Nutzer** vergeben. Ein bestehender `confirmed`- oder `review`-Status darf von der KI **niemals** auf `auto` zurückgesetzt werden
- **Datums- und Zeitformat**: Ausnahmslos `YYYY-MM-DD hh:mm:ss` (z.B. `2026-08-15 14:32:18`). Diese Vorgabe gilt **für alle neuen und aktualisierten Notizen im ganzen Vault** — nicht nur für die aktuelle Quelle oder das aktuelle Gespräch.
- **`tags`**: Ohne `#`-Zeichen (z.B. `- Geologie`, nicht `- #Geologie`)
- **`related`**: Nur Links auf existierende Dateien
- **`Rel_AI`** (kanonisches Feld; es gibt keine `Rel_KI`-Variante mehr): Zahlenwert von `1` bis `5`, nur von der KI gesetzt. Die Rel-Einschätzung dient nicht nur der Wichtigkeit, sondern als feste Lernreihenfolge: `1 = zentraler Grundbaustein / erster Lernschritt`, `2 = sehr relevant / wichtige Verbindung`, `3 = vertiefende, aber bereits bekannte Schicht`, `4 = eher Detail / Zusatzwissen`, `5 = marginales Detail / nur im Anschluss`. Die Reihenfolge ist verbindlich: Der Benutzer soll mit `Rel_AI = 1` starten, danach `2`, dann `3`, danach `4` und erst zuletzt `5`.
- **`Rel_User`**: Analoges Feld, ebenfalls `1` bis `5`, aber von der KI **leer gelassen**. Der Nutzer kann es nach eigenem Urteil befüllen. Die Reihenfolge der Lernrelevanz gilt hier ebenfalls als Empfehlung: Der Nutzer kann gezielt zwischen Kernwissen und Detailniveau wechseln.
- **Lernpfad-Regel**: Beim Ingest werden zentrale, grundlegende Konzepte bewusst als `Rel_AI: 1` markiert; Verbindungen und wesentliche Kontext-Notizen als `Rel_AI: 2`; vertiefende Argumentations- und Kausalitätsnotizen als `Rel_AI: 3`; fachlich spezialisierte Ergänzungen als `Rel_AI: 4`; einzelne Rand- oder Detailaspekte als `Rel_AI: 5`. Dadurch kann der Benutzer den Stoff in abgestuften Schritten von grob nach fein durchlaufen: zuerst die Grundbausteine, dann die Verbindungen, danach das Detail.
- **Vollständigkeits-Regel für Prüfungslernen**: Beim Ingest sind **nicht nur** die ersten relevanten Stufen zu produzieren. Die KI muss den gesamten Stoff einer Quelle in den Notizen widerspiegeln: `1` bis `5` werden als abgestufter, kompletter Lernpfad erzeugt. `1` und `2` liefern den ersten Überblick, `3` und `4` die vertiefende Wiederholung und `5` die Randdetails. So kann man allein durch die Notizen auf die Prüfung lernen, ohne die Quelle erneut lesen zu müssen.
- **Zweistufiger Ingest**: Literature Notes liefern die konzeptionelle Verdichtung; Narrative und Permanent Notes müssen ausführlich genug sein, dass sie für Prüfungslernen und Wiederholung über den gesamten Quelleninhalt genutzt werden können. Dabei gilt die Lernpfad-Logik ebenfalls: Die Notizen mit `Rel_AI: 1` bilden den Startpfad; `Rel_AI: 2` und `3` ergänzen die tiefergehende Wiederholung; `Rel_AI: 4` und `5` enthalten die ergänzenden Details und Randaspekte, damit der gesamte Stoff der Quelle in den Notizen vollständig erfasst ist.
- **Ergebnisliste der Literature Note**: Jede Literature Note endet mit einem klaren Block `## Aus dieser Quelle hervorgegangene Notizen`, der alle aus derselben Quelle neu angelegten oder aktualisierten Notizen aufführt. Das umfasst mindestens die zugehörige Narrative Note und alle Permanent Notes, die aus dieser Quelle entstanden sind oder durch sie ergänzt wurden. Die Liste ist im Fließtext nach der Zusammenfassung zu platzieren und mit tatsächlichen Kanonikalnamen verlinkt.
- **Kontextuelle Alias-Links im Fließtext**: Zusätzlich zu allen Q-/V-Belegen müssen passende Verknüpfungen zu bestehenden Notizen im Fließtext mit sinnvollen Alias-Wikilinks erfolgen, sofern sie dem Satzfluss dienen. Das gilt für Literature, Narrative, Permanent und MOC gleichermaßen.
- **Allgemeine Gültigkeit**: Diese Regeln gelten **generell und künftig für den gesamten Vault**. Sie sind keine vorübergehende Gesprächsvereinbarung, sondern verbindliche Standardvorgaben für alle nachfolgenden Notizen, Aktualisierungen und Template-Generierungen.

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
created: YYYY-MM-DD hh:mm:ss
updated: YYYY-MM-DD hh:mm:ss
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
created: YYYY-MM-DD hh:mm:ss
updated: YYYY-MM-DD hh:mm:ss
status: auto
---
```

### Permanent Note
```yaml
---
type: permanent
tags: []
related: []
created: YYYY-MM-DD hh:mm:ss
updated: YYYY-MM-DD hh:mm:ss
status: auto
---
```

### MOC
```yaml
---
type: moc
tags: []
related: []
created: YYYY-MM-DD hh:mm:ss
updated: YYYY-MM-DD hh:mm:ss
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

### AI-Chat-Quellen (NotebookLM)

AI-Chat-Quellen (NotebookLM) sind Sonderfälle, da das Rohmaterial selbst eine KI-Synthese ist:

- **Primärbeleg**: Der ai-chat-Output selbst wird wie jede andere Quelle per Q-Ref belegt — die Rohdatei liegt in `10-Raw/`, der Q-Anker zeigt auf die Stelle im Fließtext.
- **Sekundärbelege (NotebookLM zitiert externe Quellen)**: Im NotebookLM-Output sind Quellenangaben als `($"..."`)-Marker gesetzt (z.B. `($"Wikipedia-Artikel Trilobiten"`)). Diese werden während des Ingests **unverändert in Fußnoten** konvertiert. Sie bleiben Fußnoten, weil sie Belege zweiter Hand sind — die KI hat die referenzierte Quelle nicht direkt gelesen.
- **Konvertierung beim Ingest**: Die KI wandelt `($"Beschreibung")` in `[^n]: Beschreibung` um. Bei Markern mit Link — `($"[Titel](url)")` — bleibt der Link erhalten: `[^n]: [Titel](url)`. Die Fußnoten werden am Ende der jeweiligen Notiz gesammelt, nicht im Fließtext verteilt.

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
