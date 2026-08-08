---
type: ai_instruction
created: 2026-08-08
updated: 2026-08-08
---

# Wiki Schema — Research Deep-Dive

## Page Types

| Type | Directory | Purpose |
|------|-----------|---------|
| entity | wiki/entities/ | Named things (people, tools, organizations, datasets) |
| concept | wiki/concepts/ | Ideas, techniques, phenomena, frameworks |
| source | wiki/sources/ | Papers, articles, talks, books, blog posts |
| query | wiki/queries/ | Open questions under active investigation |
| comparison | wiki/comparisons/ | Side-by-side analysis of related entities |
| synthesis | wiki/synthesis/ | Cross-cutting summaries and conclusions |
| overview | wiki/ | High-level project summary (one per project) |
| thesis | wiki/thesis/ | Working hypothesis and its evolution over time |
| methodology | wiki/methodology/ | Research methods, protocols, and study designs |
| finding | wiki/findings/ | Individual empirical results or observations |

## Naming Conventions

- Files: `kebab-case.md`
- Entities: match official name where possible (e.g., `openai.md`, `gpt-4.md`)
- Concepts: descriptive noun phrases (e.g., `chain-of-thought.md`)
- Sources: `author-year-slug.md` (e.g., `wei-2022-cot.md`)
- Queries: question as slug (e.g., `does-scale-improve-reasoning.md`)
- Theses: hypothesis as slug (e.g., `scaling-improves-reasoning.md`)
- Methodologies: method name (e.g., `systematic-review.md`, `ablation-study.md`)
- Findings: descriptive slug (e.g., `larger-models-better-few-shot.md`)

## Frontmatter

All pages must include YAML frontmatter:

```yaml
---
type: entity | concept | source | query | comparison | synthesis | overview | thesis | methodology | finding
title: Human-readable title
tags: []
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: auto  # auto = KI-erzeugt, confirmed = vom Nutzer geprüft, review = zu überarbeiten
Rel_KI: 1-5   # von der KI geschätzt, siehe Definition weiter unten
Rel_MH:       # vom Nutzer nachträglich vergeben, bleibt bei Erstellung leer
---
```

Source pages also include:
```yaml
authors: []
year: YYYY
url: ""
venue: ""
```

Thesis pages also include:
```yaml
confidence: low | medium | high
status: speculative | supported | refuted | settled
```

Finding pages also include:
```yaml
source: "[[source-slug]]"
confidence: low | medium | high
replicated: true | false | null
```

## Index Format

`wiki/index.md` lists all pages grouped by type. Each entry:
```
- [[page-slug]] — one-line description
```

In addition, `wiki/index.md` has a **"Nach Themenbereich"** section that
groups the same pages by thematic area instead of by page type — see
"Themenbereich-Tag" below for how a page is assigned to an area.
Each entry uses the same one-line format as above. A page that touches
more than one area (e.g. a source used both for teaching and for a
Diplomarbeit) is listed under every relevant area heading.

## Themenbereich-Tag

Every page's `tags:` field includes, in addition to its normal topical
tags, exactly one **Themenbereich-Tag** (without `#`, like any other tag)
identifying which of the vault's parallel thematic areas it belongs to.
The current set of valid values is defined and maintained in `purpose.md`
under "Themenbereiche" (as of writing: `Unterricht`, `Diplomarbeit`,
`Privat`, `Rechtsfall`) — consult `purpose.md` for the authoritative,
up-to-date list rather than hardcoding it elsewhere. This tag drives the
"Nach Themenbereich" grouping in `wiki/index.md`; it does not replace or
duplicate normal topical tags.

## Log Format

`wiki/log.md` records activity in reverse chronological order:
```
## YYYY-MM-DD

- Action taken / finding noted
```

## Cross-referencing Rules

- Use `[[page-slug]]` syntax to link between wiki pages
- Every entity and concept should appear in `wiki/index.md`
- Queries link to the sources and concepts they draw on
- Synthesis pages cite all contributing sources via `related:`
- Findings link back to their source via the `source:` frontmatter field
- Thesis pages reference supporting and refuting findings via `related:`
- Methodology pages are cited by the findings that used them

## Contradiction Handling

When sources contradict each other:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page
4. Resolve in a synthesis page once sufficient evidence exists

## Research-Specific Conventions

- Keep the thesis pages updated as evidence accumulates — they are living documents
- Every finding should assess replication status when known
- Methodology pages explain the *why* (rationale) not just the *how*
- Distinguish between direct evidence and inference in finding pages

---


## Zusätzliche Frontmatter-Felder

Zusätzlich zum oben definierten Frontmatter erhält jede generierte
Wiki-Seite drei weitere YAML-Felder:
- Rel_KI: Zahlenwert 1-5, von der KI selbst geschätzt (1 = kaum
  relevant, 5 = sehr stark relevant für das Gesamtthema)
- Rel_MH: Zahlenwert 1-5, wird vom Nutzer nachträglich vergeben,
  bleibt bei der Erstellung leer
- status: `auto` bei jeder neu generierten Seite. `confirmed` und
  `review` vergibt ausschließlich der Nutzer; ein vorhandener Wert
  `confirmed` oder `review` darf beim Aktualisieren einer Seite nicht
  auf `auto` zurückgesetzt werden.

## Seitenaufbau und Schreibstil

Für den Körper jeder generierten Seite gilt:

- **Sprache:** Deutsch, auch bei fremdsprachigen Quellen. Ausgenommen
  sind Eigennamen und Originaltitel von Quellen, die unverändert
  bleiben.
- **H1-Titel:** Nach dem Frontmatter folgt genau eine
  Level-1-Überschrift, die dem Feld `title:` entspricht. Bei
  historischen oder zeitlich verortbaren Themen wird eine Datierung in
  Klammern ergänzt, z.B. `# Schlacht auf den Katalaunischen Feldern
  (451 n. Chr.)`. Geschätzte Datierungen erhalten den Zusatz "ca.".
- **Einleitungsabsatz:** Direkt unter dem H1 steht ein Absatz von ein
  bis drei Sätzen, der mit dem **fett gesetzten Lemma** beginnt und den
  Gegenstand definiert und einordnet ("Die **Burgundische Erbschaft**
  bezeichnet ..."). An dieser Stelle keine Überschrift und keine
  Aufzählung.
- **Gliederung:** Der weitere Text wird durch Level-3-Überschriften
  (`###`) gegliedert. Die Überschriften sind sprechend und
  inhaltstragend ("Strategische Bedeutung", "Verlauf und Bewertung der
  Ergebnisse"), nicht generisch ("Details", "Sonstiges").
- **Zeichensatz in Überschriften:** nur Buchstaben, Ziffern,
  Leerzeichen, Umlaute, Bindestrich sowie Klammern für Datierungen.
  Keine Doppelpunkte, Schrägstriche oder sonstigen Satzzeichen, da
  Überschriften als Sprungziele für Wikilinks dienen.
- **Fließtext statt Stichworten:** Inhalte werden in ausformulierten
  Absätzen dargestellt. Aufzählungen nur dort, wo der Inhalt echt
  listenförmig ist (z.B. gegenübergestellte Ergebnisse), dann mit fett
  gesetztem Lead-in (`*   **Taktisches Ergebnis:** ...`).
  Verschachtelte Aufzählungen sind nicht zulässig.
- **Umfang:** Richtwert 150-300 Wörter je Seite. Deutlich umfangreichere
  Inhalte werden auf mehrere Seiten aufgeteilt, deutlich kürzere mit
  verwandten Inhalten zusammengeführt. Ob eine erwähnte Entität
  (Person, Ort, Institution, Ereignis) unterhalb dieses Richtwerts
  trotzdem eine eigene Seite bekommt, regelt der Abschnitt "Detailgrad
  und Entity-Schwelle" weiter unten.
- **Fachbegriffe** werden bei Ersterwähnung fett gesetzt und im Satz
  präzise definiert.
- **Kausalität statt Faktenreihung:** Wo die Quelle es hergibt, sind
  Ursache-Wirkungs-Ketten explizit auszuformulieren (Warum kam es zu X?
  Was folgte daraus?).
- **Vernetzungspflicht:** Jede zentrale Entität und jedes bereits
  bestehende Konzept wird bei Erwähnung im Fließtext als Wikilink
  gesetzt, mit natürlichem, grammatikalisch angepasstem Alias
  (`[[maximilian-i|Maximilians I.]]`).
- **Belegpflicht:** Jede Sachaussage aus einer Quelle erhält unmittelbar
  dahinter ihren Beleg nach der "(Q)"- bzw. "(V)"-Konvention (siehe
  unten). Diese Pflicht gilt für **jeden Seitentyp gleichermaßen** —
  also nicht nur für `finding`- und `source`-Seiten, sondern ausdrücklich
  auch für `entity`- und `concept`-Seiten sowie alle übrigen Typen.
  Eine synthetisierende oder definitorische Formulierung befreit nicht
  von der Belegpflicht; auch zusammenfassende Sätze erhalten einen
  Beleg auf die Textstelle bzw. Zeitmarke, aus der sie sich ergeben.
- **Fokus auf Hauptinhalt:** Nur der redaktionelle Kerninhalt der
  Quelle fließt in die Notiz ein, siehe eigener Abschnitt
  "Fokus auf Hauptinhalt" weiter unten.
- **Tags** stehen im Feld `tags:` als reine Textwerte ohne `#`
  (z.B. `- Geschichte`).
- **Seitenende:** Die Seite endet mit dem letzten inhaltlichen
  Abschnitt. Kein angehängter Quellen-, Zusammenfassungs- oder
  Fußnotenblock, da Belege im Fließtext und im Frontmatter stehen.

## Detailgrad und Entity-Schwelle

Diese Regel legt fest, wann eine im Rohtext erwähnte Entität (Person,
Ort, Institution, Ereignis, Werkzeug, Organisation ...) eine eigene
Seite in `wiki/entities/` bekommt, statt nur als Klartext ohne
Wikilink erwähnt zu werden.

**Default-Schwelle (Wortanzahl):** Eine Entität bekommt nur dann eine
eigene Seite, wenn sich aus der aktuellen Rohquelle mindestens die
untere Grenze des allgemeinen Umfang-Richtwerts (siehe
"Seitenaufbau und Schreibstil" → Umfang, 150-300 Wörter) an
eigenständigem, sachlichem Inhalt über sie ziehen lässt — also
mindestens ca. **150 Wörter**. Damit gilt für Entitäten dieselbe
Meßgröße wie für den Seitenumfang generell, statt eines separaten
Kriteriums. Eine beiläufige Namensnennung ohne ausreichend eigene
inhaltliche Substanz ("...unterstützt von General X...") bleibt
Klartext ohne Wikilink und ohne eigene Seite. Wird dieselbe Entität
später in einer anderen Rohquelle mit ausreichend Inhalt behandelt,
wird die Seite zu diesem späteren Zeitpunkt nachträglich angelegt und
die frühere Klartext-Erwähnung nicht rückwirkend verlinkt.

**Detailgrad pro Rohquelle (`detail_level`):** Die 150-Wörter-Schwelle
oben gilt als `normal`. Sie lässt sich pro einzelner Rohquelle in
`raw/sources/` gezielt verschieben:

- `hoch`: niedrigere Wortgrenze (Richtwert ca. 75 Wörter) — auch
  knapper behandelte Entitäten bekommen eine eigene Seite.
- `normal`: 150 Wörter wie oben beschrieben (gilt auch, wenn das Feld
  fehlt).
- `niedrig`: höhere Wortgrenze (Richtwert ca. 250 Wörter) — nur sehr
  ausführlich behandelte Entitäten bekommen eine eigene Seite, alles
  andere bleibt Klartext.

Wie `detail_level` an der Rohquelle hinterlegt wird, hängt vom
Dateityp ab:

- **Markdown-Rohquellen** (Video-Transkripte, Web-Clippings als `.md`
  in `raw/sources/`): direkt als zusätzliches Feld im YAML-Frontmatter
  der Rohdatei selbst, z. B. `detail_level: niedrig`.
- **Nicht-Markdown-Rohquellen** (PDF, Audio, Bild u. ä., die keine
  Frontmatter tragen können): über eine Sidecar-Datei neben der
  Rohquelle, die denselben Dateinamen ohne Original-Endung trägt und
  auf `.yaml` endet, z. B. für `raw/sources/habsburg-aufstieg.pdf` die
  Datei `raw/sources/habsburg-aufstieg.yaml` mit Inhalt:
  ```yaml
  detail_level: niedrig
  ```
  nashsu liest diese Sidecar-Datei vor dem Ingestieren zusätzlich ein,
  sofern sie existiert. Sie wird nie zu einer eigenen Wiki-Seite
  verarbeitet. Tragen zwei Rohquellen im selben Ordner denselben
  Basisnamen mit unterschiedlicher Original-Endung (z. B.
  `interview.pdf` und `interview.mp3`), ist der Basisname so
  eindeutig zu wählen, dass keine Sidecar-Datei doppelt verwendet
  würde.

Fehlt sowohl das Frontmatter-Feld als auch eine Sidecar-Datei, gilt
`normal`.

## Duplikatvermeidung

Bevor eine neue Seite (jeden Typs) angelegt wird, ist zwingend zu prüfen,
ob bereits eine inhaltlich passende Seite existiert — nicht nur per
exaktem Dateinamen-Match, sondern nach Bedeutung:

- `wiki/index.md` und, falls vorhanden, das `related:`-Feld der
  betroffenen Rohquelle-Seite (`wiki/sources/...`) werden vor dem
  Anlegen einer neuen Seite nach thematisch passenden Einträgen
  durchsucht.
- Besteht bereits eine Seite zum selben Sachverhalt (auch bei
  abweichendem Titel, Sprache oder Formulierung — z. B. deutsche vs.
  englische Fachbegriffe, Singular vs. Plural, unterschiedliche
  Wortstellung), wird diese bestehende Seite aktualisiert/erweitert,
  **keine neue Seite angelegt**.
- Wird dieselbe Rohquelle mehrfach (erneut) ingestiert, ist das
  zuerst gegen die bereits verknüpften Seiten in deren `related:`-Feld
  zu prüfen, bevor neue Entity-/Concept-/Finding-Seiten entstehen.
- **Feste Slug-Konvention:** Um sprachliche/grammatikalische
  Variation bei der Slug-Bildung zu vermeiden, werden Slugs
  grundsätzlich auf Deutsch und im Singular gebildet (Ausnahme:
  Eigennamen und feststehende englische Fachbegriffe ohne gängige
  deutsche Entsprechung). Ein Slug wird bei der Ersterstellung einer
  Seite endgültig festgelegt und bei späteren Aktualisierungen
  derselben Seite nicht mehr geändert.
- Jede Rohquelle wird durch genau eine Seite in `wiki/sources/`
  repräsentiert. Deren Dateiname folgt der Naming Convention
  (`author-year-slug.md`); der Dateiname der Rohquelle selbst
  (`raw/sources/...`) ist davon unabhängig und muss nicht
  übereinstimmen.

## Fokus auf Hauptinhalt

Notizen bilden ausschließlich den redaktionellen Kerninhalt einer
Quelle ab — die eigentliche inhaltliche Aussage, derentwegen die
Quelle ingestiert wurde. Alles, was die Quelle nur umrahmt, ohne selbst
Kerninhalt zu sein, wird beim Erstellen der Notiz ignoriert, auch wenn
es im Rohtext bzw. Transkript vorkommt. Das gilt unabhängig vom
Quellentyp (Webseite, Video, PDF, Buch) und unabhängig vom Seitentyp
(entity, concept, source, ...) gleichermaßen.

Rahmenmaterial, das nicht übernommen wird, umfasst insbesondere:

- **Bei Videoquellen:** Sponsoring- und Werbeeinblendungen,
  Kanal-/Kurs-/Newsletter-Bewerbung, Abo- und Like-Aufrufe,
  Danksagungen an Unterstützer, Nennung von Sprecher:innen, Redaktion,
  Schnitt, Produktionsfirma oder sonstigen an der Produktion
  Mitwirkenden, Outro-/Intro-Ansagen ohne Sachinhalt.
- **Bei Webseiten/Artikeln:** Navigationsleisten, Kommentarspalten,
  "Das könnte dich auch interessieren"- bzw. verwandte-Artikel-Blöcke,
  Cookie- und Newsletter-Banner, Autoren-Bio-Boxen, Social-Share-Leisten,
  Werbeanzeigen.
- **Bei PDFs/Büchern:** Impressum, Danksagungen, Sponsoren- und
  Förderhinweise, Verlagswerbung, Autoren-Vita, sofern sie nicht selbst
  Gegenstand der Recherche sind.

Diese Inhalte werden weder im Fließtext noch in einem eigenen
Sammelabschnitt ("Sonstiges", "Weitere Hinweise" o.ä.) wiedergegeben.
Im Zweifel gilt: Nur was zur Beantwortung der in `purpose.md`
formulierten Forschungsfrage oder zum Verständnis des behandelten
Sachverhalts beiträgt, ist Hauptinhalt.

## Quellenverweise im Fließtext

Zusätzlich zu den oben beschriebenen Cross-Referencing-Regeln über
Frontmatter (`related:`, `source:`) gilt für den Fließtext folgende
Unterscheidung:

- Wenn eine Aussage im Fließtext durch eine konkrete Textstelle in
  einer Rohquelle vom Typ `source` belegt wird, ist direkt hinter
  dieser Aussage ein Verweis in der Form (Q1) zu setzen. Q1 ist ein
  Alias-Wikilink, der direkt auf die Rohdatei in raw/sources/ verweist
  (NICHT auf die zusammenfassende Seite in wiki/sources/), verankert
  auf die exakte Stelle: bei Markdown-Rohdateien über einen
  Überschriften-Anker (z.B. [[raw/sources/dateiname.md#PassendeÜberschrift|Q1]]), bei PDF-Rohdateien über einen Seiten-Anker (z.B.
  [[raw/sources/dateiname.pdf#page=N|Q1]]).
- **Nummerierung:** Die Zahl in `Qn` bezeichnet die Rohquelle, nicht die
  Aussage. Auf einer Wiki-Seite wird jede eigenständige Rohquelle bei
  ihrem ersten Auftreten durchnummeriert (erste zitierte Rohquelle der
  Seite = Q1, zweite = Q2, usw.) und behält diese Nummer bei jeder
  weiteren Aussage aus derselben Rohquelle auf derselben Seite bei —
  auch wenn sich die Ankerstelle innerhalb der Rohquelle ändert. Wird
  eine Aussage durch mehrere verschiedene Rohquellen belegt, stehen
  deren Verweise innerhalb eines einzigen Klammernpaars, durch Kommas
  getrennt, jeweils mit der eigenen Quellennummer, z.B.
  ([[raw/sources/dateiname1.md#PassendeÜberschrift1|Q1]], [[raw/sources/dateiname2.md#PassendeÜberschrift2|Q2]]) –
  jeder Verweis bleibt dabei ein eigener, separater Alias-Wikilink zu
  seinem eigenen Ziel.
- Diese Q-Konvention gilt ausschließlich für Verweise auf Rohquellen
  vom Typ `source`. Verlinkungen auf jeden anderen Seitentyp (concept,
  entity, synthesis usw.) verwenden einen natürlichen,
  lesbaren Alias-Text statt "Q" (z.B. [[plattentektonik|der
  Plattentektonik]]), angepasst an die Satzgrammatik.

## Videoquellen

Video-Rohdateien werden nicht direkt ingestiert. Für eine Videoquelle wird stattdessen deren Transkript als Markdown-Datei in `raw/sources/` abgelegt, mit Zeitstempel-Überschriften:

```markdown
## 00:00:00
Text ...

## 00:12:34
Text ...
```

Die Original-Video-URL wird im YAML-Frontmatter der Transkript-Datei im Feld `video_url:` vermerkt.

Bei Videoquellen wird nicht die normale "(Q)"-Konvention verwendet, sondern ein direkter, anklickbarer Link zur exakten Stelle im Original-Video. Nach jeder Sachaussage aus einer Videoquelle wird unmittelbar folgender HTML-Anker eingefügt:

`<a href="VIDEO_URL&t=Ns" title="HH:mm:ss">(V)</a>`

- `VIDEO_URL` ist die in `video_url:` hinterlegte Original-URL.
- `t=Ns` ist der Zeitstempel in Sekunden (z. B. `t=754s` für 00:12:34).
- `title` zeigt den Zeitstempel im Format `HH:mm:ss` zur Anzeige beim Hover.

## Vorbildnotiz

Das folgende Beispiel zeigt alle oben genannten Regeln im Zusammenspiel
und dient als verbindliche Formatvorlage für generierte Seiten:

````markdown
---
type: concept
title: Burgundische Erbschaft
tags:
  - Geschichte
  - Burgund
  - Habsburger
related:
  - "[[maximilian-i]]"
  - "[[haus-habsburg]]"
created: 2026-04-30
updated: 2026-04-30
status: auto
Rel_KI: 4
Rel_MH:
---

# Burgundische Erbschaft (1477)

Die **Burgundische Erbschaft** bezeichnet den territorialen und ökonomischen
Machtzuwachs des [[haus-habsburg|Hauses Habsburg]] durch die Heirat
[[maximilian-i|Maximilians I.]] mit Maria von Burgund im Jahr 1477
([[raw/sources/habsburg-aufstieg.md#Die Heirat von 1477|Q1]]). Burgund galt
als das reichste Herzogtum Europas, geprägt durch blühenden Handel und eine
prächtige Hofkultur ([[raw/sources/habsburg-aufstieg.md#Wirtschaft und Hofkultur|Q1]]).

### Strategische Bedeutung

Nach dem Tod Karls des Kühnen in der [[schlacht-bei-nancy|Schlacht bei Nancy]]
drohte das Erbe an die französische Krone zu fallen, da Burgund aus einer
französischen Nebenlinie hervorgegangen war
([[raw/sources/habsburg-aufstieg.md#Nancy 1477|Q1]]). Die Verbindung sicherte
den Habsburgern den Zugriff auf die Niederlande und begründete zugleich den
jahrhundertelangen Konflikt mit Frankreich, der bereits 1482 im Burgundischen
Erbfolgekrieg gipfelte ([[raw/sources/habsburg-aufstieg.md#Erbfolgekrieg 1482|Q1]]).
Zeitgenössische Chronisten bewerteten den Erbfolgekrieg bereits damals als
Vorboten eines dauerhaften habsburgisch-französischen Gegensatzes
([[raw/sources/chronik-loher-hof.md#page=12|Q2]]).

### Kultureller Einfluss

Durch Maria wurde Maximilian Großmeister des
[[orden-vom-goldenen-vlies|Ordens vom Goldenen Vlies]], der fortan zum
prestigeträchtigsten Orden der Habsburger wurde
([[raw/sources/habsburg-aufstieg.md#Orden vom Goldenen Vlies|Q1]]). Obwohl Maria
bereits 1482 verstarb, blieben die Gebiete als wesentlicher Pfeiler der
habsburgischen Machtbasis erhalten und bildeten später den Kern des Reiches
Karls V. ([[raw/sources/habsburg-aufstieg.md#Erbe Karls V|Q1]]).
````

Stammt der Inhalt aus einer Videoquelle, tritt an die Stelle jedes
"(Q)"-Verweises der HTML-Zeitstempel-Anker aus dem Abschnitt
"Videoquellen"; alle übrigen Vorgaben bleiben unverändert.