# Vault-Fulltext — LLMWiki_V4

_Automatisch erzeugt am 2026-08-17 19:26 aus `G:\Meine Ablage\Hidden\Synch\Obsidian\LLMWiki_V4`._

Diese Datei enthaelt den Volltext aller Wissens-Notizen des Vaults (20-Literature, 30-Narrative, 40-Permanent, 50-MOC) sowie die Startseite. Jede Notiz ist durch die Marker `--- FILENAME: <Pfad>/<Dateiname>.md`, `--- BEGIN NOTE ---` und `--- END NOTE ---` abgegrenzt.

---

## Anweisungen an NotebookLM

Du erhaeltst den Inhalt einer persoenlichen Wissensdatenbank (Obsidian-Zettelkasten) als Volltext. Jede Notiz ist durch drei Marker eindeutig abgegrenzt:
- `--- FILENAME: <Pfad>/<Dateiname>.md` — kennzeichnet Notizbeginn und Dateinamen als Pfadangabe
- `--- BEGIN NOTE ---` — Beginn des Notiztextes
- `--- END NOTE ---` — Ende des Notiztextes

Der Vault ist ein "molekularer Zettelkasten": Permanent Notes enthalten je genau eine Idee, Narrative Notes verbinden Argumentationsstraenge, MOCs (Maps of Content) sind Navigations-Hubs.

Verlinkungsregel fuer deine Ausgaben:
- Wenn du im Fliesstext deiner Ausgabe auf eine bestehende Notiz verweisen willst, setze einen **Alias-Wikilink** aus exaktem Dateinamen ohne Endung und grammatikalisch korrektem Anzeigetext: `[[Dateiname|Anzeigetext]]`. Der Anzeigetext ist die Form, die im Satz semantisch und grammatikalisch passt (z.B. `[[Reissenschuh-Rutschung|der Reissenschuh]]` oder `[[Tauernfenster|im Tauernfenster]]`), sodass der Fliesstext korrekt lesbar bleibt. Der Ingest-Prozess wandelt diese Verweise in echte Links um.
- Verwende ausschliesslich Dateinamen, die in diesem Dokument als `--- FILENAME:`-Eintrag vorkommen (oder aus dem Anhang "Kurzbeschreibungen" stammen).
- Erfinde keine Notiznamen. Existiert keine passende Notiz, belasse den Begriff im Klartext (ohne Klammern).
- Versuche NICHT, selbst strukturiertes Markdown (Frontmatter, Ueberschriften-Hierarchien) zu erzeugen -- der Text wird anschliessend von einem spezialisierten Ingest-Prozess in die Vault-Struktur ueberfuehrt.
- Falls der gesamte Erkenntnisstand nicht in eine einzelne Ausgabe passt, brich an einer sinnvollen Stelle ab und kennzeichne das Ende mit "(Fortsetzung folgt -- bitte 'continue' eingeben)".
- Wichtig: Der finale Fliesstext muss in sich vollstaendig und selbsterklaerend sein -- er wird als eigenstaendige Rohquelle im Vault gespeichert.

---

--- FILENAME: Home.md
--- BEGIN NOTE ---

# 🏠 LLMWiki_V4

> Persönliches Wissenssystem — molekularer Zettelkasten + PARA

---

## 📥 Eingang

- **`10-Raw/`** — Rohe Quelldateien ablegen (PDF, Clippings, Transkripte, ...)

---

## 🗂 Zettelkasten

- **`20-Literature/`** — Experten-Exzerpte je Quelle
- **`30-Narrative/`** — Argumentationsstränge
- **`40-Permanent/`** — Atomare Wissenseinheiten *(Herzstück)*
- [[50-MOC/_Index MOC]] — Alle Maps of Content

---

## 🚀 Projekte

- [[60-PARA/Projects/Zettelkasten Aufbau]] — *aktiv*

---

## ⚙️ Meta

- [[70-Meta/Vault Guide]] — Workflow & Struktur
- [[70-Meta/KI-Anweisungen]] — Verbindliche KI-Regeln
- [[70-Meta/Skills/ZK-ingest]] — Skill-Anweisung für Zettelkasten-Ingestion

--- END NOTE ---

# 20-Literature — Experten-Exzerpte je Quelle (17 Notizen)

--- FILENAME: 20-Literature/Bildung im Wandel.md
--- BEGIN NOTE ---

# Bildung im Wandel
> Die Quelle analysiert den Bildungsbegriff als historisch variables Deutungsmuster – von der griechischen Paideia über Aufklärer wie Rousseau und Kant bis zur digitalen Gegenwart. Bildung wird als dynamischer, mehrdimensionaler Prozess verstanden, der Selbst- und Weltverhältnisse transformiert. Kritisch hinterfragt wird eine Verflachung zu Kompetenzen oder reinem „Lernen“. Stattdessen wird Bildung als lebenslange Reflexion und gesellschaftliche Aufgabe betont.

# Bildung im Wandel

Der Studienbrief eröffnet mit der Erinnerung, dass Bildung kein starrer Begriff ist, sondern ein historisch veränderliches und mehrdimensionales Deutungsmuster. Gerade weil der Bildungsbegriff im Kontext der Digitalisierung erneut auf dem Prüfstand steht, wird ein begriffsgeschichtlicher Rückblick notwendig, um die aktuelle Bedeutung von Bildung zu verstehen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 1|Q1]]. Die Quelle zeigt zugleich, dass Bildung nicht nur mit Schule, Wissensvermittlung und Kompetenzen zusammenhängt, sondern auch mit der Stellung des Menschen in der Welt, mit gesellschaftlichen Transformationen und mit der Frage, wie Selbstbildung in einer digitalisierten Lebenswelt funktioniert [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 2|Q1]].

Der Grundgedanke der Quelle ist, dass Bildung in der Geschichte immer wieder neu begrifflich gefasst werden musste. Sie wird als historisch gewordene Antwort auf Unsicherheiten, gesellschaftliche Umbrüche und erkenntnistheoretische Probleme verstanden. Damit ist Bildung kein bloßes Lernziel, sondern ein dynamischer Prozess der Selbst- und Weltverhältnisbildung [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 2|Q1]]. Das zeigt sich besonders an der Unterscheidung zwischen Bildung, Erziehung und Lernen: Die Quelle macht deutlich, dass diese Begriffe zwar verwoben sind, aber nicht synonym verwendet werden dürfen, weil sie verschiedenartige Aspekte der menschlichen Entwicklung markieren [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 2|Q1]].

Ein zentraler Wendepunkt der Quelle liegt in der Analyse, dass der Bildungsbegriff durch Digitalisierung nicht obsolet wird, sondern in einer neuen gesellschaftlichen Situation neu gedacht werden muss. Die Verbindung von Bildungsbegriff, Lernen und gesellschaftlicher Veränderung wird dabei als Frage nach der Zukunft des Lernens verstanden. Die Autor:innen unterscheiden deshalb zwischen einer bloßen „Digitale-Bildungsrevolution“-Rhetorik und einem ernsthaften bildungstheoretischen Verständnis, das die Substanz des Begriffs bewahrt [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 2|Q1]]. Der Studienbrief lässt sich damit als Kritik an einer rein kompetenzorientierten oder lernzentrierten Verflachung lesen, die Bildung zu einem bloßen Zweck-Mittel-Verhältnis macht [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 3|Q1]].

Die Quelle macht anschließend deutlich, dass Bildungsbegriffe im deutschsprachigen Raum auf lange historische Traditionen zurückgehen und dabei nicht einfach empirisch „gemessen“, sondern historisch und theoretisch verstanden werden müssen. Aus diesem Grund werden verschiedene Dimensionen von Bildung beschrieben: Bildung als individueller Bestand, Bildung als individuelles Vermögen, Bildung als individueller Prozess, Bildung als Selbstüberschreitung und Bildung als institutionalisierte Aktivität [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 5|Q1]]. Diese Dimensionen zeigen zugleich, dass Bildung immer in Spannung zwischen Subjekt, Gesellschaft, Kultur und Institution steht [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 6|Q1]]. Diese Struktur wird in [[Bildung als Deutungsmuster]], [[Bildung als Subjektkonstitution]] und [[Bildung als Selbstüberschreitung]] weiter ausgearbeitet und verbindet die historische Perspektive mit der Gegenwart [[Bildung zwischen Tradition und digitalem Wandel|Bildung zwischen Tradition und digitalem Wandel]].

Ein besonders wichtiges Element der Quelle ist der historische Rückblick auf die griechische Antike. Der Begriff [[Paideia]] wird als Bildungsverhältnis beschrieben, das den Menschen zur Vervollkommnung seiner Seele und zur Erkenntnis der Wahrheit führt. Die griechische Tradition ist hier nicht bloß ein Vorläufer, sondern der ursprüngliche Zugang zur Idee von Bildung als Selbstverhältnis und als Transformation des Blicks auf sich und die Welt [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 10|Q1]]. Die Quelle verbindet diese Perspektive mit der späteren historisch-pädagogischen Entwicklung, die den Menschen nicht mehr nur als vernunftbegabtes, sondern auch als gesellschaftlich handelndes Subjekt begreift [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 10|Q1]]. Gerade diese Linie von [[Paideia]] über [[Mittelalter und Renaissance]] bis zu [[Rousseau und die Erziehung zum Menschsein]], [[Kant und die Autonomie der Bildung]] und [[Humboldt und die allgemeine Menschenbildung]] zeigt, wie der Bildungsbegriff in der Moderne zu einer reflexiven Selbstbestimmung wurde.

Zusammengefasst zeigt die Quelle: Bildung ist weder bloße Inhaltsvermittlung noch reine Kompetenzsteigerung, sondern ein historisch geprägter, gesellschaftlich eingebetteter und reflexiver Prozess der Selbst- und Weltveränderung. Gerade deshalb bleibt der Bildungsbegriff für die digitale Gesellschaft zentral, auch wenn seine Gestalt und seine Aufgaben sich verändern [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 8|Q1]].

## Aus dieser Quelle hervorgegangene Notizen

- [[Bildung als Deutungsmuster]]
- [[Bildung als Subjektkonstitution]]
- [[Bildung als historisches Gedächtnis]]
- [[Paideia]]
- [[Bildung als individueller Bestand und Vermögen]]
- [[Bildung als Selbstüberschreitung]]
- [[Bildung zwischen Tradition und digitalem Wandel]]
- [[Mittelalter und Renaissance]]
- [[Rousseau und die Erziehung zum Menschsein]]
- [[Kant und die Autonomie der Bildung]]
- [[Humboldt und die allgemeine Menschenbildung]]
- [[Raum, Zeit und Entgrenzung in der digitalen Bildung]]

--- END NOTE ---

--- FILENAME: 20-Literature/Bildung in der digitalisierten Gesellschaft.md
--- BEGIN NOTE ---

# Bildung in der digitalisierten Gesellschaft
> Dieser Studienbrief untersucht Bildung als lebenslangen, vernetzten Prozess in digitalen Kontexten. Er unterscheidet zwischen Digitalisierung (technische Infrastruktur) und Mediatisierung (gesellschaftliche Durchdringung durch Medien) und zeigt, wie Bildung nicht mehr an feste Institutionen gebunden ist, sondern als „Seamless Learning“ Alltag, Arbeit und Freizeit verbindet. Zentrale Themen sind Selbstverantwortung, Partizipation und die Rolle digitaler Medien als Gestaltungsräume für Lernende.

# Bildung in der digitalisierten Gesellschaft

Der Studienbrief beginnt mit einer grundlegenden Bestimmung von Bildung als Transformation von Selbst- und Weltverhältnissen. Bildung ist damit nicht bloß die Vermittlung von Wissen und Können, sondern ein Prozess, in dem das Subjekt sich im Verhältnis zu anderen und zur Welt neu orientiert [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=6|Q1]]. Diese Perspektive ist für die digitale Gesellschaft wichtig, weil der Wandel der Lebenswelt nicht nur technische, sondern auch normative und soziale Folgen hat. In diesem Sinn ist [[Mediatisierung und Digitalisierung]] keine bloße Infrastrukturfrage, sondern eine Frage der Art und Weise, in der Menschen heute lernen, handeln und sich verorten [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=7|Q2]].

Die Quelle unterscheidet dabei zwischen Digitalisierung, Mediatisierung und Vernetzung. Digitalisierung beschreibt technische und infrastrukturelle Entwicklungen, Mediatisierung die gesellschaftliche Durchdringung des Alltags durch Medien und Vernetzung die verstärkte Verbindung von Menschen, Dingen und Lernkontexten. Diese Differenzierung ist wichtig, weil Bildung in der Gegenwart nicht nur in Schule oder Familie stattfindet, sondern in einer Vielzahl sich überlappender medialer Wirklichkeiten [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=8|Q3]]. Die digitale Lebenswelt verändert nicht nur Lernmittel, sondern auch die Bedingungen von Selbstbildung, Partizipation und Verantwortung. Die heranwachsende Generation nutzt mobile Geräte nicht nur zur Wissensabfrage, sondern beteiligt sich aktiv an der Gestaltung digitaler Lernräume und übernimmt dadurch zugleich mehr Selbstverantwortung für eigenes Lernen und Qualifizierung [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=7|Q4]].

Ein zentrales Konzept der Quelle ist deshalb Bildung als lebenslanger Prozess, der mit und über digitale Medien stattfindet. Die zentrale Frage lautet nicht nur, welche Inhalte gelernt werden, sondern wie Menschen in einer mediatisierten und vernetzten Gesellschaft ihre Orientierung, ihr Urteil und ihre Teilhabe entwickeln. Das führt zu der Idee einer Bildung, die nicht an feste Institutionen oder Zeitfenster gebunden ist, sondern als durchgehender und kontextübergreifender Lernprozess verstanden werden kann. Gerade deshalb ist [[Seamless Learning]] der passende Begriff für die Verbindung von Schule, Freizeit, Arbeit und Alltag in einer digitalen Lebenswelt [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=8|Q5]].

## Aus dieser Quelle hervorgegangene Notizen

- [[Bildung in einer vernetzten und mediatisierten Lebenswelt]]
- [[Mediatisierung und Digitalisierung]]
- [[Seamless Learning]]
- [[Vernetzung, Mobilität und Mit-Gestaltung]]
- [[Mediatisierung als Metaprozess]]

--- END NOTE ---

--- FILENAME: 20-Literature/How Brawn Led to Brains.md
--- BEGIN NOTE ---

# How Brawn Led to Brains

Das PBS-Eons-Video argumentiert gegen die Vorstellung, das Gehirn sei ein "Triumph des Denkens über die bloße Muskelkraft". Stattdessen zeigt es: **Gehirne und Muskeln sind seit langem verknüpft — genauer: ohne Muskeln (Brawn) wären Gehirne (Brains) nie entstanden** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=52s" title="00:00:52">(V)</a>). Es verfolgt die Evolution des Nervensystems vom Ediacarium bis zur Kambrium-Explosion.

## Was ein Gehirn ist

Gehirne sind **zwei bis drei Zentimeter physische Verlängerungen des Nervensystems** und dienen als dessen **zentralisierter Verarbeitungshub** — "Mission Control" (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=104s" title="00:01:44">(V)</a>). Das [[Gehirn als zentraler Verarbeitungshub]] verarbeitet die komplexen, ständig durch den Körper gesendeten Signale (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=111s" title="00:01:51">(V)</a>).

**Nervensysteme** bestehen aus **Neuronen**, die elektrische Signale leiten und Informationen durch den Körper tragen; jedes Neuron verbindet sich mit vielen anderen zu einem Netzwerk, das sensorische Zellen mit jenen verbindet, die reagieren können (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=125s" title="00:02:05">(V)</a>). Vor einem Gehirn braucht es also zuerst ein [[Nervensystem]] (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=138s" title="00:02:18">(V)</a>).

**Vielfalt der Gehirne** — von donutförmigen Krakengehirnen um die Speiseröhre (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=71s" title="00:01:11">(V)</a>) über erdnussgroße Krokodilgehirne (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=79s" title="00:01:19">(V)</a>) bis zum menschlichen Gehirn — 2 % der Körpermasse, aber 20 % des Energieverbrauchs, dauerhaft ~20 Watt (eine Glühbirne) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=88s" title="00:01:28">(V)</a>).

## Wann Nervensysteme entstanden

Die Haupttiergruppen mit zentralisiertem Nervensystem (Gehirn) sind **Wirbeltiere, Arthropoden, Mollusken** und unzählige Würmer; **Cnidarier** (Korallen, Quallen) haben stattdessen ein **verteiltes neuronales Netz** ohne Gehirn, und **Schwämme** scheinen gar kein klassisches Nervensystem zu besitzen (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=150s" title="00:02:30">(V)</a>).

Mithilfe der **[[Molekulare Uhr|molekularen Uhr]]** (Gene moderner Organismen + vorhersagbare Mutationsrate) schätzt man, dass die frühesten Nervensysteme im **Ediacarium**, vor etwa **625 Mio. Jahren**, auftraten (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=189s" title="00:03:09">(V)</a>). Davor waren die Vorfahren vermutlich mikroskopisch — bloße Zellbündel ohne Bedarf oder Platz für komplexe Nervensysteme (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=199s" title="00:03:19">(V)</a>).

Im Ediacarium klaffen Gene und Fossilbericht auseinander: Die [[Ursprung der Nervensysteme|molekulare Uhr]] sagt relativ fortgeschrittene Cnidarier-Vorfahren voraus, doch Fossilbelege fehlen weitgehend (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=212s" title="00:03:32">(V)</a>). Die Ediacara-Organismen taten offenbar wenig — kaum Hinweise auf Sinnesorgane oder Bewegung (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=239s" title="00:03:59">(V)</a>).

## Explosion im Kambrium

Der überwiegende Teil der Tiergruppen mit Gehirn erschien in einem geologischen Augenblick, in der **Kambrium-Explosion vor ~540 Mio. Jahren** — und offenbar **mit bereits voll intakten Gehirnen** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=262s" title="00:04:22">(V)</a>). Unter normalen Bedingungen ist das Gehirn das **erste Organ, das nach dem Tod zerfällt**: Es besteht aus energiehungrigen Zellen und hält seine Struktur nur durch Blutfluss (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=292s" title="00:04:52">(V)</a>). Deshalb ist der gut erhaltene Brains-Fossilbestand des frühen Kambriums bemerkenswert (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=303s" title="00:05:03">(V)</a>).

**[[Fossile Hirne des Kambriums|Erhaltung]]:** Dieselben Prozesse, die Weichkörperorganismen fossilisieren, erhalten auch Nervengewebe — etwa die [[Burgess Shale|Burgess-Schale]], wo Unterwasser-Schlammrutschen Tiere schnell bedeckten und vor Verwesung schützten (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=320s" title="00:05:20">(V)</a>). Frühe Gehirne erscheinen dort als dünne Kohlenstoff-Filme (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=328s" title="00:05:28">(V)</a>).

**Beispielfossilien ([[Fossile Hirne des Kambriums]]):**
- ***Cardiodictyon*** (518 Mio. Jahre, China): Verwandter der heutigen Samtwürmer; komplettes Nervensystem erhalten, Nervenknoten entlang des vielbeinigen Körpers plus einfaches Gehirn am Kopf (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=349s" title="00:05:49">(V)</a>).
- ***Kerygmachela*** (518 Mio., Grönland): einfaches Gehirn, das die Augen mit klauenartigen Frontalanhängen verbindet (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=371s" title="00:06:11">(V)</a>).
- ***Stanleycaris*** (506 Mio., Burgess): mit **_Anomalocaris_ verwandter** Räuber; in über 80 Fossilien ein komplexeres, in zwei Segmente geteiltes Gehirn, das mit drei Augen und vorderen Klauen verbunden ist (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=384s" title="00:06:24">(V)</a>). Moderne Arthropoden haben drei Abschnitte — Stanleycaris' zwei Segmente waren "zwei Drittel des Wegs" zum Endbauplan (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=395s" title="00:06:35">(V)</a>).

## Treiber: Information und Bewegung

Diese Fossilien erzählen eine Geschichte der Gehirnevolution, die mit der **"Informationsrevolution"** nach der [[Kambrium-Explosion]] einhergeht: Die Evolution der Augen lieferte plötzlich viel mehr verarbeitbare Information, was das Wachstum neuronaler Prozessorer (Gehirne) antrieb (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=404s" title="00:06:44">(V)</a>). Das gemeinsame neuronale Grundgerüst fast aller Tiere plus die Gleichzeitigkeit des Auftretens legt nahe, dass **Gehirne nur einmal** beim frühen Tiervorfahren entstanden (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=446s" title="00:07:26">(V)</a>).

Der eigentliche Auslöser aber war **Bewegung/Muskulatur** ([[Gehirne brauchen Muskeln]]): Sobald Tiere größer wurden, brauchten große Körper **mehr Nahrung** → Bewegung (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=523s" title="00:08:43">(V)</a>). Während Pflanzen und Pilze durch Wachstum "zu" ihrer Nahrung wandern, nutzen Tiere **Muskeln** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=539s" title="00:08:59">(V)</a>).

**[[Ursprung der Nervensysteme|Anfang des Nervensystems]]:** Das elektrochemische Signalgeben begann bei einzelligen Organismen durch chemisches Erkunden der Außenfläche (wie Riechen/Schmecken) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=489s" title="00:08:09">(V)</a>); einige koloniale Einzeller, die **Choanoflagellaten** ([[Choanoflagellaten]]), nutzten schon primitive elektrische Signalgebung (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=496s" title="00:08:16">(V)</a>). Bei den ersten Vielzellern wurde äußere Sensorik zu **innerer Sensorik** kooptiert, und die bewährten elektrochemischen Systeme wurden zu den ersten Nervensystemen (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=513s" title="00:08:33">(V)</a>).

**Muskeln brauchen Koordination:** Die ersten Muskeln waren einfach kontrahierbare Fasern (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=551s" title="00:09:11">(V)</a>); gebündelt entsteht Muskelgewebe. Ein Körper muss seine Muskeln **in der richtigen Reihenfolge** kontrahieren, sonst spastiert er und schädigt sich selbst (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=593s" title="00:09:53">(V)</a>). Effizienz verlangt, die weiterleitenden und rückkoppelnden Neuronen **dicht beieinander** zu bündeln — ein **Knoten aus Nervengewebe, also ein Gehirn** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=615s" title="00:10:15">(V)</a>).

**Kernhypothese:** Die frühesten Gehirne entstanden also **nicht**, um die äußere Umwelt zu verarbeiten und zu reagieren, sondern um **die inneren Handlungen der neuen, komplizierten Muskel-Körper zu formen** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=617s" title="00:10:17">(V)</a>).

## Ediacara- und Kambrium-Belege

- **[[Haootia]]** (Ediacarium, ~560 Mio. Jahre): frühestes bekanntes Muskelgewebe; wird für eine Cnidarier-Art (mit Korallen/Quallen verwandt) gehalten (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=573s" title="00:09:33">(V)</a>). Haootia hat mutmaßlich Muskelkörper, aber wie andere Ediacara-Organismen **keine Spuren- oder Bewegungsspuren** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=645s" title="00:10:45">(V)</a>) — doch ihre zeitliche Nähe zur molekular datierten Nervensystem-Entstehung ist kein Zufall (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=636s" title="00:10:36">(V)</a>).
- Zu Beginn des Kambriums (dessen Basis ein Fossil-Wühlgang ist) beherrschten die Tier-Vorfahren die Bewegung (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=662s" title="00:11:02">(V)</a>); als Augen erschienen, war die Gehirn-Architektur zur effizienten Reizverarbeitung schon da (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=668s" title="00:11:08">(V)</a>).

## Fazit

Größere Körper, Prädation und soziales Leben erhöhten im Kambrium die Nachfrage nach Rechenleistung, die mit wachsender Gehirngröße beantwortet wurde (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=685s" title="00:11:25">(V)</a>). Die Botschaft: **ohne das Erscheinen der Brawn hätten wir unsere Brains vielleicht nie bekommen** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=700s" title="00:11:40">(V)</a>).

## Aus dieser Quelle hervorgegangene Notizen

- [[Evolution des Nervensystems]]
- [[Ursprung der Nervensysteme]]
- [[Gehirn als zentraler Verarbeitungshub]]
- [[Fossile Hirne des Kambriums]]
- [[Gehirne brauchen Muskeln]]
- [[Molekulare Uhr]]
- [[Choanoflagellaten]]
- [[Haootia]]

--- END NOTE ---

--- FILENAME: 20-Literature/How Mountains Make Evolution Weird.md
--- BEGIN NOTE ---

# How Mountains Make Evolution Weird

Das PBS-Eons-Video zeigt, wie Gebirge die [[Gebirge als Motoren der Biodiversität|Artenvielfalt]] verzerren und die Art und Weise, wie Paläontologen die Evolutionsgeschichte lesen. Ausgangspunkt ist ein Fund, der die vertraute Erzählung sprengt: In den 1960ern stieß man in den Fußhügeln Südwest-Montanas auf ein Multituberculaten-Fossil, obwohl diese Gruppe in diesem Gestein 17 Millionen Jahre nach ihrer vermeintlichen Ausrottung datierte (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=33s" title="00:00:33">(V)</a>) — und aus den Fußhügeln statt aus den üblichen niedrig gelegenen Becken (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=39s" title="00:00:39">(V)</a>). Dieser Fund lenkte den Blick auf die Berge und schließlich auf unsere eigenen Verwandten, die Primaten (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=46s" title="00:00:46">(V)</a>).

## Eozäne Primaten Nordamerikas

Zu Beginn des Eozäns (56 Mio. Jahre) war das heutige Wyoming so warm und feucht wie die heutigen Tropen; sumpfliebende Sumpfzypressen sowie fruchtende und blühende Ulmen unterstützten eine neue Gruppe — unsere Verwandten, die [[Eozäne Primaten Nordamerikas|Primaten]] (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=67s" title="00:01:07">(V)</a>). Greifhänden und -füßen erlaubten ihnen, die Baumkronen zu durchqueren, und sie diversifizierten in viele Arten (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=85s" title="00:01:25">(V)</a>).

Jahrzehntelang glaubte man, die Primaten fielen in zwei Gruppen:

- **[[Adapoidea|Adapoiden]]** — größer, lemurenartig, Obst- und Blattfresser; stets nur wenige Arten gleichzeitig (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=102s" title="00:01:42">(V)</a>).
- **[[Omomyoiden]]** — klein, spitzmausartig (tarsier-like), extrem vielfältig; spezialisiert auf Insekten, kleine Wirbeltiere, Früchte und Samen (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=115s" title="00:01:55">(V)</a>). In Nordamerika allein gab es zwischen 55 und 36 Mio. Jahren fast 40 Gattungen (Omomyoiden), die sich wiederum in zwei Gruppen teilten(<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=126s" title="00:02:06">(V)</a>):
  - **[[Anaptomorphine und Omomyine|Anaptomorphine]]** — traten ~55 Mio. Jahre auf und dominierten Nordamerika (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=135s" title="00:02:15">(V)</a>); extrem klein, z. B. _Trogolemur_ ~50 Gramm (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=143s" title="00:02:23">(V)</a>), erkennbar an scharfen Zahnhöckern und besonders prominenten vierten Prämolaren (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=150s" title="00:02:30">(V)</a>).
  - **[[Anaptomorphine und Omomyine|Omomyine]]** — im mittleren Eozän (ab ~50 Mio. Jahre) im Niedergang der Anaptomorphinen aufstrebend (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=157s" title="00:02:37">(V)</a>); etwas größer (bis 3 kg bei _Macrotarsius_), kürzere Zahnhöcker, ohne den prominenten vierten Prämolaren (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=166s" title="00:02:46">(V)</a>).

Weil es im gesamten Nordamerika (Mexiko bis Mississippi bis Kanada) eozäne Ablagerungen gab, schien es, als verdrängten die Omomyinen die Anaptomorphinen überall (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=177s" title="00:02:57">(V)</a>).

## Die Rolle der Berge

Diese Schlussfolgerung stützte sich jedoch auf **Niedriglagen-Fossilien**, wo Sedimente in Becken akkumulieren (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=190s" title="00:03:10">(V)</a>). In den 1970ern, angeregt durch die Montana-Multituberculaten, suchte man systematisch in den Fußhügeln Zentral-Wyomings (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=198s" title="00:03:18">(V)</a>).

- In den Fußhügeln auf ~1.980 m wurden **anaptomorphine Primaten** gefunden, die im mittleren Eozän **überlebten und sogar neue Arten bildeten** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=209s" title="00:03:29">(V)</a>).
- An einem Pass im Süden (~2.200 m) sammelten Forschende in den 1990ern mehr als ein Dutzend Primatenarten (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=226s" title="00:03:46">(V)</a>) — **deutlich mehr** als in den jahrzehntelang erkundeten Tieflagenfundstellen derselben Zeit (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=252s" title="00:04:12">(V)</a>).
- Seltene Gattungen wie _Artimonius_ (mit massiven vierten unteren Prämolaren) waren hier plötzlich häufig; die erwartete Häufigkeit war auf den Kopf gestellt (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=271s" title="00:04:31">(V)</a>). Sogar _Omomys carteri_, oft eine der häufigsten Arten dieser Zeit, war kaum präsent (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=271s" title="00:04:31">(V)</a>). Auch Funde aus den 2010ern von ~3.100 m bei Yellowstone zeigten dasselbe Muster mit _Omomys carteri_ (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=282s" title="00:04:42">(V)</a>).

## Warum die Berge anders sind

Zuerst vermutete man einen Alters-Mismatch durch **[[Time-Averaging in Sedimenten|Time-Averaging]]**, bei dem Sedimente unterschiedlichen Alters vermischt werden (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=307s" title="00:05:07">(V)</a>): An Hängen erodiert Regen die freiliegenden Schichten, und die Ablagerung am Hangfuß mischt mehrere Zeitperioden zu einem einzigen Fossil-Lager (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=316s" title="00:05:16">(V)</a>). Ausgeschlossen, weil an diesen Stellen gut datierte Schichten ober- und unterhalb lagen (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=339s" title="00:05:39">(V)</a>).

Stattdessen sind es die Berge und ihre Umwelt selbst:

- **Elevation und Umweltvariation:** Mit der Höhe ändern sich Atmosphärenbedingungen (Temperatur, Luftdichte, UV-Strahlung) (Gravitations-Achsen hier zufällig irrelevant) (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=362s" title="00:06:02">(V)</a>).
- **Topografische Komplexität:** Mehr Regen → aktivere Erosion → viele kleine Flusssysteme, die die Landschaft unterschiedlich zerschneiden; in einem einzigen Quadratmeile gibt es mehr Reliefänderungen als im Tiefland; dazu Klippen, Grate und tektonische Zergliederung (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=394s" title="00:06:34">(V)</a>).
- Mehr Umweltichen → mehr Arten; mehr Habitatvariation erhöht die Wahrscheinlichkeit, dass ein Merkmal selektiert wird → mehr Speziation (**[[Speziation durch Habitatvariation]]**) (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=406s" title="00:06:46">(V)</a>).
- Mehr Nischen = weniger Konkurrenz um dieselbe Nische → auch Tiere, die im Tiefland verdrängt würden, können in den Bergen länger überleben: **[[Refugia]]** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=429s" title="00:07:09">(V)</a>). Die überlebenden Anaptomorphinen in den Fußhügeln sind ein Beleg (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=447s" title="00:07:27">(V)</a>).
- Diese Kombination lässt Berge **wie Inseln** wirken, die isolierte Diversitätspocketz unterstützen (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=454s" title="00:07:34">(V)</a>).
- Manche Tiere **bevorzugen** Berge — _Artimonius_ ist vielleicht gar nicht selten, sondern nur habitatspezifisch (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=470s" title="00:07:50">(V)</a>).

## Gebirgsbildung als Treiber

Die Gebirgsbildung selbst wirkte aktiv: Die Rocky Mountains entstanden durch Störungen und Faltung in Schüben zwischen **80 und 40 Mio. Jahren** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=504s" title="00:08:24">(V)</a>), begleitet von Vulkanismus, der dicke Schichten magmatischen Gesteins ablagerte (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=497s" title="00:08:17">(V)</a>). In Wyoming selbst gab es nahezu **15 Mio. Jahre periodischer Eruptionen**, die über Hunderte Kilometer Asche auswarfen und in Teilen des Bundesstaates insgesamt **~1,5 km Sediment** ablagerten (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=531s" title="00:08:51">(V)</a>).

## Fazit: Aussterben ist nicht immer ein Schalter

Berghöhen haben steile Gradienten, hohes Erosionspotenzial und schlechte Erhaltung — deshalb ist das Lernen hier schwierig (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=548s" title="00:09:08">(V)</a>). Aber die Lehre ist zentral: **Aussterben ist nicht immer ein An-Aus-Schalter** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=554s" title="00:09:14">(V)</a>). Die Anaptomorphinen waren nicht ausgestorben, sondern **hatten sich angepasst und überlebten in den Bergen**; die ursprüngliche Erzählung ihrer Verdrängung durch die Omomyinen war weit komplexer und interessanter (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=565s" title="00:09:25">(V)</a>). Den Fossilbericht "nach oben" (in die Höhe) zu erweitern eröffnet neue Lektionen (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=583s" title="00:09:43">(V)</a>).

Anmerkung: Das Video läuft zum Folgevideo "What Happened To Primates In North America?" über (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=600s" title="00:10:00">(V)</a>).

## Aus dieser Quelle hervorgegangene Notizen

- [[Gebirge als Motoren der Biodiversität]]
- [[Speziation durch Habitatvariation]]
- [[Refugia]]
- [[Eozäne Primaten Nordamerikas]]
- [[Omomyoiden]]
- [[Anaptomorphine und Omomyine]]
- [[Multituberculata]]
- [[Time-Averaging in Sedimenten]]

--- END NOTE ---

--- FILENAME: 20-Literature/Landshuter Erbfolgekrieg (Wikipedia).md
--- BEGIN NOTE ---

# Landshuter Erbfolgekrieg

Der **Landshuter Erbfolgekrieg 1504/05** (auch Bayerische Fehde oder bairisch-pfälzischer Erbfolgekrieg) wurde durch einen Streit um die Erbfolge in Bayern-Landshut ausgelöst, nachdem der letzte dortige Herzog ohne männliche Nachkommen gestorben war ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]).

### Ursachen: Testament gegen Hausvertrag

Herzog Georg der Reiche von Bayern-Landshut setzte in seinem Testament vom 19. September 1496 seine Tochter Elisabeth, deren künftigen Gemahl Ruprecht von der Pfalz und deren Söhne als Erben ein; die Vermählung fand am 10. Februar 1499 statt ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]). Diese Erbregelung widersprach dem [[Wittelsbacher Hausvertrag von Pavia]], wonach bei Aussterben einer männlichen Linie die Besitzungen an die jeweils andere Linie fallen sollten — ein Vertragsbruch, den Albrecht IV. von Bayern-München nicht akzeptierte ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]). Nach Georgs Tod am 1. Dezember 1503 mündete der Konflikt in den Krieg.

Der Landshuter Erbfolgekrieg war der **Endpunkt eines seit Jahrzehnten aufgebauten Konflikts innerhalb des wittelsbachischen Hauses**: Die traditionell enge Verbindung zwischen den Herzögen Georg und Albrecht verschlechterte sich ab 1493 rapide, Georg stellte sich an die Seite der Kurpfalz, und Maximilian I. unterstützte Albrecht, ohne seine eigenen dynastischen Interessen aus den Augen zu verlieren ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]).

### Verhandlungen und Reichsacht

Die niederbayerischen Landstände bildeten einen Regentschaftsrat und wandten sich an das Reichskammergericht; Maximilian I. beschied die Parteien am 5. Februar 1504 nach Augsburg und stellte als Gegenleistung für seine Vermittlung **Gebietsansprüche an beide Seiten** ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]). Im April 1504 erklärte sich Albrecht bereit, die Gerichte Kufstein, Kitzbühel und Rattenberg abzutreten, worauf Maximilian 10.000 Mann Hilfstruppen zusagte und die Münchner Herzöge am 23. April mit Georgs Ländern belehnte ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]). Ruprecht wurde durch Frankreich, Böhmen und Baden unterstützt (rund 30.000 Mann), Albrecht durch Maximilian, den Schwäbischen Bund, Württemberg und Nürnberg (rund 60.000 Mann); am 5. Mai 1504 verhängte Maximilian die [[Reichsacht]] über Ruprecht und dessen Vater Philipp ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]).

### Kriegsverlauf

Albrecht belagerte ab dem 21. Juni 1504 Landau an der Isar und eroberte es; am 13. Juli kam es bei Altdorf zum ersten größeren Gefecht, bei dem der auf Albrechts Seite kämpfende Götz von Berlichingen seine Hand verlor ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Kriegsverlauf|Q1]]). Ruprecht starb am 20. August 1504 an der Ruhr; seine Witwe Elisabeth führte den Krieg fort ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Kriegsverlauf|Q1]]). Am 9. August hatten pfälzische Truppen Kufstein eingenommen, das Maximilian später zurückeroberte ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Kriegsverlauf|Q1]]). In der einzigen größeren Schlacht des Krieges wurden am 12. September 1504 in der Schlacht von Wenzenbach die Böhmen durch die vereinten Heere geschlagen; drei Tage später starb Elisabeth ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Kriegsverlauf|Q1]]). Nach der Einnahme Kufsteins ergaben sich Rattenberg, Schwaz, das Ziller- und Brixental, Traunstein, Kitzbühel und Reichenhall ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Kriegsverlauf|Q1]]). Am 23. Januar 1505 unterlag Feldherr Wisbeck bei Gangkofen den bayerischen Truppen; am 9. Februar trat ein Waffenstillstand in Kraft ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Kriegsverlauf|Q1]]). Auch die Pfalz wurde schwer verwüstet: Etwa 300 pfälzische Orte wurden zerstört ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Kriegsverlauf|Q1]]).

### Der Kölner Schiedsspruch

Am 30. Juli 1505 endete der Krieg mit dem [[Kölner Schiedsspruch 1505|Kölner Schiedsspruch]] Maximilians I. auf dem Reichstag zu Köln ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]). Die beiden Enkel Georgs, Ottheinrich und Philipp, erhielten die [[Junge Pfalz]] mit der Hauptstadt Neuburg an der Donau; das Gebiet um Kufstein, Kitzbühel und Rattenberg hatte sich Maximilian als Preis seiner Vermittlung vorbehalten ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]). Die Reichsstadt Nürnberg gewann Gebiete östlich der Stadt; der Rest von Bayern-Landshut ging an die Münchener Linie ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]). Sowohl die Wittelsbacher in Bayern als auch die Kurpfalz hatten umfangreiche Gebiete verloren ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]).

--- END NOTE ---

--- FILENAME: 20-Literature/Landshuter Erbfolgekrieg.md
--- BEGIN NOTE ---

# Landshuter Erbfolgekrieg

Der **Landshuter Erbfolgekrieg 1504/05** (auch Bayerische Fehde oder bairisch-pfälzischer Erbfolgekrieg) wurde durch einen Streit um die Erbfolge in Bayern-Landshut ausgelöst, nachdem der letzte dortige Herzog ohne männliche Nachkommen gestorben war ([[10-Raw/Landshuter Erbfolgekrieg.md#Vorgeschichte|Q1]]).

### Ursachen: Testament gegen Hausvertrag

Herzog Georg der Reiche von Bayern-Landshut setzte in seinem Testament vom 19. September 1496 seine Tochter Elisabeth, deren künftigen Gemahl Ruprecht von der Pfalz und deren Söhne als Erben ein; die Vermählung fand am 10. Februar 1499 statt ([[10-Raw/Landshuter Erbfolgekrieg.md#Vorgeschichte|Q1]]). Diese Erbregelung widersprach dem [[Wittelsbacher Hausvertrag von Pavia]], wonach bei Aussterben einer männlichen Linie die Besitzungen an die jeweils andere Linie fallen sollten — ein Vertragsbruch, den Albrecht IV. von Bayern-München nicht akzeptierte ([[10-Raw/Landshuter Erbfolgekrieg.md#Vorgeschichte|Q1]]). Nach Georgs Tod am 1. Dezember 1503 mündete der Konflikt in den Krieg.

Der Landshuter Erbfolgekrieg war der **Endpunkt eines seit Jahrzehnten aufgebauten Konflikts innerhalb des wittelsbachischen Hauses**: Die traditionell enge Verbindung zwischen den Herzögen Georg und Albrecht verschlechterte sich ab 1493 rapide, Georg stellte sich an die Seite der Kurpfalz, und Maximilian I. unterstützte Albrecht, ohne seine eigenen dynastischen Interessen aus den Augen zu verlieren ([[10-Raw/Landshuter Erbfolgekrieg.md#Vorgeschichte|Q1]]).

### Verhandlungen und Reichsacht

Die niederbayerischen Landstände bildeten einen Regentschaftsrat und wandten sich an das Reichskammergericht; Maximilian I. beschied die Parteien am 5. Februar 1504 nach Augsburg und stellte als Gegenleistung für seine Vermittlung **Gebietsansprüche an beide Seiten** ([[10-Raw/Landshuter Erbfolgekrieg.md#Vorgeschichte|Q1]]). Im April 1504 erklärte sich Albrecht bereit, die Gerichte Kufstein, Kitzbühel und Rattenberg abzutreten, worauf Maximilian 10.000 Mann Hilfstruppen zusagte und die Münchner Herzöge am 23. April mit Georgs Ländern belehnte ([[10-Raw/Landshuter Erbfolgekrieg.md#Vorgeschichte|Q1]]). Ruprecht wurde durch Frankreich, Böhmen und Baden unterstützt (rund 30.000 Mann), Albrecht durch Maximilian, den Schwäbischen Bund, Württemberg und Nürnberg (rund 60.000 Mann); am 5. Mai 1504 verhängte Maximilian die [[Reichsacht]] über Ruprecht und dessen Vater Philipp ([[10-Raw/Landshuter Erbfolgekrieg.md#Vorgeschichte|Q1]]).

### Kriegsverlauf

Albrecht belagerte ab dem 21. Juni 1504 Landau an der Isar und eroberte es; am 13. Juli kam es bei Altdorf zum ersten größeren Gefecht, bei dem der auf Albrechts Seite kämpfende Götz von Berlichingen seine Hand verlor ([[10-Raw/Landshuter Erbfolgekrieg.md#Kriegsverlauf|Q1]]). Ruprecht starb am 20. August 1504 an der Ruhr; seine Witwe Elisabeth führte den Krieg fort ([[10-Raw/Landshuter Erbfolgekrieg.md#Kriegsverlauf|Q1]]). Am 9. August hatten pfälzische Truppen Kufstein eingenommen, das Maximilian später zurückeroberte ([[10-Raw/Landshuter Erbfolgekrieg.md#Kriegsverlauf|Q1]]). In der einzigen größeren Schlacht des Krieges wurden am 12. September 1504 in der Schlacht von Wenzenbach die Böhmen durch die vereinten Heere geschlagen; drei Tage später starb Elisabeth ([[10-Raw/Landshuter Erbfolgekrieg.md#Kriegsverlauf|Q1]]). Nach der Einnahme Kufsteins ergaben sich Rattenberg, Schwaz, das Ziller- und Brixental, Traunstein, Kitzbühel und Reichenhall ([[10-Raw/Landshuter Erbfolgekrieg.md#Kriegsverlauf|Q1]]). Am 23. Januar 1505 unterlag Feldherr Wisbeck bei Gangkofen den bayerischen Truppen; am 9. Februar trat ein Waffenstillstand in Kraft ([[10-Raw/Landshuter Erbfolgekrieg.md#Kriegsverlauf|Q1]]). Auch die Pfalz wurde schwer verwüstet: Etwa 300 pfälzische Orte wurden zerstört ([[10-Raw/Landshuter Erbfolgekrieg.md#Kriegsverlauf|Q1]]).

### Der Kölner Schiedsspruch

Am 30. Juli 1505 endete der Krieg mit dem [[Kölner Schiedsspruch 1505|Kölner Schiedsspruch]] Maximilians I. auf dem Reichstag zu Köln ([[10-Raw/Landshuter Erbfolgekrieg.md#Ergebnisse|Q1]]). Die beiden Enkel Georgs, Ottheinrich und Philipp, erhielten die [[Junge Pfalz]] mit der Hauptstadt Neuburg an der Donau; das Gebiet um Kufstein, Kitzbühel und Rattenberg hatte sich Maximilian als Preis seiner Vermittlung vorbehalten ([[10-Raw/Landshuter Erbfolgekrieg.md#Ergebnisse|Q1]]). Die Reichsstadt Nürnberg gewann Gebiete östlich der Stadt; der Rest von Bayern-Landshut ging an die Münchener Linie ([[10-Raw/Landshuter Erbfolgekrieg.md#Ergebnisse|Q1]]). Sowohl die Wittelsbacher in Bayern als auch die Kurpfalz hatten umfangreiche Gebiete verloren ([[10-Raw/Landshuter Erbfolgekrieg.md#Ergebnisse|Q1]]).

--- END NOTE ---

--- FILENAME: 20-Literature/Maximilian I. (Wikipedia).md
--- BEGIN NOTE ---

# Maximilian I. (Wikipedia)

Die Quelle ist der deutschsprachige Wikipedia-Artikel über **Maximilian I. (1459–1519)**, römisch-deutscher König (ab 1486) und erster "erwählter" römisch-deutscher Kaiser (ab 1508) aus dem Haus Habsburg. Der Artikel ist eine Gesamtbiografie: Er verknüpft die persönliche Biografie mit Reichsgeschichte, Dynastie- und Kulturpolitik und ist damit eine Schlüsselquelle für die maximilianische Reichsreform, den Aufstieg des Hauses Habsburg und die Herrschaftspraxis an der Wende vom Mittelalter zur Frühen Neuzeit.

## Kernaussagen

### Herkunft und Kindheit

Maximilian wurde am 22. März 1459 in Wiener Neustadt als Sohn Kaiser Friedrichs III. und Eleonore Helenas von Portugal geboren; per Geburt trug er den Titel eines Erzherzogs von Österreich ([[10-Raw/Maximilian I. (HRR).md#Kindheit|Q1]]). Friedrich III. konnte wegen chronischen Geldmangels und Erbstreitigkeiten keine konsequente Reichspolitik betreiben; der "Bruderzwist" mit Albrecht VI. gipfelte 1462 in der Belagerung des Kaisers in der Wiener Hofburg — ein traumatisches Kindheitserlebnis für den Dreijährigen ([[10-Raw/Maximilian I. (HRR).md#Kindheit|Q1]]). Der frühe Tod der energischen, fürsorglichen Mutter Eleonore 1467 und der im Vergleich dazu verschlossene, risikoscheue Vater prägten Maximilian; die Mutter legte den Grundstein für sein ausgeprägtes monarchisches Bewusstsein ([[10-Raw/Maximilian I. (HRR).md#Kindheit|Q1]]).

### Heiratspolitik und Erwerb Burgunds

Weil Maximilian als einziger Garant dynastischer Kontinuität galt, präsentierte Friedrich III. ihn 1471 auf dem Regensburger Christentag den Reichsständen ([[10-Raw/Maximilian I. (HRR).md#Heiratskandidat|Q1]]). Der vom Papst bereits 1463 angeregte Eheplan mit Maria von Burgund wurde 1476/77 realisiert: Nach dem Tod Karls des Kühnen in der Schlacht bei Nancy heiratete Maximilian am 19. August 1477 Maria *iure uxoris* und wurde so Herzog von Burgund — die Grundlage des [[Burgundisches Erbe Maximilians|burgundischen Erbes der Habsburger]] ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]). Frankreich erkannte die Erbfolge nicht an und besetzte das Herzogtum Burgund — damit begann der jahrhundertelange [[Habsburgisch-französischer Gegensatz|habsburgisch-französische Gegensatz]] ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]). Die niederländischen Stände erzwangen als Gegenleistung für die Anerkennung Marias das Große Privileg ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]). Im burgundischen Erbfolgekrieg sicherte Maximilian 1479 durch den Sieg bei Guinegate den Großteil der burgundischen Länder; nach Marias frühem Tod 1482 konnte er Burgund nur noch als Vormund seines Sohnes Philipp behaupten, wurde von den Ständen aber nicht anerkannt und 1488 in Brügge sogar gefangen gesetzt, bis sein Vater ihn befreite ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]).

### Aufstieg zum König und Wiedervereinigung der Erblande

Am 16. Februar 1486 wurde Maximilian in Frankfurt zum **römisch-deutschen König** gewählt und am 9. April in Aachen gekrönt ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]). 1490 verzichtete Sigmund von Tirol auf Oberösterreich (Tirol, Vorlande, Stammlande) zugunsten Maximilians — die seit 1379 geteilten Habsburgischen Erblande wurden wiedervereinigt ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]). Nach dem Tod Friedrichs III. 1493 wurde Maximilian regierender König und Herr der Erblande ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).

### Die Reichsreform von 1495

Auf dem Reichstag zu Worms 1495 initiierte Maximilian eine umfassende [[Reichsreform von 1495|Reichsreform]], deren vier Gesetze im Reichsabschied den Übergang vom Mittelalter zur Frühen Neuzeit markieren ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]): Der [[Ewiger Landfrieden|Ewige Landfriede]] ordnete das Gewaltmonopol rechtlich dem Reich zu und ersetzte das mittelalterliche Fehderecht; das [[Reichskammergericht]] wurde als ständisch dominierte oberste Gerichtsbehörde eingesetzt; der [[Gemeiner Pfennig|Gemeine Pfennig]] war die erste reichsweite Steuer; das [[Reichsregiment]] als ständische Reichsregierung scheiterte am Widerstand der Reichsstände ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]). Wortführer der Stände war Erzbischof Berthold von Henneberg; das Ergebnis war ein Kompromiss zwischen kaiserlicher Zentralgewalt und ständischem Föderalismus ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]). Als neue regionale Verwaltungseinheiten entstanden die [[Reichskreise]] (sechs, später zehn), die Reichssteuern einhoben und Reichstruppen aufstellten ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]). Von der Reform hatten die Reichskreise und das Reichskammergericht dauerhaft Bestand ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).

### Dynastische Expansion: Spanien, Böhmen, Ungarn

Maximilian sicherte die habsburgische Erbfolge durch eine gezielte [[Habsburgische Heiratspolitik|Heiratspolitik]]: Sein Sohn Philipp wurde 1496 mit Johanna von Kastilien vermählt, wodurch die Habsburger an die spanischen Kronen Aragoniens und Kastiliens gelangten ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]). Mit dem [[Pressburger Vertrag 1491|Pressburger Vertrag]] (1491) und dem Ausbau zum Plan wechselseitiger Heiraten (1506) sicherte er die Nachfolge in Böhmen und Ungarn ab; die [[Wiener Doppelhochzeit 1515|Wiener Doppelhochzeit]] (1515) brachte dem Haus Habsburg nach dem Tod Ludwigs II. 1526 die Kronen von Böhmen und Ungarn ein ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]). Maximilian konnte das Reich seinem Enkel Karl V. als Universalmonarchie übergeben ([[10-Raw/Maximilian I. (HRR).md#Die Habsburgischen Erblande, Burgund und das Reich|Q1]]).

### Kaisertitel und Italienpolitik

1495 bildete Maximilian mit Mailand, Venedig, Papst Alexander VI. und Ferdinand II. von Aragón die Heilige Liga gegen Frankreichs Neapel-Zug ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]). Nachdem sein Romzug am Widerstand Venedigs gescheitert war, nahm Maximilian am 4. Februar 1508 im Dom von Trient mit Zustimmung Papst Julius' II. den Titel eines **Erwählten Römischen Kaisers** an — eine [[Erwählter Römischer Kaiser|Kaisertitulierung ohne päpstliche Krönung]] ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).

### Landshuter Erbfolgekrieg und Kölner Schiedsspruch

Auf dem Reichstag 1505 zu Köln entschied Maximilian den [[Landshuter Erbfolgekrieg]] im Wesentlichen zugunsten Albrechts IV. von Bayern ([[Kölner Schiedsspruch 1505|Kölner Schiedsspruch]]) und brachte dabei Kufstein, Kitzbühel und Rattenberg an sich ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]) — vgl. [[Maximilians Gebietsgewinne im Landshuter Erbfolgekrieg]] und [[Belagerung von Kufstein 1504]].

### Selbstinszenierung als "letzter Ritter"

Maximilian stilisierte sich als Wahrer ritterlicher Ideale und verband sie mit Elementen des Renaissancefürsten: Die Werke *Theuerdank*, *Weißkunig* und *Freydal* sind verschlüsselte Autobiografien und Denkmäler einer vergangenen Epoche zugleich ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]). Er nutzte als erster Herrscher den Holzschnitt als Propagandamedium (Ehrenpforte, *Triumphzug*) und betrieb genealogische Forschung bis zu antiken und biblischen Wurzeln, um die Herrschaft der Habsburger zu legitimieren — das Muster einer nahezu modern anmutenden [[Maximilians Selbstinszenierung|Selbstinszenierung]] ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]). Der Beiname "letzter Ritter" wurde später um "erster Kanonier" erweitert, weil Maximilian zugleich als modernisierender Herrscher galt ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]).

### Humanismus und Kunstförderung

Maximilian förderte Wissenschaft und Kunst: Er setzte das Konzept von Konrad Celtis um und gründete 1501 das [[Collegium poetarum et mathematicorum]] an der Universität Wien — eine Pioniertat der Institutionalisierung des Humanismus ([[10-Raw/Maximilian I. (HRR).md#Kunst und Literatur|Q1]]). Seine Auftragswerke (Ambraser Heldenbuch 1504–1516, die Frauensteiner Schutzmantelmadonna, Dürer-Rente ab 1515) dienten vor allem der memoriageleiteten Selbstvergewisserung, nicht rein ästhetischen Zwecken ([[10-Raw/Maximilian I. (HRR).md#Kunst und Literatur|Q1]]).

### Schulden und Finanznot

Der kriegerische, prunkvolle Lebensstil überstieg die laufenden Einnahmen bei weitem: Maximilian häufte enorme [[Schulden Maximilians I.|Schulden]] an und war auf Kredite seines Hausbankiers Jakob Fugger angewiesen; wegen seiner 17 Augsburg-Aufenthalte nannte ihn Franz I. spöttisch "Bürgermeister von Augsburg" ([[10-Raw/Maximilian I. (HRR).md#Schulden|Q1]]). Die Mitgift seiner zweiten Frau Bianca Maria Sforza (400.000 Golddukaten) war eine Folge des Gelddiktats ([[10-Raw/Maximilian I. (HRR).md#Schulden|Q1]]).

### Tod und Nachleben

Maximilian starb am 12. Januar 1519 auf der Reise in Wels, vermutlich an Darmkrebs; er inszenierte seinen Tod (ständig mitgeführter Sarg, demütige Bußgeste, Testamentsverfügungen zur Konservierung und Bestattung) ([[10-Raw/Maximilian I. (HRR).md#Tod und Nachleben|Q1]]). Sein Leichnam wurde in der St.-Georgs-Kathedrale von Wiener Neustadt unter dem Hochaltar beigesetzt, sein Herz getrennt im Sarkophag Marias von Burgund in Brügge ([[10-Raw/Maximilian I. (HRR).md#Tod und Nachleben|Q1]]). Nachfolger wurde sein Enkel Karl V.; seine Tochter Margarete wurde Regentin der Niederlande ([[10-Raw/Maximilian I. (HRR).md#Tod und Nachleben|Q1]]).

## Offene Fragen

- Wie weit reichte der reale Gestaltungsspielraum Maximilians gegenüber den Reichsständen nach der Reichsreform von 1495?
- Welche Rolle spielte die genealogische Legitimationsstrategie für die spätere (spanische und österreichische) Linie des Hauses Habsburg?

--- END NOTE ---

--- FILENAME: 20-Literature/Reissenschuh (NotebookLM 2).md
--- BEGIN NOTE ---

# Reissenschuh (NotebookLM 2)

Zweite, erweiterte Ausgabe eines NotebookLM `/produce`-Outputs zur [[Reissenschuh-Rutschung]] — inhaltlich weitgehend deckungsgleich mit der ersten Ausgabe ([[Reissenschuh (NotebookLM)]]), jedoch mit präziseren Angaben zu [[EMOD-SLAP]], DGNSS-Details, der Transferierbarkeit auf andere Rutschungen und einer klaren Forschungsfrage ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]]). **Hinweis auf ein Continue-Artefakt:** Die Ausgabe enthält die Zeile „(Fortsetzung folgt — bitte 'continue' eingeben)" und setzt danach nahtlos fort; beide Teile wurden konsolidiert ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]]).

### Geologische Grundlage

Die Rutschung am Westrand des [[Tauernfenster|Tauernfensters]] wird durch die [[Metamorphe Schieferhülle (Tauernfenster)|Metamorphe Schieferhülle]] (Glockner-Decke) geprägt: kalkhaltige Glimmerschiefer und Phyllite mit geringer mechanischer Scherfestigkeit wegen hohem Glimmeranteil und ausgeprägter Schieferung ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^1].

### Lithologische Inversion als hydrogeologische Falle

Zentraler Mechanismus bleibt die **lithologische Inversion**: kompetenter, wasserdurchlässiger mesozoischer Marmor der Hochstegen-Formation überlagert inkompetente, wasserstauende Phyllite und Schiefer ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^2]. Die Ausgabe präzisiert den Mechanismus als **hydrogeologische Falle**: Wasser versickert durch die Klüfte des Marmors, staut sich an der Kontaktfläche zum undurchlässigen Phyllit, der Porenwasserdruck-Anstieg reduziert die effektive Reibung an der Gleitfläche und löst die Bewegung aus ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^2].

### Monitoring und abweichende Bewegungsraten

Das Monitoring kombiniert terrestrische und satellitengestützte Fernerkundung: **TLS** erzeugt digitale Geländemodelle, aus denen durch multitemporale Analysen dreidimensionale Verschiebungsvektoren abgeleitet werden ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^3][^4]. **Abweichende Zahlen gegenüber der ersten Ausgabe:** Die zweite Ausgabe nennt eine mittlere jährliche Verschiebungsrate von ~0,6 m und Spitzenwerte über 1,2 m/Jahr in einzelnen Sektoren ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^5], während die erste Ausgabe 0,6–0,8 m/Jahr und Spitzen über 3 m/Jahr angab ([[10-Raw/Reissenschuh.md|Q1]]) — die Angaben widersprechen sich und sind als unsicher zu werten ^[ambiguous]. Ergänzt wird die Überwachung durch **DGNSS-Punktmessungen** (Differential Global Navigation Satellite System) für kontinuierliche Überwachung spezifischer Felspunkte ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^6].

### EMOD-SLAP: Zeitreihe in die Vergangenheit

[[EMOD-SLAP]] („Extending the integrated Monitoring Of Deep-Seated Landslide Activity into the Past") rekonstruiert die Hangdynamik bis ins Jahr **1954** durch photogrammetrische Auswertung historischer Luftbilder und generiert **3D-Punktwolken der Topographie vergangener Jahrzehnte** ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^5]. Damit verlängert das Projekt die Zeitreihen über die terrestrischen Messkampagnen **2016–2019** hinaus und adressiert die zentrale Forschungsfrage: Bleiben die Bewegungsraten über längere Zeiträume konstant oder unterliegen sie signifikanten Fluktuationen? ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^5].

### Transferierbarkeit: Steinlehnen-Rutschung

Die am Reissenschuh entwickelten Workflows sind auf vergleichbare geologische Settings übertragbar, explizit genannt wird die **Steinlehnen-Rutschung** ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^5]. Laserscanning liefert die flächenhafte Struktur der Rutschungskaskade, Differential-GNSS die präzise zeitliche Einordnung der Bewegungsvektoren ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^5][^4].

### Hydrochemie und Kalktuffe

Die Quellwässer spiegeln den Kontakt mit unterschiedlichen lithologischen Einheiten: Wo Oberflächenwasser das Zentralgneis-Basement am Grund des Tauernfensters erreicht, sind natürliche Spuren von **Arsen und Uran** nachweisbar — Beleg für die tiefgreifende tektonische Vernetzung (siehe [[Quellhydrochemie des Tauernfensters]]) ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^7]. Die **Kalktuffbildungen** (Spring-associated limestones, SAL) entstehen durch Ausfällung von Kalziumkarbonat aus kalkübersättigtem Quellwasser, begünstigt durch Algen und Moose — und sind Indikatoren für **stabile hydrogeochemische Bedingungen über längere Zeiträume** in den ansonsten instabilen Schieferhängen ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^8].

### Tektonische Kopplung und Referenzmodell

Die Hangdynamik ist untrennbar mit der tektonischen **Exhumierung des Tauernfensters** verbunden: Aufsteigen des Krustenabschnitts plus Erosion schufen die extremen Reliefgradienten, die die gravitativen Prozesse in den weichen Einheiten der Schieferhülle antreiben ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^1]. Der Reissenschuh dient heute als **Referenzmodell** für tiefgreifende Hangdeformationen in metamorphen Gebirgszügen und als Grundlage für das langfristige Risikomanagement in alpinen Regionen ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^2].

[^1]: Field trip to the Tauern Window region along the TRANSALP seismic profile
[^2]: Nowcasting the movement of the deep-seated Reissenschuh landslide based on soil-vegetation-atmosphere transfer modelling and macropore flow
[^3]: [Derivation of Three-Dimensional Displacement Vectors from Multi-Temporal Long-Range Terrestrial Laser Scanning at the Reissenschuh Landslide (Tyrol, Austria)](https://www.mdpi.com/2072-4292/10/7/1040)
[^4]: Workshop 2.4.A: Remote sensing techniques and data for natural hazard research
[^5]: [Remote sensing - Project EMOD-SLAP](https://mountainresearch.at/remote-sensing/emod-slap/)
[^6]: [Reissenschuh landslide monitoring](http://remote-sensing.mountainresearch.at/monitoring_reissenschuh/index.html)
[^7]: Full article: Hydrochemistry of the Tuxertal, NW Tauern Window, Austria
[^8]: Spring-associated limestones of the Eastern Alps: overview of facies, deposystems, minerals, and biota

--- END NOTE ---

--- FILENAME: 20-Literature/Reissenschuh (NotebookLM).md
--- BEGIN NOTE ---

# Reissenschuh (NotebookLM)

Die Quelle ist ein NotebookLM `/produce`-Output — eine vertiefte wissenschaftliche Analyse der [[Reissenschuh-Rutschung]] (DSGSD) im Schmirntal, belegt mit Fachliteratur und Studien ([[10-Raw/Reissenschuh.md|Q1]]).

### Geologische Grundlage und lithologische Inversion

Die Rutschung liegt auf 2.470 m am Westrand des Tauernfensters in der [[Metamorphe Schieferhülle (Tauernfenster)|Metamorphen Schieferhülle]] (Glockner-Decke) aus Kalkglimmerschiefern und Phylliten mit geringer mechanischer Scherfestigkeit ([[10-Raw/Reissenschuh.md|Q1]])[^1][^2]. Die **lithologische Inversion** ist der zentrale Mechanismus: Der mesozoische **Marmor der Hochstegen-Formation** liegt als kompetentes, wasserdurchlässiges Gestein über inkompetenten, wasserstauenden Phylliten und Schiefern ([[10-Raw/Reissenschuh.md|Q1]])[^2]. Meteorologisches Wasser versickert im geklüfteten Marmor und staut sich an der Grenzfläche; der resultierende **Porenwasserdruck** reduziert den Reibungswiderstand und setzt den Hang in Bewegung ([[10-Raw/Reissenschuh.md|Q1]])[^3][^2].

### Monitoring und Messdaten

Die Überwachung setzt auf [[Monitoring gravitativer Hangdeformationen|Terrestrisches Laserscanning (TLS)]] mit Langstrecken-Scannern wie dem **Riegl VZ-6000**, aus deren digitalen Geländemodellen **dreidimensionale Verschiebungsvektoren** abgeleitet werden ([[10-Raw/Reissenschuh.md|Q1]])[^4]. Die Bewegungsraten: durchschnittlich 0,6–0,8 m/Jahr; in aktiven Sektoren Spitzenwerte über 3 m/Jahr ([[10-Raw/Reissenschuh.md|Q1]])[^4][^2]. Das Projekt **EMOD-SLAP** erweiterte die Zeitreihe durch photogrammetrische Auswertung historischer Luftbilder bis zurück ins Jahr **1954** ([[10-Raw/Reissenschuh.md|Q1]])[^5].

### Hydrochemie und Kalktuff

Die Quellen im Umfeld spiegeln den Weg des Wassers durch die Gesteinseinheiten wider ([[10-Raw/Reissenschuh.md|Q1]])[^2][^6]: Karbonatische Wässer in den Kalkglimmerschiefern; **Arsen- und Uran-Spuren** als Indikator für den Kontakt mit dem Zentralgneis-Basement — ein direkter Beleg der Fenster-Struktur ([[10-Raw/Reissenschuh.md|Q1]])[^2][^6]. An den Austritten bilden sich **Kalktuffe** (Spring-Associated Limestones, SAL): Kalkgesättigtes Wasser tritt aus, biologische Aktivität (Moose, Algen) entzieht CO₂, der Kalk fällt aus ([[10-Raw/Reissenschuh.md|Q1]])[^7].

### Nowcasting und prädiktive Modellierung

Aktuelle Forschung koppelt **Boden-Vegetations-Atmosphären-Transfer-Modelle (SVAT)** mit lokalen Wetterdaten, um den Porenwasserdruck in Echtzeit zu simulieren ([[10-Raw/Reissenschuh.md|Q1]])[^3]. Besonderes Augenmerk liegt auf **Makroporen und Klüften** in den oberen Schichten: Sie ermöglichen rasche Infiltration und damit unmittelbare Druckanstiege, die die Bewegungsphasen des instabilen Marmorblocks auslösen ([[10-Raw/Reissenschuh.md|Q1]])[^3]. Dieser Nowcasting-Ansatz berücksichtigt insbesondere Schneeschmelze und Starkregen als Trigger-Ereignisse ([[10-Raw/Reissenschuh.md|Q1]])[^3].

### Kaskadenprozesse: von der Hangdeformation zur Mure

Die DSGSD des Reissenschuh ist kein isoliertes Phänomen, sondern liefert kontinuierlich **Lockermaterial in die steilen Gerinne unterhalb des Hangs** ([[10-Raw/Reissenschuh.md|Q1]])[^8]. Bei Extremwetter kann dieses Material als **schnell fließende Mure (Debris Flow)** remobilisiert werden — eine direkte Bedrohung für die Infrastruktur im Talboden ([[10-Raw/Reissenschuh.md|Q1]])[^8]. Die Wechselwirkung zwischen langsamer, tiefgreifender Deformation und schnellen oberflächennahen Prozessen ist ein zentrales Feld des lokalen Naturgefahrenmanagements ([[10-Raw/Reissenschuh.md|Q1]])[^8] (siehe [[Gravitative Kaskadenprozesse am Reissenschuh]]).

### Bergsteigerdorf-Perspektive

Der Erhalt der [[Bergmähder]] auf den Schieferschutthalden stabilisiert oberflächlich die Bodenschichten und mildert die Erosion — beeinflusst aber nicht die tiefgreifende tektonische Bewegung ([[10-Raw/Reissenschuh.md|Q1]])[^9]. High-Tech-Überwachung und traditionelle Landnutzung bilden zusammen eine ganzheitliche Strategie für das Leben mit der geologischen Instabilität am Rande des Tauernfensters ([[10-Raw/Reissenschuh.md|Q1]])[^2].

[^1]: [Wissenschaftlicher Bericht über Geographie, Geologie, Archäologie, Geschichte und Botanik des Schmirntals](https://notebooklm.google.com/source/43)
[^2]: [Schmirn Podcasts (Quelle).md](https://notebooklm.google.com/source/13)
[^3]: [Nowcasting the movement of the deep-seated Reissenschuh landslide](https://notebooklm.google.com/source/19)
[^4]: [Derivation of Three-Dimensional Displacement Vectors from Multi-Temporal Long-Range Terrestrial Laser Scanning at the Reissenschuh Landslide](https://notebooklm.google.com/source/8)
[^5]: [Remote sensing - Project EMOD-SLAP](https://notebooklm.google.com/source/21)
[^6]: [Full article: Hydrochemistry of the Tuxertal, NW Tauern Window, Austria](https://notebooklm.google.com/source/15)
[^7]: [Spring-associated limestones of the Eastern Alps: overview of facies, deposystems, minerals, and biota](https://notebooklm.google.com/source/28)
[^8]: [Observation and Modeling of Cascade Processes at the Reissenschuh (Schmirn, Austria)](https://notebooklm.google.com/source/20)
[^9]: [St. Jodok, Schmirn- und Valsertal - Bergsteigerdörfer](https://notebooklm.google.com/source/31)

--- END NOTE ---

--- FILENAME: 20-Literature/Schmirn Podcasts.md
--- BEGIN NOTE ---

# Schmirn Podcasts

Die Quelle ist ein von NotebookLM erzeugtes, fünfteiliges **Podcast-Skript über das Schmirntal** (Tirol), das die Geologie, Archäologie, Siedlungsgeschichte, Botanik und Zukunftsperspektive des Tals zusammenfasst ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Sie entstand als KI-Synthese auf Basis wissenschaftlicher Fachquellen (Geologie: TRANSALP, EMOD-SLAP, Hydrochemie-Studien) und dient als Überblicksquelle für den gesamten Themenkomplex Schmirntal. Anmerkung: Die Quelle enthält zwei Varianten der Episode 2 (Archäologie); beide wurden konsolidiert ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]], [[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Glitzernde Urzeit – Das Rätsel vom Riepenkar“|Q1]]).

### Episode 1: Geologie — Das Tal als tektonisches Labor

Das Schmirntal liegt am Westrand des **Tauernfensters**, des größten tektonischen Fensters der Alpen (160 km vom Brenner bis zum Katschberg, 5.600 km²) ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Durch die Exhumation — N-S-Kompression der afrikanischen gegen die europäische Platte plus O-W-Extension (laterale Extrusion) — kam das Europäische Grundgebirge zum Vorschein ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Am Westrand begrenzt die [[Brenner-Normalverwerfung|Brenner-Linie]] das Fenster: Die westlichen Gebirgsblöcke (Ötztal-Stubai-Kristallin) glitten nach Westen weg und ermöglichten so den Aufstieg des Fensters ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

Das Tal selbst liegt auf der **metamorphen Schieferhülle** (Glockner-Decke): Kalkglimmerschiefer, Phyllite und Tonschiefer, durch die [[Alpine Metamorphose]] in 35–40 km Tiefe umgewandelt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Die weichen Schiefer sind die Grundlage der massiven Hangbewegungen: Die [[Reissenschuh-Rutschung]] (2.470 m) ist eine tiefgreifende gravitative Hangdeformation (DSGSD), ausgelöst durch lithologische Inversion — wasserdurchlässiger Marmor über undurchlässigem Phyllit ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Der Porenwasserdruck an der Grenzschicht setzt die Reibung außer Kraft; der Hang bewegt sich um 0,6–0,8 m/Jahr, in instabilen Phasen über 3 m/Jahr ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Überwacht wird der Hang mit Terrestrischem Laserscanning (Riegl VZ-6000), DGNSS, Luftbildauswertung seit 1954 (Projekt EMOD-SLAP) und KI-gestütztem Nowcasting ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

Die Quellenchemie verrät die Tiefenstruktur: Karbonatische Wässer in den Kalkglimmerschiefern, Arsen und Uran dort, wo das Wasser das Zentralgneis-Basement erreicht — ein direkter Beweis der Fensterstruktur ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). An den Quellaustritten bilden sich Kalktuffe (SAL), weil Moose und Algen dem Wasser CO₂ entziehen und der Kalk ausfällt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

### Episode 2: Archäologie — Der älteste Hochgebirgs-Bergbau der Welt

Am **Riepenkar** (2.800 m, Südfuß des Olperers) wurde im **Mesolithikum** (ab ca. 8.000 v. Chr.) systematisch **Bergkristall** abgebaut — die weltweit älteste nachgewiesene Abbaustelle dieser Art im Hochgebirge ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Das Ziel war eine 15 Meter lange Quarzkluft in der Schieferhülle, in der hydrothermale Prozesse klare Kristalle wachsen ließen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Glitzernde Urzeit – Das Rätsel vom Riepenkar“|Q1]]). Gewonnen wurde mit Klopfsteinen aus härterem Gestein (z.B. Gneis); vor Ort zerlegte man die Kristalle zu Kernen und verarbeitete sie zu **Mikrolithen** — rasiermesserscharfen Klingen, Pfeilspitzen, Bohrern und Schabern ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Glitzernde Urzeit – Das Rätsel vom Riepenkar“|Q1]]). Wegen Transparenz und Glanz waren sie zugleich begehrte **Prestigeobjekte** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]).

Der Kristall wurde exportiert: Funde mit der chemischen Signatur des Riepenkars im **Rofangebirge** und am **Gardasee** belegen eine prähistorische **Bergkristallstraße** über die Alpenpässe ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Zentrale Transitachse war das **Tuxer Joch** (2.338 m) zwischen Wipptal und Zillertal — genutzt von mesolithischen Jägern über bronzeitliche Lochhalsnadel-Träger bis zu römischen Reisenden (Goldmünzenfund, Alpwirtschaft) ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]).

### Episode 3: Siedlungsgeschichte — Von der Schwaige zum Totenweg

Die dauerhafte Besiedlung begann mit der mittelalterlichen Landerschließung: „Vallis Smurne" erscheint erstmals **1249** in Urkunden; die Besiedlung erfolgte über **Schwaighöfe** — Viehbetriebe meist in Adels- oder Klosterbesitz, deren Zins in Käse und Schmalz entrichtet wurde ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Bis **1926** gehörten Hintertux und das obere Tuxertal politisch und kirchlich zur Gemeinde Schmirn — die Schmirner waren Verwalter, die Tuxer Untergebene ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).

Die Kehrseite dieser Bindung war der **Totenweg**: Da Hintertux kein Begräbnisrecht besaß, wurden alle Verstorbenen über das 2.338 m hohe Tuxer Joch zum Friedhof der Mutterpfarre nach **Mauern** bei Steinach getragen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Im Winter lagerten die Leichen monatelang gefroren auf den Dachböden der Bauernhäuser; die Totenkammer beim Steckholzer in Obern diente als letzte Station ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Sakrale Zentren waren die Pfarrkirche **St. Joseph** (1756/57 von Franz de Paula Penz erbaut) und die Wallfahrtskapelle Mariahilf „Zur kalten Herberge" (1730, Gnadenbild als Cranach-Kopie, eiskalte Heilquelle bei Augenleiden) ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).

### Episode 4: Botanik — Kulturlandschaft und Ethnobotanik

Die **Bergmähder** an den sonnseitigen Südhängen sind eine über Jahrhunderte geschaffene Kulturlandschaft und gehören zu den artenreichsten Lebensräumen Mitteleuropas: nur einmal jährlich spät gemäht, ohne Kunstdünger — das erhält Orchideen und Enziane ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]). Die Mahd ist zugleich Lawinenschutz: Ungemähtes Gras wird im Winter zur Rutschbahn ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]). Der **Alpenblumen- und Kräutergarten Toldern** (2020 revitalisiert, 420 Arten auf 1.000 m², Themeninseln wie Weihegartl, Schnapsgartl, Heilkräutergartl) dient der „Schule der Alm" als lebendiges Klassenzimmer ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]).

Die **Ethnobotanik** ist tief im Volksglauben verwurzelt: Der Frühlingsenzian („Schusternagele"/„Hausanbrenner") sollte Blitze anziehen, das Gefleckte Knabenkraut („Ständelwurz") galt wegen seiner Wurzelform als Aphrodisiakum, und die Ährige Teufelskralle diente in Notzeiten als Wildgemüse ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]). Hochalpine Spezialisten wie Rudolphs Steinbrech (mit aktiven Kalkdrüsen) und der Gletscher-Hahnenfuß (stabilisiert den Gletscherschutt) besiedeln die Extremstandorte ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]).

### Episode 5: Erbe und Zukunft — Zwangsarbeit, Grauvieh, Bergsteigerdorf

An der **Alpeiner Scharte** (2.800 m) liegen die Ruinen eines **Molybdänbergwerks** aus der NS-Zeit: Zwischen 1941 und 1945 mussten Kriegsgefangene das kriegswichtige Metall (Stahlhärtung für Panzer und Kanonen) als Zwangsarbeiter im höchstgelegenen Bergwerk Europas abbauen; 1944 forderte ein Lawinenunglück zahlreiche Todesopfer ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]).

Gegen die Verbuschung der instabilen Schieferhänge setzt das Tal auf das **Tiroler Grauvieh**: Die leichte, trittsichere Rasse beweidet selbst steilste Hänge und verhindert so, dass Waldbewuchs das Rutsch- und Lawinenrisiko erhöht ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]). Die Zukunftsperspektive ist das **Bergsteigerdorf**: bewusst kein Massentourismus, sondern nachhaltiger Tourismus im Sinne der Alpenkonvention — mit Ruhe, Eigenverantwortung, Erhalt der alpinen Kultur und der „Schule der Alm" als Motor der Freiwilligenarbeit ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]).

--- END NOTE ---

--- FILENAME: 20-Literature/Tauern Window (Field Guide).md
--- BEGIN NOTE ---

# Tauern Window (Field Guide)

Die Quelle ist ein Exkursionsführer des Geological Society of America Field Guide 22 (2011) über 20 Seiten: **"Field trip to the Tauern Window region along the TRANSALP seismic profile, Eastern Alps, Austria"** von Bernd Lammerer, Jane Selverstone und Gerhard Franz. Der Führer dokumentiert eine 7-tägige Exkursion entlang der TRANSALP-Seismiklinie und verknüpft dabei Erkenntnisse der tiefen Seismik mit konkreten Aufschlüssen im Tauernfenster — er ist eine Schlüsselquelle für die strukturelle Architektur und die Exhumationsmechanismen der Ostalpen.

## Kernaussagen

### Die TRANSALP-Seismik und der Unterschied zwischen West- und Ostalpen

Im deutsch-österreichisch-italienischen **TRANSALP**-Programm (1998–2001) wurde ein 300 km langes, zusammenhängendes geophysikalisches Profil durch die Alpen aufgenommen (Vibrations- und Explosionsseismik, Gravimetrie, Teleseismik-Tomographie) ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]). Die Ostalpen unterscheiden sich in vier Punkten von den Westalpen: Sie sind fast vollständig von den dicken Austroalpinen Decken überdeckt; die Pusteria-Störung (östliche Fortsetzung der Insubrischen Linie) ist entlang der Judicarie-Störung ~60 km nach Norden versetzt; es entwickelten sich **zwei** orogene Keile (ein nördlicher und ein jüngerer südlicher); und die Mantel-Tomographie zeigt eine umgekehrte Subduktionsrichtung ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).

### Die paläogeographische Entwicklung der Ostalpen in sieben Schritten

1. **Subsidenz** ab Mittlerem Perm → marine Transgression von Ost nach West bis zur Mittleren Trias; mächtige Karbonatplattformen über dem Austroalpinen Bereich, dagegen nur dünne Sedimente über der Europäischen Platte ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).
2. **Öffnung der Alpinen Tethys** ([[Penninisch-Ligurischer Ozean|Penninisch-Ligurischer und Valais-Ozean]]) im Mittleren Jura als Seitenarm des Nordatlantiks bei der Auflösung Pangäas; extrem langsames Spreading (magmaarmer, ultralangsamer Rücken), hydratisierter, metasomatisierter subkontinentaler Mantel als Ophicalcite ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).
3. **Eoalpine Orogenese** in der Oberkreide bei der Schließung des Hallstatt-Meliata-Ozeans; Eklogit-fazielle Metamorphose, Tiefenerosion, Gosau-Sedimente — nur in den Austroalpinen Decken nachweisbar ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).
4. **Hauptphase der Alpinen Orogenese** (Paleogen): Die [[Penninisch-Ligurischer Ozean|Alpine Tethys]] wird konsumiert, die Adriatische Platte kollidiert mit der Europäischen Platte; Subduktion nach Süden, bis Auftrieb und Reibung den Prozess stoppen. Abradierte Ozeansedimente (Bündnerschiefer) und Reste ozeanischer Lithosphäre (Glockner Decke) überschoben den Kontinentalrand; die Austroalpinen Decken wurden darübergeschoben ([[10-Raw/Field trip to the Tauern Window.pdf#page=3|Q1]]).
5. **Slab Breakoff** vor ~30–40 Mio. Jahren: Die subduzierte ozeanische Lithosphäre riss ab und sank in den Mantel; der östliche Alpenmittelteil stieg rasch ~2 km auf, heißer Asthenosphärenstrom erzeugte Granite, Tonalite und basische Gänge (~40–30 Ma) an Periadriatischen Störungen (Rieserferner, Rensen, Adamello) ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).
6. **Subduktionsumkehr**: Danach riss die Lithosphärenmantel vom Adriatischen Plattenrand ab und sank nach Nordosten; es entstand ein zweiter Keil im Süden, und östlich der Judicarie-Störung drang die Adriatische Platte ~60 km nach Norden in den Deckenstapel ein (Adriatischer Indenter) — dies führte zur weiteren Verschuppung und schließlich zur **Exhumation des Tauernfensters** ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).
7. **Laterale Extrusion**: Ein Teil des Orogens entwich nach Osten (zurückrollende Karpaten-Subduktion), ermöglicht durch konjugierte Störungen (sinistrale Salzach-Ennstal-Störung, dextrale Pusteria- und Mölltal-Störung), begleitet von der N-S-verlaufenden [[Brenner-Normalverwerfung|Brenner- und Katschberg-Normalverwerfung]] (neogene O-W-Extension parallel zur N-S-Kompression) ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).

### Das Tauernfenster: das größte tektonische Fenster der Alpen

Das [[Tauernfenster]] ist das größte tektonische Fenster der Alpen: Es erstreckt sich vom Brennerpass ~160 km zum Katschbergpass, umfasst ~5600 km² und ist der einzige Ort, an dem das **Europäische Grundgebirge** in einer Fläche über 100 km Breite aufgeschlossen ist ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]). Seine heutige Struktur resultiert aus: früher Ablösung und Faltung post-variszischer Deckschichten, Stapelung von Grundgebirgsdecken ([[Alpine Deckentektonik|Ahorn-, Tux-, Zillertal-, Eisbrugg-Gneise]]), Faltung des gesamten Deckenstapels in Ahorn-Tux- und Zillertal-Kuppeln sowie einer Dreieckszone am Ende der Sub-Tauern-Rampe mit Rückfaltung am Nordrand ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).

Die Basis der [[Alpine Deckentektonik|Deckenarchitektur]] bilden die Zentralgneise — ehemalige granitoide Sills oder Lakkolithe mit ihren Nebengesteinen. Von Nord nach Süd (von den tieferen zu den höheren Decken) folgen die Ahorn-, Tux-, Zillertal- und Eisbrugg-Einheiten, die alle unter dem oberjurassischen Hochstegen-Marmor (nördlich) bzw. unter klastischen Sedimenten des späten Karbons/frühen Perms (südlich) liegen ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).

### Metamorphosegeschichte

Alle Einheiten erlebten eine **[[Alpine Metamorphose]]** durch Krustenverdickung während der Alpenorogenese; die höchsten Temperaturen wurden bei ~25–30 Mio. Jahren erreicht ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]). Der metamorphe Grad steigt von Grünschiefer-Fazies an den Rändern zu mittlerer Amphibolit-Fazies im Zentrum. Ozeanische Gesteine erreichten im Südwesten nur 7–8 kbar, in der Glockner-Decke jedoch 12–17 kbar (Lawsonit-Abbau bei 30 Ma); eine tektonische Scholle mit Eklogit-Fazies erreichte 600 ± 50 °C und 20–25 kbar. Die europäischen Einheiten erreichten 10–12 kbar — das bedeutet: Der Kontakt Grundgebirge–Bedeckung wurde während der Orogenese mindestens 35–40 km tief versenkt ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).

Alle Großstrukturen (N-S-Verkürzung bei gleichzeitiger geringer E-W-Extension) begannen sich gemeinsam mit der Hochdruckmetamorphose in der Eklogit-Zone (~32 Ma) zu entwickeln; duktile Deformation an der heutigen Oberfläche endete ~15 Ma ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).

### Exkursionsroute und konkrete Belege

Die Exkursion führt über die Stops im Zillertal, Tuxertal und Pfitschtal und belegt die geologischen Kernaussagen an konkreten Aufschlüssen: u. a. die Basis der Nördlichen Kalkalpen am Schwazer Dolomit (Silur–Devon), die [[Brenner-Normalverwerfung|Brenner-Linie]] mit top-west gerichteter duktiler Scherung (~22–18 Ma, mehrere zehn km horizontaler Versatz), My lonite der Bündnerschiefer beim Brennerbad, den Wolfendorn-Schnitt mit isoklinaler Faltung des Hochstegen-Marmors sowie eine metamorphosierte, lateritische Paläoboden-Zone an der postvariszischen Diskordanz ([[10-Raw/Field trip to the Tauern Window.pdf#page=18|Q1]]).

## Offene Fragen

- Wie genau interagieren Slab Breakoff, Adriatische Indentation und Ost-gerichteter lateraler Escape zeitlich?
- Handelt es sich beim Brennerbad-Kontakt um eine ausgedünnte Metamorphic Core Complex-Abgrenzung (Meer-Boden-Ablösungsstörung)?

## Einfach erklärt

Die Erdkruste besteht aus harten Platten, die auf einem zähen, langsam strömenden Mantel schwimmen. Die Alpen entstanden, weil die Afrikanische Platte (mit Italien als "Adriatischem Vorposten") seit ~40 Mio. Jahren gegen die Europäische Platte drückt — wie zwei Kollisionsteilchen, die ineinanderfahren statt aneinander abzuprallen. Zwischen ihnen lag früher ein kleiner Ozean, der sich aufgerissen hatte (analog zum Atlantik) und beim Zusammenstoß wieder verschwand. Die Gesteine wurden dabei wie Karten aufeinander geschoben (das ist *Deckentektonik*) und dabei bis 35–40 km in die Tiefe gepresst — dort herrschen Drücke, bei denen die Mineralien umkristallisieren (das ist *Metamorphose*).

Das *Tauernfenster* ist nun die Stelle, wo durch mehrere aufeinander folgende Effekte (Abreißen der abtauchenden Platte → Auftrieb; Einstülpen der Adria-Platte → seitliches Ausweichen; Dehnung entlang des Brenners) das tiefste, eigentlich "Europäische" Gestein wieder an der Oberfläche auftaucht. Der Name "Fenster" ist wörtlich zu verstehen: Man blickt durch ein Loch in den darüberliegenden Decken auf darunter liegende, ältere Schichten. Das Papier ist ein Exkursionsführer, der diese großräumige 3D-Geschichte an Handstücken, Berghängen und Straßenanschnitten belegt — also quasi ein "Feldversuch" zu dem Modell, das die Seismik (die 300-km-Übertragungsexperimente) vorher nur indirekt erkundet hatte.

--- END NOTE ---

--- FILENAME: 20-Literature/Tauernfenster (Exkursion Pfitschtal).md
--- BEGIN NOTE ---

# Tauernfenster (Exkursion Pfitschtal)

*Exkursionsführer-Kapitel „Exkursion 1: Die Reise nach Ureuropa" (S. 86–95), Route Brenner – Sterzing – Pfitschtal – Pfitscher Joch mit 5 Haltepunkten. Die Rohdatei ist ein OCR-Extrakt eines gescannten PDFs; alle Q-Anker verweisen auf die jeweilige Seite.*

## Das Tauernfenster als geologischer Tiefpunkt der Alpen

Das Tauernfenster ist das **steinerne Herz der Alpen**: Vom Brenner bis zum Katschberg (160 km) ist der gesamte Deckenstapel angeschnitten, der sich bei der Kontinentkollision übereinandergetürmt hatte — zuunterst Ureuropa ([[Tauernfenster|Helvetikum]]), obenauf ein Splitter Urafrikas (ostalpine Decken), dazwischen die vom Penninischen Ozean abgeschürften Gesteine ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]).

Mehr als **30 km mächtige Gesteinsdecken** lasteten vor 50 Millionen Jahren auf Ureuropa und drückten es mit einer Kraft von 100 000 Tonnen pro Quadratmeter in die Tiefe. Die Gesteine heizten sich im Verlauf von 10–20 Millionen Jahren auf **500 °C** auf, wurden plastisch deformierbar und wie Zahnpasta aus der Tube wieder hochgepresst. Die Hebungstendenz ist seit 35 Millionen Jahren ungebrochen: **1,2 mm/a** wurden als Durchschnitt der letzten 60 Jahre durch Präzisionsmessungen bestimmt ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]).

Die Erosion verhindert, dass die Alpen in den Himmel wachsen: Die dicke Gesteinsschicht über den Zillertaler Alpen wurde stetig abgetragen und der einstige Südrand Ureuropas wieder freigelegt. Die Nahtstelle, an der Pangäa einst auseinanderbrach, lag mindestens 50 km südlich der Tauern; bis dorthin erstreckte sich Ureuropa, und die Decken Urafrikas schoben sich über eine Strecke von **mehr als 150 km** darüber ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]).

## Ureuropa und der „Viertelmilliarden-Jahre-Sprung"

Der kleine Grenzposten am Pfitscher Joch ist mehr als eine politische Grenze: Wer ihn überschreitet, überspringt gleichzeitig eine **Viertelmilliarde Jahre**, denn er quert die große **Diskordanz** zwischen dem von der variszischen Gebirgsbildung betroffenen Ureuropa im Norden und dem „nachvariszischen Europa" im Süden ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]). Die Diskordanz trennt im gesamten außeralpinen Europa das metamorphe, gefaltete Grundgebirge vom nicht metamorphen, ungefalteten Deckgebirge: in Spanien liegt sie an der Basis der Meseta, in Frankreich/Belgien/Deutschland grenzt sie die Schichtstufenländer vom Kristallin ab, in Südtirol trennt sie den weißen Gipfelaufsatz der Tribulaune und Telfer Weißen vom düsteren Untergrund. Nirgendwo aber ist ihr so übel mitgespielt worden wie hier, wo selbst sonst kaum beanspruchte Gesteine fast bis zur Unkenntlichkeit zerquetscht, verfaltet und senkrecht gestellt wurden ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]).

Das Fundament Ureuropas bilden die **Tuxer und Zillertaler Zentralgneise**, zwei Aufwölbungen aus Graniten, Granodioriten und Tonaliten (im Norden zudem Gabbros), die im Verlauf der Alpenfaltung zu Gneisen ausgewalzt wurden. Wie in anderen Kristallingebieten sind diese Plutonite **vor ~300 Millionen Jahren** (Variszikum) in noch ältere Gesteine eingedrungen, von denen Reste erhalten blieben: die Gesteine des „Alten Daches", meist als **Greiner Schiefer oder Untere Schieferhülle** bekannt ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]). Neben Schwarzschiefern dominieren **Grüngesteine** (Amphibolite, Hornblendegneise, Garbenschiefer, Serpentinite), die von Basalten und Peridotiten abstammen; ihre chemische Zusammensetzung ähnelt Vulkaniten von Inselbögen und Randmeeren — Reste einer sehr frühen Epoche, in der Europa im Paläozoikum (kaledonische und variszische Gebirgsbildung) aus Kontinentbruchstücken und Inselbögen zusammengeschweißt wurde ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]).

## Quantitative Methodik: Wie man 30 km Überlagerung beweist

Die Überlagerung lässt sich aus der Mächtigkeit aller Einheiten abschätzen, die einst über dem Tauernfenster lagen: ~6 km penninische Decken, 15–20 km ostalpines Kristallin, 7–8 km Sedimente — anders ausgedrückt: die Pfunderer Berge, die Ötztaler und Stubaier Alpen und die Nördlichen Kalkalpen übereinander gestapelt ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).

Quantitative Angaben ermöglichten Hochdrucklabors und Indikatorminerale: **Disthen, Lawsonit, Granat und Glaukophane zeigen hohen Druck** an, **Staurolith, Cordierit und Sillimanit hohe Temperatur**. Jedes Mineral hat einen begrenzten Stabilitätsbereich; mit vielen Mineralen lassen sich die maximal erreichten Bedingungen gut eingrenzen — möglich nur, weil sich die meisten Minerale nach Abkühlung nicht mehr zurückwandeln (es fehlt Energie und oft Wasser), „sonst gäbe es gar keine metamorphen Gesteine" ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]). Noch genauere Werte liefern **Mischkristall-Paare in Kontakt** (Granat neben Biotit oder Plagioklas): Je nach Bedingungen teilen sie Elemente anders unter sich auf, woraus sich Druck und maximale Temperatur zuverlässig berechnen lassen ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).

Für den zeitlichen Ablauf gibt es **radiometrische Uhren**: Radioaktives Kalium zerfällt mit 1,19 Mrd. Jahren Halbwertszeit in Argon, das unterhalb der **Schließungstemperatur** im Kristallgitter gefangen bleibt. Muskowit schließt Argon unterhalb ~450 °C ein, Biotit bei ~300 °C. **Apatit-Spaltspuren** (zerstörte Kristallgitter durch Uranspaltung) reparieren unterhalb 150 °C nicht mehr; ihre Häufigkeit erlaubt, den Zeitraum seit Unterschreiten dieser Temperatur zu bestimmen. So ergeben sich mehrere Fixpunkte der Abkühl- und damit Hebungsgeschichte: **vor 17 Ma unterschritten die Gesteine 450 °C, vor 14 Ma 300 °C, vor 6 Ma 150 °C** ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).

Die **Retrodeformation** schließlich: Ein Strukturgeologe, der Falten und Überschiebungen vermessen hat, kann die Gesteine wieder in die ursprüngliche Lage zurückformen — bei den Tauern liegt dafür mindestens 50 km Platz Richtung Süden allein für die innere Sedimenthülle an, mehr noch für die ozeanischen Serien. Da von diesen nur noch ein Bruchteil erhalten ist, gelten die Ergebnisse nur als **unterste Minimalbeträge**. Zieht man die Entstehungsgeschichte des Atlantiks in Betracht, hatte der trennende Ozean damals etwa die Ausdehnung des heutigen Mittelmeeres ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).

## Variszische Krustenentwicklung und Tethys-Transgression

Über einer nach Norden einfallenden Subduktionszone wurden im Variszikum große Mengen ozeanischer und kontinentaler Kruste aufgeschmolzen und in weiten Teilen Eurasiens als **variszische (herzynische) Granite und Tonalite** aufgedrungen — zu denen auch die Zentralgneise gehören. Da die Erdkruste sich bei Gebirgsbildungen stets verdickt, folgt das Wechselspiel von Hebung und Abtragung: **vor ~250 Millionen Jahren lagen die Zentralgneise (noch unvergneist) und ihre Dachgesteine, die Greiner Schiefer, an der Erdoberfläche — genau wie heute**. Das Variszische Gebirge wurde zum Hügelland eingeebnet und schließlich vom Tethysmeer überspült ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).

## Struktur: Aufwölbungen, Pfitscher Mulde, germanisch-helvetische Fazies

Im Profil dominieren die beiden Aufwölbungen der Zentralgneise — doch diese verformen noch ältere Falten, die **auf dem Kopf stehen**. Die mesozoischen Sedimente wurden während der Deckenüberschiebung von ihrem Untergrund abgeschürft und in sehr enge, nach Norden geneigte Falten gelegt. Bei fortdauernder Anpressung wurde danach die gesamte Kruste Ureuropas gestaucht und in aufrechte Großfalten gelegt, in deren **Sattelkernen die Zentralgneise aufragen**, während in den **Mulden die einstigen Sedimente erhalten blieben** (Pfitscher Mulde) ([[10-Raw/Tauernfenster (Quelle).md#Seite 3|Q1]]). Weil beide Deformationen die Schichtzusammenhänge zerstörten und die Metamorphose die feinen Gesteinsunterschiede egalisierte, war die Rekonstruktion der geologischen Geschichte hier besonders schwierig und gelang erst vor kurzem ([[10-Raw/Tauernfenster (Quelle).md#Seite 3|Q1]]).

Die Schichtfolge ähnelt dem **germanisch-helvetischen Faziesbereich** Süddeutschlands und der Nordostschweiz, nicht den Dolomiten: Die gesamte Triasfolge ist nur wenige zehn Meter mächtig, Schwarzschiefer und Quarzite gehören in den Lias, darüber folgen braune sandige Kalke des Doggers, und erst im Malm stellt sich ein mächtigerer Kalkstein ein — der **Hochstegen-Marmor**. Von den großartigen Riffen der Dolomiten oder dem tausend Meter mächtigen Hauptdolomit fehlt jede Spur: „Wir sind eben in einem ganz anderen Ablagerungsraum mit eigener Geschichte!" ([[10-Raw/Tauernfenster (Quelle).md#Seite 3|Q1]]).

Die reiche **Mineralienvielfalt** erklärt sich aus offenen Spalten, die bei der Deformation aufrissen und durch die Metamorphose zu unterschiedlichen Zeiten und Temperaturen mit differierenden Lösungen gefüllt wurden: meist Quarz und Feldspäte (Adular, Periklin); in den höher temperierten Klüften Muskowit, Biotit, Rutil, Titanit; in solchen geringerer Temperatur Chlorit (meist als Pennin), Apatit, Laumontit, Pyrit ([[10-Raw/Tauernfenster (Quelle).md#Seite 3|Q1]]).

## Anfahrt: Silltal-Störung, Schieferhülle, Sterzing

Zwischen Brenner und Sterzing verläuft die **Silltal-Störung** oberhalb der Talfurche: An ihr ist das Ötztalkristallin, das einst als riesiges Dach über dem Tauernfenster auflag, um mehrere Kilometer abgesenkt worden, sodass es jetzt in gleicher Höhe ansteht ([[10-Raw/Tauernfenster (Quelle).md#Seite 3|Q1]]). Am Brenner und im größten Teil des Tales stehen schwärzlich-graue oder bräunliche **Kalkglimmerschiefer** an — Reste des Penninischen Ozeans (**Obere Schieferhülle**). Erst kurz vor Sterzing queren Schürflinge aus Triasdolomit und stark mylonitisiertes Altkristallin von der Basis der ostalpinen Decken den Talgrund ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]).

Das versumpfte Moos von Sterzing verdankt seine Entstehung einem **Bergsturz in prähistorischer Zeit bei Trens**, der den Eisack zu einem See aufstaute, der schnell von Sedimenten gefüllt wurde — eine Geschichte, die sich in den Alpen tausendfach abspielte, nachdem die Gletscher der Eiszeit die übertieften, vegetationslosen Talhänge ihrer Stütze beraubt hatten ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]). Einzigartig ist die Lage Sterzings, von wo man **alle vier geologischen Großeinheiten auf engstem Raum überblickt**: die Südalpen (Brixner Granit jenseits von Mauls), im Westen ostalpine Gneise, im Osten das Penninikum, unter dem die ersten Zeugen des Helvetikums auftauchen — alles getrennt durch Deckengrenzen oder große Störungen ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]).

## Stop 1: Das Fenster von Afens

3 km ab Sterzing tritt unter den Kalkglimmerschiefern erstmals ureuropäisches Terrain zutage: massige graue Gneise, in unverschieferten Partien granitähnlich — vermutlich zerscherte **Zentralgneise** in der Fortsetzung der Zillertaler Aufwölbung, durch die tiefe Erosion des Pfitschbaches angeschnitten. **Bruno Sander**, der weltbekannte Innsbrucker Geologe, bezeichnete dieses isolierte Vorkommen als „Fenster von Afens" ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]). Weiter talauf quert die Straße die fast senkrecht herandrängenden Kalkglimmerschiefer mit einem zwischengeschalteten grünen **Amphibolitband** — eine ehemalige Basaltlage, die an die ozeanische Natur der Gesteine erinnert ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]).

## Stop 2: Der Pfitscher Bergsturz

Nacheiszeitlich ging von der Flanke der Überseilspitze (2493 m) ein **Bergsturz** ab, der das Tal **150 m hoch vollständig abriegelte** und den Pfitschbach zu einem **8 km langen See** aufstaute ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]). Die Sturzmassen bestehen aus fest verbackenen Schutt- und Trümmermassen von Kalkglimmerschiefern ohne jede Schichtung: hausgroße Blöcke und fein zerriebenes Material liegen unsortiert und chaotisch durcheinander, wie für Bergstürze charakteristisch ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]).

**Um das Jahr 1100** rutschte ein Stück des durchnässten Stauwalles ins Rutschen; die sofort nachstürzenden Wasserfluten setzten mit starker erosiver Kraft den Auslauf immer tiefer, bis der ganze See mit etwa **70 Millionen Kubikmetern Wasser über Nacht leergelaufen war**. Die Flutkatastrophe richtete flußabwärts im Pfitsch- und Eisacktal große Verwüstung an und forderte viele Menschenleben ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]).

Die weite, versumpfte Ebene von Kematen ist durch Seesedimente gebildet; Schwemmkegel und alte Terrassen (auf denen z. B. die Häuser von Rein stehen) erlauben, den alten Seespiegel zu rekonstruieren — auch der Ortsname **Überwasser** erinnert noch daran. In Kematen steht ein über tausend Jahre altes Haus aus der Zeit, in der die Bewohner vom Seeufersaum lebten ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]).

## Stop 3: St. Jakob und Aiger Bach

St. Jakob liegt genau auf der geologischen Grenze zwischen Ureuropa im Norden und Penninischem Ozean im Süden: Die düsteren Wände der Felbe- und Grabspitze (3059 m) mit ihren dunkelgrünen **Präsinites** (= Gestein aus Chlorit, Epidot, Aktinolith und Albit) und braunen Kalkglimmerschiefern sind ozeanischer Natur, der Tuxer Zentralgneis am Kamm der Dellwand ist bereits kontinentale Kruste ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]). Die Hüllgesteine sind südlich von St. Jakob zu einer engen Mulde gefaltet — der **Pfitscher Mulde**, die sich von der Greiner Mulde bei der Berliner Hütte bis über den Wolfendorn verfolgen lässt; weil die Schichten überall fast senkrecht stehen, sind auf kurzer Strecke viele Einheiten aufgeschlossen ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]). Der Gasthof Knappenhof erinnert an eine bescheidene Bergbauvergangenheit im 17. Jahrhundert, als am Nordhang der Felbespitze (2849 m) etwas **Kupfer** gewonnen wurde ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]).

Am Aiger Bach (100 Höhenmeter Aufstieg zum Murschutzdamm) ist die Abfolge von unten nach oben: graphithaltige Schwarzschiefer (vermutlich präkambrisch, schlecht aufgeschlossen); **Konglomeratschiefer** — flach-linsenförmige Körper, einst mehr oder weniger kugelige Flußgerölle, vor ~250 Millionen Jahren (Perm) abgelagert, während das Variszische Gebirge abgetragen wurde ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]); silbergraue Muskowitschiefer mit millimeterkleinen **Eisencarbonatkristallen (Ankerit)**, die rautenförmige Hohlräume hinterlassen, dazu Eisen-Epidot und Disthen (einst ein schwach kalk- und eisenhaltiges Sediment, etwa roter Mergel); eine Lage weißen Quarzites mit Disthen, Turmalin und Magnetit; schließlich braune und weiße **Trias-Kalke und -Dolomite** mit hellbraunem Phlogopit (ein Magnesium-Biotit) und Zwischenschaltungen grüner Chloritoidschiefer. Ihr vielfach grob-poröses Aussehen (**Zellendolomit**) ist typisch für Lagunensedimente in ariden Klimabereichen ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]).

## Stop 4: Auffahrt zum Pfitscher Joch

Unterhalb von Stein liegt ein Steinbruch, in dem schöne Natursteinplatten aus **senkrecht einfallenden Trias-Quarziten** ungewöhnlich großer Mächtigkeit gebrochen werden; die Schieferflächen sind mit grünlichen Glimmern (Chlorit, Fuchsit, Phengit) belegt und führen winzige Pyritwürfelchen. Den Muldenkern markieren schwärzliche und weiße **Lias-Quarzite**, jenseits derer sich die Folge spiegelsymmetrisch wiederholt ([[10-Raw/Tauernfenster (Quelle).md#Seite 6|Q1]]).

Oberhalb der Abzweigung zur Hochfeilerhütte quert die Straße Quellaustritte mit **rostrotem Wasser** aus pyritführenden Schiefern, die von der Rotbachlspitze herabziehen — bei der Zersetzung des Pyrites (Eisensulfid) entstehen die färbenden Eisenverbindungen ([[10-Raw/Tauernfenster (Quelle).md#Seite 6|Q1]]).

Längere Zeit verläuft die Straße in schwarzen **Graphitschiefern (Furtschaglschiefer)** der Greiner Serie: Sie wurden wahrscheinlich **vor mehr als 700 Millionen Jahren** als schwarze Tonschiefer in einem schlecht durchlüfteten kleinen Meeresbecken abgelagert — vermutlich als Rücken zwischen dem Festland und einem Inselbogen, der während der kaledonischen oder variszischen Gebirgsbildung an Ureuropa angeschweißt wurde ([[10-Raw/Tauernfenster (Quelle).md#Seite 7|Q1]]).

Von der großen Kehre bei 2050 m (Abzweigung Griesscharte/Hochferner) blickt man in die Nordwände des Hochferners: Grüne Amphibolite, graue Phyllite und braune Kalkglimmerschiefer der **penninischen Decken** sind dort eng gefaltet — eine der am stärksten komprimierten Stellen der gesamten Alpen: „Wie Strudelteig sind Gesteine verschiedensten Alters und Ursprungs zu dünnen Lamellen ausgewalzt und steil aneinandergepreßt" ([[10-Raw/Tauernfenster (Quelle).md#Seite 7|Q1]]). In der Griesscharte folgen von Süd nach Nord helle Triasmarmore und Quarzite, dunklere Glimmerschiefer der Kreide (mit einzelnen Kalkbänken, dadurch von den Furtschaglschiefern unterscheidbar) und ein grauer **Mikroklin-Augengneis** — Teil einer Zentralgneislamelle, welche die vom Hochfeiler herüberziehende Abfolge von der Greiner und Pfitscher Mulde trennt. Das ganze Hochstellermassiv besteht aus steil stehenden Furtschaglschiefern ([[10-Raw/Tauernfenster (Quelle).md#Seite 7|Q1]]).

## Stop 5: Umgebung des Pfitscher Joches

In den steilen Wänden zeigt sich die bunte Fleckung der **Konglomeratgneise**: Die Gerölle sind völlig plattgewalzt, manche nur noch papierdünn — „wie in genialen Schraubstöcken sind sie zwischen den Zentralgneisen zerquetscht" ([[10-Raw/Tauernfenster (Quelle).md#Seite 8|Q1]]). Davor zieht ein rostig-gelblich witternder, weißlicher **pyritführender Schiefer** durch, der an der Rotbachlspitze über hundert Meter mächtig wird und vermutlich ein stark verschieferter Zentralgneis aus dem ehemaligen Dachbereich der Intrusion ist. Solche Zonen sind häufig **vererzt**, weil sich hier die chemischen Restlösungen und Gase sammeln, die bei der Erstarrung des Granites nicht in die normalen Minerale eingebaut werden können — bei Mittersill in Österreich führen solche Gneise neben Pyrit das Wolframmineral **Scheelit**, das abgebaut wird ([[10-Raw/Tauernfenster (Quelle).md#Seite 8|Q1]]).

Mit weißem Quarz gefüllte Klüfte zeigen **Flüssigkeitseinschlüsse**, die den Quarz trüben und für Forscher Information über die Lösungen und P-T-Bedingungen beim Quarzwachstum liefern. Dieser derbe Quarz entstand meist bei relativ geringer Temperatur **während der Hebungsphase**; kleinere Klüfte mit Muskowit und Periklin sowie klarem Quarz sind älter und höher temperiert und zeigen eine Phase, in der das Gestein nicht mehr ganz plastisch reagierte ([[10-Raw/Tauernfenster (Quelle).md#Seite 8|Q1]]).

Aufwärts werden die Gerölle kleiner und verschwinden — ein Zeichen **nachlassender Reliefenergie**, also des Flächerwerdens der Landschaft im Lauf des Perm. Es folgen feinkörnige Glimmerschiefer aus einer Grauwacke mit feiner **Runzelschieferung** (entsteht, wenn geschiedertes und gefaltetes Gestein ein zweites Mal deformiert wird) und ein massiger grauer Gneis mit schwarzglänzenden **Turmalinnädelchen**, der im Mikroskop reliktisch das Gefüge eines **Quarzporphyrs** erkennen lässt — etwa so alt wie der Bozner Quarzporphyr, nur durch Metamorphose stark verändert. Auf den silbergrauen, epidothaltigen Ankeritschiefern steht das **Pfitscher-Joch-Haus, 2275 m** ([[10-Raw/Tauernfenster (Quelle).md#Seite 8|Q1]]).

Kurz unterhalb des Joches finden sich in den Quarzschiefern feine Hämatitschleier (Eisenoxid) und **Lazulith** sowie rote **Manganepidote**; am Nordrand der Felsplatten tritt das blaue Mineral massenhaft auf. Aufgrund des Eisengehaltes schließt der Führer, dass der Quarzit vor der Metamorphose einmal ein Rottstein (**Alpiner Buntsandstein**) war, dessen Eisenpigment zu schwarzem Hämatit kristallisierte. Die Rinne liegt exakt im **Kern der Pfitscher Mulde** — beim jüngsten Gestein; 150 Höhenmeter tiefer würde sich der Quarzitschiefer aufspalten und die **evaporitischen Serien (Rauhwacken, Dolomit) der Mittleren Trias** erschienen ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).

Am Langsee steht wieder Konglomeratgneis an; die schwächere Deformation erlaubt, den Geröllbestand zu studieren: **Aplite, Granite, Graphitschiefer, Marmore und vereinzelte Grüngesteine**, Korngrößen wechselnd, an manchen Geröllen noch Kanten und Ecken. Das sind Kennzeichen eines **„unreifen" Sediments** mit kurzen Transportwegen — weiche Gerölle wie Kalke, Marmore oder Schiefer wären sonst längst zerstört worden; zudem finden sich nur Gerölltypen aus der Greiner Serie und dem Zentralgneis. Der Führer folgert: die **Füllung eines tektonischen Grabens oder ein großer Schuttfächer in einem ariden Gebiet** ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]). Die Konglomerate sind flachgedrückt und in die Länge gezogen, ihre längste Achse taucht nach Westen ab — typisch für die gesamte Region: **Alle Gesteine sind in Ost-West-Richtung gedehnt und gestreckt**; Minerale sind parallel eingeregelt, und **Zerrklüfte** öffneten sich genau in diese Richtung, gefüllt mit Muskowit, Periklin, Bergkristall und anderen Mineralen, die erhöhte Deformationstemperaturen anzeigen ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).

Nördlich des Langsees beginnen die schwarz-grünen **Amphibolite mit schwarzen Hornblendestengeln** — spärliche Reste einer **Ur-Tethys mit ihren Inselbögen**. Sie stehen in intrusivem Verband mit dem Tuxer Zentralgneis (wegen starker Ausdünnung schwer erkennbar); helle Bänder sind Gänge granitischen Magmas, die zu dünnen Streifen ausgewalzt wurden. Die strenge parallele Ausrichtung der Hornblendenädelchen zeigt, dass sie **während der Ost-West-Dehnungsphase gewachsen sind**; Zerrklüfte sind hier meist mit Chlorit, Quarz und Periklin gefüllt ([[10-Raw/Tauernfenster (Quelle).md#Seite 10|Q1]]).

Die folgenden Zentralgneise sehen ihrem Ausgangsgranit noch recht ähnlich: Obwohl sie die gesamte alpine Gebirgsbildung mitmachten, zeigt sich nur eine schwache Schieferung durch parallele Glimmer-Orientierung. In schmalen Zonen wird die Schieferung sehr ausgeprägt — diese **duktilen Scherzonen** sind Flächen erhöhter Mobilität, an denen sich Gesteine gegeneinander bewegen, ohne zu zerbrechen: Wegen des allgemein hohen Druckes wäre die Reibung auf einer Bruchfläche viel zu groß; statt dessen finden bruchlose Deformationen innerhalb der Kristallgitter oder ausgedehnte Umkristallisationen statt, und das Gestein reagiert plastisch wie eine Flüssigkeit ([[10-Raw/Tauernfenster (Quelle).md#Seite 10|Q1]]).

**Dunkle Gänge (Lamprophyre)** rühren von basaltischen Magmen aus großer Tiefe her; die zusätzliche Wärmeenergie basischer Magmen in der tieferen Erdkruste lässt die Gesteine dort zu Granit aufschmelzen. Die zahlreichen dunklen, handgroßen Flecken in Graniten und Tonaliten werden als Reste der frühen basischen Intrusionen angesehen, die sich nicht mit dem Granitmagma mischten — andere Forscher halten sie für Zusammenballungen früh abgeschiedener Minerale ([[10-Raw/Tauernfenster (Quelle).md#Seite 10|Q1]]). Die **hellen Gänge (Aplite, Pegmatite)** entstehen erst im Lauf der Erstarrung: Durch Abkühlung schrumpft der Granit, wie in einer austrocknenden Tonpfütze kommt es zu Rissen, in die die Restschmelze aus dem noch nicht ganz verfestigten Granit wie aus einem Schwamm ausgepresst wird ([[10-Raw/Tauernfenster (Quelle).md#Seite 10|Q1]]).

Nördlich der Grenze (bei den beiden Jochseen) steckt der westlichste jener **Serpentinitkörper**, die die altkristallinen Greiner Schiefer zu Dutzenden durchsetzen — Repräsentanten eines **ozeanischen Mantels, der lange vor der Alpenbildung ans Tageslicht gebracht worden war**; in Randpartien finden sich idiomorphe **Chromit-Oktaeder** und dunkelgrüne Aktinolithstengel ([[10-Raw/Tauernfenster (Quelle).md#Seite 11|Q1]]). Vom Joch führt der Weg zur Landshuter Hütte (jetzt Europahütte, 2648 m). Vom Pfitscher-Joch-Haus genießt man den Blick auf das klassische eiszeitliche **U-Tal**: In größerer Höhe mündende Hängetäler erlauben, den Eisstrom zu rekonstruieren, der das gesamte Tal noch **vor 15 000 Jahren** ausfüllte; Seitenmoränen des Stampflkees markieren den **historischen Gletscherstand seit 1850** und den dramatischen Rückgang der Gletscher in eineinhalb Jahrhunderten. Der Tuxer Zentralgneis zieht sich blankpoliert bis unter den Wolfendorn und erscheint 200 km weiter westlich im **Aar- und Gotthardmassiv der Schweiz** wieder ([[10-Raw/Tauernfenster (Quelle).md#Seite 11|Q1]]).

## Deformationsgeschichte des Tauernfensters in vier Phasen

- **Phase 1 (60–50 Ma):** Der europäische Südrand wird von den penninischen und ostalpinen Decken überschoben ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).
- **Phase 2:** Die mesozoischen Sedimente werden losgeschürft und vom Untergrund abgelöst; die Falten sind stark nach Norden oder Nordwesten geneigt, die jüngeren Schichten liegen jeweils weiter im Norden ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).
- **Phase 3:** Durch die Überlast von 30 km Gestein wird der Bereich tief ins Erdinnere abgesenkt und heizt sich auf über 500 °C auf; die Gesteine reagieren plastisch ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).
- **Phase 4 (30–20 Ma):** Die Adriatische Platte (Italien südlich der Pustertallinie und der Insubrischen Linie) bewegt sich um einige hundert Kilometer nach Westen, gleichzeitig drückt Afrika nach Norden. Die plastischen Gesteine werden „wie von einem riesigen Caterpillar zusammengeschoben": Die großen Tuxer und Zillertaler Antiklinalkerne wölben sich hoch, die schon gefalteten Schichten der Pfitscher Mulde werden steilgestellt und erneut gequetscht; zugleich wird die ganze Region nach Westen verschleppt und die Schichten horizontal in die Länge gezogen ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).
- **Phase 5:** Die stark verdickte Erdkruste unter den Tauern bedingt starken Auftrieb: Die Region bleibt 30 Millionen Jahre lang Hochgebirge mit besonders schneller Abtragungsrate — **30 km Gesteine werden weggeschafft**; durch die Entspannung reißen Klüfte auf und füllen sich mit verschiedensten Mineralien ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).

--- END NOTE ---

--- FILENAME: 20-Literature/The Trouble With Trilobites.md
--- BEGIN NOTE ---

# The Trouble With Trilobites

Die **Trilobiten** waren für mehr als 270 Millionen Jahre die erfolgreichsten und möglicherweise häufigsten Tiere der Erde — bis sie im Verlauf von vier Aussterbeereignissen endgültig verschwanden, ohne direkte Nachfahren zu hinterlassen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=24s" title="00:00:24">(V)</a>. Der PBS-Eons-Dokumentarfilm erzählt diese Geschichte als die erste Erfolgsgeschichte des Tierreichs und fragt am Ende, warum die Trilobiten so lange überleben konnten — und nicht, warum sie ausstarben.

### Anatomische Grundlagen

Vor rund 540 Millionen Jahren lebte fast alles Leben im Meer und war überwiegend weich wie Schwämme, Würmer und Quallen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=66s" title="00:01:06">(V)</a>. Vor etwa 521 Millionen Jahren tauchten die ersten bekannten Trilobiten im heutigen Sibirien auf <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=82s" title="00:01:22">(V)</a>; sie könnten sich aus kleinen, dickhäutigen, segmentierten Würmern wie Spriggina entwickelt haben <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=94s" title="00:01:34">(V)</a>. Anders als diese Vorfahren besaßen Trilobiten Beine, komplexe Augen und einen ausgefeilten Verdauungstrakt; zudem war ihr ganzer Körper von einem Exoskelett aus Calcit und Chitin bedeckt — sie waren echte Arthropoden und ein Gründungsmitglied der Gruppe, zu der heute Spinnentiere, Krebstiere und Insekten gehören <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=105s" title="00:01:45">(V)</a>.

### Dominanz im Kambrium

Mit diesen Merkmalen dominierten die Trilobiten die kambrischen Meere und ernährten sich von Würmern und anderen ungeschützten Wirbellosen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=127s" title="00:02:07">(V)</a>. Innerhalb von 40 Millionen Jahren nach ihrem ersten Erscheinen existierten mindestens 60 taxonomische Familien — von den großäugigen Asaphus bis zum Elrathia, dem häufigsten Trilobiten-Fossil der USA <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=127s" title="00:02:07">(V)</a>.

Die kambrischen Meere wurden jedoch zunehmend feindlicher: Im Kambrium trat Prädation erstmals auf, Tiere jagten andere Tiere, und Trilobiten-Fossilien mit Bissspuren belegen das <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=157s" title="00:02:37">(V)</a>.

### Verteidigungsanpassung: Enrollierung

Gegen die neuen Räuber entwickelten einige Trilobiten die Enrollierung: Gattungen wie Flexicalymene konnten sich zu kleinen Kugeln zusammenrollen, wie heutige Asseln oder Gürteltiere <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=157s" title="00:02:37">(V)</a>.

### Ordovizium-Silur-Extinktion

Ab etwa 445 Millionen Jahren versetzte das Klima dem Leben im Meer einen Doppelschlag <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=199s" title="00:03:19">(V)</a>. Eine dramatische Abkühlung veränderte die Meeresströmungen und drosselte die Versorgung mit warmwasserliebenden Nahrungsquellen wie Algen; zugleich band eine Vereisung große Mengen Wasser und senkte den Meeresspiegel drastisch <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=205s" title="00:03:25">(V)</a>. Dieses Ereignis, die Ordovizium-Silur-Extinktion, löschte rund 25 % aller taxonomischen Familien aus, darunter etwa die Hälfte der Trilobiten-Familien <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=205s" title="00:03:25">(V)</a>. Die verbliebenen Familien waren vor allem an kühlere Meere angepasst, etwa Dalmanites <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=235s" title="00:03:55">(V)</a>.

### Jaws: Kieferfische als evolutionärer Druck

Die im Kambrium entstandenen Anpassungen wie Zangen, Stacheln und Klauen kamen nun zum Tragen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=245s" title="00:04:05">(V)</a>. Die wahrscheinliche Kryptonit der Trilobiten waren jedoch die Kiefer: Vor etwa 420 Millionen Jahren erschienen die ersten Kieferfische und übten zusätzlichen evolutiven Druck aus <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=251s" title="00:04:11">(V)</a>. Etwa 20 Millionen Jahre später tauchen im Fossilbericht neue, stachelige Trilobiten wie Dicranurus auf <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=256s" title="00:04:16">(V)</a>.

### Spätdevon-Extinktion

Ab rund 375 Millionen Jahren sanken die Sauerstoffwerte im Wasser, große Mengen kohlenstoffreicher Sedimente wurden abgelagert und Riffgemeinschaften brachen zusammen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=284s" title="00:04:44">(V)</a>. Während die neuen Kieferfische sowie die auf dem Land entstehenden Pflanzen und Insekten überlebten, verschwanden die meisten kieferlosen Bodenfresser — einschließlich der Trilobiten <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=284s" title="00:04:44">(V)</a>. Die Spätdevon-Extinktion löschte rund 20 % der marinen Tierfamilien aus; es blieben nur noch vier Trilobiten-Familien übrig <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=305s" title="00:05:05">(V)</a>.

### Perm-Trias-Massenaussterben

Der letzte Schlag kam mit dem größten Massenaussterben der Erdgeschichte: Vor 252 Millionen Jahren veränderte sich die Atmosphäre radikal <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=323s" title="00:05:23">(V)</a>. Diskutiert werden ein Asteroideneinschlag, massive vulkanische Aktivität und durch verschiebende Landmassen veränderte Klimamuster <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=327s" title="00:05:27">(V)</a>. Innerhalb von wahrscheinlich weniger als einer Million Jahren verschwanden 70 % der Landarten und 95 % der Meeresarten — einschließlich der letzten Trilobiten <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=339s" title="00:05:39">(V)</a>.

### Fazit: eine Erfolgsgeschichte

Die Geschichte der Trilobiten ist die erste Erfolgsgeschichte des gesamten Tierreichs <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=361s" title="00:06:01">(V)</a>. Mit über 15.000 beschriebenen Arten zählen sie zu den vielfältigsten ausgestorbenen Organismengruppen; sie existierten länger als die Nicht-Vogel-Dinosaurier und länger als die Säugetiere, einschließlich uns <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=361s" title="00:06:01">(V)</a>. Die eigentliche Frage ist deshalb nicht, warum sie ausstarben, sondern wie sie so lange überdauern konnten — denn wir sind heute eines der erfolgreichsten Tiere, und die Probleme der Trilobiten könnten irgendwann unsere eigenen sein <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=393s" title="00:06:33">(V)</a>.

--- END NOTE ---

--- FILENAME: 20-Literature/There's An Invisible Ocean Between These Fossils.md
--- BEGIN NOTE ---

# There's An Invisible Ocean Between These Fossils

Der PBS-Eons-Film erzählt die **hundertjährige Entdeckungsgeschichte** des [[Wilson-Zyklus]]: Wie Trilobiten-Fossilien in Neufundland halfen aufzudecken, dass Ozeanbecken alle paar hundert Millionen Jahre neu entstehen — sie werden im Grunde "reinkarniert" <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=57s" title="00:00:57">(V)</a>.

### Der Ausgangspunkt: die Entdeckung des Mittelatlantischen Rückens

Erst in den 1950er Jahren kartierte die Wissenschaft mit Sonar erstmals den Boden des Atlantiks <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=8s" title="00:00:08">(V)</a>. Dabei stieß sie auf eine Kette von Unterwasserbergen mit fast ständiger seismischer und vulkanischer Aktivität — den **Mittelatlantischen Rücken** <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=17s" title="00:00:17">(V)</a>. Er wurde zu einem entscheidenden Beleg für die Theorie der [[Kontinentaldrift|Kontinentaldrift]]: Seit der Trias, vor rund 230 Millionen Jahren, öffnet sich der Atlantik von dieser Naht aus <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=26s" title="00:00:26">(V)</a>. Trilobiten-Fossilien kleiner als eine Handfläche deuten aber darauf hin, dass dieser Vorgang schon einmal stattgefunden hat <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=46s" title="00:00:46">(V)</a>.

### Walcotts Trilobiten-Rätsel in Neufundland (1888)

1888 besuchte der Paläontologe Charles Doolittle Walcott Neufundland, um die Verbreitung verschiedener Trilobiten-Arten zu kartieren <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=74s" title="00:01:14">(V)</a>. Er beschäftigte sich damals mit den ältesten bekannten Fossilien, dem Kambrium vor rund 520 Millionen Jahren; später wurde er durch die Burgess-Schiefer berühmt <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=78s" title="00:01:18">(V)</a>. Die häufigen kambrischen Arthropoden begeisterten die Fachwelt, weil ihre Zahl und Vielfalt sie als **geologisches Werkzeug** zur relativen Datierung und Korrelation von Gesteinsschichten über weite Distanzen nutzbar machte ([[Trilobiten als biostratigraphisches Werkzeug]]) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=107s" title="00:01:47">(V)</a>.

Doch Walcott fand etwas Merkwürdiges: Die Flachwasser-Trilobiten im Osten Neufundlands unterschieden sich stark von denen im Westen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=123s" title="00:02:03">(V)</a>. Im Osten dominierten etwa Paradoxididen, im Westen Olenelliden <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=129s" title="00:02:09">(V)</a>. Das war unerwartet, weil nahe beieinanderliegende Flachwasserumgebungen eigentlich Durchmischung erlauben sollten <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=136s" title="00:02:16">(V)</a>. Walcott beschrieb zwei geografisch getrennte Fossilgemeinschaften (mit Brachiopoden und Graptolithen), die er **"Atlantische" und "Pazifische" Faunen** nannte, getrennt durch eine Linie mitten durch Neufundland <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=153s" title="00:02:33">(V)</a> (siehe [[Atlantische und Pazifische Faunen]]).

### Das weltweite Verteilungsmuster

Dasselbe Muster fand man bald weltweit: "Atlantische" Gemeinschaften in England und Wales, direkt neben "Pazifischen" in Schottland und Nordirland <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=174s" title="00:02:54">(V)</a>. Auf Spitzbergen gab es "Pazifische" Fossilien, aber keine in gleich alten Gesteinen auf der Westseite der Insel <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=187s" title="00:03:07">(V)</a>. New Brunswick beherbergte "Atlantische", die Nachbarn Maine und Quebec nur "Pazifische" Faunen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=200s" title="00:03:20">(V)</a>. Dafür gab es lange keine Erklärung <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=210s" title="00:03:30">(V)</a> — zumal die Geologen annahmen, die Kontinente seien schon immer am selben Ort gewesen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=213s" title="00:03:33">(V)</a>. Man vermutete deshalb eine gewaltige untermeerische Schlucht mitten durch Neufundland, die inzwischen verschwunden sei <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=222s" title="00:03:42">(V)</a>.

### Die Wende: Wegener und Wilson

Die Wende kam im frühen 20. Jahrhundert mit der Theorie der [[Kontinentaldrift]], vorgeschlagen 1912 von Alfred Wegener: Nordamerika und Europa sowie Südamerika und Afrika verhalten sich wie Puzzleteile <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=244s" title="00:04:04">(V)</a>. Trotz der offensichtlichen geometrischen Evidenz wurde die Theorie lange abgelehnt, weil niemand erklären konnte, wie sich die Kontinente getrennt haben <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=262s" title="00:04:22">(V)</a>. In den 1940er Jahren griff der kanadische Geologe [[John Tuzo Wilson]] das neufundländische Trilobiten-Rätsel mit der weitgehend abgelehnten Idee der Kontinentaldrift im Hinterkopf wieder auf <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=269s" title="00:04:29">(V)</a>. An der Linie zwischen den beiden Faunen fand er zerstörte, zerquetschte metamorphe und vulkanische Gesteine — ein sicheres Zeichen einer gewaltigen Kontinentalkollision <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=282s" title="00:04:42">(V)</a>. Der Grund für die verschiedenen Faunen: Sie bewohnten völlig verschiedene Küstenlinien, getrennt durch einen tiefen, unüberquerbaren Ozean, der inzwischen geschlossen und verschwunden ist <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=297s" title="00:04:57">(V)</a>.

Die Verfolgung der Fossilgemeinschaften durch die Zeit stützt das: Im Kambrium waren die Faunen sehr verschieden, im Ordovizium ähnlicher, im Silur noch ähnlicher — die gegenüberliegenden Seiten drifteten also aufeinander zu <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=313s" title="00:05:13">(V)</a>. Wilson kartierte die Kollisionsbelege auf der gesamten Nordhalbkugel (Spitzbergen, Skandinavien, Britische Inseln, Maine bis Connecticut) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=340s" title="00:05:40">(V)</a>. Diese Zonen zerstörter Gesteine bilden die **Iapetus-Sutur** — der gesamte Rest des antiken, trilobitentrennenden Iapetus-Ozeans <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=350s" title="00:05:50">(V)</a> (siehe [[Iapetus-Sutur]]). Das Seltsame: Diese Sutur folgt ungefähr derselben Linie, entlang der sich der moderne Atlantik öffnete <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=359s" title="00:05:59">(V)</a>. Walcotts Fossil-Rätsel beiderseits des Atlantiks markieren Orte, an denen Stücke der alten Kontinente bei der Öffnung auf der "falschen" Seite hängen blieben <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=370s" title="00:06:10">(V)</a>.

### Der Wilson-Zyklus

1966 fragte Wilson als erster, ob der Atlantik tatsächlich geschlossen und wieder geöffnet wurde <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=381s" title="00:06:21">(V)</a>. Diese Idee wurde zur Kerntheorie der Plattentektonik, dem [[Wilson-Zyklus]]: Ozeanbecken schließen und öffnen sich entlang derselben Kollisionsgrenzen, statt dass sich Kontinente jedes Mal neu zerbrechen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=398s" title="00:06:38">(V)</a> (siehe [[Die acht Phasen des Wilson-Zyklus]]).

Der Zyklus hat acht Hauptstadien, die weltweit an verschiedenen Orten zu beobachten sind <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=410s" title="00:06:50">(V)</a>:
1. **Extrusion/Sag-Becken**: Dehnung im Kontinent erzeugt eine Mulde in der Kruste (Beispiel: Westsibirisches Becken) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=417s" title="00:06:57">(V)</a>
2. **Kontinentales Rifting**: Dehnung bis der Kontinent aufreißt, Meerwasser strömt ein, ein embryonaler Ozean entsteht (heute: Ostafrikanischer Graben) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=430s" title="00:07:10">(V)</a>
3. **Junger Ozean**: Meeresbodenspreizung weitet den Graben (heute: Rotes Meer) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=450s" title="00:07:30">(V)</a>
4. **Reifer Ozean**: Die Hälften driften auseinander (Zustand des Atlantiks heute) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=456s" title="00:07:36">(V)</a>
5. **Subduktionszone**: An mindestens einem Beckenrand entsteht eine Subduktionszone (der "Ring of Fire" um den Pazifik) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=474s" title="00:07:54">(V)</a>
6. **Schrumpfen**: Ozeankruste wird subduziert, das Becken schrumpft (heute: Mittelmeer) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=490s" title="00:08:10">(V)</a>
7. **Schließung und Kollision**: Das Becken schließt sich, Kontinente kollidieren, eine zerstörte Suturzone bleibt (anfangs oft ein Gebirge wie der Himalaya) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=506s" title="00:08:26">(V)</a>
8. **Stabilität**: Der zusammengeschweißte Kontinent genießt Stabilität, bis der Zyklus mit Dehnung und Rifting von vorn beginnt <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=516s" title="00:08:36">(V)</a>

### Warum öffnen sich neue Ozeane an Suturzonen?

Neue Ozeanbecken öffnen sich bevorzugt an Suturzonen, weil die Plattenspreizung teilweise von unten angetrieben wird: Heißes Mantelmaterial quillt auf und breitet sich aus, wenn es auf die Krustenunterseite trifft <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=534s" title="00:08:54">(V)</a>. Im globalen Maßstab geschieht dieser Aufstrom unter alten Suturzonen mitten in Kontinenten, weil Subduktion an den Kontinenträndern das Absinken ist <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=544s" title="00:09:04">(V)</a> — was hinuntergeht, kommt oben wieder zurück <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=555s" title="00:09:15">(V)</a>. Zudem sind Suturzonen Schwächezonen der Kruste, wo die Gesteine bereits zerstört sind <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=560s" title="00:09:20">(V)</a>.

Das hängt mit Superkontinent-Zyklen zusammen, läuft aber in kleinerem geografischem Maßstab und kürzerer geologischer Zeitspanne ab <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=571s" title="00:09:31">(V)</a>. Heutige Beispiele: Der Rio-Grande-Rift (Colorado, New Mexico, Texas) folgt einer alten Sutur der Farallon-Platte <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=598s" title="00:09:58">(V)</a>; ein Riftsystem in Nordostchina öffnet sich entlang des Trans-North-China-Orogens, das vor fast 2 Milliarden Jahren entstand <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=615s" title="00:10:15">(V)</a>; der Ostafrikanische Graben ist nur fünf bis zehn Millionen Jahre von einem Ozean entfernt und folgt dem Ostafrikanischen Orogen, wo das Mosambik-Meer vor 720 Millionen Jahren lag <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=632s" title="00:10:32">(V)</a>.

### Bedeutung und Ausblick

Wilsons Lösung des Trilobiten-Rätsels half, die Kontinentaldrift-Theorie durchzusetzen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=642s" title="00:10:42">(V)</a>; heute ist der Wilson-Zyklus fundamental für das Verständnis der Plattentektonik <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=649s" title="00:10:49">(V)</a>. Entgegen der Intuition (beim Metallschweißen ist die Schweißnaht stärker als das Material) sind die gefalteten und verworfenen Suturzonen **schwächer** und brechen unter Druck zuerst <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=666s" title="00:11:06">(V)</a>. Dadurch bleiben dieselben Plattengrenzen über hunderte Millionen Jahre erhalten; viele Kontinent-Interieurs blieben Milliarden Jahre unverändert <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=675s" title="00:11:15">(V)</a>. Mit diesem Wissen lassen sich künftige Ozeane vorhersagen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=689s" title="00:11:29">(V)</a> — und es hilft zu verstehen, wie sich Gezeiten, Ozeanzirkulation und Klima über Millionen Jahre verändert haben, alles Faktoren, die die Evolution des Lebens lenken können <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=703s" title="00:11:43">(V)</a>. An den Ufern des antiken Iapetus waren es die Trilobiten, die die Wellen des Wilson-Zyklus spürten — bald werden es die Bewohner des Atlantiks sein <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=714s" title="00:11:54">(V)</a>.

--- END NOTE ---

--- FILENAME: 20-Literature/Trilobiten (Wikipedia).md
--- BEGIN NOTE ---

# Trilobiten (Wikipedia)

Der Wikipedia-Artikel „Trilobiten“ ist eine systematische Gesamtdarstellung der ausgestorbenen Klasse der Trilobita. Die **Trilobiten** („Dreilapper“, von altgriechisch *tria* „drei“ und *lobós* „Lappen“) sind eine ausgestorbene Klasse meeresbewohnender Gliederfüßer (Arthropoda) ([[10-Raw/Trilobiten (Quelle).md|Q1]]).

## Taxonomischer Umfang und Zeithorizont

Die Trilobiten existierten nahezu während des gesamten Paläozoikums — von der 2. Serie des Kambriums (Beginn vor 521 Mio. Jahren) bis zum Massenaussterben am Ende des Perms vor etwa 251 Mio. Jahren ([[10-Raw/Trilobiten (Quelle).md|Q1]]). Ihre mit Calcit (Calciumcarbonat) verstärkten Exoskelette sind als Fossilien in großer Zahl erhalten und ermöglichen die Rekonstruktion von Evolution und Formenreichtum; zusammen mit ihrer [[Trilobiten als biostratigraphisches Werkzeug|Schichtbeständigkeit]] und weiten geographischen Ausdehnung macht das die Trilobiten zu wichtigen Leitfossilien des Paläozoikums, insbesondere des Kambriums ([[10-Raw/Trilobiten (Quelle).md|Q1]]).

Die Klasse umfasst neun anerkannte [[Ordnungen der Trilobiten|Ordnungen]], über 150 Familien, über 5000 Gattungen und mehr als 15.000 beschriebene Arten — die divergenteste Gruppe unter allen ausgestorbenen Lebewesen ([[10-Raw/Trilobiten (Quelle).md|Q1]]). Die meisten Trilobiten waren 3 bis 10 cm groß; der größte bekannte Vertreter, *Isotelus rex* aus dem Oberordovizium Nordamerikas, erreichte über 70 cm ([[10-Raw/Trilobiten (Quelle).md|Q1]]). Nächste heute noch lebende Verwandte sind die Pfeilschwanzkrebse ([[10-Raw/Trilobiten (Quelle).md|Q1]]). Die Bezeichnung „Trilobit“ wurde 1771 von Johann Ernst Immanuel Walch eingeführt, setzte sich aber erst zu Beginn des 19. Jahrhunderts wissenschaftlich durch ([[10-Raw/Trilobiten (Quelle).md#Namensgebung|Q1]]).

## Körperbau

Der [[Körperbau der Trilobiten|Körperbau]] der „Dreilapper“ ist zweifach dreigeteilt: sagittal in drei Loben (Spindellobus plus zwei pleurale Loben) und transversal in drei Tagmata (Kopfschild/Cephalon, Thorax, Schwanzschild/Pygidium) ([[10-Raw/Trilobiten (Quelle).md#Körperbau|Q1]]).

Der Spindellobus trägt auf dem Cephalon die Glabella (Stirnlappen) mit Antero- und Posteroglabella, auf dem Pygidium die in Rhachisringe gegliederte Rhachis; der Übergang zur Rhachis wird als Nackenring (Occipitalring) bezeichnet ([[10-Raw/Trilobiten (Quelle).md#Spindellobus|Q1]]). Die pleuralen Loben umfassen die Freiwangen mit den Facettenaugen sowie die Pleuren des Thorax ([[10-Raw/Trilobiten (Quelle).md#Pleuraler Lobus|Q1]]). Auf der Unterseite des Cephalons diente das Hypostom als Teil des Mundapparats und ist in konterminanter, natant und unabhängiger Positionierung überliefert ([[10-Raw/Trilobiten (Quelle).md#Kopfschild (Cephalon)|Q1]]). Als Kopfanhänge existierte nur ein Paar langer Gliederantennen; die übrigen Gliedmaßen entsprechen den [[Körperbau der Trilobiten|Spaltbeinen]] der Rumpfsegmente ([[10-Raw/Trilobiten (Quelle).md#Kopfschild (Cephalon)|Q1]]).

Die [[Gesichtsnaht und Häutung der Trilobiten|Gesichtsnaht]] (*Sutura facialis*) ist eine Sollbruchstelle im Exoskelett, die die Häutung ermöglicht: Der Kopfschild zerfällt dabei in Cranidium (Glabella + Fixigenae) und die beiden Librigenae (Freiwangen) ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]). Je nach Verlauf unterscheidet man protopare/hypopare, propar, gonatopare, opisthopare und metapare Gesichtsnähte ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]).

Die [[Facettenaugen der Trilobiten|Facettenaugen]] bestehen — wie das Exoskelett — aus Calcit und sind daher als Fossilien außergewöhnlich gut erhalten ([[10-Raw/Trilobiten (Quelle).md#Augen|Q1]]). Sie treten in drei Formen auf: holochroal (bis zu 15.000 Einzelaugen), schizochroal (bis zu 700, durch dicke Sclera getrennt) und abathochroal (mit dünner Sclera) ([[10-Raw/Trilobiten (Quelle).md#Augen|Q1]]).

Der Thorax besteht aus Segmenten, deren Anzahl systematisch relevant ist: Agnostida besitzen nur zwei bis drei, größere Arten bis zu 18; die Segmente können Stacheln (Fraßschutz) oder Krümmungen (für grabende Tätigkeit) tragen ([[10-Raw/Trilobiten (Quelle).md#Thorax|Q1]]). Da nur die Oberseite verkalkt war, sind Funde mit Weichteilerhaltung der Beine selten und auf wenige Fossillagerstätten beschränkt: Die Trilobiten besaßen zweiästige [[Körperbau der Trilobiten|Spaltbeine]] mit einem Schwimm-/Kiemenbein (Exopodit) und einem Laufbein (Endopodit) ([[10-Raw/Trilobiten (Quelle).md#Spaltbeine|Q1]]).

## Entwicklung

Die [[Entwicklung der Trilobiten|Entwicklung]] erfolgte über eine Vielzahl von Stadien (Anamorphose), wobei bei jeder Häutung Segmente in einer Wachstumszone vor dem Hinterende eingeschoben wurden ([[10-Raw/Trilobiten (Quelle).md#Entwicklung|Q1]]). Die Larvenstadien durchliefen Protaspis (erste, vier gliedmaßentragende Kopf-Somiten), Meraspis (Kopf und Rumpf unterscheidbar) und schließlich das Holaspis-Stadium ohne weitere Segmentbildung; Tiere im Holaspis-Stadium häuteten sich weiter und wuchsen erheblich ([[10-Raw/Trilobiten (Quelle).md#Entwicklung|Q1]]).

## Lebensweise

Die [[Lebensweise der Trilobiten|Lebensweise]] war überwiegend benthisch (Meeresboden), mit Belegen aus litoralen Habitaten und Schelfgebieten; Tiefseeformen existierten nicht ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]). Einige ordovizische Formen mit stromlinienförmigen Körpern waren vermutlich aktive Schwimmer (pelagisch) ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]). Die meisten Trilobiten ernährten sich als Räuber und/oder Aasfresser (ursprüngliche Lebensweise); abgeleitete Formen zeigen Anpassungen als Detritus-/Sedimentfresser, Filtrierer oder Weidegänger auf Mikrobenmatten ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]). Trilobiten wurden selbst zur Beute — aus dem mittleren Kambrium stammt der Fund eines basalen Cheliceraten mit Darminhalt aus zahlreichen Trilobiten ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]).

## Trilobiten als Zeugen der Evolution

Die [[Ursprung der Trilobiten|ältesten Trilobiten]] erscheinen im Kambrium mit Beginn der 2. Serie — erst rund 13 Millionen Jahre nach den einschneidenden Ereignissen, die den Beginn des Kambriums (die „kambrische Explosion“) markieren ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Sie sind zugleich die ältesten unzweideutigen Körperfunde von Arthropoden überhaupt ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Ihr gleichzeitiges, vikariierendes Auftreten in den Flachmeeren des auseinanderbrechenden Superkontinents Rodinia mit erkennbar verwandten, aber deutlich verschiedenen Formen belegt eine ältere, nur erschlossene Existenzperiode (Ghost Range) von etwa 10 Millionen Jahren ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

Die [[Verwandtschaft der Trilobiten|Verwandtschaft]] der Trilobiten mit den rezenten Arthropodenordnungen der Spinnentiere und Krebstiere ist eine offene Frage: Ob sie mit den Spinnentieren die Gruppe Arachnata bilden (traditionelle Auffassung) oder nähere Verwandte der Krebstiere sind, hängt von der Interpretation der Homologie der Kopfsegmente und des Antennensegments ab ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Der dreilappige Körperbau, das Spaltbein sowie Kopf- und Schwanzschild sind gemeinsames Erbe der Arthropoden (Plesiomorphien) — Merkmale, die zuerst an Trilobiten beschrieben wurden, ihnen aber nicht eigentümlich sind ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

Die [[Trilobiten als Reliktgruppe|spätere Evolution]] brachte zwar Neuerungen, aber eine im Kern fast unveränderte Morphologie: Bereits vor dem endgültigen Aussterben waren die Trilobiten fast 100 Millionen Jahre lang eine artenarme Reliktgruppe, die mehrere „Beinahe-Aussterben“ überlebt hatte, sich danach aber nie wieder zu kambrischer Vielfalt entwickeln konnte ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Eine [[Schwarmintelligenz bei Trilobiten|480 Mio. Jahre alte Reihenformation]] der Art *Ampyx priscus* aus dem unteren Ordovizium wird als erstes Zeugnis von Schwarmintelligenz bei Lebewesen gedeutet ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

## Trilobiten als Leitfossilien

Trilobiten zählen zu den wichtigsten Leitfossilien der Erdgeschichte: Ihre Überreste werden zur relativen Altersbestimmung von Sedimentgesteinen genutzt (Biostratigraphie), da bestimmte Arten nur in engen zeitlichen Abschnitten vorkommen und für die Ablagerungen ihrer Zeit kennzeichnend sind ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Leitfossilien|Q1]]). Trilobiten sind nur in Gesteinen des Paläozoikums überliefert; zu den ältesten gut erhaltenen gehören Arten der Gattung *Ellipsocephalus* ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Leitfossilien|Q1]]).

## Ordnungen

Gegenwärtig sind neun [[Ordnungen der Trilobiten|Ordnungen]] anerkannt: Agnostida (Unteres Kambrium bis Oberes Ordovizium), Redlichiida (Unteres bis Mittleres Kambrium), Corynexochida (Unteres Kambrium bis Mittleres Devon), Lichida (Kambrium bis Devon), Phacopida (Unteres Ordovizium bis Oberes Devon), Proetida (Ordovizium bis Perm), Asaphida (Mittleres/Oberes Kambrium bis Oberes Ordovizium/Unteres Silur), Harpetida (Oberes Kambrium bis spätes Devon) und Ptychopariida (Unteres Kambrium bis Oberes Ordovizium) ([[10-Raw/Trilobiten (Quelle).md#Ordnungen|Q1]]).

## Fundregionen

In Deutschland sind Trilobitenfunde seit dem Kambrium überliefert, meist als Geschiebe; ergiebig sind etwa das Rheinische Schiefergebirge, der Harz, die Eifel (Trilobitenfelder bei Gees) und der Frankenwald, im europäischen Ausland vor allem das Barrandium, Schweden, Großbritannien und die Karnischen Alpen ([[10-Raw/Trilobiten (Quelle).md#Fundregionen in Deutschland und Europa|Q1]]).

## Verwendung als Wappentiere

Gehäuse von Trilobiten kommen in der Heraldik selten als Wappentiere vor; ihre Verwendung deutet auf lokale Fundstätten hin, so in den tschechischen Gemeinden Skryje nad Berounkou und Jince, im spanischen Murero, im portugiesischen Canelas und im kanadischen Percé ([[10-Raw/Trilobiten (Quelle).md#Verwendung als Wappentiere|Q1]]).

--- END NOTE ---

--- FILENAME: 20-Literature/Truppen- und Gefangenentransporte auf dem Inn.md
--- BEGIN NOTE ---

# Truppen- und Gefangenentransporte auf dem Inn

Der Artikel von **Florian Messner** untersucht die Rolle des **Inn** als militärischen Transportweg der Frühen Neuzeit: Truppen, Waffen und Gefangene wurden auf dem Fluss befördert, weil er schnellen, günstigen und vergleichsweise schadensarmen Transport erlaubte ([[10-Raw/Inn Truppentransport.pdf#page=1|Q1]]). Der Beitrag gliedert sich in Schiffbarkeit, Schiffstypen, Belagerung von Kufstein 1504, Türkenkriege und Gefangenentransporte (Galeerenstrafe).

### Der Inn: Gebirgsfluss an der Grenze der Schiffbarkeit

Vor den Regulierungen der letzten zwei Jahrhunderte hing die Schiffbarkeit von Wasserführung und Gefälle ab. Mit einem Gefälle von 1 Promille und 3 m/s Fließgeschwindigkeit (doppelt so viel wie der Rhein) lag der Inn an der Grenze der Schiffbarkeit; nur die Zeiträume März–Mai und August–November eigneten sich ([[10-Raw/Inn Truppentransport.pdf#page=2|Q1]]). Im durchschnittlichen Jahr 1856 gab es nur 150 Tage mit transportfähigem Wasserstand ([[10-Raw/Inn Truppentransport.pdf#page=2|Q1]]). In Hall sperrte die Saline den Fluss mit einem hölzernen **Rechen**, um Treibholz und Baumstämme aufzufangen — er wurde nur für den Landesfürsten und hochstehende Reisende gehoben ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]).

### Plätten, Zillen und der Schiffszug

Die Innschiffe (Zillen und Plätten) hatten einen flachen Boden und waren 5–6 bis 20 Meter lang ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). Sie wurden in Schopperwerkstätten zwischen Wörgl und Kufstein sowie in Neubeuern und Rosenheim serienweise gebaut ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). Stromaufwärts zog ein **Schiffszug** aus zwei bis vier zusammengebundenen Frachtschiffen mit bis zu 30 Zugpferden und 40 Bediensteten bis zu 5.000 Zentner ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). Die **Naufahrt** (flussabwärts) war einfach, die **Hohenaufahrt** (flussaufwärts) teuer — deshalb befuhren Soldaten den Inn fast ausschließlich flussabwärts ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). Für Truppentransporte nutzte man die großen Salzschiffe von 20–30 m Länge und 6–7 m Breite ([[10-Raw/Inn Truppentransport.pdf#page=11|Q1]]).

### Hall: logistischer Knotenpunkt der Militärschifffahrt

Zuständig für die Organisation der Militärfahrten war das **Pfannhausamt in Hall** ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). Weil sich Soldaten nicht anmeldeten, kam es zu Staus in Hall; der **Salzmair**, der die Boote zusammenziehen musste, forderte, anziehende Soldaten rechtzeitig zu melden, und klagte über Wartegelder für leere Boote ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). In Hall gab es keine Bootsbauer, daher lieh man zivile Schiffe bis nach Bayern und holte fehlende Innschiffer aus Bayern und Salzburg ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). 1601 brauchte man 700 Innschiffer für 6.000 Soldaten ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]); 1595 zog sich das Verschiffen von knapp 13.000 Soldaten und 2.677 Pferden fast zwei Monate hin ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). 1603 organisierte das Salzamt für ein Regiment von 3.000 Mann Kampfstärke 101 Schiffe mit einer Ladekapazität von 13.783 Menschen — der Tross machte über 10.000 Mann aus ([[10-Raw/Inn Truppentransport.pdf#page=5|Q1]]). 1532 standen an der Lend 45 Schiffe für 20.000 Mann bereit ([[10-Raw/Inn Truppentransport.pdf#page=10|Q1]]).

### Frühgeschichte: von den Römern bis zu den Landsknechten

Flüsse waren in der Kriegsführung zugleich natürliches Hindernis und Transportweg ([[10-Raw/Inn Truppentransport.pdf#page=4|Q1]]). Erstmals nutzten wohl die Römer den Inn militärisch — Anlagen in Veldidena (Wilten) und das Kastell Batavis bei Passau ([[10-Raw/Inn Truppentransport.pdf#page=4|Q1]]). Im Früh- und Hochmittelalter wurden nur Waren transportiert, kaum Soldaten; die Konflikte waren kleinräumig ([[10-Raw/Inn Truppentransport.pdf#page=4|Q1]]). Ab dem Spätmittelalter verdrängten professionelle Söldner (Reisläufer der Eidgenossen, Siege bei Morgarten 1315 und Sempach 1386) den Ritter — als Gegenmaßnahme begründete Maximilian I. die **Landsknechte** ([[10-Raw/Inn Truppentransport.pdf#page=4|Q1]]).

### Truppendurchzüge, Plünderungen und ihre Regulierung

Ohne geregelte Versorgung plünderten die Heere die Umgebung; spezielle Plünderkommandos und im schlimmsten Fall Gewalt waren die Folge ([[10-Raw/Inn Truppentransport.pdf#page=5|Q1]]). Willibald Pirckheimer berichtete 1499 aus dem Engadinerkrieg von einem Weinraub im Lager bei Pfunds mit 50 Toten und über 100 Verwundeten ([[10-Raw/Inn Truppentransport.pdf#page=5|Q1]]). Das **Passauer Kriegsvolk** unter Laurentius von Ramée (1609, über 10.000 Mann) brandschatzte ganze Gebiete, während Kompensationszahlungen ausblieben ([[10-Raw/Inn Truppentransport.pdf#page=6|Q1]]). Die Antwort der Landesherrschaft waren Kommissare (ab den 1520er Jahren) und die erste Ordnung des Tiroler Landtags von **1557** ("ordnung der musterplätz, durchzüg und profiantheüser") mit Provianthäusern und persönlicher Haftung des Feldobersten ([[10-Raw/Inn Truppentransport.pdf#page=6|Q1]]). Die gröbsten Ausschweifungen sowie Verletzte und Todesfälle wurden dadurch reduziert ([[10-Raw/Inn Truppentransport.pdf#page=6|Q1]]).

### Die Belagerung von Kufstein 1504

Im Landshuter Erbfolgekrieg beanspruchte Ruprecht von der Pfalz nach dem Tod Herzog Georgs des Reichen das bayerische Erbe; Maximilian I. unterstützte seinen Schwager Albrecht IV. ([[10-Raw/Inn Truppentransport.pdf#page=7|Q1]]). Im April 1504 ließ er 1.200 Zentner Waffen über Donau und Inn nach Innsbruck bringen ([[10-Raw/Inn Truppentransport.pdf#page=7|Q1]]). Nachdem Kufstein am 9. August 1504 an die Pfälzer gefallen war, belagerte Maximilian die Stadt mit rund 9.000 Mann und belieferte seinen Artilleriepark am Innufer von Innsbruck aus über den Inn ([[10-Raw/Inn Truppentransport.pdf#page=7|Q1]]). Steinkugeln waren wirkungslos; erst die größten Geschütze — die "Purlepaus" und der "Weckauf von Österreich" mit schmiedeeisernen 70-kg-Kugeln — durchbrachen Mauern und Kellergewölbe ([[10-Raw/Inn Truppentransport.pdf#page=8|Q1]]). Nach der Eroberung wurden 42 Gefangene zum Tode verurteilt und 19 hingerichtet, die übrigen erwirkte Herzog Erich von Braunschweig zu begnadigen ([[10-Raw/Inn Truppentransport.pdf#page=9|Q1]]). Der Inn schützte die Stadt wie ein riesiger Wassergraben, ermöglichte aber zugleich die relativ schnelle Eroberung ([[10-Raw/Inn Truppentransport.pdf#page=10|Q1]]).

### Der Inn in den Türkenkriegen

Im Kampf gegen die Osmanen (seit 1453 Bedrohung Europas) wurde der Inn Teil der Nachschublinie Inn–Donau ([[10-Raw/Inn Truppentransport.pdf#page=10|Q1]]). 1532 marschierten 80.000 Mann, ein Viertel davon über den Brenner; 45 Schiffe an der Haller Lend transportierten 20.000 Soldaten ([[10-Raw/Inn Truppentransport.pdf#page=10|Q1]]). 1541–43 wurden 11.500, 1566 weitere 5.000 Soldaten befördert ([[10-Raw/Inn Truppentransport.pdf#page=11|Q1]]). Der Höhepunkt lag 1594–1603: 4.000 Soldaten 1594, bis 1603 weitere 40.000, meist italienische und spanische Söldner der Heiligen Liga ([[10-Raw/Inn Truppentransport.pdf#page=11|Q1]]). 1596 transportierte man 12.827 Mann mit 2.677 Pferden — darunter Truppen des Kirchenstaats, aus Rom, Mantua, Mailand und Florenz — nach Wien ([[10-Raw/Inn Truppentransport.pdf#page=11|Q1]]). Im Dreißigjährigen Krieg blieb Tirol weitgehend verschont, 1619 zogen dennoch 14.000 Spanier durch ([[10-Raw/Inn Truppentransport.pdf#page=12|Q1]]). 1683 schickte Hall noch einmal 4.000 Soldaten nach Wien; danach flaute der Truppentransport endgültig ab — im gesamten 18. Jahrhundert sind nur vier weitere Beförderungen belegt ([[10-Raw/Inn Truppentransport.pdf#page=12|Q1]]). Gründe waren die Teilung des Hauses Habsburg in eine spanische und eine österreichische Linie, der Verlust der italienischen Gebiete und die Ostpolitik Maria Theresias, die Tirol an den Rand rückte ([[10-Raw/Inn Truppentransport.pdf#page=12|Q1]]).

### Galeerenstrafe und Gefangene auf dem Inn

Die führenden Seemächte Pisa, Genua und Venedig benötigten nach Lepanto 1571 ständig neue Ruderer; die Habsburger führten deshalb Mitte des 16. Jahrhunderts die Galeerenstrafe ein — ein beidseitig vorteilhafter Handel ([[10-Raw/Inn Truppentransport.pdf#page=13|Q1]]). Die Strafe wurde auch auf Nicht-Straftäter ausgedehnt (Bayerische Landesordnung 1695: "herumvagierende Freyleut", Roma und Sinti) ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]). Bis ins 18. Jahrhundert wurden mehrere tausend Häftlinge deportiert, von denen nur ein Bruchteil überlebte ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]). Der Landweg war gefährlich (Fluchtversuche, bis zu 200 Personen pro Zug, tote Aufseher); der Inn war gleich schnell, erforderte aber deutlich weniger Wachpersonal ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]). Das Münchner Blutbannbuch von 1568 belegt 24 Straftäter, die über den Inn nach Hall und weiter die Etsch hinauf gebracht wurden ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]).

### Die letzte Reise des Kanzlers: Wilhelm Biener

**Wilhelm Biener** (um 1590–1651), studierter Jurist, 1630 in den Reichshofrat berufen, beriet Leopold V. und Claudia de Medici und bekämpfte als Hofkanzler der österreichischen Vorlande die Korruption ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]). Nach 1648 kritisierte er den Lebensstil des jungen Erzherzogs Ferdinand Karl; ein Schauprozess verurteilte ihn zum Tode ([[10-Raw/Inn Truppentransport.pdf#page=15|Q1]]). Seine letzte Reise führte ihn als Gefangenen auf dem Inn von Hall nach Rattenberg, wo er am 17. Juli 1651 enthauptet wurde; ein unterzeichnetes kaiserliches Gnadengesuch hatte der Kammerpräsident Schmaus abgefangen ([[10-Raw/Inn Truppentransport.pdf#page=15|Q1]]).

### Resümee

Der Inn ermöglichte die Durchquerung des Unterinntals in zwei Tagen, ersparte Zeit und vor allem Plünderungen ([[10-Raw/Inn Truppentransport.pdf#page=15|Q1]]). Er war für Tirol zugleich Wassergraben und Einfallstor — seine militärische Bedeutung endete erst mit dem Bedeutungsverlust der Region im 18. Jahrhundert.

--- END NOTE ---

--- FILENAME: 20-Literature/Warum 99% aller Tiere symmetrisch sind.md
--- BEGIN NOTE ---

# Warum 99% aller Tiere symmetrisch sind

Das Video von LivingZoo beantwortet die Frage, warum über 99 % aller Tierarten einen symmetrischen Körperbau haben. Die zentrale These: Symmetrie ist **keine biologische Voreinstellung** (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=105s" title="00:01:45">(V)</a>), sondern eine Konsequenz daraus, wie ein Lebewesen der Welt mit ihren Achsen und Richtungen begegnet — symmetrische Körperpläne "fallen" aus wenigen Handlungszwängen heraus (Gravitation, gerichtete Bewegung) und sind zugleich genetisch günstig zu kodieren.

## Die drei Grundbaupläne

Tierkörper lassen sich in **drei Grundbaupläne** einteilen: radial symmetrisch, bilateral symmetrisch und asymmetrisch (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=14s" title="00:00:14">(V)</a>). Das Gegenstück zur Symmetrie ist der **Schwamm** als "poster child" der Asymmetrie: Er hat keinen Kopf, kein Vorne/Hinten, kein Links/Rechts, sondern ist ein formloser Zellklumpen, der Seewasser einsaugt und Nahrung herausfiltert; schneidet man ihn in beliebiger Richtung, gleichen sich die Hälften nicht (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=14s" title="00:00:14">(V)</a>). Diese Formlosigkeit hat für Schwämme über Hunderte Millionen Jahre hervorragend funktioniert — rund eine Milliarde Jahre (Grammatik der Größenordnung der Evolutionsdauer, engl. "for the greater part of a billion years") (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=42s" title="00:00:42">(V)</a>). Ein formloser Körper ist also ein legitimer Weg, ein Tier zu sein.

## Symmetrie muss erst aufgebaut werden

Symmetrie im Sinne von Symmetrieachsen ist nichts, worauf Leben "von selbst" ausweicht; ein Embryo muss sie aktiv konstruieren, während er selbst kaum mehr als ein Zellklumpen ist (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=105s" title="00:01:45">(V)</a>).

- **Kopf-Schwanz-Achse (anterior–posterior)**: beginnt bereits bei der Gastrulation und zu Beginn der Neurulation zu musterzubilden und läuft über die **Hox-Gene**, die Körperteile den einzelnen Körpersegmenten zuordnen (vorn, Mitte, Schwanzende) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=133s" title="00:02:13">(V)</a>).
- **Links-Rechts-Achse**: ist knifflig, weil der Embryo seine eigene "blobby Symmetrie" bewusst brechen muss — er legt fest, welche Seite links wird, und hält dabei das Ganze als makellosen Spiegel (Konzept) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>).

### Molekulare Festlegung von links/rechts

Beim (beispielhaft genannten) Hühnerembryo entscheidet eine kleine Gruppe von Signal- (Signalmolekülen) — SHH, Nodal und Activin (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>). Der entscheidende Schritt: **Nodal** schaltet nur auf einer Seite, der linken, ein anderes Gen namens **Pitx2** an (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>). Pitx2 leuchtet in einem Gewebeblatt namens *linkes laterales Plattenmesoderm* auf und überträgt den abstrakten linken Befehl in die konkrete Körperanlage (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>). Es differenziert die linke Seite nicht-arbiträr — es gibt also eine echte "linke Seite", nicht Zufall (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>).

### Die Cilien als Richtungsgeber

Wie weiß der Embryo, welche Seite links ist? Bei vielen Wirbeltieren (vermutlich auch Menschen) gibt es einen Fleck winziger, nach hinten zum Embryo-Rückens geneigter **Cilien (Nodal-Cilien)**, die sich drehen und Flüssigkeit in einer gleichbleibenden Richtung über den Embryo treiben (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=202s" title="00:03:22">(V)</a>). Die Strömungsrichtung (die der wirkliche "Tiebreaker" ist) legt fest, welche Seite links wird. Belegt wird das durch Mäuse, denen die Nodal-Cilien fehlen: Die Links-Rechts-Festlegung wird dann quasi randomisiert (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=202s" title="00:03:22">(V)</a>).

## Situs inversus — der Spiegel als "richtige falsche" Stelle

Beim Menschen gibt es die Erkrankung **Situs inversus**, bei der Organe als vollständiges Spiegelbild der üblichen Anordnung entstehen — das Herz liegt rechts, der gesamte Magen-Darm-Trakt ist gespiegelt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=234s" title="00:03:54">(V)</a>). Typischerweise geht das auf nicht funktionierende Cilien zurück (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=234s" title="00:03:54">(V)</a>). Wichtig: Auch dann verfällt der Körper nicht in Asymmetrie, sondern erzeugt eine **Spiegelkopie** — jedes Organ ist an der falschen, aber "exakt richtigen falschen" Stelle (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=258s" title="00:04:18">(V)</a>). Das zeigt, dass die Spiegel-Grammatik (mirror-Bauplan) bis ins Detail programmiert ist.

## Echinodermen — sekundäre Radialsymmetrie

Sterne wie Seesterne brechen die Regel scheinbar nicht: Sie sind radialsymmetrisch um die Fünf (odd Anzahl Spiegellinien möglich) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=269s" title="00:04:29">(V)</a>). Die Antwort überrascht: **Echinodermenlarven** (Seestern-, Seeigel-, Seegurken-Larven) sind tatsächlich **bilateral symmetrisch** mit normalem Links/Rechts — erst beim Heranwachsen bauen sie sich zu fünfarmigen, radialen Adulttieren um (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=296s" title="00:04:56">(V)</a>). Kladistisch sind sie also bilateral; die Radialsymmetrie (Körperteile um eine zentrale Achse statt einer zentralen Ebene) ist **sekundär entstanden** — ihre Vorfahren waren spiegelsymmetrisch, die Fünfachigkeit ist eine spätere, "entsetzliche" Weiterentwicklung (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=315s" title="00:05:15">(V)</a>).

## Warum Symmetrie: die Achsen-Logik

Symmetrie als Konsequenz: Evolution muss das Problem lösen, auf einem Planeten mit eigenen Achsen und Richtungen einen Körper zu bauen; die Welt hält nur wenige Richtungen bereit, nach denen sich ein Körper formen lässt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=332s" title="00:05:32">(V)</a>).

1. **Gravitation (erste Achse, oben/unten)**: Oben ist überall und verschieden von unten — also ist es sinnvoll, ein von unten verschiedenes Oben zu bauen (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=361s" title="00:06:01">(V)</a>).
2. **Bewegung (zweite Achse, vorn/hinten)**: Sobald sich ein Tier zielgerichtet fortbewegt, ist das vorausgehende Ende (das zuerst auf Nahrung, Bedrohung und alles andere trifft) nicht mehr mit dem nachschleifenden Ende austauschbar; daher lagert Evolution Nerven und Sinnesorgane vorn zu einem **Kopf** zusammen — **Cephalisation**; das ergibt ein echtes Vorn/Hinten (anterior/posterior) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=375s" title="00:06:15">(V)</a>).
3. **Links/Rechts (übrig gebliebene Achse)**: Es gibt keine Kraft, die zuverlässig die linke gegenüber der rechten Seite bevorteilt; die Umwelt bietet Links und Rechts dieselbe Welt, daher gibt es keinen Grund, sie verschieden zu bauen — sie fallen standardmäßig gleich aus. **Bilaterale Symmetrie ist die "übrig gebliebene Achse"**, die ohne Druck auf einen Spiegel — Mirror — zurückfällt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=406s" title="00:06:46">(V)</a>).

Aus derselben Logik fallen die anderen Baupläne heraus:

- **Radiale Symmetrie**: Wenn ein Tier der Welt aus jeder Richtung zugleich begegnet, aber keine Absicht hat sich zu bewegen und nur im Wasser treibt, erhält man radial symmetrische Tiere wie Quallen — oben/unten, aber ohne echtes Links/Rechts/Vorn/Hinten (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=434s" title="00:07:14">(V)</a>).
- **Ctenophoren (Rippenquallen)** sind gar nicht klar radial, sondern eher rotations- oder biradialsymmetrisch; auch die **Cnidarier** (Quallen, Seeanemonen) durchlaufen das ganze Spektrum von radial über biradial bis beinahe bilateral (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=461s" title="00:07:41">(V)</a>).
- **Schwämme**: begegnen der Welt aus jeder Richtung, ohne sich überhaupt fortzubewegen (weder gerichtet noch ungerichtet), und haben sich evolutionär sehr früh von den übrigen abgespalten — so entsteht der asymmetrische Bauplan (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=482s" title="00:08:02">(V)</a>).

## Biomechanik und Kosten der bilateralen Symmetrie

Zwei weitere Argumente:

- **Bilateral gegen radial für gerichtete Fortbewegung** (Lehrbuchantwort): Ein Körper mit Vorn/Hinten und zwei spiegelgleichen Seiten ist viel einfacher geradeaus zu steuern (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=515s" title="00:08:35">(V)</a>).
- **Biomechanik**: Bilaterale Symmetrie ist die einzige Tier-Symmetrie, die in einer Richtung stromlinienförmig, in den anderen unstromlinienförmig ist — das erlaubt maximale Kraft in wechselnder Richtung, also die Fähigkeit, auf der Stelle zu wenden (Maneuverability), entscheidend beim Jagen und Entkommen (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=515s" title="00:08:35">(V)</a>).
- **Sparsames genetisches Encoding**: Man schreibt die genetischen Instruktionen für eine Seite, die andere läuft von demselben Satz ab — man erhält eine komplizierte Körperhälfte, ohne die Information doppelt zu bezahlen; zudem wirkt jede Verbesserung im gemeinsamen Instruktionssatz auf beide Seiten zugleich, sodass eine einzige günstige Mutation genügt (statt auf zwei Stellen zu warten) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=545s" title="00:09:05">(V)</a>).

## Ursprung im Fossilbericht

Die große Verwandtschaftsgruppe der "vorn-habenden, seiten-gleichen" Tiere heißen **Bilateria**; sie spalten sich in **Protostomia** und **Deuterostomia** (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=581s" title="00:09:41">(V)</a>). Einer der ältesten bekannten Bilaterier ist das ediacarische Lebewesen ***Ikaria wutjita*** — klein und einfach, aber mit echtem Vorn/Hinten und gespiegeltem Links/Rechts (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=581s" title="00:09:41">(V)</a>). Es bewegt sich, drückt durch den Schlamm und verlagert Sediment — schon vor über **555 Millionen Jahren** (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=609s" title="00:10:09">(V)</a>).

Die "Bewegungs-Hypothese" als Ursache bilateraler Symmetrie ist nur die **vorherrschende Hypothese** (front-running); eine andere Forschergruppe glaubt, bilaterale Symmetrie könnte zuerst in einem sitzenden, am Meeresboden lebenden Tier als einfachere Art entstanden sein, Flüssigkeiten innerhalb des eigenen Körpers zu bewegen, statt den Körper durch die Welt zu schieben (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=637s" title="00:10:37">(V)</a>). Symmetrie ist also "die Standard-Annahme, nachdem man berücksichtigt, was sinnvoll ist" (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=637s" title="00:10:37">(V)</a>).

## Asymmetrie als bewusste, teure Abweichung

Das wirklich eigenartige und interessante bei Evolutionslogik ist die **bewusste Einseitigkeit**: Wenn Symmetrie "gratis" und ästhetisch ist, dann kostet das Brechen der Spiegel-Symmetrie ("mirror") etwas — man muss den billigen Standard aktiv überschreiben (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=664s" title="00:11:04">(V)</a>). Die Asymmetrie ist meist eine **neuere Erfindung**, die symmetrischen Vorfahren aufgepfropft wurde (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=664s" title="00:11:04">(V)</a>). Beispiele:

- **Plattfisch (Flatfish)**: schlüpft als normale spiegelsymmetrische Larve, macht dann eine extra Runde post-embryonaler Umgestaltung während der Metamorphose durch — ein Auge wandert langsam über den Schädel auf die andere Kopfseite, sodass der erwachsene Fisch sich auf den Grund legen kann, mit beiden Augen zur Wasseroberfläche (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=677s" title="00:11:17">(V)</a>).
- **Männliche Winkerkrabben (fiddler crabs)**: tragen eine überdimensionierte Haupt-Schere zum Kämpfen — eine massig groß, die andere klein (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=708s" title="00:11:48">(V)</a>).
- **Narwal (Einhorn des Meeres)**: der berühmte Stoßzahn ist eigentlich ein Zahn; konkret der linke, der gerade durch die Lippe herausbohrt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=708s" title="00:11:48">(V)</a>). Meist haben Männchen einen Stoßzahn, manche zwei, andere gar keinen (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=738s" title="00:12:18">(V)</a>).
- **Der Mensch**: außen ein relativ sauberer Spiegel, aber innen asymmetrisch — das Herz liegt links, die Leber rechts, der Darm ist in eine spezifische Richtung aufgewickelt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=760s" title="00:12:40">(V)</a>). Das bestimmt allerdings nicht, ob man bilateral oder radial symmetrisch ist (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=766s" title="00:12:46">(V)</a>).

## Fazit und Ausblick

Leben ist symmetrisch, weil das Sinn ergibt. Da die beschriebenen Zwänge und Achsen auch auf anderen Planeten gleich blieben, ist es plausibel, dass außerirdisches Leben bilateral symmetrisch wäre — wenn auch vermutlich nicht im Look von Clark Kent (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=794s" title="00:13:14">(V)</a>).

## Aus dieser Quelle hervorgegangene Notizen

- [[Radiale Symmetrie]]
- [[Bilaterale Symmetrie]]
- [[Körperachsen der Tiere]]
- [[Symmetrie als Konsequenz der Bewegung]]
- [[Cephalisation]]
- [[Hox-Gene]]
- [[Links-Rechts-Festlegung]]
- [[Nodal-Cilien]]
- [[Situs inversus]]
- [[Bilateria]]
- [[Ikaria wutjita]]
- [[Sekundäre Radialsymmetrie der Echinodermen]]
- [[Asymmetrie als abgeleitetes Merkmal]]

--- END NOTE ---

# 30-Narrative — Argumentationsstraenge (27 Notizen)

--- FILENAME: 30-Narrative/Asymmetrie als bewusste Abweichung vom billigen Standard.md
--- BEGIN NOTE ---

# Asymmetrie als bewusste Abweichung vom billigen Standard

War Symmetrie die günstige Standardantwort (siehe [[Symmetrie als Konsequenz weniger Achsen]]), so ist das Umgekehrte umso bemerkenswerter: Absichtlich **lopsided** (einseitig) zu sein kostet etwas, weil man das billige Standard-Encoding aktiv überschreiben muss (die Quelle spricht scherzhaft vom "7 Jahre Unglück"-Gleichnis des Spiegels) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=664s" title="00:11:04">(V)</a>). Wenn man asymmetrische Tiere entlang ihres Stammbaums zurückverfolgt, erweist sich die Asymmetrie fast immer als **neuere Erfindung**, die symmetrischen Vorfahren aufgepfropft wurde (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=664s" title="00:11:04">(V)</a>).

## Sekundäre Radialsymmetrie der Echinodermen

Seesterne scheinen die Bilateral-Regel klar zu brechen (fünfarmig, ungerade Spiegellinien möglich) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=269s" title="00:04:29">(V)</a>). Doch ihre **Larven sind bilateral symmetrisch** mit normalem Links/Rechts; erst beim Heranwachsen bauen sie sich zur fünfarmigen, radialen Adultform um (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=296s" title="00:04:56">(V)</a>). Kladistisch sind sie also Bilateria; die Radialsymmetrie (Merkmale um eine zentrale Achse statt um eine zentrale Ebene) ist **sekundär** entstanden — eine spätere, evolutionär "entsetzliche" Weiterentwicklung ([[Sekundäre Radialsymmetrie der Echinodermen]]) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=315s" title="00:05:15">(V)</a>).

## Einseitige Merkmale als Beispiele

- **Plattfisch (Flatfish)**: Schlüpft als normale Spiegel-Larve, durchläuft während der Metamorphose eine zusätzliche Runde post-embryonaler Umgestaltung, bei der ein Auge langsam über den Schädel auf die andere Kopfseite wandert; so kann der adulte Fisch auf dem Grund liegen, beide Augen zur Wasseroberfläche gerichtet (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=677s" title="00:11:17">(V)</a>).
- **Männliche Winkerkrabbe**: trägt eine überdimensionierte Haupt-Schere zum Kämpfen — eine massiv groß, die andere klein (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=708s" title="00:11:48">(V)</a>).
- **Narwal (Einhorn des Meeres)**: der berühmte Stoßzahn ist in Wahrheit nur ein Zahn — der linke, der gerade durch die Lippe herausbohrt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=708s" title="00:11:48">(V)</a>). Die meisten Männchen haben einen Stoßzahn, einige zwei, andere gar keinen (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=738s" title="00:12:18">(V)</a>).

## Innere Asymmetrie des Menschen

Auch der Mensch ist "krumm": außen ein relativ sauberer Spiegel, aber innen asymmetrisch — das Herz liegt links, die Leber rechts, der Darm ist in eine bestimmte Richtung aufgewickelt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=760s" title="00:12:40">(V)</a>). Diese Innen-Asymmetrie bestimmt allerdings nicht, ob man bilateral oder radial symmetrisch ist (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=766s" title="00:12:46">(V)</a>). Sie bildet zugleich die Grundlage für den klinischen Fall [[Situs inversus]], bei dem diese innere Links/Rechts-Anordnung als ganzer spiegelt.

## Konsequenz

Asymmetrie lässt sich als gezielte, aktive Überschreibung eines ansonsten freispiegeligen Standard-Bauplans lesen. Sie tritt dort auf, wo ein einseitiger Vorteil (Lage zum Grund, Kampf, Sinnesausrichtung) den Preis der teuren Abweichung wert ist — ein Muster, das sich über [[Asymmetrie als abgeleitetes Merkmal]] und [[Sekundäre Radialsymmetrie der Echinodermen]] zusammenfassen lässt.

--- END NOTE ---

--- FILENAME: 30-Narrative/Aufstieg des Hauses Habsburg durch Heiratspolitik.md
--- BEGIN NOTE ---

# Aufstieg des Hauses Habsburg durch Heiratspolitik

Kernfrage dieses Argumentationsstrangs: Wie wurde aus einem an Geldmangel leidenden Herrschergeschlecht ein Haus, dessen Reich "die Sonne nicht mehr unterging" — ohne dass es diese Länder erobert hätte?

1. **These:** Der Aufstieg der Habsburger zur Universalmonarchie unter Maximilian I. beruhte primär auf [[Habsburgische Heiratspolitik|dynastischen Heiraten]] und Erbverträgen, nicht auf Eroberungen ([[10-Raw/Maximilian I. (HRR).md#Die Habsburgischen Erblande, Burgund und das Reich|Q1]]).
2. **Ausgangspunkt:** Durch die Heirat mit Maria von Burgund 1477 erwarb Maximilian das [[Burgundisches Erbe Maximilians|burgundische Erbe]] *iure uxoris* — das wirtschaftlich reichste und kulturell ritterlich geprägte Territorium Europas ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]).
3. **Kosten der Erbschaft:** Frankreich erkannte die Erbfolge nicht an und besetzte das Herzogtum Burgund — die Erbschaft begründete den jahrhundertelangen [[Habsburgisch-französischer Gegensatz|habsburgisch-französischen Gegensatz]], der die habsburgische Politik über Generationen prägte ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]).
4. **Spanien:** Die Verheiratung von Sohn Philipp mit Johanna von Kastilien (1496) verband das Haus Habsburg mit den Kronen Aragoniens und Kastiliens; aus dieser Verbindung ging später Karl V. hervor ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).
5. **Böhmen und Ungarn:** Der [[Pressburger Vertrag 1491|Pressburger Vertrag]] legte die Erbfolge für den Fall des Aussterbens der Jagiellonen fest; die Erweiterung um wechselseitige Heiraten (1506) schuf die Grundlage für die [[Wiener Doppelhochzeit 1515|Wiener Doppelhochzeit]] 1515 ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).
6. **Konsequenz:** Nach dem Tod Ludwigs II. 1526 fielen die Kronen Böhmens und Ungarns an Habsburg — die Doppelhochzeit "zahlte sich" für die Enkel Maximilians aus ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).
7. **Schlussfolgerung:** Maximilian konnte das Reich seinem Enkel Karl V. als Universalmonarchie übergeben, über der "die Sonne nicht mehr unterging" — das Ergebnis einer planvoll betriebenen Heirats- und Vertragspolitik ([[10-Raw/Maximilian I. (HRR).md#Die Habsburgischen Erblande, Burgund und das Reich|Q1]]).

--- END NOTE ---

--- FILENAME: 30-Narrative/Bildung in einer vernetzten und mediatisierten Lebenswelt.md
--- BEGIN NOTE ---

# Bildung in einer vernetzten und mediatisierten Lebenswelt

> Der Text beschreibt Bildung in digitalen Lebenswelten als fluiden Prozess, der durch Mediatisierung und Vernetzung geprägt ist. Lernende nutzen mobile Geräte nicht nur zur Wissensabfrage, sondern gestalten aktiv digitale Räume mit. Bildung wird hier als „Seamless Learning“ konzipiert – ein übergreifender Prozess, der institutionelle Grenzen auflöst und Selbstverantwortung fordert.

# Bildung in einer vernetzten und mediatisierten Lebenswelt
Die Quelle beginnt damit, dass Bildung nicht nur als schulischer Output oder als Wissensakkumulation beschrieben werden kann, sondern als Transformation von Selbst- und Weltverhältnissen. Der Kernpunkt ist, dass Menschen in einer digitalisierten Gesellschaft ihre Orientierung nicht nur durch institutionelle Bildungsprozesse gewinnen, sondern auch durch ihre alltäglichen Medienpraktiken, ihre sozialen Beziehungen und ihre Teilhabe an digitalen Kommunikationsformen [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=6|Q1]]. Damit wird Bildung zu einem Prozess, der durch Medien mitgestaltet wird und zugleich über Medien verläuft. In der Familien- und Peer-Umwelt entstehen bereits früh Sozialisationserfahrungen mit mobilen Endgeräten, digitalen Plattformen und vernetzten Kommunikationsformen. Diese Erfahrungen werden nicht als bloße Freizeitpraktiken verstanden, sondern als Bildungspraktiken, die das Selbstverständnis des Lernenden mitformen [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=7|Q2]].

Die Folge ist eine Verschiebung des Bildungsbegriffs: Bildung rückt von einem rein institutionellen Modell zu einer Lebensweltperspektive. Die Quelle zeigt, dass der Mensch heute in einer Welt lebt, die durch Mediatisierung, Digitalisierung und Vernetzung zugleich gegliedert und verändert wird. Daraus folgt, dass Bildung heute nicht mehr an feste Orte, Zeiten und Räume gebunden ist. Sie geschieht im Wechsel von Schule, Mediennutzung, Freizeit, Arbeit und Selbstlernen, und diese Bereiche überschneiden sich ständig. Genau hier setzt das Konzept von [[Seamless Learning]] an: Lernen wird als durchgängiger und kontextübergreifender Prozess gedacht, der die lebensweltliche Alltagspraxis mit einschließt [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=8|Q3]]. Vor dem Hintergrund von [[Bildung im Wandel]] und [[Bildung zwischen Tradition und digitalem Wandel]] wird deutlich, dass diese Flexibilisierung nicht einfach technologisch ist, sondern die gesamte Bildungslogik von [[Paideia]] bis zur modernen Subjektbildung verändert.

Diese Argumentation macht deutlich, warum [[Mediatisierung und Digitalisierung]] für Bildungsfragen zentral sind. Medien sind nicht nur Mittel, sondern Teil der sozialen Struktur, in der Lernen stattfindet. Dadurch entsteht eine Bildungsaufgabe, die zugleich technisch, didaktisch und gesellschaftlich zu denken ist: Wie können digitale Medien so eingesetzt werden, dass sie Orientierung, Teilhabe und Selbstbestimmung fördern, statt bloße Verfügbarkeit von Informationen zu sichern? Die Quelle beantwortet diese Frage nicht mit einem technischen Optimismus, sondern mit dem bildungstheoretischen Anspruch, dass digitale Lebenswelten die reflexive und normative Seite von Bildung neu sichtbar machen [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=8|Q4]]. Gerade in der Verbindung von [[Mediatisierung als Metaprozess]], [[Vernetzung, Mobilität und Mit-Gestaltung]] und [[Seamless Learning]] wird sichtbar, dass Bildung in der digitalisierten Lebenswelt als vernetzter, situierter und selbstorganisierter Prozess zu denken ist.

--- END NOTE ---

--- FILENAME: 30-Narrative/Bildung zwischen Tradition und digitalem Wandel.md
--- BEGIN NOTE ---

> Dieser Text analysiert den Bildungsbegriff als dynamisches Konzept, das sich historisch zwischen Selbstbestimmung, gesellschaftlichem Wandel und kulturellem Gedächtnis bewegt. Von der antiken [[Paideia]] über die Aufklärung ([[Rousseau und die Erziehung zum Menschsein]], [[Kant und die Autonomie der Bildung]], [[Humboldt und die allgemeine Menschenbildung]]) bis zur digitalen Gegenwart zeigt sich Bildung als Spannung zwischen Tradition und Innovation. Zentral ist die Idee der [[Bildung als Subjektkonstitution]]: Sie umfasst nicht nur Wissenserwerb, sondern auch Reflexion, Selbstgestaltung und Verantwortung in einer vernetzten Welt. Die digitale Transformation erfordert eine Neubestimmung von Bildung – jenseits reiner Kompetenzorientierung – als lebenslanger Prozess der Orientierung und Urteilsfähigkeit.

# Bildung zwischen Tradition und digitalem Wandel

Die Quelle stellt den Bildungsbegriff als historische Antwort auf gesellschaftliche Unsicherheit und Wandel dar. Bildung entsteht nicht aus einer festen Definition, sondern aus dem Spannungsverhältnis zwischen Mensch, Welt, Kultur und sozialen Verhältnissen. Genau deshalb ist Bildung als [[Bildung als Deutungsmuster]] zu verstehen, das sich über Zeiträume hinweg verändert und dabei zugleich immer auf die Frage nach dem Menschen und seiner Lebenswelt bezogen bleibt [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 1|Q1]].

In der Antike ist diese Perspektive noch besonders deutlich: Der Begriff [[Paideia]] verweist auf die Vervollkommnung der Seele und auf die Fähigkeit, sich aus der Erscheinungswelt zur Wahrheit und zum eigentlichen Sein zu erheben. Bildung wird hier als Transformation des Blicks verstanden, die ein neues, reflexiveres Verhältnis zu sich selbst, zu anderen und zur Welt eröffnet [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 10|Q1]]. Diese Vorstellung bleibt auch in der neuzeitlichen Pädagogik wirksam, obwohl sie in andere Begriffsrahmen übersetzt wird. Die zentrale These des Textes ist, dass Bildung in jeder historischen Konstellation als Prozess der Selbstverhältnisse und der Weltdeutung fungiert [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 4|Q1]].

Mit der Moderne wird die Frage nach der [[Bildung als Subjektkonstitution]] entscheidend. Der Mensch ist nicht einfach ein Objekt sozialer oder institutioneller Einflüsse, sondern ein Subjekt, das in seinem Selbstverständnis und in seiner Weltbeziehung immer neu bestimmt wird. Die Quelle verweist auf Borst, der Bildung als Frage nach der historisch-gesellschaftlichen Existenzweise des Subjekts beschreibt. Daraus folgt, dass Bildungsprozesse nicht nur Wissen aufnehmen, sondern auch die eigene Stellung in der Welt, die eigene Reflexivität und die Fähigkeit zur Selbstgestaltung transformieren [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 4|Q1]].

Die historische Folge führt über [[Mittelalter und Renaissance]] hinaus. Der Bildungsbegriff wandelt sich dort von einem theokratisch orientierten Verständnis, in dem Bildung als Annäherung an eine göttliche Ordnung konzipiert wird, hin zu einer stärker weltlichen und subjektbezogenen Idee, in der Selbstformung, Individualität und kulturelle Selbstermächtigung zur Leitfigur werden [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 16|Q1]]. Diese Linie wird in der Aufklärung weiter ausgebaut: [[Rousseau und die Erziehung zum Menschsein]] betont die Befreiung zum Menschsein, [[Kant und die Autonomie der Bildung]] die Selbstbestimmung und moralische Autonomie, und [[Humboldt und die allgemeine Menschenbildung]] die allgemeine Menschenbildung in der Wechselwirkung mit der Welt [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 20|Q1]].

Die Quelle zeigt zudem, dass Bildung mehrere Dimensionen umfasst. Sie kann als individueller Bestand, als Vermögen, als Prozess, als [[Bildung als Selbstüberschreitung]] und als institutionelle Praxis begriffen werden. Diese Differenzierungen machen deutlich, dass Bildung von ihren sozialen Kontexten und ihren Zeitbezügen nicht zu trennen ist. Gerade die historische Analyse zeigt, dass im Bildungsbegriff verschiedene Spannungen liegen: zwischen Inhalt und Fähigkeit, zwischen Selbsttätigkeit und institutioneller Vermittlung, zwischen Tradition und Innovation, zwischen Erkenntnis und Selbstgestaltung [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 5|Q1]].

Im digitalen Kontext spielt diese Spannung noch einmal eine andere Rolle. Die Autor:innen warnen davor, Bildung auf Kompetenzen oder Lernen zu reduzieren, weil dadurch die normative und reflexive Dimension des Bildungsbegriffs verloren geht. Bildung darf nicht bloß als Funktion des lebenslangen Lernens verstanden werden; sie umfasst auch die Fähigkeit, sich in einer veränderten Welt zu orientieren, zu urteilen und Verantwortung zu übernehmen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 2|Q1]]. Genau deshalb bleibt der Bildungsbegriff zentral, auch wenn seine Aufgaben sich durch digitale Medien und neue Lebensformen verschieben [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 8|Q1]]. Die Verbindung zu [[Raum, Zeit und Entgrenzung in der digitalen Bildung]] und zu [[Seamless Learning]] zeigt dabei, dass die digitale Lebenswelt nicht nur neue Medienformen, sondern auch eine veränderte Zeit- und Raumstruktur von Bildung produziert.

Diese narrative Deutung macht zugleich eine doppelte Bewegung sichtbar: Bildung ist historisch gewachsen und zugleich immer wieder neu zu denken. Sie verlangt eine Reflexion über Herkunft und Zukunft, über Gedächtnis und Selbstbildung, über gesellschaftliche Ordnung und subjektive Selbstverwirklichung. In diesem Sinn ist der Bildungsbegriff der Quelle nicht nur ein pädagogischer Begriff, sondern ein Schlüssel für das Verständnis einer veränderten Gegenwartsgesellschaft [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 8|Q1]]. Die Verbindung zwischen [[Bildung im Wandel]], [[Bildung in einer vernetzten und mediatisierten Lebenswelt]] und dieser Synthese macht den Kern der Quelle deutlich: Bildung ist zugleich historische Tradition und Gegenwartsproblem.

--- END NOTE ---

--- FILENAME: 30-Narrative/Das Schmirntal als geologisches Labor des Tauernfensters.md
--- BEGIN NOTE ---

# Das Schmirntal als geologisches Labor des Tauernfensters

Kernfrage dieses Argumentationsstrangs: Warum bewegt sich das Schmirntal — und warum verrät gerade dieses Tal die Tiefenstruktur der Ostalpen?

1. **These:** Das Schmirntal liegt am Westrand des [[Tauernfenster|Tauernfensters]] und macht dessen Exhumationsgeschichte unmittelbar sichtbar — als bewegter Berg, als weiches Gestein und in der Chemie seiner Quellen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).
2. **Geologische Ausgangslage:** Die Exhumation des Tauernfensters wurde durch N-S-Kompression plus O-W-Extension vorangetrieben; die [[Brenner-Normalverwerfung|Brenner-Linie]] ließ den Westrand absinken und gab das tief versenkte Grundgebirge frei ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).
3. **Das weiche Fundament:** Die freigelegte [[Metamorphe Schieferhülle (Tauernfenster)|metamorphe Schieferhülle]] (Glockner-Decke) besteht aus bei 35–40 km Tiefe umgewandelten Kalkglimmerschiefern, Phylliten und Tonschiefern — durch den hohen Glimmeranteil mechanisch schwach und verwitterungsanfällig ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).
4. **Die Falle am Reissenschuh:** Wo kompetenter, wasserdurchlässiger Marmor über wasserundurchlässigem Phyllit liegt (lithologische Inversion), staut sich Wasser; der Porenwasserdruck hebt die Gesteinsmassen an und setzt die Reibung außer Kraft — der Hang rutscht als DSGSD mit 0,6–0,8 m/Jahr, bis über 3 m/Jahr ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).
5. **Messbarkeit:** Die langsame Katastrophe wird mit TLS, DGNSS, Luftbildauswertung seit 1954 (EMOD-SLAP) und KI-Nowcasting überwacht — sieben Jahrzehnte Bewegungsgeschichte sind damit rekonstruierbar ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).
6. **Der geochemische Beweis:** Quellen mit Arsen und Uran belegen den Kontakt mit dem Zentralgneis-Basement — das Wasser „sieht" die Fensterstruktur, die an der Oberfläche unter Schiefer verborgen liegt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).
7. **Schlussfolgerung:** Das Schmirntal ist kein passives Landschaftsrelikt, sondern ein aktives geologisches Labor: Dieselben Kräfte, die das Tauernfenster exhumierten, erzeugen heute die Hangbewegung, und die Quellenchemie macht die Tiefenstruktur direkt nachweisbar ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

--- END NOTE ---

--- FILENAME: 30-Narrative/Das Tauernfenster als tektonisches Exhumationsfenster.md
--- BEGIN NOTE ---

# Das Tauernfenster als tektonisches Exhumationsfenster

Kernfrage dieses Argumentationsstrangs: Warum ist ausgerechnet das Tauernfenster das größte tektonische Fenster der Alpen, und welche Mechanismen brachten das Europäische Grundgebirge an die Oberfläche?

1. **These:** Das [[Tauernfenster]] ist das größte tektonische Fenster der Alpen (~5600 km², Brenner bis Katschberg ~160 km) und der einzige Ort in den Ostalpen, an dem das Europäische Grundgebirge über eine Fläche von mehr als 100 km Breite aufgeschlossen ist ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).
2. **Ausgangslage:** Die Europäische Plattengrenze wurde durch Variszische Orogenese und die frühe Auflösung Pangäas geprägt (Horst-Graben-Strukturen); die gesamten Ostalpen wurden später durch die Hebung des Tauernfensters re-deformiert ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).
3. **Interne Struktur:** Die heutige Architektur resultiert aus vier Prozessen: früher Ablösung und Faltung post-variszischer Deckschichten, Stapelung der Grundgebirgsdecken (Ahorn-, Tux-, Zillertal-, Eisbrugg-Gneise), großräumiger Faltung des Deckenstapels in Kuppeln sowie einer Dreieckszone mit Rückfaltung am Nordrand ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).
4. **Tiefe Versenkung:** Die Hochdruckindikatoren zeigen eine Versenkung des Kontakts Grundgebirge–Bedeckung auf mindestens 35–40 km; ozeanische Gesteine erreichten in der Glockner-Decke 12–17 kbar, eine Eklogit-Scholle sogar 20–25 kbar (600 ± 50 °C) — die [[Alpine Deckentektonik|Deckenarchitektur]] des Tauernfensters bildete sich unter diesen Hochdruckbedingungen (~32 Ma) ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]). Der Exkursionsführer gibt die Überlagerung mit über 30 km Gesteinsdecken an, unter der sich der Bereich auf über 500 °C aufheizte ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q2]]).
5. **Exhumationsmechanismen:** Die Freilegung erfolgte durch eine Kombination aus [[Slab Breakoff und Exhumation|Slab Breakoff]] (rasche ~2-km-Hebung), Zentralindentation ([[Laterale Extrusion der Ostalpen|laterale Extrusion]]), sowie O-W-gerichteter Extension entlang der [[Brenner-Normalverwerfung|Brenner- und Katschberg-Normalverwerfung]] (neogene E-W-Extension neben N-S-Kompression) ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).
6. **Zeitliche Einordnung:** Die Großstrukturen entstanden gemeinsam mit der Hochdruckmetamorphose (~32 Ma); duktile Deformation an der heutigen Oberfläche endete ~15 Ma ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]). Die Abkühluhren des Tauernfensters bestätigen den Ablauf: 450 °C vor 17 Ma, 300 °C vor 14 Ma, 150 °C vor 6 Ma — und die Hebungstendenz setzt sich bis heute mit durchschnittlich 1,2 mm/a fort (60 Jahre Präzisionsmessung) ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q2]]).
7. **Schlussfolgerung:** Das Tauernfenster ist das Produkt von Krustenverdickung durch Deckenstapelung und anschließender Exhumation durch Slab Breakoff, Indentation und O-W-Extension — es dokumentiert damit den kompletten Exhumationszyklus eines tief versenkten Grundgebirges ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).

## Einfach erklärt

Stellen Sie sich einen Berg aus mehreren übereinander geschobenen Teppichen vor. Normalerweise sieht man nur den obersten Teppich (die *Austroalpinen Decken*). An manchen Stellen ist der oberste Teppich aber durch einen Querbruch so zerrissen, dass man auf den darunterliegenden, ursprünglich "Europäischen" Teppich blickt — dieses freigelegte Blickfeld heißt *tektonisches Fenster*. Das Tauernfenster ist das größte davon (ca. 5600 km², also etwa so groß wie der Bodensee × 10).

Damit der unterste Teppich oben sichtbar wird, muss erst etwas passieren: Die Gesteine wurden von oben bis 35–40 km in die Tiefe gedrückt (das entspricht dem Druck in ~1000 km Wassertiefe) und dann wieder hochgeholt. Diese Hebung lief nicht kontinuierlich, sondern in mehreren Schüben: ein Schnappeffekt durch das Abreißen der Platte, danach das seitliche Verquetschen und schließlich das "Aufreißen" zweier großer Abschiebungen (Brenner im Westen, Katschberg im Osten), die den Mittelteil wie einen Kuchen auf dem Teller bestimmt gleichmäßig herausheben. Der zeitliche Ablauf (~32 Ma bis ~15 Ma) liest sich wie eine Uhr: Alle großen Strukturen entstanden "gleichzeitig mit" der tiefen Metamorphose — Sie können sich das vorstellen wie die gleichzeitige Aktivierung mehrerer Deformationsmechanismen eines Spannungstensors (Kompression in N-S, Extension in E-W).

--- END NOTE ---

--- FILENAME: 30-Narrative/Der Inn als militärischer Transportweg.md
--- BEGIN NOTE ---

# Der Inn als militärischer Transportweg

Kernfrage dieses Argumentationsstrangs: Warum wurde der Inn in der Frühen Neuzeit zum wichtigsten Militärtransportweg Tirols — und warum flaute diese Rolle wieder ab?

1. **These:** Der Inn erlaubte schnellen, günstigen und schadensarmen Truppentransport und bewahrte Tirol vor den Plünderungen durchziehender Heere ([[10-Raw/Inn Truppentransport.pdf#page=1|Q1]], [[10-Raw/Inn Truppentransport.pdf#page=15|Q1]]).
2. **Ausgangslage:** Landwege waren langsam (kaum mehr als 20 km pro Tag) und zwangen die Heere zur Selbstversorgung durch Plünderung → Flüsse als Alternative ([[10-Raw/Inn Truppentransport.pdf#page=5|Q1]]).
3. **Technik:** Flacher Boden der [[Plätten und Schiffszug|Plätten]] und die Beschränkung auf die Naufahrt machten Massentransporte flussabwärts wirtschaftlich ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]).
4. **Logistik:** [[Hall in Tirol als Zentrum der Militärschifffahrt]] bündelte die Transporte, erzeugte aber durch fehlende Bootsbauer und unregelmäßige Anmeldungen Engpässe ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]).
5. **Beweis der Effizienz:** Die [[Belagerung von Kufstein 1504]] zeigte, wie Artillerie über den Inn binnen Stunden vor die belagerte Stadt gebracht wurde ([[10-Raw/Inn Truppentransport.pdf#page=8|Q1]]).
6. **Höhepunkt:** In den Türkenkriegen wurden 1594–1603 bis zu 40.000 Soldaten auf der Linie Inn–Donau verschifft ([[10-Raw/Inn Truppentransport.pdf#page=11|Q1]]).
7. **Schlussfolgerung:** Der Inn spielte eine zwiespältige Rolle — Wassergraben und Angriffsweg zugleich —, verlor aber im 18. Jahrhundert an Bedeutung, als sich das Habsburgerreich teilte und Tirol in die Peripherie geriet ([[10-Raw/Inn Truppentransport.pdf#page=10|Q1]], [[10-Raw/Inn Truppentransport.pdf#page=12|Q1]]).

--- END NOTE ---

--- FILENAME: 30-Narrative/Der Kölner Schiedsspruch als territoriale Neuordnung.md
--- BEGIN NOTE ---

# Der Kölner Schiedsspruch als territoriale Neuordnung

Kernfrage dieses Argumentationsstrangs: Wie verteilte der Kölner Schiedsspruch das Erbe Georgs des Reichen — und warum gewannen gerade die Habsburger?

1. **These:** Der Kölner Schiedsspruch vom 30. Juli 1505 beendete den Krieg als **Schiedsentscheidung Maximilians I.** auf dem Reichstag zu Köln ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]).
2. **Kompromiss an die Erben:** Die beiden Enkel Georgs, Ottheinrich und Philipp, erhielten die [[Junge Pfalz]] mit Neuburg an der Donau als Hauptstadt — ein zersplittertes Gebiet von der oberen Donau über Franken bis zur nördlichen Oberpfalz ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]).
3. **Preis der Vermittlung:** Maximilian hatte sich das Gebiet um Kufstein, Kitzbühel und Rattenberg selbst vorbehalten; auch das Zillertal und das Mondseeland gingen von Bayern an die Habsburger ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]).
4. **Weitere Gewinner:** Die Reichsstadt Nürnberg gewann die Ämter Lauf, Hersbruck und Altdorf; der Rest von Bayern-Landshut fiel an die Münchener Linie ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]).
5. **Verlierer:** Die Kurpfalz verlor ihre elsässischen Besitzungen größtenteils an die Habsburger und weitere Gebiete an Hessen und Württemberg ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]).
6. **Schlussfolgerung:** Beide wittelsbachischen Linien verloren, die Habsburger stiegen zum eigentlichen Nutznießer auf — die [[Maximilians Gebietsgewinne im Landshuter Erbfolgekrieg|Gebietsgewinne Maximilians]] banden Kufstein und das Unterinntal dauerhaft an die [[Innschifffahrt als militärischer Transportweg|Innschifffahrt Tirols]] ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]).

--- END NOTE ---

--- FILENAME: 30-Narrative/Der Niedergang der Trilobiten.md
--- BEGIN NOTE ---

# Der Niedergang der Trilobiten

Kernfrage dieses Argumentationsstrangs: Warum endete die rund 270 Millionen Jahre währende Erfolgsgeschichte der [[Trilobiten]] — und warum ist die eigentliche Frage nicht ihr Aussterben, sondern ihre Langlebigkeit? <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=24s" title="00:00:24">(V)</a>

1. **These:** Die Natur musste vier Mal versuchen, die Trilobiten auszulöschen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=60s" title="00:01:00">(V)</a>. Ihre Geschichte ist die erste Erfolgsgeschichte des gesamten Tierreichs <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=361s" title="00:06:01">(V)</a>.
2. **Grundlage des Erfolgs:** Anatomische Überlegenheit (Exoskelett, Augen, Beine) → Dominanz der kambrischen Meere → Diversifizierung in mindestens 60 Familien <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=127s" title="00:02:07">(V)</a>. → [[Trilobiten]]
3. **Erste Bedrohung:** Auftreten der Prädation im Kambrium → Verteidigungsanpassungen wie die [[Enrollierung]] gegen neue Räuber <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=157s" title="00:02:37">(V)</a>.
4. **Verschärfung der Bedrohung:** Klimawandel ([[Ordovizium-Silur-Extinktion]]) <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=205s" title="00:03:25">(V)</a> und Kieferfische mit dem daraus folgenden [[Evolutionäres Wettrüsten|evolutionären Wettrüsten]] <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=251s" title="00:04:11">(V)</a> dezimierten die Bestände massiv.
5. **Ende:** Die [[Spätdevon-Extinktion]] reduzierte die Trilobiten auf vier Familien <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=305s" title="00:05:05">(V)</a>, das [[Perm-Trias-Massenaussterben]] löschte sie vollständig aus <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=339s" title="00:05:39">(V)</a>.
6. **Schlussfolgerung:** Entscheidend ist nicht, warum sie starben, sondern wie sie so lange überleben konnten — denn wir sind heute eines der erfolgreichsten Tiere, und ihre Probleme könnten irgendwann unsere eigenen sein <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=393s" title="00:06:33">(V)</a>.

--- END NOTE ---

--- FILENAME: 30-Narrative/Der Pfitscher Bergsturz und der verschwundene Stausee.md
--- BEGIN NOTE ---

# Der Pfitscher Bergsturz und der verschwundene Stausee

Kernfrage dieses Argumentationsstrangs: Was passiert, wenn ein ganzer Bergrücken in ein Tal stürzt — und was bleibt davon nach über tausend Jahren noch sichtbar?

1. **Auslöser:** Nach dem Abschmelzen der eiszeitlichen Gletscher verloren die übertieften, vegetationslosen Talhänge ihre Stütze durch das Eis und brachen zusammen — eine Geschichte, die sich in den Alpen tausendfach abspielte ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]).
2. **Der Bergsturz:** Nacheiszeitlich ging von der Flanke der Überseilspitze (2493 m) im Pfitschtal ein Bergsturz ab, der das Tal **150 m hoch vollständig abriegelte** und den Pfitschbach zu einem **8 km langen See** aufstaute. Die Sturzmassen bestehen aus fest verbackenen Kalkglimmerschiefer-Trümmermassen ohne jede Schichtung: hausgroße Blöcke und fein zerriebenes Material liegen unsortiert und chaotisch durcheinander — wie für Bergstürze charakteristisch ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]).
3. **Der Dammbruch um 1100 n. Chr.:** Um das Jahr 1100 rutschte ein Stück des durchnässten Stauwalles ins Rutschen. Die sofort nachstürzenden Wasserfluten setzten mit ihrer starken erosiven Kraft den Auslauf immer tiefer, bis der ganze See mit etwa **70 Millionen Kubikmetern Wasser über Nacht leergelaufen war** ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]).
4. **Die Flutkatastrophe:** Die Flut richtete flußabwärts im Pfitsch- und Eisacktal große Verwüstung an und forderte viele Menschenleben — eines der dokumentierten Bergsturz-Dammbruch-Ereignisse der Alpen mit historischen Folgen ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]).
5. **Das Landschaftsarchiv:** Die weite, stellenweise versumpfte Ebene von Kematen ist durch Seesedimente gebildet. Schwemmkegel und alte Terrassen (auf denen z. B. die Häuser von Rein stehen) erlauben, den alten Seespiegel exakt zu rekonstruieren; der Ortsname **Überwasser** erinnert noch daran, und in Kematen steht ein über tausend Jahre altes Haus aus der Zeit, in der die Bewohner vom Seeufer lebten ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]).
6. **Parallele:** Das Moos von Sterzing verdankt seine Entstehung einem weiteren prähistorischen Bergsturz bei Trens, der den Eisack aufstaute und dessen See schnell von Sedimenten gefüllt wurde — die gleiche Kaskade in anderer Größenordnung ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]).
7. **Schlussfolgerung:** Bergsturz-Stauseen sind flüchtige Landschaftselemente: Ihr Aufbau dauert Jahrtausende, ihre katastrophale Entleerung eine Nacht. Die Pfitschtaler Landschaft ist ohne diese Katastrophe nicht verständlich — Seesedimente, Terrassen und Ortsnamen konservieren das Ereignis bis heute ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]).

## Einordnung

Der Pfitscher Bergsturz gehört in die Klasse der gravitativen Großereignisse, zu denen im Vault auch die [[Reissenschuh-Rutschung]] gehört — dort allerdings als langsame, monitoring-überwachte Bewegung ([[Gravitative Kaskadenprozesse am Reissenschuh]]) statt als plötzlicher Kollaps. Die Nacheiszeit als Auslösezeitfenster verbindet ihn mit dem Bergsturz-gesättigten Gebirgsrelief der [[Metamorphe Schieferhülle (Tauernfenster)|weichen Schieferhülle]] des Tauernfensters.

--- END NOTE ---

--- FILENAME: 30-Narrative/Der Reissenschuh als Referenzmodell tiefgreifender Hangdeformationen.md
--- BEGIN NOTE ---

# Der Reissenschuh als Referenzmodell tiefgreifender Hangdeformationen

Kernfrage dieses Argumentationsstrangs: Warum ist der Reissenschuh mehr als eine lokale Rutschung — und was macht ihn zum Referenzmodell für alpine Risikomanagement?

1. **These:** Die Reissenschuh-Rutschung ist das herausragende Beispiel einer tiefgreifenden gravitativen Hangdeformation (DSGSD) in den Ostalpen — und zugleich das wissenschaftlich am besten dokumentierte ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]]).

2. **Tektonische Kopplung:** Die Hangdynamik ist untrennbar mit der Exhumierung des [[Tauernfenster|Tauernfensters]] verbunden: Aufsteigen des Krustenabschnitts plus Erosion erzeugten die extremen Reliefgradienten, welche die gravitativen Prozesse in den weichen Einheiten der [[Metamorphe Schieferhülle (Tauernfenster)|Metamorphen Schieferhülle]] antreiben — dieselben Kräfte, die das Fenster bildeten, erzeugen heute die Rutschung ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]]).

3. **Der Auslösemechanismus:** Die lithologische Inversion (wasserdurchlässiger Marmor über wasserstauendem Phyllit) wirkt als hydrogeologische Falle: Porenwasserdruck-Anstieg an der Grenzfläche reduziert die effektive Reibung und setzt die Bewegung in Gang ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]]).

4. **Multi-Sensor-Überwachung:** TLS (flächendeckende 3D-Verschiebungsvektoren) und DGNSS (kontinuierliche Punktmessung) erfassen die Bewegung in räumlicher und zeitlicher Präzision ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]]).

5. **Zeitliche Tiefe:** [[EMOD-SLAP]] verlängert die Zeitreihe per Luftbild-Photogrammetrie bis 1954 — weit über die Messkampagnen 2016–2019 hinaus — und adressiert damit die entscheidende Frage: Sind die Bewegungsraten konstant oder fluktuierend? ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]]).

6. **Transferierbarkeit:** Die am Reissenschuh entwickelten Workflows lassen sich auf vergleichbare geologische Settings übertragen, etwa die Steinlehnen-Rutschung — der Reissenschuh ist damit methodischer Vorreiter, nicht Einzelfall ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]]).

7. **Schlussfolgerung:** Beobachtung plus computergestützte Modellierung machen den Reissenschuh zum Referenzmodell für tiefgreifende Hangdeformationen in metamorphen Gebirgszügen und zur essenziellen Grundlage für das langfristige Risikomanagement in alpinen Regionen ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]]).

--- END NOTE ---

--- FILENAME: 30-Narrative/Die acht Phasen des Wilson-Zyklus.md
--- BEGIN NOTE ---

# Die acht Phasen des Wilson-Zyklus

Kernfrage dieses Argumentationsstrangs: Wie funktioniert der wiederkehrende Zyklus von Geburt und Tod der Ozeane — und warum folgen neue Ozeane alten Suturzonen?

1. **These:** Ozeanbecken durchlaufen einen Zyklus von Öffnung und Schließung entlang derselben Kollisionsgrenzen — der [[Wilson-Zyklus]] mit acht Hauptstadien <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=398s" title="00:06:38">(V)</a>.
2. **Öffnung:** Dehnung im Kontinent erzeugt zuerst ein Sag-Becken (Beispiel: Westsibirisches Becken), dann ein kontinentales Rifting mit embryonalem Ozean (Ostafrikanischer Graben) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=417s" title="00:06:57">(V)</a>. Meeresbodenspreizung weitet es zum jungen Ozean (Rotes Meer) und schließlich zum reifen Ozean (Atlantik heute) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=450s" title="00:07:30">(V)</a>.
3. **Schließung:** Eine Subduktionszone (Ring of Fire) kippt das Becken vom Wachsen ins Schrumpfen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=474s" title="00:07:54">(V)</a>; das Becken schließt sich (Mittelmeer), bis die Kontinente kollidieren und eine Suturzone zurückbleibt, die anfangs wie der Himalaya wie ein Gebirge aussieht <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=506s" title="00:08:26">(V)</a>.
4. **Stabilität:** Der verschweißte Kontinent bleibt stabil, bis der Zyklus mit Dehnung und Rifting erneut beginnt <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=516s" title="00:08:36">(V)</a>.
5. **Warum Suturzonen?** Neue Ozeane öffnen sich bevorzugt an alten Suturen, weil heißer Mantel unter Kontinentmitte aufsteigt (Subduktion an den Rändern erzeugt Kompensation in der Mitte) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=544s" title="00:09:04">(V)</a> und weil Suturen Schwächezonen sind, die zuerst nachgeben <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=560s" title="00:09:20">(V)</a>.
6. **Heutige Beispiele:** Der Atlantik nutzt die alte [[Iapetus-Sutur]] <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=584s" title="00:09:44">(V)</a>; auch der Rio-Grande-Rift (Farallon-Sutur), das Riftsystem in Nordostchina (Trans-North-China-Orogen) und der Ostafrikanische Graben (Mosambik-Meer) folgen alten Suturen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=598s" title="00:09:58">(V)</a>.
7. **Schlussfolgerung:** Suturzonen sind trotz Gebirgsbildung **schwächer** als intakte Kruste (anders als eine Schweißnaht), weshalb dieselben Plattengrenzen hunderte Millionen Jahre bestehen bleiben <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=666s" title="00:11:06">(V)</a> — die Grundlage, um künftige Ozeane vorherzusagen und vergangenes Klima zu verstehen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=689s" title="00:11:29">(V)</a>.

--- END NOTE ---

--- FILENAME: 30-Narrative/Die Brenner-Normalverwerfung und die Exhumation der Ostalpen.md
--- BEGIN NOTE ---

# Die Brenner-Normalverwerfung und die Exhumation der Ostalpen

Kernfrage dieses Argumentationsstrangs: Wie konnte während der andauernden N-S-Kompression der Ostalpen gleichzeitig O-W-Extension stattfinden — und welche Rolle spielte dabei die Brenner-Linie?

1. **These:** Die [[Brenner-Normalverwerfung|Brenner-Linie]] ist eine große N-S-streichende Abschiebung, an der das Hangende des Ötztal-Stubai-Kristallins (Austroalpine Decke) relativ zum [[Tauernfenster]] nach Westen versetzt wurde; der horizontale Versatz seit dem Miozän beträgt mehrere zehn Kilometer ([[10-Raw/Field trip to the Tauern Window.pdf#page=15|Q1]]).
2. **Duplikation durch zwei Abschiebungstypsysteme:** Am Brennerbad sind S-C-C′-Gefüge und semiduktile sowie spröde Scherzonen mit top-west gerichteter Extensionsbewegung zu beobachten ([[10-Raw/Field trip to the Tauern Window.pdf#page=16|Q1]]).
3. **Jüngerwerdende, steiler werdende Struktur:** Die jüngste spröde Inkarnation exzidierte ~2 km der Bündnerschiefer, während ältere top-west Mylonite auf eine frühe Phase als flachliegende, duktile Scherzone verweisen (niedrige Winkel-Abschiebung im frühen Stadium) ([[10-Raw/Field trip to the Tauern Window.pdf#page=16|Q1]]).
4. **Footwall-Uplift:** Der Fußblock-Aufstieg erfolgte durch subvertikale einfache Scherung entlang zahlreicher engständiger steiler Abschiebungen: westwärts fallende Strukturen bei 10–20 km Tiefe und ~450 °C wurden von ostwärts fallenden Abschiebungen bei 2–10 km Tiefe und 300 ± 50 °C überprägt ([[10-Raw/Field trip to the Tauern Window.pdf#page=16|Q1]]).
5. **Datierung:** Top-west gerichtete duktile Scherung wurde auf ~22–18 Ma datiert; die heute noch schwache Seismizität belegt, dass die Störung weiterhin aktiv ist ([[10-Raw/Field trip to the Tauern Window.pdf#page=15|Q1]]).
6. **Gegenstück:** Eine analoge, top-ost gerichtete Extensionsstörung (Katschberg-Normalverwerfung) begrenzt den östlichen Rand des Tauernfensters — beide bilden zusammen das symmetrische O-W-Extensionssystem ([[10-Raw/Field trip to the Tauern Window.pdf#page=15|Q1]]).
7. **Schlussfolgerung:** Die Brenner-Linie ist der zentrale Mechanismus der endgültigen Exhumation des Westteils des Tauernfensters: Sie erlaubte die O-W-Extension parallel zur N-S-Kompression und damit die Freilegung der während des [[Alpine Metamorphose|Metamorphose-Höhepunkts]] tief versenkten Einheiten; ihr Rollen-Hinge-Mechanismus und der duktile-spröde Übergang verbindet Exhumation mit [[Slab Breakoff und Exhumation]] und [[Laterale Extrusion der Ostalpen|lateraler Extrusion]] ([[10-Raw/Field trip to the Tauern Window.pdf#page=16|Q1]]).

## Einfach erklärt

Eine *Normalverwerfung* ist das geologische Gegenstück zu einer Dehnung: Zwei Gesteinsblöcke werden auseinandergezogen, und der eine rutscht an einer schrägen Bruchfläche relativ zum anderen nach unten. Beim Brenner passierte das aber in einer seltsamen Geometrie — der Gebirgsblock (Ötztal-Stubai) bewegte sich nach **Westen**, während die Alpen gleichzeitig in Nord-Süd-Richtung zusammengestaucht wurden. Das ist nur scheinbar ein Widerspruch: Zur N-S-Kompression kommt eine O-W-gerichtete Dehnungskomponente hinzu, sodass der Spannungszustand eher einer "Verquetschung" gleicht — komprimiert in einer Richtung, expressiv in der anderen.

Die Störung wurde im Lauf der Zeit immer steiler und spröder, ähnlich wie ein Material, das erst langsam (duktil: Honig, warmes Plastik) und später schnell (spröde: kaltes Glas) bricht, wenn es langsam gekühlt wird. Der *Footwall-Uplift* (Hebung des unteren Blocks) funktioniert wie ein sich aufrollender Scharnier-Mechanismus: Während der obere Block seitlich wegfährt, wird im unteren Block heißes, tiefes Gestein wie auf einem Förderband nach oben und zu kühleren Bedingungen gehoben (von ~450 °C bei 15 km Tiefe zu ~300 °C bei 5 km Tiefe). Am Ende steht das tief versenkte Tauernfenster-Gestein an der Oberfläche — der bisherige Home-Run-Mechanismus der Alpen-Exhumation.

--- END NOTE ---

--- FILENAME: 30-Narrative/Die Deformationsgeschichte des Tauernfensters in vier Phasen.md
--- BEGIN NOTE ---

# Die Deformationsgeschichte des Tauernfensters in vier Phasen

Kernfrage dieses Argumentationsstrangs: Wie wurde aus einem flachen Kontinentalrand ein 30 km tief versenktes, plastisch deformiertes Gebirge, und woran liest man diese Geschichte heute ab?

1. **Ausgangslage:** Vor 50 Millionen Jahren lasteten über dem europäischen Südrand am späteren Tauernfenster mehr als 30 km Gesteinsdecken: ~6 km penninische Decken, 15–20 km ostalpines Kristallin und 7–8 km Sedimente — die Pfunderer Berge, Ötztaler und Stubaier Alpen und die Nördlichen Kalkalpen übereinander gestapelt ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).
2. **Phase 1 — Überschiebung (60–50 Ma):** Der europäische Südrand wird von den penninischen und ostalpinen Decken überschoben; die Decken Urafrikas schoben sich dabei über eine Strecke von mehr als 150 km über Ureuropa, das einst bis mindestens 50 km südlich der heutigen Tauern reichte ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]], [[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).
3. **Phase 2 — Abschürfung:** Die mesozoischen Sedimente werden während der Überschiebung von ihrem Untergrund losgeschürft und in sehr enge, nach Norden bzw. Nordwesten geneigte Falten gelegt; die jüngeren Schichten liegen jeweils weiter im Norden ([[10-Raw/Tauernfenster (Quelle).md#Seite 3|Q1]], [[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).
4. **Phase 3 — Versenkung und Aufheizung:** Die Überlast von 30 km Gestein senkt den Bereich tief ins Erdinnere ab; im Verlauf von 10–20 Millionen Jahren heizt er sich auf über 500 °C auf und reagiert plastisch — deformierbar „wie Zahnpasta" ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]], [[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).
5. **Phase 4 — Caterpillar-Kompression und O-W-Dehnung (30–20 Ma):** Die Adriatische Platte (Italien südlich der Pustertallinie und der Insubrischen Linie) bewegt sich um einige hundert Kilometer nach Westen, während Afrika nach Norden drückt. Die plastischen Gesteine werden zusammengeschoben: Die großen Tuxer und Zillertaler Antiklinalkerne wölben sich hoch, die Pfitscher Mulde wird steilgestellt und erneut gequetscht — zugleich wird die gesamte Region nach Westen verschleppt, und die Schichten werden horizontal in die Länge gezogen ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).
6. **Phase 5 — Auftrieb und Abtragung:** Die stark verdickte Kruste bedingt starken Auftrieb; die Region bleibt 30 Millionen Jahre lang Hochgebirge mit besonders schneller Abtragung, durch die 30 km Gesteine weggeschafft werden. Durch die Entspannung reißen Klüfte auf und füllen sich mit verschiedensten Mineralien — die [[Zerrklüfte]] dokumentieren die Dehnungsphase bis heute ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).
7. **Schlussfolgerung:** Das Tauernfenster ist das Ergebnis einer Kaskade: Überschiebung → Abschürfung → Versenkung/Erhitzung → seitliche Extrusion → Hebung und Abtragung. Die vier Phasen lassen sich heute direkt im Gelände lesen — an den kopfstehenden Falten, den aufrechten Großfalten der Zentralgneise und den Ost-West gestreckten Geröllen und Zerrklüften ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]], [[10-Raw/Tauernfenster (Quelle).md#Seite 3|Q1]], [[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).

## Die quantitative Methodik hinter der Geschichte

Die Aussagen über Tiefe, Temperatur und Zeit sind keine Spekulation, sondern Ergebnis einer Kette von Methoden (ausführlich in [[Geothermobarometrie]]):

- **Mächtigkeitsbilanz:** Die 30-km-Überlagerung folgt aus der Summe der Einheiten, die einst über dem Tauernfenster lagen ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).
- **Indikatorminerale:** Disthen, Lawsonit, Granat und Glaukophan zeigen hohen Druck; Staurolith, Cordierit und Sillimanit hohe Temperatur ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).
- **Mischkristall-Thermobarometrie:** Granat-Biotit- und Granat-Plagioklas-Paare verteilen Elemente je nach Bedingungen anders und liefern Druck und maximale Temperatur ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).
- **Radiometrische Uhren:** K-Ar mit Schließungstemperatur (Muskowit <450 °C, Biotit <300 °C) und Apatit-Spaltspuren (<150 °C) ergeben Fixpunkte der Abkühlgeschichte: vor 17 Ma 450 °C, vor 14 Ma 300 °C, vor 6 Ma 150 °C — und damit die Hebungsgeschwindigkeit, die sich in den heutigen 1,2 mm/a Hebung (60 Jahre Präzisionsmessung) fortsetzt ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]], [[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]).
- **Retrodeformation:** Das Rückfalten der vermessenen Strukturen verlangt mindestens 50 km Platz Richtung Süden für die innere Sedimenthülle — Minimalbeträge, weil von den ozeanischen Serien nur Bruchstücke erhalten sind; der trennende Ozean hatte etwa die Ausdehnung des heutigen Mittelmeeres ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).

## Einfach erklärt

Stellen Sie sich ein Sandwich aus mehreren Lagen vor, das von oben immer weiter beschwert wird: Erst wird es zusammengeschoben (Phase 1–2), dann so tief ins heiße Erdinnere gedrückt, dass es weich wie Teig wird (Phase 3). Später schiebt sich von Südwesten ein massiver Presskolben (die Adriatische Platte) dagegen — der Teig wird hochgequetscht und zugleich seitlich nach Westen ausgezogen (Phase 4). Sobald der Druck nachlässt, bläht sich die Kruste auf (Phase 5), und Regen, Eis und Flüsse tragen sie wieder ab — übrig bleibt, was wir heute sehen: das Tauernfenster mit seinen aufragenden Zentralgneis-Kuppeln und der steilgestellten Pfitscher Mulde.

--- END NOTE ---

--- FILENAME: 30-Narrative/Die Reichsreform von 1495.md
--- BEGIN NOTE ---

# Die Reichsreform von 1495

Kernfrage dieses Argumentationsstrangs: Wie konnte aus dem Wormser Reichstag 1495 eine Reichsreform entstehen, die den Übergang vom Mittelalter zur Frühen Neuzeit markierte — und warum blieb sie nur ein Kompromiss?

1. **These:** Die Reichsreform von 1495 veränderte das Verhältnis von kaiserlicher Zentralgewalt und Reichsständen grundlegend; sie ist ein Wendepunkt, weil sie das Gewaltmonopol auf das Reich übertrug und erstmals reichsweite Institutionen schuf ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).
2. **Ausgangslage:** Vor 1495 war das Kaisertum nach Jahrhunderten der Erosion von Reichsrechten an einem administrativen Tiefpunkt; Maximilian wollte die kaiserliche Zentralgewalt gegenüber den Reichsständen stärken ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).
3. **Gegenspieler:** Der Mainzer Erzbischof Berthold von Henneberg wurde von den Fürsten zum Wortführer der Reichsstände gewählt und rang Maximilian die Zustimmung zu den Reformen ab — der Konflikt zwischen [[Reichsreform von 1495|Zentralismus und Föderalismus]] prägte alle Verhandlungen ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).
4. **Kernstück:** Der [[Ewiger Landfrieden|Ewige Landfriede]] ersetzte das mittelalterliche Fehderecht durch ein zeitlich unbegrenztes, unbedingtes Fehdeverbot und ordnete das Gewaltmonopol rechtlich dem Reich zu ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).
5. **Institutionalisierung der Rechtsprechung:** Das [[Reichskammergericht]] wurde als ständisch dominierte oberste Gerichtsbehörde eingesetzt und wurde (seit 1527 in Speyer) zur ersten Instanz für reichsunmittelbare Stände ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).
6. **Finanzierung:** Der [[Gemeiner Pfennig|Gemeine Pfennig]] wurde als erste reichsweite Steuer erhoben; die [[Reichskreise]] (sechs, später zehn) übernahmen die Einhebung von Reichssteuern, die Durchsetzung von Reichsbeschlüssen und die Aufstellung von Reichstruppen ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).
7. **Grenze der Reform:** Das [[Reichsregiment]] als ständische Reichsregierung scheiterte am Widerstand der Reichsstände; die komplexen Strukturen des Reiches ließen sich nicht aufbrechen ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).
8. **Schlussfolgerung:** Die Reform war ein Kompromiss zwischen kaiserlicher Zentralgewalt und ständischer Mitbestimmung; dauerhaft Bestand hatten Reichskreise und Reichskammergericht, während die Stärkung des Reichstags (nach Moraw) durch Gewöhnung der politischen Eliten die Institution faktisch aufwertete ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

--- END NOTE ---

--- FILENAME: 30-Narrative/Entstehung der Ostalpen entlang des TRANSALP-Profils.md
--- BEGIN NOTE ---

# Entstehung der Ostalpen entlang des TRANSALP-Profils

Kernfrage dieses Argumentationsstrangs: Wie entstanden die Ostalpen aus der Auflösung Pangäas, und welche siebenschrittige Entwicklung führt von der Öffnung eines Ozeans zur Gebirgsbildung?

1. **These:** Die Ostalpen sind das Produkt eines vollständigen [[Wilson-Zyklus]]-Ablaufs: von langandauernder Subsidenz über die Öffnung des [[Penninisch-Ligurischer Ozean|Penninisch-Ligurischen Ozeans]] bis zu seiner Schließung durch Kollision der Afrikanischen (Adriatischen) mit der Europäischen Platte ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).
2. **Öffnung:** Im Mittleren Jura bildete sich die Alpine Tethys als kleiner Seitenarm des Nordatlantiks bei der Auflösung Pangäas; das Spreading war extrem langsam (magmaarmer, ultralangsamer Rücken), sodass subkontinentaler Mantel am Meeresboden freigelegt und zu Serpentiniten/Ophicalciten metasomatisiert wurde ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).
3. **Erste Orogenese (Eoalpin):** Bereits in der Oberkreide bewirkte die Schließung des kleinen Hallstatt-Meliata-Ozeans die [[Eoalpine Orogenese]] — nachweisbar an eklogitfazieller Metamorphose und Gosau-Flysch in den Austroalpinen Decken ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).
4. **Hauptkollision:** Im Paleogen konsumierte die nach Süden subduzierende Platte die Alpine Tethys; die Deckenstapelung folgte dem klassischen Schema — ozeanische Decken (Bündnerschiefer, Glockner Decke) überschoben den Europäischen Kontinentalrand, die Austroalpinen Decken wurden darübergeschoben ([[10-Raw/Field trip to the Tauern Window.pdf#page=3|Q1]]).
5. **Slab Breakoff:** Vor ~30–40 Ma riss die ozeanische Lithosphäre ab; der plötzliche Verlust der negativen Auftriebskräfte ließ den zentralen Teil der Ostalpen um ~2 km aufsteigen und erzeugte durch heißen Asthenosphärenstrom kollisionsbezogenen Magmatismus (Granite, Tonalite, basische Gänge) ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).
6. **Subduktionsumkehr:** Danach sank der vom Adriatischen Plattenrand gelöste Lithosphärenmantel nach Nordosten, und es entstand ein zweiter, aktiver Keil im Süden (heute seismisch aktiv, Erdbeben Friuli 1976 mit ~1000 Opfern) ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).
7. **Schlussfolgerung:** Die Ostalpen unterscheiden sich von den Westalpen genau in dieser Subduktionsumkehr, der Nordversetzung der Pusteria-Störung um ~60 km und der Entwicklung zweier orogener Keile — die [[Laterale Extrusion der Ostalpen|laterale Extrusion]] und der Einbau des [[Tauernfenster|Tauernfensters]] sind direkte Folgen dieser Abfolge ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).

## Einfach erklärt

Denken Sie an einen *Wilson-Zyklus* als eine Art "Atmen" der Erdkruste: Ein Ozean klafft auf (Ausdehnung), muss sich später wieder schließen, und dabei kollidieren die Kontinente (Gebirgsbildung). Vor ~200 Mio. Jahren zerbrach der Superkontinent Pangaea — zwischen Afrikanischer und Europäischer Platte entstand ein schmaler Meeresstreifen, die *Alpine Tethys*. Dessen Meeresboden war aber keine normale spröde Platte, sondern wie dünn auseinandergezogener Plastilin: extrem langsam gewachsene Kruste, stellenweise sogar bloß liegender, veränderter Erdmantel (Ophicalcite).

Beim Schließen um ~40 Mio. Jahren tauchte der Meeresboden unter die Adria-Platte ab — wie Papier unter einen Locherrand geschoben wird. Ein Schlüsselereignis war der *Slab Breakoff*: Die abtauchende Platte riss irgendwann ab (wie ein zu schweres Seil, das am Haken reißt). Plötzlich zog nichts mehr nach unten — der Gebirgsabschnitt "federt" um ~2 km auf. Danach kehrte sich die Bewegungsrichtung um, und durch die Verzahnung mit der nördlich vordringenden Adria-Platte wurde das Gebirge seitlich nach Osten herausgequetscht. Das ist im Kern ein Kräftespiel, das Sie mit zwei Platten und einer Feder phänomenologisch beschreiben können: Hier wird die *Richtung der größten Spannung* von vertikal zu horizontal "umgeschaltet".

--- END NOTE ---

--- FILENAME: 30-Narrative/Gefangene und Galeeren auf dem Inn.md
--- BEGIN NOTE ---

# Gefangene und Galeeren auf dem Inn

Kernfrage dieses Argumentationsstrangs: Wie hing der Gefangenentransport auf dem Inn mit dem Krieg gegen die Osmanen zusammen — und warum war der Fluss für diese Transporte besonders geeignet?

1. **These:** Auch Gefangenentransporte nutzten den Inn; sie waren weniger spektakulär, aber ebenso vom Kampf gegen die Osmanen bestimmt ([[10-Raw/Inn Truppentransport.pdf#page=13|Q1]]).
2. **Ausgangspunkt:** Nach dem Sieg von Lepanto 1571 benötigten die Mittelmeer-Seemächte zigtausende Ruderer → die [[Galeerenstrafe]] wurde zum Ersatz für die Todesstrafe ([[10-Raw/Inn Truppentransport.pdf#page=13|Q1]]).
3. **Vorteil für beide Seiten:** Die Habsburger leerten ihre Gefängnisse und sparten Unterbringungskosten, die Seemächte erhielten die benötigten Ruderer ([[10-Raw/Inn Truppentransport.pdf#page=13|Q1]]).
4. **Transportweg:** Der Landweg war gefährlich (bis zu 200 Personen starke Verbrechergruppen, Fluchtversuche, tote Aufseher), der Inn dagegen gleich schnell, aber mit viel weniger Wachpersonal ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]).
5. **Ausweitung:** Die Strafe traf auch Nicht-Straftäter — Roma, Sinti, "Freyleut und Schinder" sowie die gewaltlosen Hutterer, deren Anführer Jakob Hutter 1536 vor dem Goldenen Dachl verbrannt wurde ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]).
6. **Fallbeispiel:** [[Wilhelm Biener]] — seine letzte Reise führte ihn als Gefangener über den Inn von Hall nach Rattenberg ([[10-Raw/Inn Truppentransport.pdf#page=15|Q1]]).
7. **Schlussfolgerung:** Der Inn war auch für den unsichtbareren Teil der Kriegslogistik die kostengünstigere und sicherere Route.

--- END NOTE ---

--- FILENAME: 30-Narrative/Maximilians Selbstinszenierung als letzter Ritter.md
--- BEGIN NOTE ---

# Maximilians Selbstinszenierung als letzter Ritter

Kernfrage dieses Argumentationsstrangs: Wie konnte ein Herrscher, dessen Politik von modernen Verwaltungsreformen und Schulden bei Bankiers geprägt war, zugleich als "letzter Ritter" in die Geschichte eingehen?

1. **These:** Maximilians Image als "letzter Ritter" war das Ergebnis einer bewussten, nahezu modern anmutenden [[Maximilians Selbstinszenierung|Selbstinszenierung]] — er stilisierte sich als Wahrer ritterlicher Ideale, obwohl sein Handeln stark von modernen Herrschaftspraktiken geprägt war ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]).
2. **Widerspruch:** Der ritterlichen Fassade standen Reichsreform, Verwaltungsapparat und Kreditfinanzierung gegenüber — der "letzte Ritter" war zugleich der "erste Kanonier", ein vorausschauender Herrscher der anbrechenden Neuzeit ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]).
3. **Medium:** Maximilian nutzte als erster Herrscher den Holzschnitt für Propagandazwecke (Ehrenpforte, *Triumphzug*, Illustrationen zu *Theuerdank*, *Weißkunig*, *Freydal*) — seine autobiografischen Dichtungen sind verschlüsselte Autobiografien und zugleich Denkmäler einer vergangenen Epoche ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]).
4. **Legitimation:** Die genealogische Forschung bis zu antiken und biblischen Wurzeln sollte die Herrschaft der Habsburger im Wettstreit mit konkurrierenden Geschlechtern legitimieren — Maximilian verstand sich als legitimer Nachfolger antiker Herrscher ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]).
5. **Selbstermächtigung:** Auch die [[Erwählter Römischer Kaiser|Annahme des Kaisertitels 1508 ohne päpstliche Krönung]] folgte dieser Logik der Selbststilisierung: Der Herrscher machte seinen Titel von der Kirche unabhängig ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).
6. **Realität hinter dem Bild:** Die [[Schulden Maximilians I.|Schulden bei Jakob Fugger]] und der Spottname "Bürgermeister von Augsburg" zeigen, dass die Inszenierung des Prunks die tatsächliche Finanznot des Kaisers überdecken musste ([[10-Raw/Maximilian I. (HRR).md#Schulden|Q1]]).
7. **Schlussfolgerung:** Das romantische Schlagwort vom "letzten Ritter" trifft genau genommen nicht zu: Seine Ritterlichkeit war kein Rückzug in die Vergangenheit, sondern eine politisch motivierte Inszenierung eines modernen Herrschers ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]).

--- END NOTE ---

--- FILENAME: 30-Narrative/Symmetrie als Konsequenz weniger Achsen.md
--- BEGIN NOTE ---

# Symmetrie als Konsequenz weniger Achsen

Die Kernargumentation der Quelle lautet: Symmetrie ist kein Zufall und keine biologische Voreinstellung, sondern die **logische Konsequenz daraus, wie ein Lebewesen der Welt mit ihren Achsen und Richtungen begegnet** (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=332s" title="00:05:32">(V)</a>). Evolution muss auf einem Planeten, der eigene Achsen vorgibt, nur wenige "Richtungen" berücksichtigen — und genau daraus erwachsen die drei Bauplan-Typen.

## Die Achsen der Welt

1. **Gravitation** liefert die erste Achse: *oben* ist überall und verschieden von *unten*, daher baut man sinnvollerweise ein von unten verschiedenes Oben (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=361s" title="00:06:01">(V)</a>).
2. **Bewegung** liefert die zweite Achse: Sobald ein Tier zielgerichtet loszieht, ist das vorauslaufende Ende nicht mehr mit dem nachschleifenden austauschbar — das Vorderende trifft zuerst auf Nahrung, Bedrohung und alles andere. Deshalb drängt Evolution Nerven und Sinnesorgane vorn zu einem **Kopf** zusammen (**Cephalisation**), und es entsteht ein echtes Vorn/Hinten (anterior/posterior) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=375s" title="00:06:15">(V)</a>).
3. **Links/rechts bleibt "übrig"**: Es gibt keine Kraft, die zuverlässig die linke zugunsten de rechten Seite bevorteilt — aus Sicht der Umwelt sind Links und Rechts dieselbe Welt, also gibt es keinen Grund, sie verschieden zu bauen; sie fallen standardmäßig gleich aus. Genau das ist **bilaterale Symmetrie**: die übrig gebliebene Achse, die ohne weiteren Druck auf einen Spiegel zurückfällt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=406s" title="00:06:46">(V)</a>).

Daraus folgen auch die anderen Baupläne:

- **Radiale Symmetrie**: Wer der Welt aus jeder Richtung zugleich begegnet, aber nicht gezielt wandert (etwa treibende Quallen), bekommt eine Oben/Unten-Achse, aber kein echtes Links/Rechts/Vorn/Hinten (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=434s" title="00:07:14">(V)</a>).
- **Ctenophoren und Cnidarier**: Die Unterscheidung ist weich — Rippenquallen sind eher rotations-/biradialsymmetrisch, Quallen und Anemonen laufen von radial über biradial bis nahezu bilateral (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=461s" title="00:07:41">(V)</a>).
- **Schwämme**: begegnen der Welt aus allen Richtungen, bewegen sich weder gerichtet noch ungerichtet fort und haben sich früh von den übrigen Tieren abgespalten — so resultiert die reine Asymmetrie (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=482s" title="00:08:02">(V)</a>).

## Zwei ergänzende Argumente

Über das "Herausfallen" aus den Achsen hinaus nennt die Quelle zwei mechanistische Gründe:

- **Bilateral übertrifft radial bei gerichteter Fortbewegung**: Ein Körper mit Vorn/Hinten und zwei spiegelgleichen Seiten lässt sich in gerade Linien viel leichter steuern (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=515s" title="00:08:35">(V)</a>).
- **Biomechanik der Manövrierfähigkeit**: Bilaterale Symmetrie ist die einzige Tier-Symmetrie, die in einer Richtung stromlinienförmig und in den übrigen unstromlinienförmig ist — das erlaubt maximale Kraft in wechselnder Richtung, also das Wenden auf der Stelle (Maneuverability), was beim Jagen und Entkommen entscheidend ist (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=515s" title="00:08:35">(V)</a>).
- **Sparsames genetisches Encoding**: Die Instruktionen werden nur für eine Körperseite geschrieben, die andere läuft vom selben Satz ab; jeder genetische Vorteil greift so auf beide Seiten zugleich (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=545s" title="00:09:05">(V)</a>).

## Historische Tiefe im Fossilbericht

Die Gruppe der "vorn-habenden, seiten-gleichen" Tiere, die **Bilateria** (Protostomia/Deuterostomia), reicht tief ins Ediacarium zurück: ***Ikaria wutjita***, ein kleiner, einfach gebauter Bilaterier mit echtem Vorn/Hinten und Spiegel-Links/Rechts, bewegte sich bereits vor über 555 Millionen Jahren durch den Schlamm und verlagerte Sediment (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=609s" title="00:10:09">(V)</a>). Die Bewegungshypothese als Ursache ist allerdings nur die vorherrschende — eine rivalisierende Deutung sieht die bilaterale Symmetrie zuerst in sitzenden Bodenbewohnern entstanden, für einfachere Fluiddynamik im Körperinnern (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=637s" title="00:10:37">(V)</a>).

## Konsequenz

Symmetrie ist die "Standard-Antwort", nachdem man berücksichtigt, was sinnvoll ist. Da dieselben Achsen und Zwänge (Gravitation, Bewegung) mutmaßlich auf allen Planeten gelten, wäre außerirdisches Leben plausibel ebenfalls bilateral symmetrisch (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=794s" title="00:13:14">(V)</a>). Diese Argumentationskette verknüpft [[Körperachsen der Tiere]], [[Cephalisation]], [[Bilaterale Symmetrie]], [[Radiale Symmetrie]] und [[Symmetrie als Konsequenz der Bewegung]] zu einem einzigen Erklärungsmodell, das die drei Baupläne aus ein und derselben Achsen-Logik ableitet.

--- END NOTE ---

--- FILENAME: 30-Narrative/Trilobiten als Zeugen der Evolution.md
--- BEGIN NOTE ---

# Trilobiten als Zeugen der Evolution

Kernfrage dieses Argumentationsstrangs: Was erzählt die Erfolgs- und Verfallsgeschichte der [[Trilobiten]] über die Evolutionsmechanismen des Lebens — von der kambrischen Explosion bis zum größten Massenaussterben der Erdgeschichte?

1. **These:** Trilobiten sind ein Paradebeispiel dafür, wie Fossilien Evolution sichtbar machen — vom rätselhaften Auftauchen im Kambrium bis zu ihrem Endstadium als Reliktgruppe ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).
2. **Ursprung im Kambrium:** Die [[Ursprung der Trilobiten|ältesten Trilobiten]] erscheinen erst rund 13 Millionen Jahre nach den Ereignissen, die den Beginn des Kambriums markieren ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). → [[Trilobiten]]
3. **Der Ghost-Range-Schluss:** Ihr gleichzeitiges Auftreten in den Flachmeeren des auseinanderbrechenden Superkontinents Rodinia mit verwandten, aber deutlich verschiedenen Formen zeigt, dass ihr Ursprung älter sein muss, als der Fossilbericht belegt — eine nur erschlossene Existenzperiode von etwa 10 Millionen Jahren ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). → [[Ursprung der Trilobiten]]
4. **Arthropoden-Erbe statt Sonderweg:** Der dreilappige Körperbau, das Spaltbein sowie Kopf- und Schwanzschild sind Plesiomorphien — gemeinsames Erbe aller Arthropoden, das zuerst an Trilobiten beschrieben wurde, ihnen aber nicht eigentümlich ist ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). → [[Verwandtschaft der Trilobiten]]
5. **Offene Verwandtschaftsfrage:** Ob die Trilobiten mit den Spinnentieren die Gruppe Arachnata bilden oder nähere Verwandte der Krebstiere sind, hängt von der Interpretation der Kopfsegment-Homologie ab — ein bis heute ungelöster Streit ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). → [[Verwandtschaft der Trilobiten]]
6. **Verhalten als evolutionärer Beleg:** Die 480 Mio. Jahre alte Reihenformation von *Ampyx priscus* wird als ältestes Zeugnis von [[Schwarmintelligenz bei Trilobiten|Schwarmintelligenz]] gedeutet — Verhaltensfossilien erweitern die evolutionsbiologische Aussagekraft des Fossilberichts ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).
7. **Die Grenze der Resilienz:** Nach mehreren „Beinahe-Aussterben“ war die Gruppe fast 100 Millionen Jahre lang eine artenarme [[Trilobiten als Reliktgruppe|Reliktgruppe]] und erholte sich nie wieder zu kambrischer Vielfalt — die verlorenen ökologischen Nischen kehrten nicht zurück ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).
8. **Schlussfolgerung:** Die Trilobiten zeigen, dass evolutionärer Erfolg nicht linear ist: rasanter Diversitätsschub, lange Stabilität, schrittweiser Niedergang und schließlich das Erlöschen mit dem [[Trilobiten als Reliktgruppe|Perm-Trias-Massenaussterben]] — eine Geschichte, die als biostratigraphisches Werkzeug bis heute nachwirkt ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Leitfossilien|Q1]]). → [[Trilobiten als biostratigraphisches Werkzeug]]

--- END NOTE ---

--- FILENAME: 30-Narrative/Ursachen des Landshuter Erbfolgekriegs.md
--- BEGIN NOTE ---

# Ursachen des Landshuter Erbfolgekriegs

Kernfrage dieses Argumentationsstrangs: Wie konnte ein Erbfall in Bayern-Landshut zu einem Krieg werden, der auch die Habsburger Gebietsgewinne am Inn ermöglichte?

1. **These:** Der Krieg war kein plötzlicher Ausbruch, sondern der **Endpunkt eines jahrzehntelangen Konflikts innerhalb des wittelsbachischen Hauses** ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]).
2. **Auslöser:** Georg der Reiche setzte per Testament vom 19. September 1496 seine Tochter Elisabeth und deren Ehemann Ruprecht von der Pfalz als Erben ein — ein **Bruch des [[Wittelsbacher Hausvertrag von Pavia|Hausvertrags von Pavia]]**, der die Erbfolge bei Aussterben einer männlichen Linie der jeweils anderen Linie zusicherte ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]).
3. **Gegenspieler:** Albrecht IV. von Bayern-München akzeptierte den Vertragsbruch nicht; seine eigene Erbfolge schien mit der Geburt seines Sohnes Wilhelm gesichert, Georgs Kurswechsel zur Kurpfalz war für ihn inakzeptabel ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]).
4. **Machtvermittler:** Maximilian I. stellte sich auf Albrechts Seite, verfolgte aber eigene dynastische Interessen und verlangte für seine Vermittlung **Gebietsansprüche** (Kufstein, Kitzbühel, Rattenberg) ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]).
5. **Eskalation:** Die Verhängung der [[Reichsacht]] über Ruprecht und seinen Vater am 5. Mai 1504 machte den Konflikt zum Reichskrieg und mobilisierte beide Seiten (rund 30.000 gegen 60.000 Mann) ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]).
6. **Schlussfolgerung:** Die [[Belagerung von Kufstein 1504]] war nicht der Auslöser, sondern eine Folge dieses dynastischen Konflikts — Maximilian nutzte den Krieg, um die Gerichte Kufstein, Kitzbühel und Rattenberg an sich zu bringen ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Kriegsverlauf|Q1]]).

--- END NOTE ---

--- FILENAME: 30-Narrative/Wie der Bergkristall vom Riepenkar ein prähistorisches Handelsnetz erschloss.md
--- BEGIN NOTE ---

# Wie der Bergkristall vom Riepenkar ein prähistorisches Handelsnetz erschloss

Kernfrage dieses Argumentationsstrangs: Wie wurde ein entlegenes Hochtal in 2.800 Metern Höhe zum zentralen Knotenpunkt eines steinzeitlichen Handelsnetzes?

1. **These:** Der Bergkristall vom Riepenkar war das „Silikon der Steinzeit" — ein begehrtes Hightech-Material, dessen Abbau und Export das Schmirntal bereits im Mesolithikum auf die Landkarte der Urgeschichte setzte ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Glitzernde Urzeit – Das Rätsel vom Riepenkar“|Q1]]).
2. **Der Rohstoff:** In einer 15 Meter langen Quarzkluft der Schieferhülle wuchsen durch hydrothermale Prozesse lupenreine Kristalle — die geologische Voraussetzung für alles Weitere ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Glitzernde Urzeit – Das Rätsel vom Riepenkar“|Q1]]).
3. **Der Abbau:** Systematische Gewinnung mit Klopfsteinen aus härterem Gestein (wie Gneis), Zerlegung in Kerne und Verarbeitung zu Mikrolithen — die weltweit älteste nachgewiesene Abbaustelle dieser Art im Hochgebirge ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]).
4. **Wertsteigerung:** Die winzigen Klingen, Spitzen und Bohrer waren nicht nur hochfunktional (sie schnitten Fleisch und Leder), sondern wegen Transparenz und Glanz prestigeträchtige Kultobjekte — ein doppelter Wert, der den Export lohnte ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]).
5. **Das Netzwerk:** Die chemische Signatur des Riepenkars findet sich im Rofangebirge und am Gardasee — der Beleg für eine funktionierende Logistik über die Alpenpässe hinweg ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]).
6. **Die Transitachse:** Das [[Tuxer Joch]] verband Wipptal und Zillertal und blieb von den mesolithischen Jägerstationen über die bronzeitliche Lochhalsnadel bis zur römischen Goldmünze die Lebensader der Region ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]).
7. **Schlussfolgerung:** Die „Bergkristallstraße" widerlegt das Bild vom isolierten Hochgebirgstal: Schmirn war bereits in der Steinzeit ein Exporteur von Luxusgütern und damit eingebunden in ein überregionales Netz von Rohstoff, Arbeit und Handel ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Glitzernde Urzeit – Das Rätsel vom Riepenkar“|Q1]]).

--- END NOTE ---

--- FILENAME: 30-Narrative/Wie ein Embryo aus eigener Kraft symmetrisch wird.md
--- BEGIN NOTE ---

# Wie ein Embryo aus eigener Kraft symmetrisch wird

Die entscheidende Einsicht der Quelle ist, dass Symmetrie nicht die **Voreinstellung** des Lebens ist, sondern von jedem Embryo **physisch aufgebaut** werden muss, während er selbst noch kaum mehr als ein Zellklumpen ist (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=105s" title="00:01:45">(V)</a>). Der Körper eines Tieres definiert sich nicht über eine Symmetrie "von selbst", sondern der Keim baut Achsen aus den Handlungszwängen seiner Umgebung.

## Die erste Achse: vorn und hinten über Hox-Gene

Die Kopf-Schwanz-Achse (anterior–posterior) beginnt bereits während der **Gastrulation** und zu Beginn der **Neurulation** zu musterzubilden (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=105s" title="00:01:45">(V)</a>). Sie läuft über die bekannten **Hox-Gene**, deren Aufgabe es ist, jedem Körpersegment seine Funktion zuzuordnen — "dieses Stück ist vorn, dieses in der Mitte, dieses am Schwanzende" (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=133s" title="00:02:13">(V)</a>). Damit ist aber noch nicht geklärt, welche Seite links und welche rechts ist.

## Die zweite Achse: links/rechts über Nodal, Pitx2 und Cilien

Die Links-Rechts-Differenzierung ist tückisch, weil der wachsende Embryo seine eigene symmetrische Masse bewusst brechen muss — er entscheidet, welche Seite links wird, während er das Ganze als makellosen Spiegel erhält (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>).

Beim Hühnerembryo liegt die Entscheidung bei den Signalmolekülen **SHH, Nodal und Activin**, wobei der Schlüsselmove **Nodal** ist: Nodal schaltet das Gen **Pitx2** nur auf der linken Seite an (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>). Pitx2 leuchtet im *linken lateralen Plattenmesoderm* auf und übersetzt den abstrakten Befehl "das ist links" in die tatsächliche Körperanlage; die Differenzierung ist nicht-arbiträr, es gibt also eine echte linke Seite (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>).

Doch woher weiß der Embryo überhaupt, was links ist? Bei vielen Wirbeltieren (vermutlich auch Menschen) übernehmen dazu **Nodal-Cilien**: ein Fleck winziger, nach hinten gegeneigter Härchen, die sich drehen und Flüssigkeit in eine gleichbleibende Richtung über den Embryo treiben; diese Strömungsrichtung setzt fest, welche Seite links wird (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=202s" title="00:03:22">(V)</a>). Den Beweis liefern Mäuse ohne diese Cilien: Ihre Links-Rechts-Festlegung wird schlicht randomisiert (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=202s" title="00:03:22">(V)</a>).

## Situs inversus: die Spiegel-Grammatik bleibt intakt

Die Folge einer gestörten Cilienfunktion beim Menschen ist **Situs inversus** — die Organe entstehen als komplette Spiegelbilder der üblichen Anordnung: Herz rechts, der gesamte Magen-Darm-Trakt gespiegelt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=234s" title="00:03:54">(V)</a>). Entscheidend ist: Auch dann zerfällt der Körper nicht in chaotische Asymmetrie, sondern erzeugt eine perfekte Spiegelkopie — jedes Organ ist an der falschen, aber "exakt richtigen falschen" Stelle (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=258s" title="00:04:18">(V)</a>). Das belegt, wie robust die spiegelsymmetrische Baugrammatik des Körpers programmiert ist — selbst eine Fehlentscheidung für die links/rechts-Achse erreicht das Ergebnis noch im Spiegelmodus.

## Fazit

Die Symmetrie des adulten Tiers ist das Endprodukt einer Kaskade embryonaler Achsenentscheidungen (Hox für vorn/hinten, Nodal/Pitx2 für links/rechts), die von den Nodal-Cilien ihren Startimpuls erhält. Diese Schichtung ist wichtig für das Verständnis der Tierkörperbaupläne ([[Körperachsen der Tiere]]) und dafür, wie [[Links-Rechts-Festlegung]] und [[Nodal-Cilien]] die genetisch gebaute Spiegelsymmetrie hervorbringen. Der Fall [[Situs inversus]] zeigt, dass die Symmetrie-Logik selbst beim Fehler erhalten bleibt.

--- END NOTE ---

--- FILENAME: 30-Narrative/Wie Gebirge die Evolutionsgeschichte schreiben.md
--- BEGIN NOTE ---

# Wie Gebirge die Evolutionsgeschichte schreiben

Die Kernaussage der Quelle: Gebirge verzerren unser Bild von der Artenvielfalt im Laufe der Zeit, weil sie **eigene Evolutionsmuster** erzeugen, die sich von den Tieflandbecken unterscheiden (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=56s" title="00:00:56">(V)</a>).

## Die falsche Erzählung

Im Eozän (56 Mio. Jahre) war Wyoming tropisch warm-feucht und unterstützte blühende Ulmen und Sumpfzypressen, die unserer Verwandtschaft, den Primaten ([[Eozäne Primaten Nordamerikas]]), Lebensraum und Nahrung boten (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=67s" title="00:01:07">(V)</a>). Ursprünglich glaubten Forschende, die [[Omomyoiden]]-Primaten bestünden aus zwei Gruppen, unter denen die **Omomyinen** die **Anaptomorphinen** überall verdrängten (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=177s" title="00:02:57">(V)</a>) — eine Erzählung, die sich allerdings fast ausschließlich auf Fossilien aus **niedrig gelegenen Becken** stützte (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=190s" title="00:03:10">(V)</a>).

## Die Entdeckung in der Höhe

In den 1970ern begannen Forschende — angeregt vom Montana-Multituberculaten-Fund — in den Fußhügeln Zentral-Wyomings zu graben (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=198s" title="00:03:18">(V)</a>). Auf ~1.980 m fanden sie anaptomorphine Primaten aus dem mittleren Eozän, die **nicht nur überlebten, sondern sich diversifizierten** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=209s" title="00:03:29">(V)</a>). Ein südlicher Pass (~2.200 m) lieferte in den 1990ern **mehr als ein Dutzend Primatenarten** — deutlich mehr als in den jahrzehntelang erkundeten Tieflagenfundstellen derselben Zeit (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=252s" title="00:04:12">(V)</a>). Die erwartete Häufigkeit wurde auf den Kopf gestellt: seltene Gattungen wie _Artimonius_ waren hier häufig, während _Omomys carteri_ kaum präsent war (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=271s" title="00:04:31">(V)</a>). Gleiche Muster zeigte eine Fundstelle nahe Yellowstone auf ~3.100 m (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=282s" title="00:04:42">(V)</a>).

## Warum Berge anders sind

Nach Ausschluss der [[Time-Averaging in Sedimenten|Time-Averaging]]-Hypothese (gut datierte Schichten schließen eine Sedimentvermischung aus) (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=339s" title="00:05:39">(V)</a>) zeigte sich die Berge eigene Dynamik ([[Gebirge als Motoren der Biodiversität]]):

- **Umweltvariation** durch Höhenunterschiede (Temperatur, Luftdichte, UV) (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=362s" title="00:06:02">(V)</a>).
- **Topografische Komplexität:** mehr Regen → mehr Erosion → viele kleine Flusssysteme → mehr Reliefwechsel pro Flächeneinheit; Klippen und Grate (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=394s" title="00:06:34">(V)</a>).
- **Mehr Nischen → [[Speziation durch Habitatvariation]]**: Habitatvielfalt erhöht die Chance, dass ein Merkmal selektiert wird → neue Arten (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=406s" title="00:06:46">(V)</a>).
- **[[Refugia]]:** Mehr Nischen = weniger Konkurrenz; im Tiefland verdrängte Tiere überleben in den Bergen länger (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=429s" title="00:07:09">(V)</a>).
- **Inselwirkung:** Die Kombination macht Berge zu isolierten Diversitätspocketz wie Inseln (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=454s" title="00:07:34">(V)</a>).

## Tektonische Untermalung

Während die [[Anaptomorphine und Omomyine|Omomyoiden]] evolvierten, entstanden die Rocky Mountains aktiv ([[Gebirge als Motoren der Biodiversität]]) durch Störung und Faltung zwischen 80 und 40 Mio. Jahren (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=504s" title="00:08:24">(V)</a>) mit fast 15 Mio. Jahren Vulkanismus und bis zu ~1,5 km sedimentierter Asche in Teilen Wyomings (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=531s" title="00:08:51">(V)</a>).

## Lektion

Aussterben ist kein An-Aus-Schalter ([[Gebirge als Motoren der Biodiversität]]): Die Anaptomorphinen waren nicht ausgestorben, sondern **hatten sich angepasst und in den Bergen überlebt** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=565s" title="00:09:25">(V)</a>). Die ursprüngliche Verdrängungserzählung war komplexer und interessanter (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=574s" title="00:09:34">(V)</a>). Den Fossilbericht "nach oben" (in die Höhenlagen) zu erweitern eröffnet neue Lektionen (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=583s" title="00:09:43">(V)</a>).

--- END NOTE ---

--- FILENAME: 30-Narrative/Wie Muskeln zu Gehirnen führten.md
--- BEGIN NOTE ---

# Wie Muskeln zu Gehirnen führten

Die zentrale, gegenintuitive These der Quelle: **Brawn führte zu Brains** — die Evolution des Gehirns ist keine Trennung von, sondern eine Konsequenz der Muskelevolution (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=52s" title="00:00:52">(V)</a>).

## Vom Nervensystem zum Gehirn

Vor einem Gehirn braucht es ein [[Nervensystem]] — ein Netzwerk aus Neuronen, das elektrische Signale durch den Körper leitet (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=125s" title="00:02:05">(V)</a>). Die ersten Nervensysteme entstanden (molekular datiert) im Ediacarium, vor ~625 Mio. Jahren (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=189s" title="00:03:09">(V)</a>). Ihr Vorläufer: elektrochemische Signalgebung, die zunächst bei einzelligen Organismen der Außensensorik diente und später zur **inneren Sensorik** der ersten Vielzeller kooptiert wurde ([[Ursprung der Nervensysteme]]) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=513s" title="00:08:33">(V)</a>).

## Der Treiber: größere, bewegungsfähige Körper

Große Körper brauchen mehr Nahrung — und um mehr zu finden, müssen **Tiere sich bewegen** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=523s" title="00:08:43">(V)</a>). Anders als Pflanzen und Pilze, die durch Wachstum zur Nahrung gelangen, nutzen Tiere **Muskeln** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=539s" title="00:08:59">(V)</a>). Die ersten Muskeln begannen als einfach kontrahierbare Fasern; gebündelt formen sie kontrahierendes Muskelgewebe (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=551s" title="00:09:11">(V)</a>). Das älteste bekannte Muskelgewebe ([[Haootia]], Ediacarium ~560 Mio. Jahre) stammt aus genau dieser Phase (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=560s" title="00:09:20">(V)</a>).

## Muskeln brauchen Koordination → Gehirn

Muskeln müssen **in der richtigen Reihenfolge** kontrahieren, um Bewegung in die gewünschte Richtung zu erzeugen — sonst spastiert der Körper nur und schädigt sich selbst (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=593s" title="00:09:53">(V)</a>). Schon **vor** jeder äußeren Sinnesverarbeitung brauchten die frühen Muskelwesen einen **internen Prozessor**, um ihre neuen Körperteile zu koordinieren (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=597s" title="00:09:57">(V)</a>). Effizienz legt nahe, die weiterleitenden und rückkoppelnden Neuronen **dicht zu bündeln** — einen **Knoten aus Nervengewebe, ein Gehirn** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=615s" title="00:10:15">(V)</a>).

**Kernhypothese:** Die frühesten Gehirne evolvierten nicht zur Verarbeitung der äußeren Umwelt, sondern um **die inneren Handlungen der neuen, komplizierten Muskelkörper zu formen** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=617s" title="00:10:17">(V)</a>). Daher ist es kein Zufall, dass [[Haootia]] ungefähr zur selben Zeit liegt wie die molekular datierte Entstehung der Nervensysteme (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=636s" title="00:10:36">(V)</a>).

## Kambrium-Explosion und Informationsrevolution

Im Kambrium (~540 Mio. Jahre) erschien die große Mehrheit der Gruppen mit Gehirnen, **bereits voll ausgebildet** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=262s" title="00:04:22">(V)</a>); ihre architektonische Grundlage war schon im Ediacarium gelegt worden (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=608s" title="00:10:08">(V)</a>). Die **Informationsrevolution** — die Evolution der Augen mit ihrer plötzlichen Informationsflut — trieb zusätzlich das Wachstum neuronaler Prozessoren ([[Fossile Hirne des Kambriums]], [[Evolution des Nervensystems]]) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=404s" title="00:06:44">(V)</a>). Gröβere Körper, Prädation und soziales Leben erhöhten im Kambrium weiter die Nachfrage nach Rechenleistung, was die Gehirngröße wachsen ließ (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=685s" title="00:11:25">(V)</a>).

## Fazit

Ohne das Erscheinen der Muskelkraft (Brawn) hätte die Natur vielleicht nie Gehirne (Brains) hervorgebracht (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=700s" title="00:11:40">(V)</a>). Die Gehirnarchitektur ist kein "Triumph über", sondern ein **Produkt von** Muskeleinsatz ([[Gehirne brauchen Muskeln]]).

--- END NOTE ---

--- FILENAME: 30-Narrative/Wie Trilobiten den Wilson-Zyklus aufdeckten.md
--- BEGIN NOTE ---

# Wie Trilobiten den Wilson-Zyklus aufdeckten

Kernfrage dieses Argumentationsstrangs: Wie konnte aus einem rätselhaften Verteilungsmuster von Trilobiten-Fossilien eine der Kerntheorien der Plattentektonik entstehen?

1. **These:** Eine unscheinbare Beobachtung — zwei unterschiedliche Trilobiten-Faunen auf derselben Insel — wurde über fast ein Jahrhundert zur Entdeckung des Wilson-Zyklus verdichtet <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=57s" title="00:00:57">(V)</a>.
2. **Ausgangspunkt:** 1888 kartierte Walcott die Trilobiten Neufundlands und fand im Osten andere Arten (Paradoxididen) als im Westen (Olenelliden) — obwohl die Flachwasserumgebungen nahe beieinanderlagen und Durchmischung erwarten ließen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=123s" title="00:02:03">(V)</a>. Er beschrieb die zwei getrennten Gemeinschaften als [[Atlantische und Pazifische Faunen]] <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=153s" title="00:02:33">(V)</a>.
3. **Verbreiterung:** Dasselbe Muster fand man überall in der Nordhalbkugel (England/Wales neben Schottland, Spitzbergen, Maine neben Quebec) — lange unerklärbar, solange man glaubte, die Kontinente seien fix <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=200s" title="00:03:20">(V)</a>.
4. **Theorie:** 1912 schlug Wegener die [[Kontinentaldrift]] vor, die wegen fehlenden Mechanismus lange abgelehnt wurde <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=244s" title="00:04:04">(V)</a>.
5. **Auflösung:** Wilson fand an der Faunen-Linie zerquetschte metamorphe und vulkanische Gesteine — Beleg einer Kontinentalkollision <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=282s" title="00:04:42">(V)</a>. Die Faunen bewohnten getrennte Küsten eines Ozeans, der inzwischen geschlossen war <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=297s" title="00:04:57">(V)</a>.
6. **Bestätigung durch Zeitreihe:** Kambrium → Ordovizium → Silur wurden die Faunen zunehmend ähnlicher — die Kontinentteile drifteten aufeinander zu <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=313s" title="00:05:13">(V)</a>. Wilsons Kollisionsbelege bilden die [[Iapetus-Sutur]], die auffällig der Linie des modernen Atlantiks folgt <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=350s" title="00:05:50">(V)</a>.
7. **Schlussfolgerung:** Trilobiten dienten damit nicht nur der Datierung von Gesteinsschichten, sondern als **Indiz für Ozeanzyklen** — 1966 führte die Frage, ob der Atlantik sich geschlossen und wieder geöffnet hat, zum [[Wilson-Zyklus]] <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=381s" title="00:06:21">(V)</a>.

--- END NOTE ---

--- FILENAME: 30-Narrative/Zwischen Pass und Pfarre - Wie politische Grenzen den Totenweg erzwangen.md
--- BEGIN NOTE ---

# Zwischen Pass und Pfarre: Wie politische Grenzen den Totenweg erzwangen

Kernfrage dieses Argumentationsstrangs: Warum trugen die Schmirner ihre Toten über einen 2.338 Meter hohen Pass — und was sagt das über die Logik alpiner Siedlungsstrukturen?

1. **These:** Der Totenweg über das [[Tuxer Joch]] war keine romantische Tradition, sondern die zwingende Folge politischer und kirchlicher Grenzziehung in der Schwaighof-Landschaft ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).
2. **Die Siedlungsform:** Die Besiedlung erfolgte seit dem 13. Jahrhundert („Vallis Smurne" 1249) über [[Schwaighöfe]] — Viehbetriebe in Adels- und Klosterbesitz, deren Zins in Käse und Schmalz entrichtet wurde; sie waren das Rückgrat der alpinen Wirtschaft ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).
3. **Die politische Klammer:** Bis 1926 gehörten Hintertux und das obere Tuxertal politisch und kirchlich zur Gemeinde Schmirn — die Grenze lag nicht am Pass, sondern quer zur Tallinie ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).
4. **Das Begräbnisrecht:** Da Hintertux kein eigenes Begräbnisrecht besaß, mussten alle Verstorbenen zum Friedhof der Mutterpfarre nach Mauern bei Steinach gebracht werden ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).
5. **Die Logistik des Todes:** Särge wurden von Trägern über den 2.338 m hohen Pass geschleppt; im Winter lagerten die Toten monatelang gefroren auf Dachböden, die Totenkammer beim Steckholzer diente als Zwischenlager bei Wetterstürzen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).
6. **Der sakrale Rahmen:** Die [[Sakrale Landschaft des Schmirntals|Pfarrkirche St. Joseph]] (1756/57 von Franz de Paula Penz) und die Wallfahrtskapelle Mariahilf verankerten den Glauben, der die Bestattungspflicht trug — Leben und Tod waren immer eine Frage der Anpassung an die Berge ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).
7. **Schlussfolgerung:** Der Totenweg zeigt die harte Logik alpiner Verwaltungsstrukturen: Eine kirchlich-politische Grenze, die sich über die Wasserscheide hinwegsetzte, erzwang über Jahrhunderte eine der ungewöhnlichsten Bestattungslogistiken der Alpen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).

--- END NOTE ---

# 40-Permanent — Atomare Wissenseinheiten (132 Notizen)

--- FILENAME: 40-Permanent/Adapoidea.md
--- BEGIN NOTE ---

# Adapoidea

**Definition:** Die Adapoiden sind die **größeren, lemurenartigen** Primaten Nordamerikas neben den kleinen, tarsier-artigen [[Omomyoiden]]; sie waren **Obst- und Blattfresser** und durch **wenige gleichzeitig lebende Arten** repräsentiert (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=102s" title="00:01:42">(V)</a>).

**Einordnung:** Adapoiden und Omomyoiden bilden gemeinsam die [[Eozäne Primaten Nordamerikas|eozänen Primaten Nordamerikas]] (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=102s" title="00:01:42">(V)</a>). Gegenüber den vielgestaltigen Omomyoiden (fast 40 Gattungen) hielten sich die Adapoiden zahlenmäßig klein (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=126s" title="00:02:06">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Alpenblumen- und Kräutergarten Toldern.md
--- BEGIN NOTE ---

# Alpenblumen- und Kräutergarten Toldern

Der **Alpenblumen- und Kräutergarten in Toldern** ist ein lebendes Archiv der Pflanzenwelt des Schmirntals: Auf rund **1.000 m²** wachsen hier über **420 dokumentierte Pflanzenarten** der Region ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]). Der Garten wurde **2020 von Freiwilligen revitalisiert** und ist in Themeninseln gegliedert ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]).

Die Themenbereiche spiegeln die vielfältige Nutzung der Alpenflora wider: das **Weihegartl** mit Pflanzen für religiöse Rituale, das **Schnapsgartl** mit Kräutern wie der Meisterwurz und das **Heilkräutergartl** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]). Der Garten dient der **„Schule der Alm“** als lebendiges Klassenzimmer, um altes Wissen über Tinkturen und Heilsalben zu bewahren und weiterzugeben ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]).

Der Garten ergänzt die Kulturlandschaft der [[Bergmähder]] um eine konservatorische Ebene: Während die Mähder die Biodiversität in situ erhalten, sichert der Garten das dazugehörige Anwendungswissen — inklusive der [[Ethnobotanik im Schmirntal|ethnobotanischen Traditionen]]. Als Ort der Freiwilligenarbeit ist er zugleich Teil des [[Bergsteigerdorf|Bergsteigerdorf-Konzepts]] von Schmirn.

--- END NOTE ---

--- FILENAME: 40-Permanent/Alpine Deckentektonik.md
--- BEGIN NOTE ---

# Alpine Deckentektonik

Die **Alpine Deckentektonik** beschreibt, wie der Alpenorogen durch Stapelung großräumiger, übereinander geschobener Gesteinsdecken entstanden ist — ein Modell, das in den Alpen seit über einem Jahrhundert entwickelt wurde (Bertrand 1884, Termier 1904) ([[10-Raw/Field trip to the Tauern Window.pdf#page=1|Q1]]).

Im Ostalpen-Profil folgt die Stapelung einem festen Schema von oben nach unten: Die **Austroalpinen Decken** (Kristallin und Karbonatplattformen der Adria-Platte) liegen am höchsten; darunter folgen die **ozeanischen Decken** des [[Penninisch-Ligurischer Ozean|Penninikums]] (Bündnerschiefer, Glockner-Decke, Ophiolithe) und zuunterst die **Europäische Platte und ihre Sedimentbedeckung**, die im [[Tauernfenster]] aufgeschlossen ist ([[10-Raw/Field trip to the Tauern Window.pdf#page=3|Q1]]).

Der räumliche Übergang von West- zu Ostalpen durchläuft dabei einen orogenen Keil: einen dünnhäutigen Keil im Norden, einen dickhäutigen Keil im Süden und das verschuppte, aufgeschobene Tauernfenster dazwischen; die Bildung begann mit der Hauptkollision im Paleogen und wurde durch die [[Eoalpine Orogenese]] (Kreide) vorbereitet ([[10-Raw/Field trip to the Tauern Window.pdf#page=3|Q1]]).

Verwandte Konzepte: [[Tauernfenster]], [[Eoalpine Orogenese]], [[Penninisch-Ligurischer Ozean]]

## Einfach erklärt

*Deckentektonik* beschreibt, wie sich Gebirge wie die Alpen durch die Stapelung riesiger, dünner "Gesteinsfolien" aufbauen. Wenn zwei Kontinentalplatten zusammenstoßen, taucht die eine nicht einfach unter die andere, sondern die obersten Krustenschichten brechen auf und werden — wie mehrere übereinander geschobene Tischtücher — weit über eine Landschaft gefaltet und geschoben. Einzelne dieser *Decken* können hunderte Kilometer über ihr ursprüngliches Herkunftsgebiet verfrachtet sein; das war im 19. Jahrhundert eine wissenschaftliche Sensation (wie Yosemite, das sich plötzlich als bewegt herausstellt).

Im Ostalpenprofil herrscht eine klare Reihenfolge: oben die **Austroalpinen Decken** (Gestein der afrikanischen/Adriatischen Platte, "spät angekommen"), darunter **ozeanische Decken** (Reste des zwischenzeitlichen Ozeans) und unten **europäisches Grundgebirge**. Man kann das wie ein Sandwich lesen, dessen Schichten die Bewegungsgeschichte erzählen. Für einen Physiker steckt darin die Idee von Scherzonen: Verformung ist nicht homogen über eine große Dicke verteilt, sondern konzentriert sich auf wenige dünne, diskrete Flächen — die Deckenbahnen.

--- END NOTE ---

--- FILENAME: 40-Permanent/Alpine Metamorphose.md
--- BEGIN NOTE ---

# Alpine Metamorphose

Die **Alpine Metamorphose** ist die regionalmetamorphe Überprägung, die alle Einheiten der Ostalpen als Folge der Krustenverdickung während der Alpenorogenese erfasste ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).

Ihren Höhepunkt erreichte die Metamorphose im Tauernfenster bei ~25–30 Mio. Jahren während nahezu isothermer Dekompression nach tiefer Versenkung ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]). Der metamorphe Grad steigt von **Grünschiefer-Fazies** an den Fensterrändern zu **mittlerer Amphibolit-Fazies** im zentralen Bereich und war stark von Verschuppung und unterschiedlichen Versenkungstiefen der einzelnen Einheiten geprägt: Ozeanische Gesteine erreichten im Südwesten nur 7–8 kbar, in der Glockner-Decke 12–17 kbar, eine tektonische Eklogit-Scholle bis 20–25 kbar (600 ± 50 °C) und die europäischen Einheiten 10–12 kbar ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).

Diese Werte belegen eine Versenkung des Kontakts Grundgebirge–Bedeckung auf **mindestens 35–40 km** während der Orogenese. Die Hauptdeformation (N-S-Verkürzung bei geringer E-W-Extension) begann gemeinsam mit der Hochdruckmetamorphose in der Eklogit-Zone (~32 Ma); duktile Deformation an der heutigen Oberfläche endete ~15 Ma ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).

Verwandte Konzepte: [[Tauernfenster]], [[Alpine Deckentektonik]], [[Slab Breakoff und Exhumation]]

## Einfach erklärt

*Metamorphose* heißt: Ein Gestein wird bei geänderten Bedingungen (höherer Temperatur, höherem Druck) umkristallisiert, ohne zu schmelzen. Analog zu einem Phasendiagramm eines Materials hat jedes Gestein ein "Phasenfeld": Bei 600 °C und 20 kbar (das entspricht ~70–90 km Tiefe, wenn man Druck aus Gewicht berechnet) entstehen andere Minerale als an der Erdoberfläche. Die Geologen lesen aus diesen Mineralparagenesen die *P-T-Geschichte* eines Gesteins ab — wie man aus der Kristallstruktur eines Festkörpers dessen thermische Historie rekonstruieren könnte.

Der Clou im Tauernfenster: Man hat die Asservate (die heute oben liegen) tatsächlich 35–40 km tief versenkt — nachweisbar über die Hochdruck-Mineralien. Die Zahlen 7–8 kbar bzw. 20–25 kbar sind einfach *Druckangaben* (1 kbar ≈ 1000 bar; 20 kbar entsprechen dem hydrostatischen Druck in ~200 km Wassersäule bzw. der Wirkung von ~70 km Gestein). Der "Höhepunkt bei ~25–30 Mio. Jahren" ist dabei nichts anderes als der Zeitpunkt maximaler T — danach kühlte das System beim Aufstieg wieder ab (isotherme Dekompression: Erst Druck vermindern, dann Temperatur).

--- END NOTE ---

--- FILENAME: 40-Permanent/Anaptomorphine und Omomyine.md
--- BEGIN NOTE ---

# Anaptomorphine und Omomyine

Die Omomyoiden ([[Omomyoiden]]) teilt man in zwei Untergruppen:

**Anaptomorphine** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=135s" title="00:02:15">(V)</a>):
- Traten vor ~55 Mio. Jahren auf und dominierten Nordamerika (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=135s" title="00:02:15">(V)</a>).
- **Extrem klein**: _Trogolemur_ wog nur ~50 g (etwa eine Zitrone) (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=143s" title="00:02:23">(V)</a>).
- Erkennbar an **scharfen Zahnhöckern** (cusps) und besonders **prominenten vierten Prämolaren** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=150s" title="00:02:30">(V)</a>).
- Im mittleren Eozän (~50 Mio. Jahre) begannen sie im Tiefland zu sinken (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=157s" title="00:02:37">(V)</a>) — überlebten jedoch in den Bergen ([[Refugia]]).

**Omomyine** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=166s" title="00:02:46">(V)</a>):
- Etwas größer, bis 3 kg bei _Macrotarsius_ (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=166s" title="00:02:46">(V)</a>).
- Kürzere Zahnhöcker, **ohne** den prominenten vierten Prämolaren der Anaptomorphinen (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=172s" title="00:02:52">(V)</a>).

**Die Lehre:** _Omomys carteri_, eine oft häufigste Omomyine der Zeit, war an Hochlagen-Fundstellen (Yellowstone, ~3.100 m) kaum präsent, während seltene Anaptomorphinen dort häufig waren(<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=271s" title="00:04:31">(V)</a>). Das zeigt: Die "Verdrängung" durch die Omomyinen war eine Tiefland-/Becken-Erzählung; in den Bergen überlebten die Anaptomorphinen und speziierten weiter (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=565s" title="00:09:25">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Asymmetrie als abgeleitetes Merkmal.md
--- BEGIN NOTE ---

# Asymmetrie als abgeleitetes Merkmal

**Kernidee:** Wenn Symmetrie der billige, "gratis" erhältliche Standard ist ([[Symmetrie als sparsames genetisches Encoding]]), dann kostet absichtliche Einseitigkeit etwas: Man muss die billige Spiegel-Grammatik **aktiv überschreiben** (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=664s" title="00:11:04">(V)</a>).

**Grundregel:** Verfolgt man lopsided (einseitige) Tiere im Stammbaum zurück, erweist sich die Asymmetrie fast immer als **neuere Erfindung**, die symmetrischen Vorfahren aufgepfropft wurde (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=664s" title="00:11:04">(V)</a>).

**Beispiele:**
- **Plattfisch:** normale Spiegel-Larve, dann wanderndes Auge über den Schädel während der Metamorphose (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=677s" title="00:11:17">(V)</a>).
- **Winkerkrabbe:** männliche Tiere mit einer überdimensionierten Haupt-Schere zum Kämpfen — eine massiv, eine klein (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=708s" title="00:11:48">(V)</a>).
- **Narwal:** der Stoßzahn ist der linke Zahn, der durch die Lippe bohrt; die meisten Männchen haben einen, einige zwei, andere keinen (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=708s" title="00:11:48">(V)</a>).
- **Mensch innen:** Herz links, Leber rechts, Darm in spezifischer Richtung — außen fast perfekter Spiegel (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=760s" title="00:12:40">(V)</a>).

**Abgrenzung:** Innere Asymmetrie (z. B. Organlage) bestimmt nicht, ob man bilateral oder radial symmetrisch ist (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=766s" title="00:12:46">(V)</a>). Der Spiegel bleibt sogar bei [[Situs inversus]] vollständig erhalten. Eine Sonderform der "sekundären" Symmetrie-Abweichung ist die [[Sekundäre Radialsymmetrie der Echinodermen]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Atlantische und Pazifische Faunen.md
--- BEGIN NOTE ---

# Atlantische und Pazifische Faunen

**"Atlantische" und "Pazifische" Faunen** sind zwei geografisch getrennte Fossilgemeinschaften des Kambriums, die der Paläontologe Charles Doolittle Walcott 1888 in Neufundland beschrieb <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=153s" title="00:02:33">(V)</a>. Sie umfassten neben Trilobiten auch Brachiopoden und Graptolithen und wurden durch eine Linie mitten durch Neufundland getrennt: Im Osten dominierten Paradoxididen, im Westen Olenelliden <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=129s" title="00:02:09">(V)</a>.

Die Trennung war deshalb rätselhaft, weil nahe beieinanderliegende Flachwasserumgebungen zur gleichen Zeit eigentlich Durchmischung erlaubt hätten <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=136s" title="00:02:16">(V)</a>. Dasselbe Muster fand man überall: "Atlantische" Faunen in England und Wales neben "Pazifischen" in Schottland und Nordirland, "Pazifische" auf Spitzbergen, "Atlantische" in New Brunswick neben "Pazifischen" in Maine und Quebec <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=174s" title="00:02:54">(V)</a>.

Die Auflösung lieferte Wilson: Die Faunen bewohnten völlig verschiedene Küstenlinien, die durch einen tiefen, unüberquerbaren Ozean getrennt waren — den Iapetus-Ozean, der inzwischen geschlossen und verschwunden ist ([[Iapetus-Sutur]]) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=297s" title="00:04:57">(V)</a>. Die Faunen sind damit ein fossiler Beleg für die Existenz eines geschlossenen Ozeans und die entscheidende Spur zum Wilson-Zyklus.

--- END NOTE ---

--- FILENAME: 40-Permanent/Belagerung von Kufstein 1504.md
--- BEGIN NOTE ---

# Belagerung von Kufstein 1504

Die **Belagerung von Kufstein 1504** war das größte kriegerische Ereignis, das je am Inn stattfand, und der am besten dokumentierte Artillerieeinsatz Maximilians I. ([[10-Raw/Inn Truppentransport.pdf#page=7|Q1]]). Sie fiel in den Landshuter Erbfolgekrieg 1504/05: Nach dem Tod Herzog Georgs des Reichen (1503) beanspruchte Ruprecht von der Pfalz das bayerische Erbe, während König Maximilian auf der Seite seines Schwagers Albrecht IV. von Bayern-München kämpfte ([[10-Raw/Inn Truppentransport.pdf#page=7|Q1]]). Die Ausrüstung wurde auf dem Wasserweg herangeschafft — im April 1504 befahl der König, 1.200 Zentner Waffen (Harnischblech, Feldschlangen, Hakenbüchsen) über Donau und Inn nach Innsbruck zu bringen ([[10-Raw/Inn Truppentransport.pdf#page=7|Q1]]).

Nachdem Kufstein am 9. August 1504 kampflos an die Pfälzer gefallen war, belagerte Maximilian mit rund 9.000 Mann die Stadt und stellte den Artilleriepark am gegenüberliegenden Innufer auf, der von Innsbruck aus über den Inn beliefert wurde ([[10-Raw/Inn Truppentransport.pdf#page=7|Q1]]). Die ersten Geschütze verschossen nur Steinkugeln, die an den Mauern wirkungslos zerschellten ([[10-Raw/Inn Truppentransport.pdf#page=7|Q1]]). Erst die schwersten Hauptstücke aus dem Zeughaus — die "Purlepaus" und der "Weckauf von Österreich" mit schmiedeeisernen 70-kg-Kugeln — durchbrachen die Mauern und die dahinterliegenden Kellergewölbe ([[10-Raw/Inn Truppentransport.pdf#page=8|Q1]]). Nach der Eroberung ließ Maximilian 42 Gefangene zum Tode verurteilen; 19 wurden hingerichtet, die übrigen erwirkte Herzog Erich von Braunschweig zu begnadigen ([[10-Raw/Inn Truppentransport.pdf#page=9|Q1]]). Der Inn spielte eine zwiespältige Rolle: Er schützte die Stadt wie ein riesiger Wassergraben, ermöglichte aber zugleich die relativ schnelle Eroberung ([[10-Raw/Inn Truppentransport.pdf#page=10|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Bergkristallbergbau am Riepenkar.md
--- BEGIN NOTE ---

# Bergkristallbergbau am Riepenkar

Der **Bergkristallbergbau am Riepenkar** ist die weltweit älteste nachgewiesene Abbaustelle von Bergkristall im Hochgebirge und datiert in das **Mesolithikum** (Mittelsteinzeit, ab etwa 8.000 v. Chr.) ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Die Fundstelle liegt auf rund **2.800 Metern Höhe** am Südfuß des Olperers ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]).

Ziel des Abbaus war eine rund **15 Meter lange Quarzkluft**, in der durch hydrothermale Prozesse über Jahrmillionen lupenreine, klare Kristalle heranwuchsen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Die Quarzkluft liegt innerhalb der weichen Schieferhülle des [[Tauernfenster|Tauernfensters]] ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Glitzernde Urzeit – Das Rätsel vom Riepenkar“|Q1]]).

Die Gewinnung erfolgte ohne Metall: Mit **Klopfsteinen** aus härterem Gestein (wie Gneis) wurden die Kristalle vorsichtig aus der Kluft geschlagen und vor Ort zu kleineren Stücken („Kernen“) zerlegt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Glitzernde Urzeit – Das Rätsel vom Riepenkar“|Q1]]). Aus den Rohlingen entstanden **Mikrolithen** — winzige, rasiermesserscharfe Klingen, Pfeilspitzen, Bohrer und Schaber, die selbst Fleisch und Leder mühelos schnitten ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Wegen Transparenz und Glanz waren diese Objekte jedoch weit mehr als Werkzeuge: Sie galten als hochgeschätzte **Prestigeobjekte** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Der Abbau war kein Zufallsfund, sondern gezielte, systematische Gewinnung — die Menschen der Steinzeit waren damit weit organisierter als lange angenommen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Glitzernde Urzeit – Das Rätsel vom Riepenkar“|Q1]]). Die Kristalle wurden über ein prähistorisches Handelsnetz exportiert ([[Bergkristallstraße]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Bergkristallstraße.md
--- BEGIN NOTE ---

# Bergkristallstraße

Die **Bergkristallstraße** ist ein prähistorisches Handelsnetz, über das Bergkristall aus dem Schmirntal weit über die Alpen verbreitet wurde ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Archäologen fanden Kristalle mit der exakten chemischen Signatur des [[Bergkristallbergbau am Riepenkar|Riepenkars]] im **Rofangebirge** und sogar am **Gardasee** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]).

Der Nachweis über die chemische Signatur macht den Unterschied zu bloßen Fundparallelen: Es handelt sich nicht um ähnliche Stücke, sondern um nachweislich dasselbe Material aus derselben Lagerstätte — ein Beleg für eine funktionierende **Logistik über die Alpenpässe hinweg** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Das Schmirntal war damit bereits in der Steinzeit ein wichtiger **Exporteur von Luxusgütern** und kein isoliertes Ende der Welt, sondern ein zentraler Knotenpunkt eines prähistorischen Handelssystems ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Glitzernde Urzeit – Das Rätsel vom Riepenkar“|Q1]]).

Der wichtigste Transportweg dieses Netzwerks war das [[Tuxer Joch]], das Wipptal und Zillertal verband ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Die Bezeichnung „Silikon der Steinzeit“ für den Bergkristall bringt seine Rolle auf den Punkt: ein Hightech-Material, das Schmirn auf die Landkarte der Urgeschichte setzte ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Glitzernde Urzeit – Das Rätsel vom Riepenkar“|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Bergmähder.md
--- BEGIN NOTE ---

# Bergmähder

Die **Bergmähder** sind die sonnseitigen, waldfreien Südhänge des Schmirntals — eine über Jahrhunderte geschaffene **Kulturlandschaft**, die heute zu den artenreichsten Lebensräumen Mitteleuropas zählt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]).

Das Rezept für die Biodiversität ist die **Extensivierung**: Die Bauern mähen diese Wiesen nur einmal im Jahr, und das sehr spät — nachdem die Blumen ihre Samen verstreut haben ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]). Zudem wird konsequent auf **Kunstdünger** verzichtet ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]). Nur so können seltene **Orchideen und Enziane** überleben ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]).

Die Mahd ist zugleich **aktiver Katastrophenschutz**: Wird das Gras nicht gemäht, legt es sich im Winter flach auf den Boden und bildet eine glatte Rutschbahn für **Lawinen** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]). Die mühsame Handarbeit mit der Sense auf über 1.800 Metern — ursprünglich Teil der [[Schwaighöfe|Schwaighof-Wirtschaft]] — hält damit das Risiko von Lawinen und Rutschungen niedrig. Diese Funktion übernimmt heute zunehmend die Beweidung durch das [[Tiroler Grauvieh]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Bergsteigerdorf.md
--- BEGIN NOTE ---

# Bergsteigerdorf

**Bergsteigerdorf** ist ein Konzept nachhaltigen Tourismus für alpine Gemeinden, für das sich Schmirn bewusst entschieden hat — gegen den Massentourismus mit großen Liftanlagen und Hotelburgen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]).

Im Mittelpunkt stehen **Ruhe, Eigenverantwortung und der Erhalt der alpinen Kultur** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]). Das Konzept folgt dem Gedanken der **Alpenkonvention**, die den Alpenraum als gemeinsames Lebens- und Wirtschaftsgebiet schützen will ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]).

Die **„Schule der Alm“** ist der operative Kern der Idee: Durch Freiwilligenarbeit werden Almen revitalisiert und Wissen über die Natur weitergegeben — etwa im [[Alpenblumen- und Kräutergarten Toldern|Kräutergarten Toldern]] ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]). Schmirn demonstriert damit das Prinzip „weniger ist mehr“: Der Schutz der Heimat gilt als die beste Investition in die Zukunft ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]). Das Konzept ist die Antwort des Tals auf die Frage, wie eine Region nach dem [[Molybdänbergwerk Alpeiner Scharte|dunklen Kapitel der NS-Zwangsarbeit]] und der Abwanderungsgefahr eine eigene, wertschöpfende Identität entwickeln kann.

--- END NOTE ---

--- FILENAME: 40-Permanent/Bilaterale Symmetrie.md
--- BEGIN NOTE ---

# Bilaterale Symmetrie

Über 99 % aller Tierarten sind symmetrisch gebaut; zieht man die Mittellinie, spiegeln sich die beiden Hälften nahezu exakt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=75s" title="00:01:15">(V)</a>).

**Definition:** Bilaterale Symmetrie bedeutet, dass sich eine Tierebene um eine **einzige zentrale Ebene** (Spiegel-/Mediane) gruppiert — im Gegensatz zur radialen Symmetrie um eine zentrale Achse (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=315s" title="00:05:15">(V)</a>).

**Ursprung (Kernlogik):** Es gibt keinen Umwelttreiber, der zuverlässig die linke bevorzugt — Links und Rechts erleben dieselbe Welt. Daher gibt es keinen Grund, die Seiten verschieden zu bauen, und sie fallen standardmäßig gleich aus: Bilaterale Symmetrie ist die **übrig gebliebene Achse** ([[Körperachsen der Tiere]]) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=406s" title="00:06:46">(V)</a>).

**Vorteile:**
- **Gerichtete Fortbewegung:** Ein Körper mit Vorn/Hinten und zwei spiegelgleichen Seiten ist viel leichter geradeaus zu steuern (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=515s" title="00:08:35">(V)</a>).
- **Manövrierfähigkeit (Biomechanik):** Es ist die einzige Tier-Symmetrie, die in einer Richtung stromlinienförmig und in den übrigen unstromlinienförmig ist — das erlaubt maximale Kraft in wechselnder Richtung, also das Wenden auf der Stelle (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=515s" title="00:08:35">(V)</a>).
- **Sparsames Encoding:** Die Instruktionen werden nur für eine Seite geschrieben; Vorteile wirken auf beide Seiten zugleich ([[Symmetrie als sparsames genetisches Encoding]]) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=545s" title="00:09:05">(V)</a>).

Die große Gruppe dieser Tiere sind die **[[Bilateria]]** (Protostomia/Deuterostomia). Wichtig: Auch ein Innenspiegel wie bei [[Situs inversus]] bleibt symmetrisch (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=258s" title="00:04:18">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Bilateria.md
--- BEGIN NOTE ---

# Bilateria

**Definition:** Die Bilateria sind die große, alle "front-habenden, seiten-gleichen" Tiere umfassende Gruppe ([[Bilaterale Symmetrie]]). Sie spalten sich in zwei große Entwicklungslinien: die **Protostomia** und die **Deuterostomia** (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=581s" title="00:09:41">(V)</a>).

**Alter:** Die Bilateria sind uralt — das Ediacarium enthält die frühesten Vertreter. Einer der ältesten bekannten Bilaterier ist [[Ikaria wutjita]] (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=581s" title="00:09:41">(V)</a>).

**Bedeutung:** Die Bilateria korrespondieren mit der zweiten und dritten [[Körperachsen der Tiere|Körperachse]] (Vorn/Hinten über [[Cephalisation]], Links/Rechts als Spiegel). Echinodermen gehören deuterostom zu den Bilateria, obwohl ihr Adulttier sekundär radial ist ([[Sekundäre Radialsymmetrie der Echinodermen]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Bildung als Deutungsmuster.md
--- BEGIN NOTE ---

# Bildung als Deutungsmuster

> Die Quelle beschreibt Bildung als historisch und gesellschaftlich geprägtes Deutungsmuster – kein festes Wissen, sondern eine dynamische Perspektive auf Selbst- und Weltverhältnisse. Der Begriff bleibt offen für neue Kontexte (z. B. Digitalisierung), ohne seinen Kern zu verlieren: Reflexion, Urteilsfähigkeit und Orientierung.

# Bildung als Deutungsmuster
Nach Bollenbeck ist Bildung kein präzise definierter und abgrenzbarer Begriff, sondern ein disziplinübergreifendes, mehrdimensionales Deutungsmuster, das sich aus dem jeweiligen historischen Kontext ergibt [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 1|Q1]]. Diese Formulierung ist für den Studienbrief zentral, weil sie den Bildungsbegriff von einem festen Gegenstand weg und hin zu einer pragmatischen, reflexiven und historischen Perspektive auf die Welt verschiebt [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 1|Q1]].

Das bedeutet: Bildung ist weder bloßes Wissen noch bloße Kompetenz, sondern eine Weise, wie Menschen sich selbst, andere und die Welt interpretieren und in Beziehung setzen. In diesem Sinn kann Bildung als regulative Idee verstanden werden, die immer an die Lebenswirklichkeit gebunden bleibt und dort ihre konkrete Gestalt erhält [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 1|Q1]]. Die Eigenart des Begriffs liegt deshalb in seiner historischen Offenheit: Er kann in verschiedenen Zeiten und Kontexten unterschiedliche Bedeutungen annehmen, ohne dabei seinen Kern zu verlieren.

Gerade diese Offenheit erklärt, warum Bildung in der modernen Gesellschaft besonders kritisch reflektiert werden muss. Die Quelle zeigt, dass Bildungsbegriffe nicht nur von Institutionen oder Lehrplänen bestimmt werden, sondern von gesellschaftlichen Konflikten, wissenschaftlichen Theorien und anthropologischen Vorstellungen über den Menschen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 2|Q1]]. Bildungsbegriffe sind daher immer zugleich Gegenstand von Theorie und praktischer Lebensbewältigung.

Damit ist Bildung kein bloßes Repertoire an Inhalten, sondern eine Daueraufgabe der Selbst- und Weltverhältnisse. Genau aus dieser Perspektive wird der gebrauchshafte Alltagsbegriff von „Bildung“ verständlich: Er ist nicht explizit, aber in seinen fachlichen und gesellschaftlichen Varianten auf ein komplexes Deutungs- und Gestaltungspotenzial zurückzuführen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 2|Q1]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Bildung als historisches Gedächtnis.md
--- BEGIN NOTE ---

# Bildung als historisches Gedächtnis

> Bildung wird als kulturelles Gedächtnis verstanden: Sie bewahrt historische Denkformen und verbindet Vergangenheit mit Gegenwart. Die Quelle betont, dass Bildungsfragen nur durch Rückgriff auf die Geschichte (z. B. Antike, Aufklärung) verstanden werden können – als Reflexion über Kontinuität und Wandel.

# Bildung als historisches Gedächtnis
Ein wichtiger Gedanke der Quelle ist, dass Bildung als kulturelles Gedächtnis begriffen werden kann. Bildung dient nicht nur der Gegenwart und der Gegenwartserwartung, sondern bewahrt Ideen, Fragen und Antworten, die über das subjektive Moment hinausreichen und orientierende Bedeutung für Mensch und Gesellschaft haben [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 7|Q1]].

Dieser Gedanke ist für die bildungstheoretische Perspektive der Quelle entscheidend: Wer Bildungsfragen heute beantworten will, muss die historische Genese des Begriffs kennen. Die Autor:innen betonen, dass die Kenntnis der Vergangenheit den Blick vor naiver Weltbegegnung schützt und das eigene Denken in Frage stellt. Bildung ist deshalb auch ein Medium der Reflexion über Herkunft, historische Situation und Gegenwartskonstellationen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 8|Q1]].

Mit dieser Sicht wird deutlich, warum ein Rückgriff auf die 2.500-jährige Bildungsgeschichte nicht bloß Zusatzliteratur ist, sondern eine Voraussetzung für ein ernsthaftes Verständnis des Bildungsbegriffs. Die historische Dimension ist keine bloße Vorgeschichte, sondern die Grundlage dafür, dass aktuelle Bildungsfragen überhaupt angemessen eingeordnet werden können [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 8|Q1]].

Damit wird Bildung zugleich zu einem Medium der Erinnerung und der Vergegenwärtigung historischer Denkformen. Die Quelle verbindet damit Vergangenheit und Gegenwart, wodurch das Bildungsverständnis als zeitlich und gesellschaftlich offen erscheint, aber zugleich durch Erinnerung und Reflexion stabilisiert wird [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 8|Q1]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Bildung als individueller Bestand und Vermögen.md
--- BEGIN NOTE ---

# Bildung als individueller Bestand und Vermögen

> Die Quelle unterscheidet Bildung als individuellen Wissensbestand (erworbenes Wissen) und als Vermögen (Fähigkeiten zur Selbstgestaltung). Sie argumentiert, dass beide Dimensionen – Inhalte und Kompetenzen – für eine ganzheitliche Bildung notwendig sind, insbesondere in der digitalen Welt, die lebenslanges Lernen erfordert.

# Bildung als individueller Bestand und Vermögen
Lenzen wird in der Quelle herangezogen, um die Vielfalt der bildungstheoretischen Dimensionen zu zeigen. Bildung kann zunächst als individueller Bestand verstanden werden: als erworbenes Wissen, als Kompetenzen und als kultureller Besitz, den das Individuum in seiner Bildungsgeschichte aufbaut [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 5|Q1]].

Diese Sichtweise macht deutlich, warum Bildung oft mit Wissensvermittlung und Bildungsinhalten verbunden wird. Auch wenn diese Dimension für die Institutionalisierung von Bildung zentral ist, zeigt die Quelle zugleich, dass sie für sich allein zu kurz greift. Bildung ist nicht bloß Besitz, sondern auch Fähigkeit, Reflexion und Selbstgestaltung [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 5|Q1]].

Die zweite Dimension, das individuelle Vermögen, rückt genau diese Seite in den Mittelpunkt: nicht der Stoff allein, sondern die Kräfte, Fähigkeiten und Fertigkeiten, die Menschen befähigen, sich in Welt und Gesellschaft zu orientieren. Diese Perspektive ist gegenläufig zur reinen Inhaltslogik, weil sie Bildung als Potenzial und Selbsttätigkeit begreift [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 5|Q1]].

Die Quelle macht damit ein wichtiges bildungstheoretisches Problem sichtbar: Wissen und Fähigkeit dürfen nicht gegeneinander ausgespielt werden. Bildung braucht beides: Inhalte und Fähigkeiten, Subjekt und Welt, Selbsttätigkeit und Aneignung [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 5|Q1]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Bildung als Selbstüberschreitung.md
--- BEGIN NOTE ---

# Bildung als Selbstüberschreitung

> Bildung wird hier als Prozess der Selbsttransformation verstanden: Sie ermöglicht es dem Subjekt, über sich hinauszuwachsen, neue Perspektiven zu entwickeln und tradierte Denkmuster zu hinterfragen. Die Quelle betont die Verbindung von historischen Bildungsbegriffen (z. B. Paideia) mit modernen Herausforderungen wie Digitalisierung.

# Bildung als Selbstüberschreitung
Die Quelle thematisiert Bildung auch als individuelle Selbstüberschreitung. Die Idee ist nicht nur, vorhandenes Wissen zu erweitern, sondern sich selbst zu überschreiten, also neue Deutungs- und Handlungsmöglichkeiten zu entwickeln. In dieser Perspektive wird Bildung als Prozess der Selbstbestimmung und der Vervollkommnung verstanden, der über bloßes Lernen hinausgeht [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 6|Q1]].

Gerade in der historisch-gesellschaftlichen Perspektive wird deutlich, dass Bildung eine Form der Selbsttransformation ist. Der Mensch wird nicht nur als bestehendes Wesen gedacht, sondern als sich entwickelndes, reflexives Subjekt. Diese Vorstellung ist mit dem Gedanken der Selbsttätigkeit und der Bildsamkeit verbunden und setzt den Menschen als aktives, autonomes und zugleich durch Welt und Gesellschaft bestimmtes Wesen voraus [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 6|Q1]].

Damit ist Bildung keine bloße Anpassung an bestehende Verhältnisse, sondern eine Ermöglichung neuer Perspektiven. Die Quelle zeigt, dass Bildung im Kern ein Aufbrechen von Gewissheiten und ein Hinausgehen über das bisher Gegebene bedeutet – mit dem Ziel, das eigene Verhältnis zu Welt und Gesellschaft reflexiv zu verändern [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 6|Q1]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Bildung als Subjektkonstitution.md
--- BEGIN NOTE ---

# Bildung als Subjektkonstitution

> Bildung wird hier als Subjektkonstitution verstanden: Sie formt nicht nur Wissen, sondern das Selbst in seinem Verhältnis zu Welt und Gesellschaft. Die digitale Lebenswelt erfordert dabei lebenslange Reflexion und Selbstgestaltung – Bildung als aktive Auseinandersetzung, nicht passive Anpassung.

# Bildung als Subjektkonstitution
Die Quelle macht deutlich, dass Bildung nur dann sinnvoll verstanden werden kann, wenn man das Subjekt in den Mittelpunkt stellt. Borst wird darin zitiert, dass Bildung nicht isoliert von anthropologischen Fragen verstanden werden kann, sondern immer bezogen auf ein menschliches Subjekt ist. Je nach erkenntnis- und gesellschaftstheoretischer Position verändert sich dabei die Vorstellung davon, was ein Subjekt ist und was es werden soll [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 4|Q1]].

Diese Pointe ist wichtig, weil Bildung nicht bloß die Aneignung von Wissen beschreibt, sondern die Konstitution des Subjekts in historisch-gesellschaftlichen Verhältnissen. Das Subjekt wird nicht einfach „gebildet“, sondern es bildet sich in der Auseinandersetzung mit Welt, Kultur, Beziehungen und neuen Problemlagen selbst. Diese Selbst- und Weltverhältnisbildung ist zentral für die Quelle, denn Bildung ist als Prozess der Selbstveränderung gedacht, nicht als bloße Informationsaufnahme [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 4|Q1]].

Die Autor:innen betonen zudem, dass sich der Bildungsbegriff nicht in einem statischen Zustand erschöpft. Bildung ist in dieser Lesart ein dynamischer Prozess, in dem das Subjekt neue Dispositionen der Wahrnehmung, Deutung und Bearbeitung von Problemen entwickelt. Menschen lernen dadurch, mit neuen Problemen besser umzugehen, und sie gewinnen eine veränderte Stellung zur Welt [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 4|Q1]].

Das ist der Schlüssel für die digitale Gesellschaft: Bildung ist dann nicht nur schulisch oder institutionell, sondern lebenslang, reflexiv und selbstgestaltend. Die digitale Lebenswelt verlangt deshalb eine Bildung, die das Subjekt nicht bloß als Nutzer, sondern als handelnde, mitverantwortliche und reflexive Person begreift [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 6|Q1]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Brenner-Normalverwerfung.md
--- BEGIN NOTE ---

# Brenner-Normalverwerfung

Die **Brenner-Normalverwerfung** (Brenner-Linie, Brenner Fault) ist eine große, N-S-streichende Abschiebung, die den Westrand des [[Tauernfenster|Tauernfensters]] begrenzt: Das Hangende des Ötztal-Stubai-Kristallins (Teil des Austroalpinen Deckenstapels) wurde relativ zum Tauernfenster nach Westen versetzt ([[10-Raw/Field trip to the Tauern Window.pdf#page=15|Q1]]).

Der **horizontale Versatz** seit dem Miozän wird auf mehrere zehn Kilometer geschätzt; top-west gerichtete duktile Scherung wurde auf ~22–18 Ma datiert, schwache Seismizität zeigt, dass die Störung bis heute aktiv ist ([[10-Raw/Field trip to the Tauern Window.pdf#page=15|Q1]]). Die junge spröde Inkarnation exzidierte ~2 km der Bündnerschiefer; ältere Mylonite belegen eine frühe Phase als flachliegende duktile Scherzone ([[10-Raw/Field trip to the Tauern Window.pdf#page=16|Q1]]).

Der **Footwall-Uplift** erfolgte durch subvertikale einfache Scherung an engständigen steilen Abschiebungen: westfallende Strukturen bei 10–20 km Tiefe (~450 °C) wurden von ostfallenden bei 2–10 km Tiefe (300 ± 50 °C) überprägt — ein klassisches Rollen-Hinge-Muster ([[10-Raw/Field trip to the Tauern Window.pdf#page=16|Q1]]). Zusammen mit der Katschberg-Normalverwerfung am Ostrand bildet die Brenner-Linie das O-W-Extensionssystem, das parallel zur andauernden N-S-Kompression die Exhumation des Tauernfensters ermöglichte ([[10-Raw/Field trip to the Tauern Window.pdf#page=15|Q1]]).

Verwandte Konzepte: [[Tauernfenster]], [[Laterale Extrusion der Ostalpen]], [[Alpine Metamorphose]]

## Einfach erklärt

Eine *Normalverwerfung* entsteht unter **Dehnung**: Gestein wird horizontal auseinandergezogen und bricht dabei an einer schrägen Ebene, wobei der eine Block relativ zum anderen *hinab* rutscht — das Gegenteil einer Überschiebung, bei der Gestein unter Kompression *hinauf* geraten würde. Brenner und Katschberg sind zwei solcher Abschiebungen an den beiden Rändern des Tauernfensters, und zusammen bewirken sie, dass die dazwischen liegende Zone wie ein exhumierter Block aus der Tiefe gefördert wird.

Entscheidend ist die Geometrie: Während die Alpen weiterhin von Norden und Süden zusammengequetscht wurden, lief die *Gegenrichtung* (Dehnung) senkrecht dazu — O-W. Aus Sicht der Kontinuumsmechanik ist das kein Widerspruch: Ein Spannungszustand kann gleichzeitig eine kompressive Komponente in N-S und eine extensive Komponente in O-W enthalten, insbesondere wenn die tiefe Platte seitlich (östlich) Raum lässt. Die beiden Störungssysteme waren über Millionen Jahre aktiv, werden immer steiler und zeigen einen klassischen Übergang von duktilem (langsam-fließendem) zu sprödem (schnell-brechendem) Verhalten, sobald die Temperatur beim Kegeln des Materials abfällt (beschreibbar über eine *Brittle-Ductile Transition* analog zur Glas-Übergangstemperatur).

--- END NOTE ---

--- FILENAME: 40-Permanent/Burgess Shale.md
--- BEGIN NOTE ---

# Burgess Shale (Burgess-Schiefer)

Die **Burgess-Shale** in Kanada ist ein berühmter Fundort der **Weichteilerhaltung**: Dort wurden frühe Tiere durch **schnelle Unterwasser-Schlammrutschen** bedeckt, wodurch die organische Substanz **nicht verrottete** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=320s" title="00:05:20">(V)</a>). Die Fossilien sind zwar abgeflacht, aber **frühe Gehirne und Nervengewebe** können als **dünne Kohlenstoff-Filme** durch den Körper erkennbar sein (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=328s" title="00:05:28">(V)</a>).

**Bedeutung:** Dieselben Prozesse, die Weichkörperorganismen überhaupt fossilisieren, erhalten auch ihr Nervengewebe — das schafft die Grundlage für die [[Fossile Hirne des Kambriums]] (z. B. dem mit Anomalocaris verwandten _Stanleycaris_) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=384s" title="00:06:24">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Burgundisches Erbe Maximilians.md
--- BEGIN NOTE ---

# Burgundisches Erbe Maximilians

Das **burgundische Erbe** bezeichnet die Länder des Hauses Burgund, die Maximilian I. durch seine Heirat mit Maria von Burgund (19. August 1477) *iure uxoris* — kraft des Rechts seiner Ehefrau — als Herzog von Burgund erwarb ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]).

Das Herzogtum Burgund galt damals als das erstrebenswerteste Land Europas: nicht nur wegen seines sagenhaften Reichtums aus dem Handel der flandrischen Städte, sondern auch als letzter Hort des ritterlichen Lebens und der ritterlichen Kultur ([[10-Raw/Maximilian I. (HRR).md#Heiratskandidat|Q1]]). Gleichzeitig hatte sich der Besitz des Hauses Burgund zu einem modernen Verwaltungsstaat entwickelt — eine Verwaltung, die Maximilian später zum Vorbild seiner eigenen Reformen wurde ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Die Erbschaft war der Ausgangspunkt des jahrhundertelangen [[Habsburgisch-französischer Gegensatz|habsburgisch-französischen Gegensatzes]]: Frankreich erkannte die Erbfolge nicht an, besetzte das eigentliche Herzogtum Burgund, und die niederländischen Stände erzwangen das Große Privileg ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]). Durch den Sieg bei Guinegate 1479 und die spätere Stabilisierung durch Friedrich III. blieb der Großteil der burgundischen Länder bei Habsburg ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]).

Verwandte Konzepte: [[Habsburgische Heiratspolitik]], [[Habsburgisch-französischer Gegensatz]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Cephalisation.md
--- BEGIN NOTE ---

# Cephalisation

**Definition:** Cephalisation ist die evolutionäre Konzentration von Nerven- und Sinnesorganen am **vorderen** Körperende zur Bildung eines **Kopfes**.

**Warum sie entsteht:** Bei gerichteter Bewegung ist das vorauslaufende Ende das erste, das auf Nahrung, Bedrohung und alles andere trifft — es ist nicht mehr mit dem nachschleifenden Ende austauschbar (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=375s" title="00:06:15">(V)</a>). Deshalb "crammt" Evolution die Nerven und Sinne dorthin und erzeugt so ein echtes Vorn/Hinten (anterior/posterior) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=375s" title="00:06:15">(V)</a>).

**Bedeutung für die Symmetrie:** Zusammen mit der Gravitationsachse (oben/unten, [[Körperachsen der Tiere]]) liefert die gerichtete Bewegung die zweite Hauptachse des [[Bilaterale Symmetrie|bilateralen Bauplans]]; die dritte Achse (links/rechts) bleibt als ''übrig gebliebene'' Spiegelachse übrig (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=406s" title="00:06:46">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Choanoflagellaten.md
--- BEGIN NOTE ---

# Choanoflagellaten

**Definition:** Einige **koloniale Einzeller**, bekannt als **Choanoflagellaten**, evolvierten dazu, eine **primitive elektrische Signalgebung** zu nutzen (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=496s" title="00:08:16">(V)</a>). Sie sind damit ein Kandidat für die Vorstufe des auf [[Evolution des Nervensystems|elektrochemischen Signalgeben]] basierenden Nervensystems.

**Bedeutung:** Zusammen mit dem chemischen Erkunden der Außenfläche einzelliger Organismen (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=489s" title="00:08:09">(V)</a>) liefern die Choanoflagellaten das Ausgangssignal, das bei den ersten Vielzellern zur **inneren Signalgebung** ([[Ursprung der Nervensysteme]]) kooptiert wurde (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=513s" title="00:08:33">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Cnidarier.md
--- BEGIN NOTE ---

# Cnidarier

**Definition:** Die Cnidarier (Nesseltiere) sind die Gruppe der Quallen und Seeanemonen.

**Symmetrie-Spektrum:** Cnidarier veranschaulichen, dass die Bauplan-Kategorien ([[Radiale Symmetrie|radial]], biradial, [[Bilaterale Symmetrie|bilateral]]) **fließend** sind: Sie laufen je nach Art das ganze Spektrum von *radial* über *biradial* bis *nahezu bilateral* durch (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=461s" title="00:07:41">(V)</a>). Ähnlich unklar positionieren sich die Ctenophoren (Rippenquallen), die eher rotations- oder biradialsymmetrisch sind (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=461s" title="00:07:41">(V)</a>).

**Bedeutung:** Diese Übergänge stützen die Kernlogik, dass der Bauplan eine Folge der Begegnungsweise mit der Welt ist ([[Körperachsen der Tiere]]) — wer nicht gezielt wandert, braucht kein ausgeprägtes Vorn/Hinten.

--- END NOTE ---

--- FILENAME: 40-Permanent/Collegium poetarum et mathematicorum.md
--- BEGIN NOTE ---

# Collegium poetarum et mathematicorum

Das **Collegium poetarum et mathematicorum** (1501) war eine von Maximilian I. an der Universität Wien gegründete Institution, die ein Konzept von Konrad Celtis umsetzte: zwei Lehrstühle für Poetik und Rhetorik sowie zwei für Mathematik und deren naturwissenschaftliche Anwendungsgebiete ([[10-Raw/Maximilian I. (HRR).md#Kunst und Literatur|Q1]]).

Die Gründung war eine **Pioniertat der Institutionalisierung des Humanismus**: Erstmals wurden humanistische Fächer als feste Lehrstühle in eine Universität integriert, statt nur als privates Gelehrtentum zu existieren ([[10-Raw/Maximilian I. (HRR).md#Kunst und Literatur|Q1]]). Sie zeigt die Förderung von Wissenschaft und Literatur durch Maximilian, die neben der kunstsinnigen Selbstdarstellung stand ([[10-Raw/Maximilian I. (HRR).md#Kunst und Literatur|Q1]]).

Zugleich ist die Gründung Teil der [[Maximilians Selbstinszenierung|Selbstinszenierung]] des Kaisers als Mäzen: Die Auftragswerke zielten zuallererst darauf ab, die Erinnerung an seine Person und Familie festzuschreiben ([[10-Raw/Maximilian I. (HRR).md#Kunst und Literatur|Q1]]).

Verwandte Konzepte: [[Maximilians Selbstinszenierung]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Diskordanz am Pfitscher Joch.md
--- BEGIN NOTE ---

# Diskordanz am Pfitscher Joch

Am Grenzposten Pfitscher Joch überschreitet man mehr als eine politische Grenze: Man **überspringt eine Viertelmilliarde Jahre**, denn die große **Diskordanz** zwischen dem von der variszischen Gebirgsbildung betroffenen Ureuropa im Norden und dem „nachvariszischen Europa" im Süden quert hier den Gebirgskamm ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]).

Die Diskordanz trennt im gesamten außeralpinen Europa das **metamorphe, gefaltete Grundgebirge** vom **nicht metamorphen, wenig oder ungefalteten Deckgebirge**: In Spanien liegt sie an der Basis der Meseta, in Frankreich, Belgien und Deutschland grenzt sie die Schichtstufenländer von den Kristallingesteinen ab, in Südtirol trennt sie den weißen Gipfelaufsatz der Tribulaune und Telfer Weißen vom düsteren Untergrund ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]).

Nirgendwo aber ist dieser Grenze so übel mitgespielt worden wie im Tauernfenster: Hier wurden die sonst in Europa kaum beanspruchten Gesteine darüber fast bis zur Unkenntlichkeit zerquetscht, verfaltet und senkrecht gestellt — weil die gesamte [[Alpine Deckentektonik|Deckenstapelung]] über diesen alten Sockel hinwegging ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]).

Die Diskordanz ist damit ein **geologisches Zeitarchiv in der Landschaft**: Wo sie ansteht, fehlen die Gesteine von ~250 Millionen Jahren — abgetragen vor der Tethys-Transgression, als die Zentralgneise und ihre Dachgesteine vor ~250 Ma an der Erdoberfläche lagen ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/EMOD-SLAP.md
--- BEGIN NOTE ---

# EMOD-SLAP

**EMOD-SLAP** („Extending the integrated Monitoring Of Deep-Seated Landslide Activity into the Past") ist ein Forschungsprojekt, das die Bewegungsgeschichte tiefgreifender Hangdeformationen in die Vergangenheit verlängert ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^1].

Die Methode: **photogrammetrische Auswertung historischer Luftbildaufnahmen** erzeugt 3D-Punktwolken, die die Topographie vergangener Jahrzehnte repräsentieren ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^1]. Am [[Reissenschuh-Rutschung|Reissenschuh]] reicht die so rekonstruierte Zeitreihe bis ins Jahr **1954** zurück — sie verlängert die terrestrischen Messkampagnen (2016–2019) erheblich ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^1].

Die zentrale Forschungsfrage des Projekts: Bleiben die beobachteten Bewegungsraten über längere Zeiträume konstant oder unterliegen sie signifikanten Fluktuationen? ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q1]])[^1]. Die Beantwortung ist entscheidend, weil nur ein konstanter oder quantifizierbar variabler Trend eine Extrapolation für das Risikomanagement erlaubt ^[inferred].

[^1]: Remote sensing - Project EMOD-SLAP (https://mountainresearch.at/remote-sensing/emod-slap/)

--- END NOTE ---

--- FILENAME: 40-Permanent/Enrollierung.md
--- BEGIN NOTE ---

# Enrollierung

Die **Enrollierung** ist ein Verteidigungsverhalten von [[Trilobiten]], bei dem sich das Tier wie eine heutige Assel oder ein Gürteltier zu einer Kugel zusammenrollt <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=157s" title="00:02:37">(V)</a>. Sie entstand als Reaktion auf die erstmals im Kambrium auftretende Prädation, als Tiere begannen, andere Tiere zu jagen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=157s" title="00:02:37">(V)</a>.

Der segmentierte Körperbau der Trilobiten machte dieses Verhalten möglich: Gattungen wie Flexicalymene konnten ihren Körper so weit einrollen, dass die hart gepanzerten Segmente nach außen wiesen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=157s" title="00:02:37">(V)</a>. Dadurch wurde es für Räuber deutlich schwerer, in das Tier zu beißen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=157s" title="00:02:37">(V)</a>. Der selektive Druck der neuen Räuber führte also direkt zur Verbreitung dieser Anpassung.

Die Enrollierung ist damit ein frühes Beispiel für defensive Koevolution: Je wirkungsvoller die Räuber im Kambrium wurden, desto stärker wurde die Einrollfähigkeit als Verteidigung selektiert.

--- END NOTE ---

--- FILENAME: 40-Permanent/Entwicklung der Trilobiten.md
--- BEGIN NOTE ---

# Entwicklung der Trilobiten

Die **Entwicklung der Trilobiten** erfolgte über eine Vielzahl von Stadien, bei der bei jeder Häutung Segmente in einer Wachstumszone unmittelbar vor dem Hinterende eingeschoben wurden — ein Muster, das als Anamorphose bezeichnet wird ([[10-Raw/Trilobiten (Quelle).md#Entwicklung|Q1]]). Die meisten Arten besaßen als Adulti eine fixierte Anzahl von Segmenten; bei einigen sehr beinreichen Taxa schritt die Einfügung neuer Segmente offenbar auch nach der Geschlechtsreife bis zum Tode fort ([[10-Raw/Trilobiten (Quelle).md#Entwicklung|Q1]]).

Die Entwicklung ist dank zahlreicher Funde verschieden großer Tiere sowie von Exuvien (Häutungsresten) gut bekannt ([[10-Raw/Trilobiten (Quelle).md#Entwicklung|Q1]]):

- **Protaspis** (erstes Larvenstadium): vier gliedmaßentragende Kopf-Somiten, kurzer Kopfschild und knospenartige Anlage des Thorax ([[10-Raw/Trilobiten (Quelle).md#Entwicklung|Q1]]).
- **Meraspis** (spätere Stadien): zwei Regionen (Kopf und Rumpf) erkennbar; neue Segmente entstehen am Hinterende des transitorischen Pygidiums, wandern durch die Struktur und werden am vorderen Ende zu freien Rumpfsegmenten abgeschnürt ([[10-Raw/Trilobiten (Quelle).md#Entwicklung|Q1]]).
- **Holaspis** (Endstadium): keine neuen Segmente mehr; die Tiere häuteten sich weiter und konnten erheblich an Größe gewinnen ([[10-Raw/Trilobiten (Quelle).md#Entwicklung|Q1]]).

In der Regel besaßen auch die Larvenstadien eine verkalkte Dorsalhülle; eine Ausnahme bilden die Agnostida ([[10-Raw/Trilobiten (Quelle).md#Entwicklung|Q1]]). Wann genau die Geschlechtsreife eintrat, ist am Fossilmaterial nicht zu erkennen, ausgewachsene Exemplare sind aber durch klar definierte Segmentzahl, Form und Größe erkennbar ([[10-Raw/Trilobiten (Quelle).md#Entwicklung|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Eoalpine Orogenese.md
--- BEGIN NOTE ---

# Eoalpine Orogenese

Die **Eoalpine Orogenese** war die erste Gebirgsbildungsphase der Alpen in der Oberkreide, verursacht durch die Schließung des kleinen Hallstatt-Meliata-Ozeans im Osten ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).

Sie betraf ausschließlich die **Austroalpinen Decken** (die ja die oberste, Adriatische Platte repräsentieren) und ist heute nur dort nachweisbar: an kretazischer Eklogit-fazieller Metamorphose und Deformation, an Tiefenerosion sowie an der Ablagerung von Flysch- und Wildflysch-Sedimenten (sog. **Gosau-Sedimente**) ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).

Die Eoalpine Orogenese stellt damit die frühe Phase im großen Wilson-Zyklus der Alpen dar: Bevor im Paleogen die [[Penninisch-Ligurischer Ozean|Alpine Tethys]] geschlossen und die [[Alpine Deckentektonik|Hauptdeckenstapelung]] erfolgte, hatte die Adria-Platte bereits im Osten eine erste Kollision erfahren. Sie ist nur in den höchsten Decken im Deckengebirge aufgezeichnet, nicht in den tieferen ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).

Verwandte Konzepte: [[Alpine Deckentektonik]], [[Penninisch-Ligurischer Ozean]]

## Einfach erklärt

*Eoalpine* bedeutet "früh-alpin": Bevor die "klassischen" Alpen im Paleogen (~40–20 Mio. Jahre) entstanden, gab es bereits in der Oberkreide (vor ~100–70 Mio. Jahren) eine erste Gebirgsbildungs-Runde an der Ostflanke — verursacht durch die Schließung eines kleinen Nebenmeeres (Hallstatt-Meliata-Ozean) östlich des späteren Alpenkerns.

Diese Vor-Orogenese hat nur die *oberen* Decken erfasst (die Austroalpinen Decken, die damals die "Frontlinie" der Adria bildeten). Ihre Spuren — eklogitfazielle Hochdruckmineralien, Tiefenerosion, Gosau- (d. h. synorogen abgelagerte) Sedimente — sind heute wie eingefrorene Momentaufnahmen in diesen Decken konserviert, in den tieferen, jüngeren Decken dagegen fehlen sie. Das ist vergleichbar mit einer "ersten Stoßwelle", die nur den äußersten Ring eines Mehrmassenproblems trifft, bevor die Hauptkollision beginnt. In der Ereignishistorie der Alpen ist die Eoalpine Orogenese damit der Auftakt einer längeren, mehrstufigen Deckengebirgs-Entwicklung — ein *erster Akkretionsakt* im Wilson-Zyklus der Alpen.

--- END NOTE ---

--- FILENAME: 40-Permanent/Eozäne Primaten Nordamerikas.md
--- BEGIN NOTE ---

# Eozäne Primaten Nordamerikas

Am Beginn des Eozäns (56 Mio. Jahre) war das heutige Wyoming so warm und feucht wie heutige Tropen; Sumpfzypressen und blühende Ulmen unterstützten unsere Verwandten, die **Primaten** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=67s" title="00:01:07">(V)</a>). Mit ihren **greiffähigen Händen und Füßen** konnten sie den Lebensraum der Baumkronen (Canopy) besser als alle Säugetiere vor ihnen durchqueren und diversifizierten in viele Arten (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=85s" title="00:01:25">(V)</a>).

Jahrzehntelang glaubte man, sie fielen in **zwei Gruppen**:
- **Adapoiden** — größer, lemurenartig, Obst-/Blattfresser; nur wenige Arten gleichzeitig (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=102s" title="00:01:42">(V)</a>)
- **[[Omomyoiden]]** — klein, spitzmausartig (tarsier-like), sehr vielfältig; spezialisiert auf Insekten, kleine Wirbeltiere, Früchte und Samen (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=115s" title="00:01:55">(V)</a>)

Diese Primaten sind Prüfstoff, weil sie zeigen, wie **Gebirge** ([[Gebirge als Motoren der Biodiversität]]) die scheinbar klare Evolutionsgeschichte (Verdrängung durch Omomyinen) verzerrten ([[Anaptomorphine und Omomyine]], [[Refugia]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Erwählter Römischer Kaiser.md
--- BEGIN NOTE ---

# Erwählter Römischer Kaiser

**Erwählter Römischer Kaiser** war der Titel, den Maximilian I. am 4. Februar 1508 im Dom von Trient mit Zustimmung Papst Julius' II. annahm, nachdem sein Romzug zur Kaiserkrönung am Widerstand der Republik Venedig gescheitert war ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).

Die Titulatur war eine Neuerung: Der Kaisertitel wurde erstmals **ohne päpstliche Krönung in Rom** angenommen, nur gestützt auf die Zustimmung des Papstes. Damit löste Maximilian die Kaiserkrönung von der zeremoniellen Abhängigkeit vom Papsttum und stärkte die Eigenständigkeit des Kaisertitels ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).

Der Schritt passt in das Muster der [[Maximilians Selbstinszenierung|Selbstinszenierung]] Maximilians: Auch hier machte er eine Herrschaftsinsignie von kirchlicher Vermittlung unabhängig. Die Formel "Erwählter Römischer Kaiser" blieb für seine Nachfolger prägend.

Verwandte Konzepte: [[Maximilians Selbstinszenierung]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Ethnobotanik im Schmirntal.md
--- BEGIN NOTE ---

# Ethnobotanik im Schmirntal

Die **Ethnobotanik im Schmirntal** dokumentiert, wie tief die Pflanzenwelt im Volksglauben und Alltag der Schmirner verwurzelt ist — mit teils überraschenden Traditionen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]).

- **Frühlingsenzian** („Schusternagele“): Im Volksmund auch **„Hausanbrenner“** genannt — man glaubte früher, er ziehe Blitze an, wenn man ihn ins Haus bringt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]).
- **Geflecktes Knabenkraut:** Diese Orchidee galt wegen ihrer Wurzelform als **Aphrodisiakum**; sie wurde auch „Ständelwurz“ genannt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]).
- **Ährige Teufelskralle:** In Notzeiten wurden ihre Wurzeln als nährstoffreiches **Wildgemüse** gegraben und verzehrt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]).

Die Beispiele zeigen das typische Muster volkstümlicher Botanik: Pflanzen werden über Analogie-Eigenschaften (Wurzelform, Farbe, Standort) mit unsichtbaren Kräften belegt — vom Blitzschutz über Liebeszauber bis zur Notnahrung. Dieses Wissen wird heute u.a. im [[Alpenblumen- und Kräutergarten Toldern|Kräutergarten Toldern]] und durch die „Schule der Alm“ bewahrt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 4: „Überlebenskünstler am Abgrund – Die Botanik des Schmirntals“|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Evolution des Nervensystems.md
--- BEGIN NOTE ---

# Evolution des Nervensystems

**Ausgangslage heutiger Tiere:** Vertebraten, Arthropoden, Mollusken und unzählige Würmer haben ein um ein Gehirn **zentralisiertes** Nervensystem; **Cnidarier** (Korallen, Quallen) dagegen ein **distribuiertes neuronales Netz** (aber kein Gehirn); **Schwämme** offenbar gar kein traditionelles Nervensystem (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=150s" title="00:02:30">(V)</a>).

**Kambrium-Explosion:** Die übergroße Mehrzahl der Tiergruppen mit Gehirn erschien innerhalb eines geologischen Augenblickes, in der [[Kambrium-Explosion]] vor ~540 Mio. Jahren, und kam **bereits mit intakten Gehirnen** in die Welt (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=262s" title="00:04:22">(V)</a>). Überraschend, weil unter normalen Bedingungen das Gehirn das **erste Organ ist, das nach dem Tod zerfällt** (energiehungrige Zellen, Struktur nur durch Blutfluss) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=292s" title="00:04:52">(V)</a>).

**Informationsrevolution als Treiber:** Die Evolution der **Augen** erzeugte plötzlich viel mehr zu verarbeitende Information, was das Wachstum neuronaler Prozessoren (Gehirne) antrieb (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=404s" title="00:06:44">(V)</a>).

**Ein einziger Ursprung:** Das **gemeinsame neuronale Grundgerüst** fast aller Tiere plus die Gleichzeitigkeit des Erscheinens machen es hochwahrscheinlich, dass **Gehirne nur einmal** bei den frühen Tiervorfahren entstanden (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=446s" title="00:07:26">(V)</a>). Die Vorstufen sind unter [[Ursprung der Nervensysteme]] dokumentiert; die kambrischen Charakterstücke sind unter [[Fossile Hirne des Kambriums]] dokumentiert.

--- END NOTE ---

--- FILENAME: 40-Permanent/Evolutionäres Wettrüsten.md
--- BEGIN NOTE ---

# Evolutionäres Wettrüsten

Als **evolutionäres Wettrüsten** bezeichnet man die wechselseitige Eskalation von Angriffs- und Verteidigungsanpassungen zwischen Räubern und Beute. Im Kambrium, als Prädation erstmals auftrat, hinterließen Trilobiten-Fossilien mit Bissspuren den frühen Beleg dieser Dynamik <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=157s" title="00:02:37">(V)</a>.

Die entscheidende Verschärfung kam mit den Kiefern, die als wahrscheinliche Kryptonit der Trilobiten galten <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=251s" title="00:04:11">(V)</a>: Vor etwa 420 Millionen Jahren erschienen die ersten Kieferfische. Diese neuen Räuber übten einen so starken selektiven Druck auf die [[Trilobiten]] aus, dass rund 20 Millionen Jahre später verstärkt stachelige Trilobiten wie Dicranurus im Fossilbericht auftauchen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=256s" title="00:04:16">(V)</a> — eine klassische Wettrüstenspirale aus offensiven Waffen der Jäger und defensiver Panzerung der Beute.

Diese Spirale zeigt, dass die Bedrohung einer Tiergruppe selten an einem einzelnen Faktor hängt, sondern an einer sich ständig verschärfenden Konkurrenz, die Überleben zu einem fortlaufenden Anpassungswettlauf macht.

--- END NOTE ---

--- FILENAME: 40-Permanent/Ewiger Landfrieden.md
--- BEGIN NOTE ---

# Ewiger Landfrieden

Der **Ewige Landfrieden** (1495) war das zeitlich unbegrenzte, immerwährende und unbedingte Fehdeverbot, das das mittelalterliche Fehderecht ersetzte und das Gewaltmonopol rechtlich dem Reich zuordnete ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Er war das Kernstück der [[Reichsreform von 1495]] und ging wesentlich auf den langwierigen Einsatz des Mainzer Erzbischofs Berthold von Henneberg zurück ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]). Mit dem Landfrieden verlor der private Fehdegang seine Rechtmäßigkeit — Gewalt wurde zum Privileg des Reiches und seiner Organe. Der Ewige Landfriede hing eng mit der Einsetzung des [[Reichskammergericht]]s zusammen, das als Rechtsinstanz die Durchsetzung des Friedens und der neuen Rechtsordnung sichern sollte; die Verhandlungen darum fanden gemeinsam auf dem Wormser Reichstag statt ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Damit ist der Ewige Landfriede ein früher Schritt in Richtung eines staatlichen Gewaltmonopols — die "Handhabung Friedens und Rechts" wurde als Vertrag zwischen König und Ständen institutionalisiert ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Verwandte Konzepte: [[Reichsreform von 1495]], [[Reichskammergericht]], [[Reichsacht]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Facettenaugen der Trilobiten.md
--- BEGIN NOTE ---

# Facettenaugen der Trilobiten

Die **Facettenaugen der Trilobiten** sind einzigartige Sehorgane: Sie bestehen wie das Exoskelett aus dem anorganischen Material Calcit (Calciumcarbonat) und sind daher bei fossilierten Exuvien und Individuen außergewöhnlich gut erhalten — anders als die Augen heutiger Gliederfüßer wurden sie nicht von Mikroorganismen zersetzt ([[10-Raw/Trilobiten (Quelle).md#Augen|Q1]]). Nicht alle Trilobitenarten besaßen Augen; wenn vorhanden, gelten sie den meisten Forschern als homolog zu den Facettenaugen der übrigen Arthropoden ([[10-Raw/Trilobiten (Quelle).md#Augen|Q1]]).

Die Augen treten in drei Formen auf ([[10-Raw/Trilobiten (Quelle).md#Augen|Q1]]):

- **Holochroale Facettenaugen**: Einzelaugen eng aneinandergereiht ohne Sclera dazwischen; eine gemeinsame Hornhaut bedeckt alle Einzelaugen; bis zu 15.000 Einzelaugen ([[10-Raw/Trilobiten (Quelle).md#Augen|Q1]]).
- **Schizochroale Facettenaugen**: Einzelaugen durch eine ausgeprägte, dicke Sclera getrennt; jedes Einzelauge hat eine eigene, tief ins Exoskelett reichende Hornhaut; nur bis zu 700 Einzelaugen ([[10-Raw/Trilobiten (Quelle).md#Augen|Q1]]).
- **Abathochroale Facettenaugen**: Sclera vorhanden, aber dünner als bei schizochroalen Augen; jedes Einzelauge mit eigener Hornhaut, die am Beginn der Sclera endet ([[10-Raw/Trilobiten (Quelle).md#Augen|Q1]]).

Die Facettenaugen sitzen auf den Freiwangen des [[Körperbau der Trilobiten|Kopfschilds]] ([[10-Raw/Trilobiten (Quelle).md#Pleuraler Lobus|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Fossile Hirne des Kambriums.md
--- BEGIN NOTE ---

# Fossile Hirne des Kambriums

**Erhaltung:** Trotz der Weichheit und Zersetzlichkeit von Gehirnen (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=292s" title="00:04:52">(V)</a>) gibt es einen erstaunlich guten Fossilerhalt aus dem frühen Kambrium — dank [[Burgess Shale|Burgess-Schale]]-artiger Prozesse: Unterwasser-Schlammrutschen bedeckten Tiere schnell und hielten die Verwesung auf (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=320s" title="00:05:20">(V)</a>); frühe Gehirne erscheinen als dünne Kohlenstoff-Filme (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=328s" title="00:05:28">(V)</a>).

**Beispiele zunehmender Komplexität:**
- ***Cardiodictyon*** — 518 Mio. Jahre, China; Verwandter der heutigen Samtwürmer; komplettes Nervensystem mit Nervenknoten entlang des vielbeinigen Körpers plus einfaches Gehirn am Kopf (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=349s" title="00:05:49">(V)</a>).
- ***Kerygmachela*** — 518 Mio., Grönland; einfaches Gehirn, das die Augen mit klauenartigen Frontalanhängen verbindet (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=371s" title="00:06:11">(V)</a>).
- ***Stanleycaris*** — 506 Mio., Burgess Schale; mit _Anomalocaris_ verwandter Räuber; in >80 Fossilien ein komplexeres, **zweigeteiltes** Gehirn, mit drei Augen und vorderen Klauen verbunden (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=384s" title="00:06:24">(V)</a>). Da moderne Arthropoden drei Segmente haben, war Stanleycaris' Gehirn "zwei Drittel des Weges" zum Endbauplan (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=395s" title="00:06:35">(V)</a>).

**Informationsrevolution:** Diese Fossilien passen zur Zunahme der Rechenleistung nach der Augenevolution (siehe [[Evolution des Nervensystems]]) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=404s" title="00:06:44">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Furtschaglschiefer.md
--- BEGIN NOTE ---

# Furtschaglschiefer

Die **Furtschaglschiefer** sind schwarze Graphitschiefer der **Greiner Serie**, die zur [[Metamorphe Schieferhülle (Tauernfenster)|Unteren Schieferhülle]] des Tauernfensters gehört. Sie sind das älteste Gestein, das auf der Pfitscher-Joch-Straße angetroffen wird: Sie wurden wahrscheinlich **vor mehr als 700 Millionen Jahren** als schwarze Tonschiefer in einem **schlecht durchlüfteten kleinen Meeresbecken** abgelagert ([[10-Raw/Tauernfenster (Quelle).md#Seite 7|Q1]]).

Die Beckenposition war vermutlich ein **Rücken zwischen dem Festland und einem Inselbogen**, der während der kaledonischen oder variszischen Gebirgsbildung an Ureuropa angeschweißt wurde ([[10-Raw/Tauernfenster (Quelle).md#Seite 7|Q1]]). Sie sind von den Graphitschiefern am Wolfendorn verschieden und bilden u. a. das gesamte Hochstellermassiv ([[10-Raw/Tauernfenster (Quelle).md#Seite 7|Q1]]).

Die schwarze Färbung und der Graphitgehalt sind Kennzeichen von **Sauerstoffmangel am Meeresboden** — der organische Kohlenstoff wurde nicht oxidiert, sondern als Kohlenstoff angereichert. Damit sind die Furtschaglschiefer ein Fenster in die präkambrische Ozeanchemie Ureuropas.

--- END NOTE ---

--- FILENAME: 40-Permanent/Galeerenstrafe.md
--- BEGIN NOTE ---

# Galeerenstrafe

Die **Galeerenstrafe** war eine Mitte des 16. Jahrhunderts eingeführte Rechtsfolge für schwere Verbrechen wie Mord oder Hochverrat: Verurteilte mussten als Ruderer auf den Galeeren der Mittelmeer-Seemächte dienen ([[10-Raw/Inn Truppentransport.pdf#page=13|Q1]]). Sie hing unmittelbar mit dem Krieg gegen die Osmanen zusammen — nach dem Sieg von Lepanto 1571 benötigten Pisa, Genua und Venedig zigtausende Ruderer, die aus den eigenen Strafanstalten nicht zu decken waren, sodass sich ein Handel mit Gefangenen über die Alpen entwickelte ([[10-Raw/Inn Truppentransport.pdf#page=13|Q1]]).

Die Habsburger leerten ihre Gefängnisse und sparten Unterbringungskosten, die Seemächte erhielten die dringend benötigten Ruderer — ein beidseitig vorteilhafter Handel ([[10-Raw/Inn Truppentransport.pdf#page=13|Q1]]). Die Strafe wurde schließlich auch auf eigentlich nicht straffällige Personen ausgedehnt: Die Bayerische Landesordnung von 1695 nannte "herumvagierende Freyleut und Schinder", zudem standen Roma und Sinti auf der Liste ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]). Praktische Schwierigkeiten entstanden durch die zeitliche Begrenzung der Strafe, die Venedig oft missachtete ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]). Bis ins 18. Jahrhundert wurden so mehrere tausend Häftlinge aus Österreich nach Italien deportiert, von denen nur ein Bruchteil überlebte ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Gebirge als Motoren der Biodiversität.md
--- BEGIN NOTE ---

# Gebirge als Motoren der Biodiversität

**Kernidee:** Berge erhöhen die Artenvielfalt, weil sie **mehr Umweltvariation** bieten als Tiefländer und daher **mehr ökologische Nischen** unterstützen (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=402s" title="00:06:42">(V)</a>).

**Mechanismen:**
- **Höhenbedingte Umweltvariation:** Mit der Höhe ändern sich Temperatur, Luftdichte und UV-Strahlung (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=362s" title="00:06:02">(V)</a>).
- **Topografische Komplexität:** Mehr Regen → aktivere Erosion → viele kleine Flusssysteme, die die Landschaft unterschiedlich zerschneiden; pro Flächeneinheit mehr Reliefwechsel als im Tiefland; dazu Klippen, Grate und tektonische Zergliederung (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=394s" title="00:06:34">(V)</a>).
- **Mehr Nischen → mehr Arten:** Jede Habitatvariation erhöht die Wahrscheinlichkeit, dass ein Merkmal selektiert wird → [[Speziation durch Habitatvariation]] (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=406s" title="00:06:46">(V)</a>).
- **[[Refugia]]:** Mehr Nischen = weniger Konkurrenz; im Tiefland verdrängte Arten überleben (und halten) in den Bergen länger (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=429s" title="00:07:09">(V)</a>).
- **Inselwirkung:** Die Kombination lässt Berge wie Inseln wirken — isolierte Diversitätspocketz (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=454s" title="00:07:34">(V)</a>).

**Konsequenzen für den Fossilbericht:** Bergumgebungen haben steile Gradienten, hohes Erosionspotenzial und schlechte Erhaltung (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=548s" title="00:09:08">(V)</a>). Weil Tieflandbecken leichter erforscht wurden, kann der scheinbare "Niedergang" einer Gruppe in Wahrheit ein Rückzug in die Häfen der Berge sein — Aussterben ist nicht immer ein An/Aus-Schalter (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=554s" title="00:09:14">(V)</a>). Grundlage dazu ist die tektonische Aktivität selbst (Rocky Mountains, 80–40 Mio. Jahre) (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=504s" title="00:08:24">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Gehirn als zentraler Verarbeitungshub.md
--- BEGIN NOTE ---

# Gehirn als zentraler Verarbeitungshub

Alle Gehirne — vom [[Haootia|Ediacara-Zeitalter]] bis heute — haben einen gemeinsamen Unterbau: Sie sind **physische Verlängerungen des Nervensystems**, die als dessen **zentralisierter Verarbeitungshub** dienen ("Mission Control") (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=104s" title="00:01:44">(V)</a>). Das Gehirn ist gewissermaßen das **Motherboard**, das die komplexen, ständig durch den Körper gesendeten Signale versteht (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=111s" title="00:01:51">(V)</a>).

**Formenvielfalt:**
- **Kraken (Octopoden):** donutförmiges Gehirn um die Speiseröhre — zu große Mahlzeiten riskieren Gehirnschäden (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=71s" title="00:01:11">(V)</a>).
- **Krokodile:** erdnussgroßes Gehirn, koordiniert dennoch effiziente Jagdstrategien (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=79s" title="00:01:19">(V)</a>).
- **Mensch:** 2 % der Körpermasse, aber 20 % des Energieverbrauchs; dauerhaft ~20 Watt — genug für eine Glühbirne (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=88s" title="00:01:28">(V)</a>).

**Basis:** Vor einem Gehirn braucht es ein [[Nervensystem]] aus [[Neuronen-Netz]]. Die [[Evolution des Nervensystems]] zeigt, dass dieses zentralisierte Gehirn im Kambrium mit voll ausgebildeter Architektur erschien (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=262s" title="00:04:22">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Gehirne brauchen Muskeln.md
--- BEGIN NOTE ---

# Gehirne brauchen Muskeln

**Kernidee:** Die Evolution des Gehirns ist untrennbar mit der **Bewegung** verknüpft — Brawn (Muskelkraft) führte zu Brains (Gehirnen) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=52s" title="00:00:52">(V)</a>).

**Begründungskette:**
1. **Große Körper brauchen mehr Nahrung** — und um mehr zu finden, müssen die Tiere sich bewegen (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=523s" title="00:08:43">(V)</a>).
2. Anders als Pflanzen und Pilze, die durch **Wachstum** zu ihrer Nahrung gelangen, nutzen Tiere **Muskeln** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=539s" title="00:08:59">(V)</a>).
3. Die ersten **Muskeln** waren einfache, kontrahierbare Fasern; gebündelt kontrahieren sie als Muskelgewebe (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=551s" title="00:09:11">(V)</a>). Frühestes Muskelgewebe: [[Haootia]], Ediacarium ~560 Mio. Jahre (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=560s" title="00:09:20">(V)</a>).
4. **Muskeln brauchen Koordination**: Der Körper muss Muskeln in der richtigen Reihenfolge kontrahieren, sonst spastiert er und schädigt sich (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=593s" title="00:09:53">(V)</a>).
5. Schon vor jeder sensorischen Reaktion brauchten die frühen Muskelwesen einen **internen Prozessor** zur Koordination ihrer neuen Körperteile (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=597s" title="00:09:57">(V)</a>).
6. Effizienz verlangt, die weiter- und rückgekoppelten Neuronen **dicht zu bündeln** — ein **Nervenknoten, also ein Gehirn** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=615s" title="00:10:15">(V)</a>).

**Kernhypothese:** Die frühesten Gehirne entstanden daher nicht (nur) zur Verarbeitung der äußeren Umwelt, sondern um **die inneren Handlungen der neuen, komplizierten Muskelkörper zu formen** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=617s" title="00:10:17">(V)</a>). Ohne die Muskelkraft gäbe es mutmaßlich keine Gehirne (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=700s" title="00:11:40">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Gemeiner Pfennig.md
--- BEGIN NOTE ---

# Gemeiner Pfennig

Der **Gemeine Pfennig** war die erste reichsweite Steuer des Heiligen Römischen Reiches, beschlossen im Rahmen der [[Reichsreform von 1495]] auf dem Reichstag zu Worms ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Er war Teil von Maximilians I. Versuch, die kaiserliche Zentralgewalt zu stärken, indem das Reich eigene Einnahmen erhielt, statt von den Beiträgen der Stände abzuhängen ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]). Die Einhebung sollte über die neu geschaffenen [[Reichskreise]] erfolgen, die als regionale Verwaltungseinheiten mit der Erhebung von Reichssteuern betraut waren ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Als erster Versuch einer reichsweiten Besteuerung scheiterte der Gemeine Pfennig letztlich an der Erhebungspraxis und dem Widerstand der Stände — die [[Reichsreform von 1495]] blieb in diesem Punkt fragmentarisch, wie auch bei anderen Reformvorhaben ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Verwandte Konzepte: [[Reichsreform von 1495]], [[Reichskreise]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Geothermobarometrie.md
--- BEGIN NOTE ---

# Geothermobarometrie

Die **Geothermobarometrie** rekonstruiert aus Mineralen die Druck- und Temperaturbedingungen (P-T-Bedingungen), unter denen Gesteine metamorph wurden — und mit radiometrischen Uhren auch den Zeitpunkt. Im [[Tauernfenster]] belegt sie, dass das Gebirge unter mehr als 30 km Gesteinsüberlagerung auf über 500 °C aufgeheizt wurde ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]], [[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).

**Indikatorminerale** sind die erste Stufe: **Disthen, Lawsonit, Granat und Glaukophane zeigen hohen Druck** an, **Staurolith, Cordierit und Sillimanit hohe Temperatur**. Jedes Mineral hat einen begrenzten Stabilitätsbereich; mit vielen Mineralen lassen sich die maximal erreichten Bedingungen gut eingrenzen ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).

Genauer sind **Mischkristall-Gleichgewichte**: Granat neben Biotit oder Plagioklas verteilt je nach P-T-Bedingungen bestimmte Elemente anders zwischen den Mineralen auf, woraus sich Druck und maximale Temperatur zuverlässig berechnen lassen ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).

Die **Zeitachse** liefern radiometrische Uhren mit Schließungstemperatur: Radioaktives Kalium zerfällt (Halbwertszeit 1,19 Mrd. Jahre) in Argon, das unterhalb der Schließungstemperatur im Kristallgitter gefangen bleibt — **Muskowit schließt Argon unterhalb ~450 °C ein, Biotit bei ~300 °C**; **Apatit-Spaltspuren** (durch Uranspaltung zerstörte Gitter, die unterhalb 150 °C nicht mehr repariert werden) datieren den Zeitpunkt, seit dem das Gestein unter 150 °C ist. Für das Tauernfenster ergibt sich: **vor 17 Ma unterschritten die Gesteine 450 °C, vor 14 Ma 300 °C, vor 6 Ma 150 °C** — Fixpunkte der Hebungsgeschichte, die sich in den heutigen 1,2 mm/a Hebung (60 Jahre Präzisionsmessung) fortsetzt ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]], [[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q1]]).

Voraussetzung für alle Methoden ist, dass sich die meisten Minerale beim Abkühlen **nicht zurückwandeln** (es fehlt Energie und oft Wasser) — „sonst gäbe es gar keine metamorphen Gesteine" ([[10-Raw/Tauernfenster (Quelle).md#Seite 2|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Gesichtsnaht und Häutung der Trilobiten.md
--- BEGIN NOTE ---

# Gesichtsnaht und Häutung der Trilobiten

Die **Gesichtsnaht** (*Sutura facialis*) ist eine Sollbruchstelle im Exoskelett des Kopfschilds, die es dem Trilobiten ermöglicht, bei der [[Körperbau der Trilobiten|Häutung]] aus dem alten Panzer zu kriechen ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]). Bei der Häutung zerfällt der Kopfschild in das Cranidium — Glabella plus Fixigenae (feste Wangen) — und die beiden Librigenae (freie Wangen) ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]).

Je nach Position und Verlauf der Gesichtsnaht werden mehrere Grundtypen unterschieden ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]):

- **Protopare/hypopare Naht**: Verläuft entlang der Außenkante des Cephalons; Freiwangen werden nicht ausgebildet. Tritt besonders häufig bei urtümlichen Trilobiten (Agnostida) auf, sekundär auch bei hochspezialisierten Formen wie den Harpetida ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]).
- **Propare Naht**: Verläuft nur im vordersten Bereich entlang der Außenkante, übertritt dann auf die Oberseite, zieht zum Augenhügel und entlang der Innenseite der Facettenaugen und kehrt vor dem Wangeneck zur Außenkante zurück ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]).
- **Gonatopare Naht**: Ähnlicher Verlauf, endet aber direkt im Wangeneck bzw. an der Spitze des Wangenstachels ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]).
- **Opisthopare Naht**: Endet erst nach dem Wangeneck bzw. Wangenstachel an der Hinterkante des Kopfschilds ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]).
- **Metapare Naht**: Beginnt an der Hinterkante, verläuft zum Augenhügel und zurück zu einem ebenfalls an der Hinterkante liegenden Austrittspunkt ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]).

Da die Häutung wiederholt stattfand, sind isolierte Librigenae als Häutungsreste häufig zu finden — die Gesichtsnaht ist damit ein diagnostisch bedeutsames Merkmal und ein Indiz für die [[Körperbau der Trilobiten|Anatomie]] und das Wachstum der Tiere ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Gravitative Kaskadenprozesse am Reissenschuh.md
--- BEGIN NOTE ---

# Gravitative Kaskadenprozesse am Reissenschuh

**Gravitative Kaskadenprozesse** beschreiben die Wechselwirkung zwischen einer tiefgreifenden gravitativen Hangdeformation (DSGSD) und schnellen oberflächennahen Massenbewegungen: Die langsame, kontinuierliche Bewegung des [[Reissenschuh-Rutschung|Reissenschuh]]-Hangs liefert permanent **Lockermaterial** in die steilen Gerinne unterhalb der Rutschung ([[10-Raw/Reissenschuh.md|Q1]])[^1].

Der Kaskadenmechanismus funktioniert in zwei Zeitskalen ([[10-Raw/Reissenschuh.md|Q1]])[^1]:

1. **Akkumulationsphase** (Jahre): Die DSGSD mit 0,6–0,8 m/Jahr Bewegung zerkleinert und transportiert kontinuierlich Gesteinsmaterial hangabwärts, das sich in den Abflussrinnen sammelt.

2. **Trigger-Phase** (Stunden): Bei **Extremwetterereignissen** — insbesondere Starkregen oder schneller Schneeschmelze — wird das angesammelte Lockermaterial als **schnell fließende Mure (Debris Flow)** remobilisiert und schießt mit hoher Geschwindigkeit ins Tal.

Für das lokale **Naturgefahrenmanagement** ist diese Kaskade zentral ([[10-Raw/Reissenschuh.md|Q1]])[^1]: Die Überwachung muss nicht nur die langsame Hangbewegung selbst erfassen ([[Monitoring gravitativer Hangdeformationen|TLS, DGNSS]]), sondern auch die Materialbilanz in den Abflussrinnen — denn die eigentliche akute Gefahr für die Talinfrastruktur entsteht erst durch den Umschlag von langsamer Deformation in schnelle Mure.

[^1]: [Observation and Modeling of Cascade Processes at the Reissenschuh (Schmirn, Austria)](https://notebooklm.google.com/source/20)

--- END NOTE ---

--- FILENAME: 40-Permanent/Habsburgisch-französischer Gegensatz.md
--- BEGIN NOTE ---

# Habsburgisch-französischer Gegensatz

Der **habsburgisch-französische Gegensatz** war die jahrhundertelange strukturelle Rivalität zwischen dem Haus Habsburg und der französischen Krone, die mit dem Erbe Karls des Kühnen begann ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]).

Seine Ursache lag in der ungeklärten Nachfolge nach dem Tod Karls des Kühnen 1477: Frankreich erkannte die Erbfolge Marias von Burgund nicht an und besetzte das eigentliche Herzogtum Burgund, das zum französischen Lehensverband zählte ([[10-Raw/Maximilian I. (HRR).md#Herzog von Burgund und römisch-deutscher König|Q1]]). Das [[Burgundisches Erbe Maximilians|burgundische Erbe]] war damit von Anfang an umstritten und machte die habsburgische Position in den Niederlanden zum ständigen Konfliktherd.

Maximilian wehrte die französischen Rückeroberungsversuche 1479 in der Schlacht bei Guinegate ab und sicherte die Herrschaft in den meisten Ländern der burgundischen Herzöge — nur das Herzogtum Burgund selbst blieb unter französischer Kontrolle ([[10-Raw/Maximilian I. (HRR).md#Die Habsburgischen Erblande, Burgund und das Reich|Q1]]). Der Gegensatz prägte die gesamte habsburgische Politik der Frühen Neuzeit und bildete den Rahmen für die [[Habsburgische Heiratspolitik|Heiratspolitik]], mit der Habsburg sich Verbündete gegen Frankreich sicherte (etwa Spanien 1494/96).

Verwandte Konzepte: [[Burgundisches Erbe Maximilians]], [[Habsburgische Heiratspolitik]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Habsburgische Heiratspolitik.md
--- BEGIN NOTE ---

# Habsburgische Heiratspolitik

Die **habsburgische Heiratspolitik** war die strategische Verbindung von Eheschließungen mit politischen Zielen: Durch gezielte Heiraten wurden Erbansprüche auf fremde Herrschaftsgebiete erworben, ohne dass diese erobert werden mussten ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).

Maximilian I. perfektionierte dieses Muster: Seine eigene Heirat mit Maria von Burgund brachte das [[Burgundisches Erbe Maximilians|burgundische Erbe]] ein; die Vermählung seines Sohnes Philipp mit Johanna von Kastilien (1496) verband das Haus mit den Kronen Aragoniens und Kastiliens; die [[Wiener Doppelhochzeit 1515]] sicherte die Nachfolge in Böhmen und Ungarn ab ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).

Die Strategie wirkte über Generationen: Maximilian konnte das Reich seinem Enkel Karl V. als Universalmonarchie übergeben, über der "die Sonne nicht mehr unterging" ([[10-Raw/Maximilian I. (HRR).md#Die Habsburgischen Erblande, Burgund und das Reich|Q1]]). Die Heiratspolitik war damit der zentrale Mechanismus des habsburgischen Aufstiegs — mit der Kehrseite, dass sie zugleich den langwierigen [[Habsburgisch-französischer Gegensatz|Gegensatz zu Frankreich]] begründete.

Verwandte Konzepte: [[Burgundisches Erbe Maximilians]], [[Wiener Doppelhochzeit 1515]], [[Pressburger Vertrag 1491]], [[Habsburgisch-französischer Gegensatz]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Hall in Tirol als Zentrum der Militärschifffahrt.md
--- BEGIN NOTE ---

# Hall in Tirol als Zentrum der Militärschifffahrt

**Hall in Tirol** war der logistische Knotenpunkt der militärischen Innschifffahrt. Zuständig für die Organisation der Militärfahrten war das Pfannhausamt; ein hölzerner Rechen der Saline sperrte den Fluss, um Treibholz aufzufangen, und machte Hall zum Endpunkt des regulären Warentransports, den man dort auf Wagen umlud ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]).

Die Konzentration auf Hall erzeugte Engpässe: Da sich Soldaten nicht regelmäßig anmeldeten, kam es zu Staus, und der Salzmair musste Wartegelder für leer bereitgestellte Boote zahlen ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). In Hall gab es keine Bootsbauer, sodass man zivile Schiffe bis nach Bayern auslieh und fehlende Innschiffer aus Bayern und Salzburg holte — 1601 brauchte man 700 Innschiffer für 6.000 Soldaten ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). 1595 zog sich das Verschiffen von knapp 13.000 Soldaten und 2.677 Pferden fast zwei Monate hin ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). Die Dimension wird an den Zahlen deutlich: 1603 organisierte das Salzamt für ein Regiment von 3.000 Mann Kampfstärke 101 Schiffe mit einer Ladekapazität von 13.783 Menschen — der Tross machte über 10.000 Mann aus ([[10-Raw/Inn Truppentransport.pdf#page=5|Q1]]). 1532 standen an der Lend 45 Schiffe für 20.000 Mann bereit ([[10-Raw/Inn Truppentransport.pdf#page=10|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Haootia.md
--- BEGIN NOTE ---

# Haootia

**Definition:** Haootia ist ein merkwürdiges, runzliges Ediacara-Organismus aus dem heutigen Kanada, vor ~560 Mio. Jahren (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=39s" title="00:00:39">(V)</a>).

**Bedeutung:** Es enthält eines der **frühesten bekannten Muskelgewebe** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=560s" title="00:09:20">(V)</a>) und wird für eine **Cnidarier-Art** (mit Korallen und Quallen verwandt) gehalten (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=593s" title="00:09:33">(V)</a>). Wie andere Ediacara-Organismen besitzt es **keine Spuren- oder Bewegungsspuren** — keine Belege für koordinierte Bewegung (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=645s" title="00:10:45">(V)</a>).

**Relevanz für Gehirne:** Haootia liegt zeitlich nahe an der molekular datierten Entstehung der Nervensysteme (~625 Mio. Jahre, [[Ursprung der Nervensysteme]]) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=189s" title="00:03:09">(V)</a>). Ihre Muskel-Nervenz-Kopplung stützt die Hypothese **[[Gehirne brauchen Muskeln]]**: Muskeln brauchen Koordination, und diese leistet früh ein gebündelter Nervenknoten — ein Gehirn (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=615s" title="00:10:15">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Hox-Gene.md
--- BEGIN NOTE ---

# Hox-Gene

**Definition:** Hox-Gene sind eine berühmte Gruppe von Entwicklungsgenen, deren Aufgabe es ist, jedem Körpersegment seine Funktion zu-zuordnen — "dieses Stück ist vorn, dieses in der Mitte, dieses am Schwanzende" (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=133s" title="00:02:13">(V)</a>).

**Zeitpunkt:** Die Musterbildung der Kopf-Schwanz-Achse (anterior–posterior) beginnt **während der Gastrulation** und zu Beginn der **Neurulation** (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=105s" title="00:01:45">(V)</a>).

**Bedeutung:** Hox-Gene legen die erste der drei [[Körperachsen der Tiere|Körperachsen]] fest. Sie reichen aber nicht für die komplette Symmetrie — die Links/Rechts-Achse wird separat über die [[Links-Rechts-Festlegung]] determiniert. Die Hox-Gene sind damit ein Beispiel dafür, dass Symmetrie **aktiv aufgebaut** werden muss und keine biologische Voreinstellung ist (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=105s" title="00:01:45">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Humboldt und die allgemeine Menschenbildung.md
--- BEGIN NOTE ---

# Humboldt und die allgemeine Menschenbildung

Wilhelm von Humboldt gilt in der Quelle als Mitbegründer einer modernen Bildungstheorie, die den Menschen als Selbstzweck begreift. Bildung ist für ihn nicht die Ausbildung zu einer bestimmten Funktion oder eines beruflichen Zwecks, sondern die Selbstformung und Höherbildung des Individuums in Richtung einer ganzheitlichen Totalität. Der Mensch soll nicht bloß als Mittel für gesellschaftliche Zwecke dienen, sondern als Selbstzweck entwickelt werden [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 31|Q1]].

Die zentrale Idee ist die „allgemeine Bildung“. Sie ist kein bloßes Wissen über einzelne Gegenstände, sondern eine rege, freie Wechselwirkung zwischen Mensch und Welt, in der die Kräfte des Individuums sich entfalten und gegenseitig fördern. Bildung entsteht daher nicht durch bloße Berufsvorbereitung, sondern durch die aktive und freie Auseinandersetzung mit einer Welt, die dem Menschen fremd und zugleich bildungsreich gegenübertritt [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 32|Q1]].

Die Quelle zeigt dabei den bildungsrelevanten Gedanken der Selbstentfremdung. Durch Begegnung mit der Welt, durch fremde Sprachen, andere Perspektiven und neue Inhalte wird das bisherige Selbst in Frage gestellt. Bildung ist deshalb nicht bloß Rückkehr zu sich selbst, sondern ein Prozess, in dem das Selbst sich durch Fremdes erweitert und verändert [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 32|Q1]].

Humboldt verbindet diese Idee mit einem dreistufigen Bildungswesen: Elementarbildung, Schulunterricht und Universität. Die Schule soll die grundlegende Bildung ermöglichen, die Universität aber vor allem die freie, zweckfreie Wissenschaft und die Verbindung von Forschung und Lehre fördern. Damit ist der Bildungsbegriff nicht auf Ökonomie oder Berufsziel reduziert, sondern auf die allgemeine Moralisierung, die philosophische Reflexion und die Kultivierung des Menschen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 34|Q1]].

Für die Gegenwart ist Humboldts Theorie deshalb von Bedeutung, weil sie eine kritische Gegenposition zu rein funktionaler, ökonomischer oder outputorientierter Bildung bildet. Bildung ist bei ihm ein lebenslanger Prozess, dessen Ziel nicht die Erreichung eines Endpunkts ist, sondern die dynamische und unbegrenzte Höherentwicklung des Menschen in seiner Totalität [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 32|Q1]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Iapetus-Sutur.md
--- BEGIN NOTE ---

# Iapetus-Sutur

Die **Iapetus-Sutur** ist die Zerstörungszone, die beim Schließen des antiken Iapetus-Ozeans entstand — sie ist der gesamte Rest, der von diesem trilobitentrennenden Ozean übrig blieb <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=350s" title="00:05:50">(V)</a>. John Tuzo Wilson kartierte diese Zonen zerstörter metamorpher und vulkanischer Gesteine über die gesamte Nordhalbkugel — in Spitzbergen, Skandinavien, den Britischen Inseln und von Maine bis Connecticut <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=340s" title="00:05:40">(V)</a>.

Das Entscheidende: Die Iapetus-Sutur folgt ungefähr **derselben Linie, entlang der sich der moderne Atlantik öffnete** <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=359s" title="00:05:59">(V)</a>. Walcotts Fossil-Rätsel beiderseits des heutigen Atlantiks markieren Stellen, an denen Stücke der alten Kontinente bei der Öffnung auf der "falschen" Seite der Linie hängen blieben <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=370s" title="00:06:10">(V)</a>. Die Sutur ist damit der konkrete Beleg, dass sich der Atlantik als Reinkarnation des Iapetus-Ozeans entlang derselben Naht wieder öffnete — ein Paradebeispiel des [[Wilson-Zyklus]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Ikaria wutjita.md
--- BEGIN NOTE ---

# Ikaria wutjita

**Definition:** Ikaria wutjita ist ein kleines, einfaches ediacarisches Lebewesen, das zu den **ältesten bekannten Bilateriern** ([[Bilateria]]) zählt. Obwohl klein und simpel, besaß es ein **echtes Vorn und Hinten** sowie ein **gespiegeltes Links und Rechts** (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=581s" title="00:09:41">(V)</a>).

**Bedeutung für die Evolution der Symmetrie:** Der entscheidende Punkt ist die Verknüpfung mit **Bewegung** — Ikaria war unterwegs: Es schob sich durch den Schlamm und verdrängte Sediment **vor über 555 Millionen Jahren** (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=609s" title="00:10:09">(V)</a>). Damit stützt es die These, dass [[Bilaterale Symmetrie]] als Konsequenz gerichteter Bewegung entstand ([[Symmetrie als Konsequenz der Bewegung]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Innschifffahrt als militärischer Transportweg.md
--- BEGIN NOTE ---

# Innschifffahrt als militärischer Transportweg

Die **Innschifffahrt als militärischer Transportweg** bezeichnet die Nutzung des Inns für die Beförderung von Truppen, Waffen und Gefangenen in der Frühen Neuzeit. Der Fluss war die bevorzugte Alternative zum Landweg, weil er schnell, günstig und vor allem mit weniger Schaden für die Umgebung war ([[10-Raw/Inn Truppentransport.pdf#page=1|Q1]]). Flüsse dienten in der Kriegsführung zugleich als natürliches Hindernis und als Transportweg ([[10-Raw/Inn Truppentransport.pdf#page=4|Q1]]).

Die wirtschaftliche Logik begrenzte die Fahrtrichtung: Die Naufahrt (flussabwärts) war einfach und billig, die Hohenaufahrt teuer, weil Schiffe von Pferdegespannen gezogen werden mussten; Soldaten befuhren den Inn daher fast ausschließlich flussabwärts ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). So konnten Massenheere schnell verlegt werden — beim Höhepunkt der Militärtransporte 1594–1603 wurden bis zu 40.000 Soldaten befördert ([[10-Raw/Inn Truppentransport.pdf#page=11|Q1]]).

Der Transport auf dem Inn ersparte den Anwohnern Plünderungen: Das Unterinntal konnte in zwei Tagen durchquert werden ([[10-Raw/Inn Truppentransport.pdf#page=15|Q1]]). Im 18. Jahrhundert flaute der Truppentransport ab, weil sich das habsburgische Weltreich in eine spanische und eine österreichische Linie getrennt hatte und Tirol durch die Ostpolitik Maria Theresias in die Peripherie der Macht geriet ([[10-Raw/Inn Truppentransport.pdf#page=12|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/John Tuzo Wilson.md
--- BEGIN NOTE ---

# John Tuzo Wilson

**John Tuzo Wilson** war ein kanadischer Geologe, der das neufundländische Trilobiten-Rätsel in den 1940er Jahren mit der damals weitgehend abgelehnten Idee der Kontinentaldrift wieder aufgriff <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=269s" title="00:04:29">(V)</a> — anfangs selbst skeptisch <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=280s" title="00:04:40">(V)</a>.

An der Linie zwischen den "Atlantischen" und "Pazifischen" Faunen fand er zerstörte, zerquetschte metamorphe und vulkanische Gesteine — ein sicheres Zeichen einer gewaltigen Kontinentalkollision <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=282s" title="00:04:42">(V)</a>. Er kartierte die Kollisionsbelege über die gesamte Nordhalbkugel und führte sie zur [[Iapetus-Sutur]] zusammen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=340s" title="00:05:40">(V)</a>. 1966 fragte er als erster, ob der Atlantik tatsächlich geschlossen und wieder geöffnet worden sei <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=381s" title="00:06:21">(V)</a> — die Geburtsstunde des nach ihm benannten [[Wilson-Zyklus]] <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=389s" title="00:06:29">(V)</a>. Seine Lösung des Trilobiten-Rätsels half, die Theorie der [[Kontinentaldrift]] durchzusetzen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=642s" title="00:10:42">(V)</a>.

--- END NOTE ---

--- FILENAME: 40-Permanent/Junge Pfalz.md
--- BEGIN NOTE ---

# Junge Pfalz

Die **Junge Pfalz** (auch Pfalz-Neuburg) war das neue Territorium, das die beiden Enkel Herzog Georgs des Reichen, Ottheinrich und Philipp, durch den Kölner Schiedsspruch von 1505 erhielten ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]). Es war ein zersplittertes Gebiet von der oberen Donau über Franken bis zur nördlichen Oberpfalz ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]).

Als Hauptstadt des neuen Staates wurde Neuburg an der Donau gewählt; da die beiden Erben noch nicht volljährig waren, regierte dort Pfalzgraf Friedrich II. als Vormund ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]). Der spätere Pfalzgraf Ottheinrich baute Neuburg an der Donau mit gewaltigen Geldmitteln zur Residenz aus und wurde später durch Erbfolge Kurfürst der Pfalz, wo er mit dem Ottheinrichsbau des Heidelberger Schlosses zu einem der bedeutendsten Bauherren der deutschen Renaissance aufstieg ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]). Die Junge Pfalz war damit ein politischer Kompromiss: Sie entschädigte die Erbansprüche der Georgs-Enkel, ohne die Münchner Linie oder die Habsburger zu benachteiligen.

--- END NOTE ---

--- FILENAME: 40-Permanent/Kambrium-Explosion.md
--- BEGIN NOTE ---

# Kambrium-Explosion

**Definition:** Die Kambrium-Explosion vor etwa 540 Mio. Jahren war die geologisch abrupte Entfaltung fast aller größeren Tiergruppen. Im Kontext der Gehirnevolution erschien dabei **die große Mehrheit der Gruppen mit Gehirn in einem geologischen Augenblick** — und kam **bereits mit voll ausgebildeten Gehirnen** in die Welt (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=262s" title="00:04:22">(V)</a>).

**Überraschung:** Angesichts des dürftigen Fossilbelegs für Vorläufernervensysteme (siehe [[Fossile Hirne des Kambriums]]) war mit kaum Fossilbelegen für die ersten Gehirne zu rechnen (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=279s" title="00:04:39">(V)</a>) — doch der Fossilerhalt (etwa die Burgess-Schale) bewahrte sie (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=311s" title="00:05:11">(V)</a>).

**Bedeutung:** Die Gleichzeitigkeit des Erscheinens unterstützt die These, dass Gehirne **einmalig** in der frühen Tierevolution entstanden ([[Evolution des Nervensystems]]) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=446s" title="00:07:26">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Kant und die Autonomie der Bildung.md
--- BEGIN NOTE ---

# Kant und die Autonomie der Bildung

Immanuel Kant ist in der Quelle der zentrale Vertreter einer Bildungstheorie, die die Autonomie des Subjekts an die erste Stelle setzt. Die Bildung des Menschen ist für Kant nicht die Anpassung an fremde Vorschriften, sondern die Entwicklung der Fähigkeit, selbst zu denken, selbst zu urteilen und seinen Verstand ohne fremde Leitung zu gebrauchen. Die Aufklärung wird in diesem Sinn als Ausgang aus der selbstverschuldeten Unmündigkeit verstanden: Der Mensch muss die Bereitschaft entwickeln, sich seines eigenen Verstandes zu bedienen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 27|Q1]].

Kants Bildungskonzept ist an die Idee der Freiheit und der moralischen Selbstbestimmung gekoppelt. Das höchste Ziel der Bildung ist nicht bloß Wissen, sondern die Entwicklung eines autonomen, vernunftgeleiteten Handelns. Der kategorische Imperativ ist hier der Kern: Man soll so handeln, dass die Maxime des Handelns zugleich allgemeines Gesetz für vernünftige Wesen sein könnte [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 27|Q1]]. Bildung bedeutet deshalb nicht nur Kompetenzen zu erwerben, sondern die Fähigkeit, Freiheit in einer Weise zu gebrauchen, die zugleich die Freiheit anderer respektiert [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 27|Q1]].

Die Quelle zeigt, dass Kants Erziehungstheorie das pädagogische Problem der Autonomie in besonderer Schärfe thematisiert. Wie kann jemand zur Freiheit erzogen werden, wenn Erziehung selbst Zwang ausübt? Kant löst diese Spannung, indem er Erziehung als notwendigen, aber zeitlich begrenzten Eingriff in die Freiheit des Kindes versteht. Zwang ist legitim, wenn er dazu dient, den Menschen zur späteren selbstbestimmten und moralischen Handlungsfähigkeit zu führen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 28|Q1]].

Diese Einordnung wird in den vier Stufen der Erziehung konkretisiert: Disziplinierung, Kultivierung, Zivilisierung und Moralisierung. Die erste Stufe dient der Bezähmung tierischer Triebe; die zweite der Ausbildung von Fähigkeiten und Kulturtechniken; die dritte der sozialen Kompetenz; die vierte und höchste Stufe ist die Moralisierung, also die Ausbildung eines guten Willens und eines Handelns aus Pflicht und Vernunftgründen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 28|Q1]].

Dabei ist entscheidend, dass der moralische Wert einer Handlung nicht im Erfolg liegt, sondern im guten Willen, der sich am Sittengesetz orientiert. Kant betont deshalb, dass Erziehung nicht bloß „dressieren“ darf, sondern Kinder dazu anleiten muss, selbst zu denken, eigene Maximen zu prüfen und sich an den Anforderungen der Vernunft zu orientieren [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 30|Q1]]. Genau darin liegt die besondere Modernität seiner Bildungsphilosophie: Bildung wird zur Ermöglichung von Selbstdenken, moralischer Selbstbestimmung und gesellschaftlicher Mündigkeit.

--- END NOTE ---

--- FILENAME: 40-Permanent/Konglomeratgneis.md
--- BEGIN NOTE ---

# Konglomeratgneis

Der **Konglomeratgneis** des Pfitschtals ist ein metamorphes Konglomerat aus dem Perm: Die ursprünglichen Flußgerölle wurden vor ~250 Millionen Jahren abgelagert, während das Variszische Gebirge abgetragen wurde ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]), und später durch Metamorphose und plastische Deformation zu Konglomeratschiefern bzw. -gneisen umgeformt.

Der Geröllbestand (Aplite, Granite, Graphitschiefer, Marmore, vereinzelte Grüngesteine) stammt ausschließlich aus der Greiner Serie und dem Zentralgneis — **nicht von weit her**. An manchen Geröllen sind trotz Deformation noch Kanten und Ecken erhalten, die Korngröße wechselt schnell. Das sind Kennzeichen eines **„unreifen" Sediments mit kurzen Transportwegen**: Weiche Gerölle wie Kalke, Marmore oder Schiefer wären sonst längst zerstört, Kanten abgeschliffen worden ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).

Die Ablagerung erfolgte deshalb wahrscheinlich in einem **tektonischen Graben oder als großer Schuttfächer in einem ariden Gebiet** ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]). Aufwärts werden die Gerölle kleiner und verschwinden schließlich — ein Zeichen nachlassender Reliefenergie, also des Flächerwerdens der Landschaft im Lauf des Perm ([[10-Raw/Tauernfenster (Quelle).md#Seite 8|Q1]]).

Heute sind die Konglomeratgneise ein **Deformationsmessgerät**: Ihre Gerölle sind völlig plattgewalzt und in die Länge gezogen, die längste Achse taucht nach Westen ab — dokumentiert wie alle Gesteine der Region die Ost-West-Dehnung ([[10-Raw/Tauernfenster (Quelle).md#Seite 8|Q1]], [[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Kontinentaldrift.md
--- BEGIN NOTE ---

# Kontinentaldrift

Die **Kontinentaldrift** ist die Theorie, dass die Kontinente nicht immer an ihrem heutigen Ort lagen, sondern sich im Lauf der Erdgeschichte bewegt haben. Sie wurde 1912 von Alfred Wegener vorgeschlagen und basierte auf der Idee, dass Nordamerika und Europa sowie Südamerika und Afrika wie Paare von Puzzleteilen sind, die durch den Atlantik getrennt werden <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=244s" title="00:04:04">(V)</a>.

Trotz der offensichtlichen geometrischen Evidenz wurde die Theorie lange abgelehnt, weil niemand erklären konnte, wie sich die Kontinente überhaupt getrennt haben <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=262s" title="00:04:22">(V)</a>. Wichtige Unterstützung kam in den 1950er Jahren vom Mittelatlantischen Rücken: Die Entdeckung dieser Kette von Unterwasserbergen mit ständiger seismischer und vulkanischer Aktivität war ein entscheidender Beleg für die Drift <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=17s" title="00:00:17">(V)</a> — er zeigte, dass sich der Atlantik seit der Trias (vor rund 230 Millionen Jahren) von dieser Naht aus öffnet <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=34s" title="00:00:34">(V)</a>.

John Tuzo Wilson knüpfte mit seiner Deutung der neufundländischen Trilobiten-Rätsel an die abgelehnte Theorie an und trug wesentlich dazu bei, dass sie sich durchsetzte ([[Wie Trilobiten den Wilson-Zyklus aufdeckten]]) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=269s" title="00:04:29">(V)</a>. Die Kontinentaldrift wurde so zur Grundlage der modernen Plattentektonik und des [[Wilson-Zyklus]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Kölner Schiedsspruch 1505.md
--- BEGIN NOTE ---

# Kölner Schiedsspruch 1505

Der **Kölner Schiedsspruch** vom 30. Juli 1505 war der Friedensschluss, der den Landshuter Erbfolgekrieg beendete. Er erging als Schiedsentscheidung König Maximilians I. auf dem Reichstag zu Köln ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]).

Der Spruch verteilte das Erbe Herzog Georgs des Reichen neu: Die beiden Enkel Georgs, Ottheinrich und Philipp, erhielten die [[Junge Pfalz]] mit Neuburg an der Donau als Hauptstadt ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]). Das Gebiet um Kufstein, Kitzbühel und Rattenberg hatte sich Maximilian als Preis seiner Vermittlung vorbehalten; auch das Zillertal und das Mondseeland fielen an die Habsburger ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]). Die Reichsstadt Nürnberg gewann die Ämter Lauf, Hersbruck und Altdorf, der Rest von Bayern-Landshut ging an die Münchener Linie ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]). Der Schiedsspruch war damit eine territoriale Neuordnung Süddeutschlands: Beide wittelsbachischen Linien verloren, die Habsburger gewannen strategische Positionen entlang des Inns.

--- END NOTE ---

--- FILENAME: 40-Permanent/Körperachsen der Tiere.md
--- BEGIN NOTE ---

# Körperachsen der Tiere

Die drei Grundbaupläne von Tierkörpern sind **radial symmetrisch**, **bilateral symmetrisch** und **asymmetrisch** (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=14s" title="00:00:14">(V)</a>).

Die Achsen, an denen sich diese Baupläne ausrichten, werden von der Umgebung vorgegeben:

- **Gravitation** erzeugt die Oben/Unten-Achse (Dorsoventral) — Oben ist überall und verschieden von unten (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=361s" title="00:06:01">(V)</a>).
- **Gerichtete Bewegung** erzeugt die Vorn/Hinten-Achse (Anterior/Posterior) über die [[Cephalisation]] (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=375s" title="00:06:15">(V)</a>).
- **Links/Rechts** ist die übrig gebliebene Achse, die ohne Druck als [[Bilaterale Symmetrie]] zum Spiegel zurückfällt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=406s" title="00:06:46">(V)</a>).

Die embryonale Festlegung dieser Achsen läuft über [[Hox-Gene]] (vorn/hinten) und die [[Links-Rechts-Festlegung]] (links/rechts). Welcher Bauplan entsteht, hängt davon ab, aus welchen Richtungen das Tier der Welt begegnet und ob es sich gezielt fortbewegt — die Ableitung erfolgt in [[Symmetrie als Konsequenz der Bewegung]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Körperbau der Trilobiten.md
--- BEGIN NOTE ---

# Körperbau der Trilobiten

Der **Körperbau der Trilobiten** ist durch eine doppelte Dreiteilung gekennzeichnet, die der Gruppe ihren Namen gibt: Die Trilobiten („Dreilapper“) bestehen immer aus drei sagittal verlaufenden Loben — dem mittleren Spindellobus (auch Axislobus) und zwei pleuralen Loben links und rechts ([[10-Raw/Trilobiten (Quelle).md#Körperbau|Q1]]). Transversal sind sie in drei Glieder (Tagmata) geteilt: Kopfschild (Cephalon), Thorax und Schwanzschild (Pygidium) ([[10-Raw/Trilobiten (Quelle).md#Körperbau|Q1]]).

Der Spindellobus trägt auf dem Kopfschild die Glabella (Stirnlappen), die häufig aus mehreren verwachsenen Loben besteht und in Anteroglabella und Posteroglabella unterteilt wird ([[10-Raw/Trilobiten (Quelle).md#Spindellobus|Q1]]). Auf dem Thorax wird die Spindel in Spindelringe (Axialringe) gegliedert, auf dem Pygidium als Rhachis mit Rhachisringen bezeichnet; der Übergang von der Glabella zur Rhachis ist der Nackenring (Occipitalring), der bei manchen Arten einen Occipitaltuberkel trägt ([[10-Raw/Trilobiten (Quelle).md#Spindellobus|Q1]]).

Die pleuralen Loben umfassen die Freiwangen des Kopfschilds, über die sich meist die [[Facettenaugen der Trilobiten|Facettenaugen]] ziehen, sowie die Pleuren der Thoraxsegmente ([[10-Raw/Trilobiten (Quelle).md#Pleuraler Lobus|Q1]]). Auf der Unterseite des Cephalons dient das Hypostom als Teil des Mundapparats; seine Form und Positionierung (konterminant, natant oder unabhängig) sind wesentliche Merkmale der systematischen Einteilung ([[10-Raw/Trilobiten (Quelle).md#Kopfschild (Cephalon)|Q1]]).

Die Trilobiten besaßen nur ein Paar spezialisierte Kopfanhänge — lange Gliederantennen als Sinnesorgane; nur bei den Agnostida waren sie kürzer und stark beborstet ([[10-Raw/Trilobiten (Quelle).md#Kopfschild (Cephalon)|Q1]]). Die übrigen Gliedmaßen waren zweiästige [[Verwandtschaft der Trilobiten|Spaltbeine]]: ein Schwimm-/Kiemenbein (Exopodit) für die Fortbewegung im Wasser und ein Laufbein (Endopodit) für das Gehen auf dem Meeresgrund ([[10-Raw/Trilobiten (Quelle).md#Spaltbeine|Q1]]). Der Thorax besteht aus systematisch relevanter Anzahl an Segmenten — zwei bis drei bei den Agnostida, bis zu 18 bei größeren Arten —, die je nach Lebensweise Stacheln (Fraßschutz) oder Krümmungen (grabende Tätigkeit) tragen können ([[10-Raw/Trilobiten (Quelle).md#Thorax|Q1]]).

Die [[Gesichtsnaht und Häutung der Trilobiten|Gesichtsnaht]] im Cephalon ist eine Sollbruchstelle, die den Kopfschild bei der Häutung in Cranidium und Librigenae zerfallen lässt ([[10-Raw/Trilobiten (Quelle).md#Gesichtsnaht|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Laterale Extrusion der Ostalpen.md
--- BEGIN NOTE ---

# Laterale Extrusion der Ostalpen

Die **laterale Extrusion der Ostalpen** ist das seitliche (östliche) Ausweichen von Teilen des Orogens, das als Reaktion auf die Indentation der Adriatischen Platte von Süden und das Zurückrollen der Karpaten-Subduktionszone nach Osten erfolgte ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).

Östlich der Judicarie-Störung drang die Adriatische Platte ~60 km nach Norden tief in den Deckenstapel ein (Adriatischer Indenter). Ein Teil des Orogens entwich daraufhin nach Osten — erleichtert durch **konjugierte Störungen**: die sinistrale Salzach-Ennstal-Mariazell-Puchberg-Störung (SEMP) und die dextralen Pusteria- und Mölltal-Störungen ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).

Zusammen mit den N-S-verlaufenden Extensionostörungen ([[Brenner-Normalverwerfung|Brenner- und Katschberg-Normalverwerfung]]) dokumentiert die laterale Extrusion die **O-W-Extension parallel zur N-S-Kompression** in den Ostalpen — sie war mitverantwortlich für die Verschuppung im [[Tauernfenster]] und schließlich dessen Exhumation ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).

Verwandte Konzepte: [[Tauernfenster]], [[Brenner-Normalverwerfung]], [[Slab Breakoff und Exhumation]]

## Einfach erklärt

*Laterale Extrusion* bedeutet: Teile des Alpenorogens wurden seitwärts (nach Osten) hinausgequetscht, anstatt an Ort und Stelle weiter zusammengestaucht zu werden. Das passiert, wenn von Süden die darunterliegende Adriatische Platte wie ein Keil (Adriatischer Indenter) nach Norden stößt, während im Osten gleichzeitig durch das Zurückrollen der Karpaten-Subduktion "freier Raum" entsteht. Das Gebirge verhält sich dann wie eine Tüte mit zäher Masse, die man von zwei Seiten zusammendrückt und auf der einen Seite eine Öffnung lässt: Die Masse entweicht seitlich.

Im Gestein bleibt diese Bewegung als zwei Familien gegensätzlich verschiebender Störungen erhalten — *konjugierte* Blattverschiebungen, ähnlich wie die Scherlinien in einem Einachs-Kompressionsversuch (X- bzw. N-förmige Verwerfungsmuster, die man in der Materialmechanik als Fließstrukturen kennt). Die involvierten Störungen werden im Paper namentlich genannt (Salzach-Ennstal-Störung, Pusteria-, Mölltal-Störung), die zuletzt genannten Unterbrechungen der *N-S-Kompression* sind dabei nur die eine Hälfte der Geschichte: Die O-W-Extension (insbesondere an der [[Brenner-Normalverwerfung]]) ist die komplementäre Dehnungskomponente im selben Verformungsfeld.

--- END NOTE ---

--- FILENAME: 40-Permanent/Lebensweise der Trilobiten.md
--- BEGIN NOTE ---

# Lebensweise der Trilobiten

Die **Lebensweise der Trilobiten** war in der Regel die von Bewohnern des Meeresbodens (Benthos): Die meisten Fossilien stammen aus küstennahen (litoralen) Habitaten und Schelfgebieten mittlerer Meerestiefe; Tiefseeformen existierten offensichtlich nicht ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]). Schwimmende (pelagiale) Trilobiten erscheinen hingegen hoch wahrscheinlich — einige ordovizische Formen mit stromlinienförmigen Körpern könnten schnelle, aktive Schwimmer gewesen sein ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]). Einige Arten lebten in sauerstoffarmen, schlammigen Sedimenten, wenige konnten offenbar Tunnel in das Sediment graben ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]).

Auch die Ernährung war vielfältig ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]):

- **Räuber und/oder Aasfresser**: vermutlich die ursprüngliche und häufigste Lebensweise ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]).
- **Detritus-/Sedimentfresser** und **Filtrierer**: abgeleitete Formen, deren Morphologie auf diese Ernährungsweise hindeutet ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]).
- **Weidegänger**: einige Arten weideten Mikrobenmatten und anderen Aufwuchs vom Meeresboden ab ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]).

Die Trilobiten standen selbst auf der Speisekarte: Aus dem mittleren Kambrium liegt der Fund eines Arthropoden einer ausgestorbenen Linie (vermutlich ein basaler Vertreter der Chelicerata) vor, dessen Darminhalt aus zahlreichen Trilobiten bestand — ein direkter Beleg für [[Trilobiten|Prädation auf Trilobiten]] im Kambrium ([[10-Raw/Trilobiten (Quelle).md#Lebensweise|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Links-Rechts-Festlegung.md
--- BEGIN NOTE ---

# Links-Rechts-Festlegung

Die Links-Rechts-Differenzierung ist die **kniffligste Achse**: Der wachsende Embryo muss seine eigene blobby Symmetrie bewusst brechen, sich für eine Seite als "links" entscheiden und das Ganze dennoch als makellosen Spiegel erhalten (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>).

**Molekularer Mechanismus (beim Hühnerembryo):** Eine kleine Gruppe von Signalmolekülen — **SHH, Nodal und Activin** — steuert die Entscheidung (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>). Der Schlüsselmove: **Nodal** schaltet das Gen **Pitx2** nur auf der **linken** Seite an (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>).

**Ausführung:** Pitx2 leuchtet in einem Gewebeblatt namens *linkes laterales Plattenmesoderm* auf und überträgt den abstrakten Befehl "das ist links" in die tatsächliche Körperanlage (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>). Die Differenzierung erfolgt **nicht-arbiträr** — es gibt also eine echte linke Seite, kein Zufall (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=161s" title="00:02:41">(V)</a>).

**Ursache des Startimpulses:** Woher der Embryo weiß, was links ist, liefern die [[Nodal-Cilien]] (Richtung der Strömung). Fällt dieser Mechanismus aus, wird die Links/Rechts-Wahl [[Situs inversus|spiegelverkehrt oder/randomisiert]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Maximilians Gebietsgewinne im Landshuter Erbfolgekrieg.md
--- BEGIN NOTE ---

# Maximilians Gebietsgewinne im Landshuter Erbfolgekrieg

Die **Gebietsgewinne Maximilians I. im Landshuter Erbfolgekrieg** bezeichnen die territorialen Zugewinne der Habsburger aus dem Konflikt von 1504/05. Maximilian hatte sich als Preis seiner Vermittlung das Gebiet um Kufstein, Kitzbühel und Rattenberg vorbehalten; auch das Zillertal und das Mondseeland gingen von Bayern an die Habsburger verloren ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]).

Der Weg zu diesen Gewinnen führte über den Krieg: Nach der pfälzischen Einnahme Kufsteins am 9. August 1504 eroberte Maximilian die Stadt zurück, worauf sich Rattenberg, Schwaz, das Ziller- und Brixental, Traunstein, Kitzbühel und Reichenhall ergaben ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Kriegsverlauf|Q1]]). Der Kölner Schiedsspruch von 1505 machte die territoriale Neuordnung rechtsverbindlich ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]). Die Gewinne verankerten die Habsburger entlang des Inns und banden das Unterinntal dauerhaft an Tirol — die Grundlage für die spätere Rolle des Inns als [[Innschifffahrt als militärischer Transportweg|militärischer Transportweg]] der Habsburger ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Ergebnisse|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Maximilians Selbstinszenierung.md
--- BEGIN NOTE ---

# Maximilians Selbstinszenierung

Die **Selbstinszenierung Maximilians I.** war die bewusste, nahezu modern anmutende Konstruktion des eigenen Bildes als "letzter Ritter" — als Wahrer ritterlicher Ideale und zugleich als Renaissancefürst ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]).

Ihre Medien waren vielfältig: Maximilian nutzte als erster Herrscher den Holzschnitt für Propagandazwecke, ließ die monumentale Ehrenpforte und den *Triumphzug* als großflächige Druckwerke vervielfältigen und beteiligte sich selbst an der Konzeption ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]). Seine autobiografischen Dichtungen *Theuerdank*, *Weißkunig* und *Freydal* sind verschlüsselte Autobiografien, die neben realen Ereignissen auch unausgeführte Pläne des Kaisers festhielten und an seiner eigenen Legende strickten ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]).

Die Strategie war legitimatorisch: Die genealogischen Stammbäume bis zu antiken und biblischen Wurzeln sollten die Herrschaft der Habsburger im Wettstreit mit konkurrierenden Adelsgeschlechtern belegen, und die Wahl des Heiligen Georg zum Schutzpatron spiegelte die ritterlichen Tugenden ([[10-Raw/Maximilian I. (HRR).md#Feudaler Ritter und Renaissance-Fürst|Q1]]). Die Inszenierung diente zugleich der Überdeckung der eigenen Finanznot — vgl. die [[Schulden Maximilians I.|Schulden bei Jakob Fugger]].

Verwandte Konzepte: [[Erwählter Römischer Kaiser]], [[Collegium poetarum et mathematicorum]], [[Schulden Maximilians I.]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Mediatisierung als Metaprozess.md
--- BEGIN NOTE ---

# Mediatisierung als Metaprozess

> Mediatisierung wird als langfristiger gesellschaftlicher Wandel verstanden, der Kommunikation und Kultur transformiert. Die Quelle argumentiert, dass Medien nicht nur Mittel sind, sondern soziale Wirklichkeit mitgestalten – eine Herausforderung für Bildung, die diese Veränderungen reflektieren muss.

# Mediatisierung als Metaprozess
Die Quelle verwendet den Begriff des Metaprozesses, um die langfristige und tiefgreifende Wirksamkeit von Mediatisierung zu fassen. Dabei geht es nicht um einzelne Medienereignisse oder einzelne Kommunikationsakte, sondern um die langdauernden Veränderungen, die sich aus der fortschreitenden Ausbreitung und Ausdifferenzierung von Kommunikation ergeben [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=12|Q1]]. Mediatisierung ist deshalb kein isoliertes Phänomen, sondern ein übergreifender Prozess, der Gesellschaft, Kultur und Alltag in ihrer Kommunikationsstruktur verändert [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=12|Q2]].

Die theoretische Pointe ist, dass Kommunikation und Gesellschaft nicht getrennt gedacht werden können. Medien verändern nicht nur die Art, wie Menschen sich austauschen, sondern auch die Bedingungen, unter denen Wirklichkeit überhaupt hergestellt wird. Krotz beschreibt dies im Sinne eines wechselseitigen Verhältnisses von Gesellschaft und Kommunikation: Medien ermöglichen neue Kommunikationsbedingungen und werden zugleich durch soziale Strukturen mitgestaltet [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=11|Q3]]. Die Folge ist, dass Mediatisierung als ein übergreifender gesellschaftlicher Wandel begriffen werden muss, der einzelne Entwicklungen wie Vernetzung, Mobilität oder digitale Teilhabe in einen gemeinsamen Rahmen stellt [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=12|Q4]].

Im Bildungszusammenhang ist dieser Punkt wichtig, weil er zeigt, dass Medien nicht einfach nur Lernmittel sind, sondern die Rahmenbedingungen des Lernens mitformen. Die Quelle setzt daher die Verbindung zwischen Mediatisierung und Bildung ausdrücklich an der Stelle an, an der gesellschaftliche Kommunikationsformen und digitale Strukturen die Lebenswelt des Lernenden umformen [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=16|Q5]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Mediatisierung und Digitalisierung.md
--- BEGIN NOTE ---

# Mediatisierung und Digitalisierung

> Die Quelle unterscheidet zwischen Digitalisierung (technische Infrastruktur) und Mediatisierung (gesellschaftliche Durchdringung durch Medien). Sie zeigt, dass Medien nicht nur Werkzeuge sind, sondern soziale Strukturen prägen, was neue Formen der Kommunikation und des Lernens erfordert. Bildung muss diese mediatisierte Lebenswelt reflektieren.

# Mediatisierung und Digitalisierung
Die Quelle macht eine wichtige Unterscheidung: Digitalisierung und Mediatisierung sind eng miteinander verbunden, aber sie bezeichnen keine identischen Prozesse. Digitalisierung meint die technische und infrastrukturelle Ausbreitung digitaler Kommunikationssysteme, Datenstrukturen und Medienlogiken. Mediatisierung beschreibt dagegen die gesellschaftliche Durchdringung sozialer Wirklichkeit durch Medien, also die Weise, in der Medien Alltag, Wahrnehmung, Beziehungen und Wissen mitformen [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=9|Q1]].

Die Kernidee ist, dass Medien nicht bloß Mittel sind, sondern soziale Strukturen mitprägen. Dadurch entstehen neue Formen der Wahrnehmung, der Kommunikation und des Lernens. Digitale Technologien leisten nicht nur technische Funktionen, sondern verändern die Bedingungen, unter denen Menschen sich orientieren, Wissen erwerben und handeln [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=9|Q2]]. Im Bildungsbereich bedeutet das: Lernen verläuft nicht außerhalb, sondern in einer mediatisierten Lebenswelt. Plattformen, alltagsnahe Medienpraktiken und digitale Infrastrukturen organisieren Lernprozesse mit, auch wenn sie nicht allein Bildungsräume erzeugen [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=10|Q3]].

Für die Bildungswissenschaft ist diese Unterscheidung bedeutsam, weil sie zeigt, dass mediale und technische Bedingungen der Bildung ernst genommen werden müssen. Eine Bildungstheorie, die nur auf institutionelle Wissensvermittlung schaut, verkennt, dass Lernprozesse in der Gegenwart über Familien, Peer-Gruppen, Plattformen und mobile Medien laufen. Wer die digitale Gesellschaft verstehen will, muss deshalb auch das Verhältnis von Medienlogik und Bildungslogik verstehen [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=10|Q4]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Metamorphe Schieferhülle (Tauernfenster).md
--- BEGIN NOTE ---

# Metamorphe Schieferhülle (Tauernfenster)

Die **metamorphe Schieferhülle** ist die Gesteinseinheit, aus der der Großteil des Schmirntals aufgebaut ist; sie entspricht der **Glockner-Decke** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Vorherrschend sind **Kalkglimmerschiefer**, **Phyllite** und **Tonschiefer** — Gesteine, die durch die [[Alpine Metamorphose]] bei hohem Druck und hoher Temperatur in 35–40 km Krustentiefe umgewandelt wurden ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

Der hohe Glimmeranteil macht die Schiefer mechanisch schwach: Sie sind weich, verwitterungsanfällig und besitzen eine geringe Festigkeit ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Diese Eigenschaft ist die geologische Grundlage der massiven Hangbewegungen im Tal, insbesondere der [[Reissenschuh-Rutschung]] ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

Inmitten der weichen Schiefer liegen kompetente, harte Gesteinsinseln — darunter der mesozoische **Hochstegen-Marmor**, der für die Dynamik am Reissenschuh entscheidend ist ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Die Schieferhülle ist Teil der Einheiten, die durch die Exhumation des [[Tauernfenster|Tauernfensters]] (u.a. entlang der [[Brenner-Normalverwerfung]]) an die Oberfläche kamen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

Im Pfitschtal gliedert sich die Schieferhülle in eine **Obere** und eine **Untere** Einheit: Die schwärzlich-grauen oder bräunlichen **Kalkglimmerschiefer** am Brenner und im Pfitschtal sind Reste des Penninischen Ozeans (**Obere Schieferhülle**) ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q2]]). Die **Greiner Schiefer (Untere Schieferhülle)** dagegen sind das „Alte Dach", in das die Zentralgneise vor ~300 Millionen Jahren eindrangen; neben Schwarzschiefern dominieren **Grüngesteine** (Amphibolite, Hornblendegneise und -garbenschiefer, Serpentinite), die von Basalten und Peridotiten abstammen und auf paläozoische Inselbögen und Randmeere zurückgehen ([[10-Raw/Tauernfenster (Quelle).md#Seite 1|Q2]]). Der **Hochstegen-Marmor** ist dort ein ehemaliger Kalkstein des oberen Jura (Malm) und bildet als hellgrauer Kalkmarmor den Gipfel des Wolfendorns (2776 m) ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q2]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Mittelalter und Renaissance.md
--- BEGIN NOTE ---

# Mittelalter und Renaissance

> Die Quelle kontrastiert mittelalterliche Bildung (theokratisch, gottgegeben) mit renaissancehafter Selbstermächtigung. Während im Mittelalter Bildung als Annäherung an göttliche Ordnung galt, wird sie in der Renaissance zum Werkzeug individueller und kultureller Selbstgestaltung – ein Schlüsselübergang zur modernen Bildungstheorie.

# Mittelalter und Renaissance
Der Studienbrief zeigt, dass der Bildungsbegriff im Mittelalter über eine starke theologische Ausrichtung bestimmt war. Bildung wurde nicht primär als Erkenntnisgewinn oder Selbstbildung verstanden, sondern als Annäherung an eine gedachte Gottesebenbildlichkeit. Menschliche Bildung war damit in ein transzendentales Ordnungssystem eingebunden, in dem die Welt im Sinne eines göttlich gesetzten Ganzen verstanden wurde [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 16|Q1]]. Diese Perspektive impliziert eine enge Verbindung von Religion, Dogma und Bildung: Die Entfaltung des Menschen war nicht Selbstzweck, sondern Teil eines größeren, von Gott gesetzten Sinnzusammenhangs [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 16|Q1]].

Die Autor:innen betonen zugleich, dass der mittelalterliche Bildungsbegriff nicht rein konservativ war, sondern durch mystische, asketische und theologische Traditionen ergänzt wurde. Die mystische Tradition des Mittelalters etwa beschreibt Bildung als Über-sich-Hinausgehen und als die Fähigkeit, sich aus dem weltlichen Bezug zu lösen und in ein neues, höheres Sein überzugehen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 16|Q1]]. Bildung wird hier also nicht als sinnlich-politische Selbstverwirklichung, sondern als transzendente Selbsttranszendenz verstanden.

Mit der Renaissance verschiebt sich dieser Horizont grundlegend. Die Quelle beschreibt die Renaissance als Epoche, in der die alte mittelalterliche Ordnung aufbricht und der Mensch zunehmend als Subjekt eigener Selbstgestaltung verstanden wird. Dabei ist die Renaissance nicht nur religiös, sondern zugleich wissenschaftlich, künstlerisch und gesellschaftlich geprägt; sie ist Ausdruck einer neuen Selbst- und Weltstellung des Menschen, der sich aus vorgegebenen Bindungen löst und einen eigenständigen Ort im Kosmos beansprucht [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 17|Q1]].

Die neue Haltung lässt sich mit der Formel des Menschen als „Werk seiner selbst“ zusammenfassen: Der Mensch wird nicht länger nur als Teil einer vorgegebenen Ordnung verstanden, sondern als Akteur, der Freiheit, Willen, Individualität und Gestaltungskraft besitzt. Diese Entwicklung verbindet sich mit dem Humanismus, der Sprache, Bildung und Wissenschaft als zentrale Formen der Selbstbildung wertschätzt und in der Wiederbelebung der Antike einen neuen Maßstab für Menschenbildung erkennt [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 17|Q1]].

Die Folge ist eine neue bildungstheoretische Spannung: Zwischen mittelalterlicher Theokratie und neuzeitlicher Selbstermächtigung entsteht ein Bildungsverständnis, das Individualität und Autonomie ernst nimmt, aber noch nicht völlig von religiösen und historischen Traditionen emanzipiert ist. Genau hier liegt der Übergang zur Aufklärung: Die Renaissance bereitet den Boden für ein weltliches Bildungsverständnis, dessen zentrale Merkmale Mündigkeit, Selbstdenken und Selbstbestimmung werden [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 20|Q1]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Molekulare Uhr.md
--- BEGIN NOTE ---

# Molekulare Uhr

**Definition:** Die molekulare Uhr ist eine Methode, mit der Forschende mithilfe der **Gene heutiger Organismen** in Kombination mit einer **vorhersagbaren Mutationsrate** evolutionäre Ursprünge rekonstruieren (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=177s" title="00:02:57">(V)</a>).

**Einsatzfall:** So wurde auf die Entstehung der ersten Nervensysteme im **Ediacarium (≈625 Mio. Jahre)** geschlossen (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=189s" title="00:03:09">(V)</a>).

**Grenze:** Die molekulare Uhr und der Fossilbericht **klaffen im Ediacarium auseinander** — sie sagt relativ fortgeschrittene Cnidarier-Vorfahren voraus, doch Fossilbelege fehlen weitgehend (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=212s" title="00:03:32">(V)</a>). Deshalb liest sich die frühe Nervensystemevolution ([[Ursprung der Nervensysteme]]) über beide Datenguellen.

--- END NOTE ---

--- FILENAME: 40-Permanent/Molybdänbergwerk Alpeiner Scharte.md
--- BEGIN NOTE ---

# Molybdänbergwerk Alpeiner Scharte

Das **Molybdänbergwerk an der Alpeiner Scharte** (2.800 m) im Schmirntal ist ein Relikt nationalsozialistischer Rüstungswirtschaft im Hochgebirge ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]).

**Molybdän** war im Zweiten Weltkrieg kriegswichtig: Das seltene Metall dient dazu, Stahl für Panzer und Kanonen zu härten ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]). Zwischen **1941 und 1945** mussten hier **Kriegsgefangene unter menschenunwürdigen Bedingungen** Zwangsarbeit leisten ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]). Das Lager war das **höchstgelegene Bergwerk Europas** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]).

Im Jahr **1944** forderte ein schweres **Lawinenunglück** zahlreiche Todesopfer unter den Arbeitern ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]). Heute zeugen nur noch Ruinen und die Überlieferung von diesem Leid — sie mahnen, das Erbe der Berge mit Respekt zu behandeln ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]). Der Ort ist ein dunkles Gegenstück zur positiven Zukunftserzählung des [[Bergsteigerdorf|Bergsteigerdorfs]]: Derselbe Hochgebirgsraum, der heute für sanften Tourismus steht, war während des Zweiten Weltkriegs Schauplatz rüstungswirtschaftlicher Ausbeutung.

--- END NOTE ---

--- FILENAME: 40-Permanent/Monitoring gravitativer Hangdeformationen.md
--- BEGIN NOTE ---

# Monitoring gravitativer Hangdeformationen

Das **Monitoring gravitativer Hangdeformationen** kombiniert mehrere Messverfahren, um langsame Hangbewegungen wie die [[Reissenschuh-Rutschung]] quantitativ zu erfassen und Gefahren einzuschätzen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

- **Terrestrisches Laserscanning (TLS):** Hochleistungs-Scanner wie der **Riegl VZ-6000** erzeugen digitale Punktwolken der Erdoberfläche; damit lassen sich Veränderungen der Geländestruktur — etwa das Aufreißen neuer Spalten — im **Millimeterbereich** erfassen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).
- **DGNSS-Messungen:** GPS-Empfänger an markanten Felsblöcken im Rutschgebiet werden mit einer festen Basisstation abgeglichen (Differential Global Navigation Satellite System); daraus berechnen sich exakte **dreidimensionale Verschiebungsvektoren** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Die Punktmessungen ermöglichen die kontinuierliche Überwachung spezifischer Felspunkte und die präzise zeitliche Einordnung der Bewegungsvektoren ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q2]]).
- **Historische Luftbildauswertung ([[EMOD-SLAP]]):** Durch digitale Auswertung von Luftbildern, die bis ins Jahr **1954** zurückreichen, lässt sich die Bewegungsgeschichte des Hangs über sieben Jahrzehnte rekonstruieren ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Die photogrammetrische Auswertung generiert 3D-Punktwolken der Topographie vergangener Jahrzehnte und verlängert damit die terrestrischen Messkampagnen (2016–2019) deutlich in die Vergangenheit ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q2]]).
- **KI-gestütztes Nowcasting:** Aktuelle Forschungsprojekte koppeln Bodenmodelle mit Wetterdaten; Ziel ist, Beschleunigungen des Hangs (z.B. nach Starkregen) in Echtzeit vorherzusagen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

Die Verfahren ergänzen sich: TLS und DGNSS liefern den Ist-Zustand mit hoher räumlicher bzw. punktueller Genauigkeit, die Luftbildauswertung den langfristigen Trend, und das KI-Nowcasting überträgt das Modell in die nahe Zukunft ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Multituberculata.md
--- BEGIN NOTE ---

# Multituberculata

**Definition:** Die Multituberculata sind eine Säugetiergruppe, die vor rund **165 Mio. Jahren** erstmals im Fossilbericht erschien und bis vor etwa **56 Mio. Jahren** **extrem häufig** war — bis moderne Säugetiergruppen evolvierten und sie zu verdrängen begannen (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=41s" title="00:00:20">(V)</a>).

**Der Montana-Fund:** In den späten 1960ern entdeckte man in den Fußhügeln Südwest-Montanas ein Multituberculaten-Fossil in Gestein, das **17 Mio. Jahre nach ihrem vermeintlichen Aussterben** datierte (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=33s" title="00:00:33">(V)</a>) — und das aus den **Fußhügeln** statt aus den üblichen Tieflandbecken (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=39s" title="00:00:39">(V)</a>). Dieser Anomalie-Fund lenkte die Paläontologen zu den Bergen und damit zu den eozänen Primaten (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=46s" title="00:00:46">(V)</a>).

**Bedeutung:** Das Beispiel illustriert, wie [[Refugia]] und [[Gebirge als Motoren der Biodiversität|gebirgsbedingte Habitatvielfalt]] das Bild des "Aussterbens" verzerren können — eine Gruppe kann in zurückgebliebenen Hochlagen-Pocketz überleben (ergänzend zu [[Eozäne Primaten Nordamerikas]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Nervensystem.md
--- BEGIN NOTE ---

# Nervensystem

**Definition:** Ein Nervensystem besteht aus Zellen, den **Neuronen** ([[Neuronen-Netz]]), die **elektrische Signale leiten** und Informationen durch den Körper tragen (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=125s" title="00:02:05">(V)</a>). Es verbindet Zellen, Gewebe und Organe, die etwas **wahrnehmen** können, mit solchen, die **reagieren** können (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=125s" title="00:02:05">(V)</a>).

**Gehirn-Vorstufe:** Vor einem [[Gehirn als zentraler Verarbeitungshub|Gehirn]] braucht es zuerst ein Nervensystem — das Gehirn ist eine zentralisierte Ausprägung davon (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=138s" title="00:02:18">(V)</a>).

**Typen:** Vertebraten, Arthropoden, Mollusken und Würmer haben ein zentralisiertes Nervensystem; Cnidarier ein distribuiertes neuronales Netz ohne Gehirn; Schwämme offenbar gar keines (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=150s" title="00:02:30">(V)</a>). Die evolutionäre Entstehung ist unter [[Ursprung der Nervensysteme]] dokumentiert.

--- END NOTE ---

--- FILENAME: 40-Permanent/Neuronen-Netz.md
--- BEGIN NOTE ---

# Neuronen-Netz

**Definition:** Neue [[Nervensystem|Nervensysteme]] bestehen aus Zellen namens **Neuronen**, die elektrische Signale leiten und Informationen durch den Körper tragen (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=125s" title="00:02:05">(V)</a>).

**Vernetzung:** Jedes Neuron kann sich mit vielen anderen verbinden und so ein Netz bilden, das Zellen, Gewebe und Organe, die etwas wahrnehmen, mit solchen verbindet, die reagieren können (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=125s" title="00:02:05">(V)</a>).

**Bedeutung:** Das gebündelte Neuronen-Netz — ein **Knoten aus Nervengewebe** — ist das [[Gehirn als zentraler Verarbeitungshub|Gehirn]], das die komplexen Körpersignale zentral verarbeitet (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=615s" title="00:10:15">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Nodal-Cilien.md
--- BEGIN NOTE ---

# Nodal-Cilien

**Definition:** Bei vielen Wirbeltieren (vermutlich auch beim Menschen) gibt es einen Fleck winziger, **nach hinten zum Embryo-Rückens geneigter** Härchen, die **Nodal-Cilien**. Sie drehen sich und treiben **Flüssigkeit in einer gleichbleibenden Richtung** über den Embryo (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=202s" title="00:03:22">(V)</a>).

**Funktion:** Die Richtung dieser Strömung ist der eigentliche Tiebreaker — sie setzt fest, welche Seite des Embryos **links** wird (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=202s" title="00:03:22">(V)</a>). Damit liefern die Nodal-Cilien den Startimpuls für die [[Links-Rechts-Festlegung]].

**Beleg:** Mäuse ohne diese Nodal-Cilien weisen eine **randomisierte** Links/Rechts-Festlegung auf (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=202s" title="00:03:22">(V)</a>). Fällt die Strömung aus, kann sich als Folge auch [[Situs inversus]] (Spiegel-Lage der Organe) ergeben (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=234s" title="00:03:54">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Omomyoiden.md
--- BEGIN NOTE ---

# Omomyoiden

**Definition:** Die Omomyoiden sind eine der beiden Gruppen der [[Eozäne Primaten Nordamerikas|eozänen Primaten]] Nordamerikas — klein, tarsier- bzw. spitzmausartig und **extrem vielfältig** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=115s" title="00:01:55">(V)</a>). Sie spezialisierten sich auf **Insekten, kleine Wirbeltiere, Früchte und Samen** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=115s" title="00:01:55">(V)</a>).

**Verbreitung:** Allein in Nordamerika gab es zwischen 55 und 36 Millionen Jahren **fast 40 Gattungen** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=126s" title="00:02:06">(V)</a>), die sich in zwei Untergruppen gliederten ([[Anaptomorphine und Omomyine]]) (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=126s" title="00:02:06">(V)</a>).

**Bedeutung:** Weil Omomyoiden-Funde zunächst nur aus tiefliegenden Becken stammten, entstand die (falsche) Erzählung, die Omomyinen verdrängten die Anaptomorphinen überall — bis Hochlagenfunde [[Refugia]] und [[Gebirge als Motoren der Biodiversität|Gebirgsdiversität]] offenbarten.

--- END NOTE ---

--- FILENAME: 40-Permanent/Ordnungen der Trilobiten.md
--- BEGIN NOTE ---

# Ordnungen der Trilobiten

Die ausgestorbene Klasse Trilobita umfasst gegenwärtig **neun anerkannte Ordnungen** ([[10-Raw/Trilobiten (Quelle).md|Q1]]):

- **Agnostida**: sehr kleine, oft nur wenige Millimeter lange Trilobiten; Unteres Kambrium bis Oberes Ordovizium ([[10-Raw/Trilobiten (Quelle).md#Ordnungen|Q1]]).
- **Redlichiida**: sehr alte Trilobiten mit vielen, in Pleuralstacheln auslaufenden Thoraxsegmenten; Unteres bis Mittleres Kambrium ([[10-Raw/Trilobiten (Quelle).md#Ordnungen|Q1]]).
- **Corynexochida**: verlängerte Glabella, oft mit konkav laufenden Seiten und gut ausgeprägten Augen; Unteres Kambrium bis Mittleres Devon ([[10-Raw/Trilobiten (Quelle).md#Ordnungen|Q1]]).
- **Lichida**: zumeist stachelige Trilobiten; Kambrium bis Devon ([[10-Raw/Trilobiten (Quelle).md#Ordnungen|Q1]]).
- **Phacopida**: vielfältige Gruppe mit zahlreichen Erscheinungsformen; Unteres Ordovizium bis Oberes Devon ([[10-Raw/Trilobiten (Quelle).md#Ordnungen|Q1]]).
- **Proetida**: meist recht kleine Formen; Ordovizium bis Perm ([[10-Raw/Trilobiten (Quelle).md#Ordnungen|Q1]]).
- **Asaphida**: vielfältige Gruppe; Mittleres/Oberes Kambrium bis Oberes Ordovizium/Unteres Silur ([[10-Raw/Trilobiten (Quelle).md#Ordnungen|Q1]]).
- **Harpetida**: Haupterkennungsmerkmal ist ein extrem großer Cephalonsaum; Oberes Kambrium bis spätes Devon ([[10-Raw/Trilobiten (Quelle).md#Ordnungen|Q1]]).
- **Ptychopariida**: große Gruppe mit unausgereifter Klassifizierung; Unteres Kambrium bis Oberes Ordovizium ([[10-Raw/Trilobiten (Quelle).md#Ordnungen|Q1]]).

Mit über 150 Familien, über 5000 Gattungen und mehr als 15.000 beschriebenen Arten machen diese Ordnungen die [[Trilobiten]] zur divergentesten Gruppe aller ausgestorbenen Lebewesen ([[10-Raw/Trilobiten (Quelle).md|Q1]]). Die Ordnungen unterscheiden sich vor allem im [[Körperbau der Trilobiten|Körperbau]] — Segmentzahl des Thorax, Glabellaform, Stachelbildung und Augenausprägung —, was ihre systematische Abgrenzung und ihre Nutzung als [[Trilobiten als biostratigraphisches Werkzeug|Leitfossilien]] ermöglicht ([[10-Raw/Trilobiten (Quelle).md#Ordnungen|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Ordovizium-Silur-Extinktion.md
--- BEGIN NOTE ---

# Ordovizium-Silur-Extinktion

Die **Ordovizium-Silur-Extinktion** ist ein Massenaussterben vor etwa 445 Millionen Jahren, das rund 25 % aller taxonomischen Familien im Meer auslöschte — darunter etwa die Hälfte der Trilobiten-Familien <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=205s" title="00:03:25">(V)</a>.

Ursache war ein zweifacher klimatischer Schlag <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=199s" title="00:03:19">(V)</a>. Erstens veränderte eine dramatische Abkühlung die Meeresströmungen und unterbrach die Versorgung mit warmwasserliebenden Nahrungsquellen wie Algen. Zweitens band eine Vereisung große Mengen Wasser und senkte den Meeresspiegel drastisch, wodurch Flachwasserlebensräume verschwanden <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=205s" title="00:03:25">(V)</a>.

Diese Kombination aus Nahrungs- und Lebensraumverlust traf die [[Trilobiten]] hart. Überlebt hatten vor allem Familien, die an kühlere Meere angepasst waren, wie Dalmanites <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=235s" title="00:03:55">(V)</a>. Das Ereignis zeigt, dass schon allein klimatischer Wandel ohne Beteiligung von Räubern ganze Tiergruppen an den Rand der Ausrottung bringen kann <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=205s" title="00:03:25">(V)</a>.

--- END NOTE ---

--- FILENAME: 40-Permanent/Paideia.md
--- BEGIN NOTE ---

# Paideia

> Der antike Begriff „Paideia“ beschreibt Bildung als Vervollkommnung der Seele durch Erkenntnis und Wahrheitssuche. Im Gegensatz zu modernen Kompetenzmodellen geht es um eine ganzheitliche Transformation des Selbst- und Weltverhältnisses – ein Grundgedanke, der bis heute bildungstheoretisch relevant bleibt.

# Paideia
Der Studienbrief verwendet den antiken Begriff Paideia als zentrale Bezeichnung für Bildung im griechischen Denken. Paideia meint hier nicht bloß Wissenserwerb oder formale Ausbildung, sondern die Vervollkommnung der menschlichen Seele im Rahmen eines guten und verantworteten Lebens [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 10|Q1]].

Im platonischen Sinne wird Bildung als ein Prozess verstanden, in dem der Mensch sich aus der Scheinwelt der wahrnehmbaren Dinge zu einer Welt der Ideen und der Wahrheit erhebt. Das Denken wird dabei zur Grundlage einer Umwendung des Blicks: Der Mensch erkennt, dass sein Verhältnis zu sich selbst, anderen und der Welt verändert werden muss [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 10|Q1]]. Diese Grundidee steht in enger Beziehung zu [[Bildung als Deutungsmuster]], [[Bildung als Subjektkonstitution]] und [[Bildung im Wandel]], weil sie den Bildungsbegriff als Selbstverhältnis und Weltbezug begreift.

In dieser Perspektive ist Paideia mehr als ein Bildungsziel; sie ist eine zentrale Form der menschlichen Selbstveränderung. Die Quelle zeigt damit, dass der antike Bildungsbegriff schon früh eine Verbindung von Erkenntnis, Selbstbildung und Lebensführung geknüpft hat [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 10|Q1]]. Gerade dieser historische Ausgangspunkt macht den Übergang zu [[Mittelalter und Renaissance]], [[Rousseau und die Erziehung zum Menschsein]] und [[Kant und die Autonomie der Bildung]] nachvollziehbar, weil der Bildungsbegriff über Jahrhunderte immer wieder neu als Beziehung von Selbst und Welt gedacht wurde.

--- END NOTE ---

--- FILENAME: 40-Permanent/Penninisch-Ligurischer Ozean.md
--- BEGIN NOTE ---

# Penninisch-Ligurischer Ozean

Der **Penninisch-Ligurische Ozean** (auch Alpine Tethys, mit dem Valais-Ozean) war ein kleiner Ozean, der sich im Mittleren Jura als Seitenarm des Nordatlantiks bei der Auflösung Pangäas öffnete — ohne Verbindung zum großen Tethys-Ozean und den kleinen Hallstatt- und Meliata-Ozeanen im Osten ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).

Das Spreading des Ozeans war **extrem langsam** (magmaarmer, ultralangsamer Rücken): Es wurde nur wenig neue ozeanische Kruste gebildet, stattdessen wurde subkontinentaler Mantel über weite Flächen am Meeresboden freigelegt und durch Hydratation sowie metasomatische Veränderung in Serpentinite und Ophicalcite umgewandelt ([[10-Raw/Field trip to the Tauern Window.pdf#page=2|Q1]]).

Als Sedimentationsraum lieferte er die Bündnerschiefer, als Reste seiner ozeanischen Lithosphäre gingen die Ophiolithe und die Glockner-Decke hervor. Während der Hauptkollision im Paleogen wurde der Ozean vollständig konsumiert: Seine abradierten Sedimente und ozeanischen Reste überschoben — in der [[Alpine Deckentektonik|alpinen Deckenarchitektur]] unter den Austroalpinen Decken liegend — den Kontinentalrand der Europäischen Platte ([[10-Raw/Field trip to the Tauern Window.pdf#page=3|Q1]]). Damit ist er das Gegenstück des [[Wilson-Zyklus|Wilson-Zyklus]] in den Ostalpen.

Verwandte Konzepte: [[Alpine Deckentektonik]], [[Eoalpine Orogenese]], [[Wilson-Zyklus]]

## Einfach erklärt

Der *Penninisch-Ligurische Ozean* (auch "Alpine Tethys") ist der kleine Ozean, der sich vor ~160–170 Mio. Jahren öffnete, als Pangaea auseinanderbrach. Er war kein offener Atlantik, sondern ein schmaler, *langsam gespreizter* Meeresstreifen zwischen Afrika (Adria) und Europa. Bei extrem langsamer Spreizrate blieb der neue Meeresboden nicht aus frischem Magma, sondern es wurde altes Mantelgestein bloßgelegt und durch Meerwasserkontakt zu Serpentiniten/Ophicalciten umgewandelt (Gesteine, die sich wie verseiftes Material verhalten).

Für einen Physiker: Die "magmaarme" Spreizung ist im Grunde eine ultraschnelle *Dehnungsrate* mit verzögerter Nachlieferung von Magma — die Trennung läuft, aber der Nachschub aus dem Mantel kann nicht mithalten, sodass die Kruste "reißt" statt aufzuschmelzen. Als der Ozean im Paleogen geschlossen wurde, blieben seine Sedimente (Bündnerschiefer) und ozeanischen Reste als mittlere Decken im Alpenstapel übrig. Er ist damit das alpine Beispiel für einen vollständigen Ozean-Lebenszyklus (*[[Wilson-Zyklus]]*).

--- END NOTE ---

--- FILENAME: 40-Permanent/Perm-Trias-Massenaussterben.md
--- BEGIN NOTE ---

# Perm-Trias-Massenaussterben

Das **Perm-Trias-Massenaussterben**, auch als The Great Dying bekannt, ist das größte Massensterben der Erdgeschichte. Vor 252 Millionen Jahren starben innerhalb von vermutlich weniger als einer Million Jahren 70 % der Landarten und 95 % der Meeresarten — darunter die letzten [[Trilobiten]] <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=339s" title="00:05:39">(V)</a>.

Die Auslöser sind umstritten: Asteroideneinschlag, massiver Vulkanismus und durch verschobene Landmassen veränderte Klimamuster werden diskutiert <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=327s" title="00:05:27">(V)</a>. Gemeinsam ist allen Hypothesen, dass sich Atmosphäre und Ozeane in radikal kurzer Zeit veränderten.

Für die Trilobiten war dies der vierte und letzte Schlag <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=316s" title="00:05:16">(V)</a>. Sie überlebten die [[Ordovizium-Silur-Extinktion]] und die [[Spätdevon-Extinktion]], nicht aber die schärfste Krise. Das Aussterben zeigt, dass selbst die erfolgreichste und langlebigste Tiergruppe an einem einzigen Ereignis scheitern kann, wenn dieses die Lebensbedingungen schneller verändert, als Anpassung möglich ist.

--- END NOTE ---

--- FILENAME: 40-Permanent/Pfitscher Bergsturz.md
--- BEGIN NOTE ---

# Pfitscher Bergsturz

Der **Pfitscher Bergsturz** ist ein nacheiszeitliches Großereignis im Pfitschtal (Südtirol): Von der Flanke der Überseilspitze (2493 m) stürzte ein Bergrücken ab, der das Tal **150 m hoch vollständig abriegelte** und den Pfitschbach zu einem **8 km langen See** aufstaute ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]).

Die Sturzmassen bestehen aus fest verbackenen Schutt- und Trümmermassen von Kalkglimmerschiefern der [[Metamorphe Schieferhülle (Tauernfenster)|Schieferhülle]]: hausgroße Blöcke und fein zerriebenes Material liegen unsortiert und chaotisch durcheinander, eine Schichtung fehlt völlig — wie für Bergstürze charakteristisch ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]).

**Um das Jahr 1100** rutschte ein Stück des durchnässten Stauwalles ins Rutschen; die nachstürzenden Wasserfluten setzten den Auslauf mit starker erosiver Kraft immer tiefer, bis der See mit etwa **70 Millionen Kubikmetern Wasser über Nacht leergelaufen war**. Die Flutkatastrophe richtete flußabwärts im Pfitsch- und Eisacktal große Verwüstung an und forderte viele Menschenleben ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]).

Die **Spuren des Ereignisses sind bis heute lesbar**: Die versumpfte Ebene von Kematen besteht aus Seesedimenten; Schwemmkegel und alte Terrassen (u. a. die Häuser von Rein) rekonstruieren den alten Seespiegel, der Ortsname **Überwasser** erinnert daran, und in Kematen steht ein über tausend Jahre altes Haus aus der Zeit, in der die Bewohner vom Seeufer lebten ([[10-Raw/Tauernfenster (Quelle).md#Seite 5|Q1]]).

Der Auslösekontext ist typisch für die Nacheiszeit: Nach dem Abschmelzen der Gletscher verloren die übertieften, vegetationslosen Talhänge ihre Stütze durch das Eis und brachen zusammen ([[10-Raw/Tauernfenster (Quelle).md#Seite 4|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Plätten und Schiffszug.md
--- BEGIN NOTE ---

# Plätten und Schiffszug

Die **Plätten und der Schiffszug** waren die zentralen Elemente der Innschifffahrt. Plätten (und kleinere Zillen) besaßen einen flachen Boden, um die zahlreichen Untiefen schadlos zu überqueren; ihre Länge variierte von 5–6 Metern bis zu 20 Metern für große Frachten ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). Sie wurden von spezialisierten Handwerkern in Schopperwerkstätten entlang des Inns in Serie hergestellt; Zentren lagen von Wörgl bis Kufstein sowie in Neubeuern und Rosenheim ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]).

Die Schiffbarkeit hing von Wasserführung und Gefälle ab: Mit einem Gefälle von 1 Promille und einer Fließgeschwindigkeit von 3 m/s (mehr als doppelt so viel wie beim Rhein) lag der Inn an der Grenze der Schiffbarkeit, sodass nur die Zeiträume März–Mai und August–November zur Verfügung standen ([[10-Raw/Inn Truppentransport.pdf#page=2|Q1]]). Stromaufwärts wurden die Schiffe von bis zu 30 Zugpferden und 40 Bediensteten gezogen — ein Schiffszug aus zwei bis vier zusammengebundenen Frachtschiffen beförderte bis zu 5.000 Zentner ([[10-Raw/Inn Truppentransport.pdf#page=3|Q1]]). Für große Truppentransporte nutzte man die großen Salzschiffe von 20–30 m Länge und 6–7 m Breite ([[10-Raw/Inn Truppentransport.pdf#page=11|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Pressburger Vertrag 1491.md
--- BEGIN NOTE ---

# Pressburger Vertrag 1491

Der **Pressburger Vertrag** (1491) war ein Erbvertrag zwischen Maximilian I. und König Vladislav II. von Böhmen und Ungarn: Die Kronen Böhmens und Ungarns sollten an das Haus Habsburg fallen, wenn Vladislav ohne Erben bleiben sollte ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).

Der Vertrag war ein zentrales Element der [[Habsburgische Heiratspolitik|habsburgischen Heiratspolitik]]: Er sicherte die Erbfolge in zwei Königreichen, ohne dass Maximilian sie militärisch erobern musste ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).

Da Vladislav aus seiner Ehe mit Anne de Foix-Candale doch Kinder bekam (Tochter Anna, geb. 1503, und Sohn Ludwig II., geb. 1506), wurde die Vereinbarung von Pressburg 1506 durch den Plan **wechselseitiger Heiraten** zwischen den jeweiligen Thronfolgern erweitert — daraus entwickelte sich die [[Wiener Doppelhochzeit 1515|Wiener Doppelhochzeit]] ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]). Der Vertrag war damit das juristische Fundament, auf dem 1526 die Kronen von Böhmen und Ungarn an Habsburg fielen.

Verwandte Konzepte: [[Wiener Doppelhochzeit 1515]], [[Habsburgische Heiratspolitik]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Quellhydrochemie des Tauernfensters.md
--- BEGIN NOTE ---

# Quellhydrochemie des Tauernfensters

Die chemische Zusammensetzung von Quellen im Schmirntal ist ein **Informationsträger aus dem Erdinneren**: Sie spiegelt exakt den Weg des Wassers durch den Fels wider ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

Im Bereich der Kalkglimmerschiefer der [[Metamorphe Schieferhülle (Tauernfenster)|Schieferhülle]] finden sich **karbonatische Wässer** mit hohem Kalkgehalt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Eine Besonderheit ist das Auftreten von **Arsen und Uran** in bestimmten Quellen: Es tritt dort auf, wo das Wasser Kontakt mit dem tief liegenden **Zentralgneis-Basement** hat ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Die Metalle werden auf natürlichem Weg aus dem Gestein gelöst — ein direkter geochemischer Beweis für die **Fenster-Struktur**, die diese tiefen Schichten nach oben bringt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

An vielen Quellaustritten bilden sich **Kalktuffe** (Spring-Associated Limestones, SAL): Moose und Algen entziehen dem Wasser CO₂, wodurch der gelöste Kalk ausfällt und bizarre Gesteinsformationen direkt an der Oberfläche entstehen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Die Kalktuffbildungen sind **Indikatoren für stabile hydrogeochemische Bedingungen über längere Zeiträume** — ein bemerkenswerter Kontrast zu den ansonsten instabilen Schieferhängen ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q2]]). Die Hydrochemie wirkt damit wie ein Fenster in das [[Tauernfenster]] selbst: Wo das Grundgebirge oberflächennah liegt, verrät es sich durch seine Element-Signatur im Quellwasser.

Auch **Eisen-Signaturen** gehören zum geochemischen Fingerabdruck des Fensters: An der Pfitscher-Joch-Straße queren Quellaustritte mit **rostrotem Wasser** pyritführende Schiefer, die von der Rotbachlspitze herabziehen — bei der Zersetzung des Pyrites (Eisensulfid) entstehen die färbenden Eisenverbindungen ([[10-Raw/Tauernfenster (Quelle).md#Seite 6|Q3]]). Solche vererzten Zonen sammeln die chemischen Restlösungen und Gase, die bei der Erstarrung des Granites nicht in die normalen Minerale eingebaut wurden — die gleiche Quelle, aus der auch Scheelit-führende Gneise bei Mittersill gespeist werden ([[10-Raw/Tauernfenster (Quelle).md#Seite 8|Q3]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Radiale Symmetrie.md
--- BEGIN NOTE ---

# Radiale Symmetrie

**Definition:** Radiale (auch radiäre) Symmetrie bedeutet, dass sich Körpermerkmale um eine **zentrale Achse** anordnen (statt um eine einzige zentrale Ebene wie bei [[Bilaterale Symmetrie]]) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=315s" title="00:05:15">(V)</a>).

**Ursprung:** Sie entsteht, wenn ein Tier der Welt **aus jeder Richtung zugleich** begegnet, aber **keine gerichtete Bewegung** ausführt — es treibt z. B. nur im Wasser. Ergebnis ist eine Oben/Unten-Achse, aber kein echtes Links/Rechts, Vorn/Hinten (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=434s" title="00:07:14">(V)</a>). Beispiel: Quallen.

**Achtung — ungerade Spiegellinien sind möglich:** Ein Körper wie ein fünfarmiger Seestern kann eine ungerade Anzahl von Spiegellinien haben (Teilbarkeit durch zwei ist nicht die Voraussetzung) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=269s" title="00:04:29">(V)</a>). Bei Echinodermen ist die Radialsymmetrie zudem **nicht ursprünglich** ([[Sekundäre Radialsymmetrie der Echinodermen]]).

**Grenzfälle:** Ctenophoren sind eher rotations-/biradialsymmetrisch; Cnidarier ([[Cnidarier|Quallen, Anemonen]]) laufen von radial über biradial bis beinahe bilateral (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=461s" title="00:07:41">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Raum, Zeit und Entgrenzung in der digitalen Bildung.md
--- BEGIN NOTE ---

# Raum, Zeit und Entgrenzung in der digitalen Bildung

Ein wesentlicher Abschnitt der Quelle geht von der Grundannahme aus, dass die Welt und damit auch Bildung immer in Raum und Zeit verfasst sind. Raum und Zeit sind keine bloßen Gegebenheiten des Alltags, sondern Grundkategorien menschlicher Existenz und damit auch der Bildung. Diese Kategorien bestimmen, wie Menschen sich orientieren, wie sie lernen, wie sie Zeiträume organisieren und wie sie sich zu Orten und sozialen Zusammenhängen verhalten [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 35|Q1]].

Die Autor:innen zeigen dann, dass Digitalisierung und Mediatisierung diese Grundkategorien ernsthaft verschieben. Die räumliche und zeitliche Organisation menschlicher Praxis wird durch mobile Endgeräte, digitale Kommunikationsformen und vernetzte Infrastrukturen nicht einfach ergänzt, sondern umgebaut. Räume verlieren an feste Bindung, Zeit wird durch technische Synchronisierung und digitale Verfügbarkeit flexibler, und das Verhältnis von Nähe und Ferne wird verändert [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 38|Q1]].

Der Begriff der Entgrenzung ist hier entscheidend. Er beschreibt, dass Medien und digitale Kommunikationsformen nicht mehr streng an festgelegte Orte, Zeitpunkte, soziale Kontexte und Zwecksetzungen gebunden sind. Lernen, Arbeit, Freizeit und Mediennutzung verschieben sich in immer stärkere Überschneidungen. Das führt zu veränderten Lernformen, in denen trotz räumlicher und zeitlicher Flexibilität zugleich neue Anforderungen an Selbstorganisation und Medienkompetenz entstehen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 42|Q1]].

In bildungswissenschaftlicher Perspektive ist die Entgrenzung nicht bloß technischer Fortschritt, sondern eine soziale und kulturelle Veränderung. Sie ermöglicht neue Lernprozesse, etwa durch E-Learning, Mobile Learning, vernetzte Lernangebote und informelles Lernen außerhalb der Institution Schule. Zugleich zeigt die Quelle, dass diese Entgrenzung nicht automatisch zu „besserem Lernen“ führt. Sie schafft neue Möglichkeiten, aber sie erhöht auch den Bedarf an didaktischer Gestaltung, Reflexion und pädagogischer Verantwortung [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 44|Q1]].

Damit wird in der Quelle deutlich: Digitale Bildung ist nicht nur ein technisches Format, sondern eine veränderte Bildungsökologie. Lernprozesse sind zeitlich und räumlich entgrenzt, aber sie bleiben an soziale, sachliche und pädagogische Bedingungen gebunden. Die Bildungsaufgabe besteht darin, diese neue Flexibilität und Erreichbarkeit so zu gestalten, dass sie nicht bloß Geschwindigkeit und Verfügbarkeit erhöht, sondern tatsächlich die Selbstbildung und die Lernfähigkeit des Menschen fördert [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 45|Q1]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Refugia.md
--- BEGIN NOTE ---

# Refugia

**Definition:** Refugia sind kleine Regionen, in denen eine Art **überlebt**, während sie in einem Teil ihres einst viel größeren Verbreitungsgebietes verschwindet; ein Refugium bildet eine **Teilmenge eines früher viel größeren Areals** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=439s" title="00:07:19">(V)</a>).

**Warum in Gebirgen:** Mehr Nischen bedeutet weniger Konkurrenz um dieselbe Nische. Tiere, die im Tiefland von Konkurrenten verdrängt würden, können daher in den Bergen **länger überleben** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=429s" title="00:07:09">(V)</a>).

**Fallbeispiel:** Die im mittleren Eozän in den Fußhügeln Zentral-Wyomings überlebenden **anaptomorphinen Primaten** ([[Anaptomorphine und Omomyine]]), die trotz Konkurrenz durch die Omomyinen weiterhin Speziation betrieben, sind direkter Beleg für Refugia (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=447s" title="00:07:27">(V)</a>). Millionen Jahre später waren sie noch nicht ausgestorben, sondern hatten sich angepasst (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=565s" title="00:09:25">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Reichsacht.md
--- BEGIN NOTE ---

# Reichsacht

Die **Reichsacht** war die höchste Strafe des mittelalterlichen und frühneuzeitlichen Reichsrechts: Der Geächtete verlor seinen Frieden und seine Rechtssicherheit und stand außerhalb des Gesetzes — wer ihn tötete, machte sich nicht strafbar.

Im Landshuter Erbfolgekrieg verhängte König Maximilian I. am 5. Mai 1504 die Reichsacht über Ruprecht von der Pfalz und dessen Vater, Pfalzgraf Philipp den Aufrichtigen, wegen der Auslösung des Krieges ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]). Die Acht war damit ein politisches Druckmittel des Königs, mit dem er seine Parteinahme für Albrecht IV. von Bayern-München rechtlich unterlegte und den Konflikt vom innerwittelsbachischen Streit zum Reichskrieg erhob ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]). Sie mobilisierte die Reichsstände (Schwäbischer Bund, Württemberg, Nürnberg) an der Seite Albrechts und verschärfte die Isolierung Ruprechts, der dennoch mit rund 30.000 Mann von Frankreich, Böhmen und Baden unterstützt wurde.

--- END NOTE ---

--- FILENAME: 40-Permanent/Reichskammergericht.md
--- BEGIN NOTE ---

# Reichskammergericht

Das **Reichskammergericht** war die ständisch dominierte oberste Gerichtsbehörde des Heiligen Römischen Reiches, eingesetzt im Zuge der [[Reichsreform von 1495]] ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Es tagte zunächst an verschiedenen Orten im Reich und wurde seit 1527 über einen längeren Zeitraum in Speyer ansässig ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]). Es war die erste Instanz für die reichsunmittelbaren Stände und stand in direktem Zusammenhang mit den Verhandlungen um den [[Ewiger Landfrieden|Ewigen Landfrieden]], den es durchsetzen sollte — die "Handhabung Friedens und Rechts" wurde als Vertrag zwischen König und Ständen ausgestaltet ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Das Gericht ist eines der nachhaltigsten Ergebnisse der [[Reichsreform von 1495]]: Es hatte über Jahrhunderte Bestand und verankerte eine reichsweite, ständisch mitgetragene Rechtsprechung als Alternative zur privaten Fehde.

Verwandte Konzepte: [[Reichsreform von 1495]], [[Ewiger Landfrieden]], [[Reichsacht]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Reichskreise.md
--- BEGIN NOTE ---

# Reichskreise

Die **Reichskreise** waren die neuen regionalen Verwaltungseinheiten des Heiligen Römischen Reiches, die als Ergebnis der [[Reichsreform von 1495]] eingeführt wurden: Das Reichsgebiet wurde zunächst in sechs, später in zehn Kreise geteilt ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Die Kreise übernahmen konkrete Reichsaufgaben: die Einhebung von Reichssteuern (etwa des [[Gemeiner Pfennig|Gemeinen Pfennigs]]), die Durchsetzung von Anordnungen der Reichsorgane sowie die Aufstellung und den Unterhalt von Reichstruppenkontingenten ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Zusammen mit dem [[Reichskammergericht]] hatten die Reichskreise dauerhaft Bestand — anders als die komplexen, ständisch verfassten Strukturen des Reiches, die die Reform insgesamt nicht aufbrechen konnte ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]). Die Kreise wurden so zu einem bleibenden Baustein der Reichsverfassung der Frühen Neuzeit.

Verwandte Konzepte: [[Reichsreform von 1495]], [[Gemeiner Pfennig]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Reichsreform von 1495.md
--- BEGIN NOTE ---

# Reichsreform von 1495

Die **Reichsreform von 1495** war ein Bündel von Reformgesetzen, die auf dem Reichstag zu Worms beschlossen wurden und einen Wendepunkt in der europäischen Geschichte markieren: den Übergang vom Mittelalter zur Frühen Neuzeit ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Der Anlass war ein Machtproblem: Die kaiserliche Zentralgewalt war nach Jahrhunderten der Erosion von Reichsrechten an einem administrativen Tiefpunkt angelangt, während die Reichsfürsten wachsende Eigenständigkeit beanspruchten ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]). Maximilian I. wollte die Zentralgewalt stärken und die Reichsfürsten an Kaisertum und Reich binden; der Mainzer Erzbischof Berthold von Henneberg trat als Wortführer der Reichsstände dagegen an und erzwang einen Kompromiss ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Das Ergebnis waren vier miteinander zusammenhängende Reformgesetze im Reichsabschied von 1495: der [[Ewiger Landfrieden|Ewige Landfriede]], das [[Reichskammergericht]], das [[Reichsregiment]] und der [[Gemeiner Pfennig|Gemeine Pfennig]]. Dauerhaft Bestand hatten davon die Reichskreise und das Reichskammergericht; das Reichsregiment scheiterte am Widerstand der Stände ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]). Die Reform festigte faktisch den Reichstag als oberste Rechts- und Verfassungsinstitution, ohne dass es dafür einen formellen Einsetzungsakt gab ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Verwandte Konzepte: [[Ewiger Landfrieden]], [[Reichskammergericht]], [[Reichskreise]], [[Gemeiner Pfennig]], [[Reichsregiment]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Reichsregiment.md
--- BEGIN NOTE ---

# Reichsregiment

Das **Reichsregiment** war eine im Zuge der [[Reichsreform von 1495]] geplante ständische Reichsregierung — ein Regierungsorgan, das die Reichsgewalt stellvertretend für den König ausüben sollte ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Es war einer der vier Reformgesetze des Wormser Reichstags und Teil von Maximilians I. Streben, die kaiserliche Zentralgewalt zu stärken. Der Mainzer Erzbischof Berthold von Henneberg rang Maximilian die Zustimmung zu dem Reichsregiment als Teil der "Handhabung Friedens und Rechts" ab ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]).

Das Reichsregiment **scheiterte am Widerstand der Reichsstände** und wurde nie dauerhaft etabliert — es ist das prominenteste Beispiel für die Grenzen der [[Reichsreform von 1495]]: Was den Ständen zu zentralistisch war, konnte gegen sie nicht durchgesetzt werden ([[10-Raw/Maximilian I. (HRR).md#Kaiserliche Innenpolitik und Verwaltungsreformen|Q1]]). Im Gegensatz zum [[Reichskammergericht]] blieb das Reichsregiment Episode.

Verwandte Konzepte: [[Reichsreform von 1495]], [[Reichskammergericht]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Reissenschuh-Rutschung.md
--- BEGIN NOTE ---

# Reissenschuh-Rutschung

Die **Reissenschuh-Rutschung** (2.470 m) im Schmirntal ist eine „Deep-Seated Gravitational Slope Deformation" (DSGSD), also eine **tiefgreifende gravitative Hangdeformation**: Ein ganzer Berghang bewegt sich langsam, aber unaufhaltsam talwärts ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

Die Ursache ist eine **lithologische Inversion** — eine ungünstige Schichtabfolge ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]): Wasserdurchlässiger, geklüfteter Marmor ([[Metamorphe Schieferhülle (Tauernfenster)|Hochstegen-Marmor]]) liegt obenauf, darunter vollkommen wasserundurchlässiger Phyllit. Regen- und Schmelzwasser versickern im Marmor, können aber nicht in den Phyllit eindringen — es entsteht ein **Wasserstau an der Grenzschicht** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]).

Der dadurch aufgebaute **Porenwasserdruck** hebt die Gesteinsmassen minimal an und setzt die Reibung außer Kraft — der Hang beginnt zu rutschen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Die Mechanik ist physikalisch dieselbe wie bei einem Wasserfilm unter einem Reifen: Die Normalkraft zwischen den Gleitflächen wird reduziert, sodass die Haftreibung unterschritten wird ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Die Bewegungsraten betragen im Durchschnitt 0,6 bis 0,8 Meter pro Jahr; in besonders instabilen Phasen wurden Beschleunigungen auf über 3 Meter pro Jahr gemessen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]). Eine zweite NotebookLM-Ausgabe nennt abweichende Werte — mittlere Verschiebung ~0,6 m/Jahr, Spitzen über 1,2 m/Jahr in einzelnen Sektoren ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q2]]) — die genaue Zahl hängt offenbar vom berücksichtigten Messzeitraum und Sektor ab ^[ambiguous]. Der Hang wird mit moderner Messtechnik überwacht ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 1: „Schmirntaler Tiefenblicke – Die Erde in Bewegung“|Q1]]; siehe [[Monitoring gravitativer Hangdeformationen]]), die Zeitreihe reicht durch photogrammetrische Luftbildauswertung des Projekts [[EMOD-SLAP]] bis 1954 zurück ([[10-Raw/Reissenschuh (NotebookLM 2).md|Q2]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Rousseau und die Erziehung zum Menschsein.md
--- BEGIN NOTE ---

# Rousseau und die Erziehung zum Menschsein

> Rousseau kritisiert Bildung als gesellschaftliche Anpassung und fordert stattdessen eine „negative Erziehung“, die die natürliche Entwicklung des Kindes respektiert. Sein Konzept betont Selbsttätigkeit, Erfahrungslernen und die Befreiung von künstlichen Konventionen – ein Grundgedanke moderner Reformpädagogik.

# Rousseau und die Erziehung zum Menschsein
Im Zentrum von Rousseaus Pädagogik steht die Idee, dass Bildung nicht die Anpassung an gesellschaftliche Erwartungen bedeutet, sondern die Befreiung des Menschen zu seinem eigenen Menschsein. Er wendet sich gegen eine Erziehung, die Kinder und Jugendliche in die Interessen der bestehenden Gesellschaft hineinformen will, statt ihre individuelle Natur und ihre sich entfaltende Persönlichkeit ernst zu nehmen [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 20|Q1]]. In dieser Perspektive ist Bildung kein bloßer Zweck der Gesellschaft, sondern die Ermöglichung einer selbstbestimmten und natürlichen Entwicklung [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 20|Q1]].

Der Studienbrief betont, dass Rousseau mit der Entdeckung der Kindheit eine grundlegende Umstellung der Pädagogik bewirkt. Der Heranwachsende wird nicht mehr nur als zukünftiger Erwachsener verstanden, sondern als eigenständige Lebensphase mit eigener Logik. Rousseaus formale Grundthese lautet: „Die Natur will, daß Kinder Kinder sind, ehe sie Männer werden“ [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 21|Q1]]. Diese Einordnung ist für die Moderne von großer Bedeutung, weil sie den Bildungsprozess von der frühen, instinktiven und sinnesbezogenen Entwicklung her denkt und nicht von einem Zielbild des Erwachsenen aus [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 21|Q1]].

Rousseaus Erziehungskonzept wird als „negative und natürliche Erziehung“ beschrieben. Der Erzieher soll den natürlichen Entwicklungsprozess nicht beschleunigen oder künstlich steuern, sondern Zeit lassen, damit das Kind die Welt in eigener Weise erkunden kann. Das Bildungsziel ist eine Selbstbildung, die auf der individuellen natürlichen Bestimmung und Perfektibilität des Menschen beruht [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 22|Q1]].

Die Quelle nennt dabei drei Erzieher: Natur, Dinge und Menschen. Die Natur bildet im Inneren aus; die Dinge geben über die sinnliche Erfahrung und die Begegnung mit der Umwelt Orientierung; der Mensch als Erzieher soll dabei indirekt anleiten und nicht autoritär instruktiv bestimmen. Rousseau fordert also eine Erziehung, die die Selbsttätigkeit des Kindes stärkt und in der natürlichen Umgebung des Kindes verankert ist [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 22|Q1]].

Der entscheidende bildungstheoretische Punkt ist die Verbindung von menschlicher Individualität und sozialer Vergesellschaftung. Rousseau will nicht nur Bildung zum Menschsein, sondern zugleich die Einbindung in die Gesellschaft. Dennoch ist die Rangfolge klar: Die natürliche Erziehung zielt zunächst auf eine Bildung zum Menschen, nicht auf gesellschaftliche Brauchbarkeit. Erst danach kann der Mensch als Bürger in die Gesellschaft treten [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 26|Q1]]. Die Folge ist eine Spannung zwischen Autonomie und sozialer Integration, die für die Pädagogik bis heute zentral bleibt.

Rousseau wird deshalb als Vorläufer moderner pädagogischer Kritik verstanden. Seine Erziehungstheorie ist nicht bloß konservativ, sondern richtet sich gegen Verformung, künstliche Konventionen und die Übernahme gesellschaftlicher Rollen ohne Rücksicht auf die Individualität des Kindes. Die Leitidee ist die Befreiung des Menschen zu einem genuinen Menschsein, das auf Selbstbestimmung, Selbsttätigkeit und natürlicher Entwicklung beruht [[10-Raw/17_TFLE1 Bildung in der digitalisierten Gesellschaft.md#Seite 20|Q1]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Sakrale Landschaft des Schmirntals.md
--- BEGIN NOTE ---

# Sakrale Landschaft des Schmirntals

Die sakrale Landschaft des Schmirntals umfasst zwei zentrale Orte des Glaubens: die Pfarrkirche St. Joseph und die Wallfahrtskapelle „Zur kalten Herberge“ ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).

Die **Pfarrkirche St. Joseph** ist das geistliche Zentrum von Schmirn — ein barockes Juwel, das **1756/57** nach den Plänen des berühmten Priesterarchitekten **Franz de Paula Penz** erbaut wurde ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Penz war ein Meister darin, prunkvolle Kirchenräume zu schaffen, die den Menschen im kargen Gebirge Hoffnung gaben ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).

Tief im Wald liegt die **Kapelle Mariahilf**, Ziel der Wallfahrt „Zur kalten Herberge“ ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Die Legende erzählt, dass die Kapelle an jener Stelle errichtet wurde, an der Hirten ein **Gnadenbild** — eine Kopie des berühmten Cranach-Bildes — an einer Quelle fanden ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Unter den Wurzeln einer alten Fichte entspringt dort eine **eiskalte, heilkräftige Quelle**, deren Wasser nach volkstümlicher Überlieferung besonders bei **Augenleiden** hilft ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Die 1730 erbaute Kapelle ist bis heute Ziel vieler Wallfahrer ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Der tiefe Glaube war der Anker im harten Alltag der [[Schwaighöfe|Schwaighof-Wirtschaft]] — die Kirche ordnete auch das letzte Geleit der Verstorbenen ([[Totenweg über das Tuxer Joch]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Schulden Maximilians I..md
--- BEGIN NOTE ---

# Schulden Maximilians I.

Die **Schulden Maximilians I.** waren der enorme Schuldenberg, den der Kaiser durch seine Kriege, seinen prunkvollen Hofstaat und die Erblasten früherer Reichsoberhäupter hinterließ — die Kosten überstiegen die laufenden Einnahmen bei weitem ([[10-Raw/Maximilian I. (HRR).md#Schulden|Q1]]).

Maximilian war daher ständig auf Kredite seines Hausbankiers Jakob Fugger angewiesen; das Augsburger Bankhaus erlangte dadurch zahlreiche Privilegien ([[10-Raw/Maximilian I. (HRR).md#Schulden|Q1]]). Wegen seiner 17 Aufenthalte in Augsburg (insgesamt über zwei Jahre) gab ihm der französische König Franz I. den Spottnamen "Bürgermeister von Augsburg" ([[10-Raw/Maximilian I. (HRR).md#Schulden|Q1]]).

Das Diktat der leeren Kassen zwang Maximilian sogar zu einer unstandesgemäßen Ehe: Er heiratete Bianca Maria Sforza, deren Onkel Ludovico dafür eine Mitgift von 400.000 Golddukaten in bar und 40.000 Dukaten in Juwelen zahlte und im Gegenzug das Herzogtum Mailand als Reichslehen erhielt ([[10-Raw/Maximilian I. (HRR).md#Schulden|Q1]]). Die Finanznot ist die Kehrseite der prunkvollen [[Maximilians Selbstinszenierung|Selbstinszenierung]] und der imperialen [[Habsburgische Heiratspolitik|Heiratspolitik]].

Verwandte Konzepte: [[Maximilians Selbstinszenierung]], [[Habsburgische Heiratspolitik]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Schwaighöfe.md
--- BEGIN NOTE ---

# Schwaighöfe

Die **Schwaighöfe** waren spezialisierte Viehbetriebe der mittelalterlichen Alpwirtschaft, die meist dem **Adel oder Klöstern** gehörten ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Sie bildeten das Rückgrat der alpinen Wirtschaft und trotzten der kargen Natur: Statt Getreide anzubauen — was in der Höhenlage kaum möglich war — hielten die Bauern Vieh und zahlten ihren Zins in Form von **Käse und Schmalz** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).

Die dauerhafte Besiedlung des Schmirntals ist eng mit dieser Landerschließung verknüpft. Der Name **„Vallis Smurne“** taucht erstmals im Jahr **1249** in Urkunden auf ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Die Wirtschaftsform prägte auch die Kulturlandschaft: Die späte, extensive Mahd der [[Bergmähder]] ist direkte Fortsetzung dieser Bewirtschaftungstradition. Eine politische Besonderheit der Schwaighof-Landschaft: Bis zum Jahr **1926** gehörten Hintertux und das obere Tuxertal politisch und kirchlich zur Gemeinde Schmirn — die Schmirner waren die Verwalter, die Tuxer die Untergebenen ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Diese lange Zugehörigkeit erzwang über Jahrhunderte den [[Totenweg über das Tuxer Joch|Totenweg über das Tuxer Joch]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Schwarmintelligenz bei Trilobiten.md
--- BEGIN NOTE ---

# Schwarmintelligenz bei Trilobiten

Die **Schwarmintelligenz bei Trilobiten** bezeichnet die Interpretation einer fossilen Reihenformation als frühestes Zeugnis kollektiven Verhaltens. 480 Millionen Jahre alte Fossilien der Art *Ampyx priscus* aus dem unteren Ordovizium belegen eine „Gänsemarsch“-Formation der Tiere — eine lineare Anordnung, in der die Individuen einander in Reihe folgen ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

Diese Reihenformation wurde als die **ersten Zeugnisse von Schwarmintelligenz bei Lebewesen** gedeutet — kollektives Verhalten, bei dem die Koordination der Gruppe einen Nutzen stiftet, den das einzelne Tier allein nicht erreichen könnte ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Parallelen gibt es bei heutigen Gliederfüßern, etwa bei den Marschformationen von Wanderheuschrecken oder den Kolonnen wandernder Hummerlarven.

Der Fund erweitert die evolutionsbiologische Aussagekraft des Fossilberichts: Er zeigt, dass nicht nur Körperfossilien, sondern auch Verhaltensspuren der [[Trilobiten]] Rückschlüsse auf die Ökologie und die kognitiven Fähigkeiten früher Tiere erlauben ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Damit steht die Deutung im Kontext des Argumentationsstrangs, dass Trilobiten in vielfacher Hinsicht als [[Trilobiten als Zeugen der Evolution|Zeugen der Evolution]] gelten können.

--- END NOTE ---

--- FILENAME: 40-Permanent/Seamless Learning.md
--- BEGIN NOTE ---

# Seamless Learning

> Der Begriff „Seamless Learning“ beschreibt Bildung als kontextübergreifenden Prozess, der Schule, Freizeit und Arbeit verbindet. Digitale Medien ermöglichen ein mobiles, lebenslanges Lernen, das nicht an feste Orte oder Zeiten gebunden ist. Die Quelle betont die Selbststeuerung und Reflexion als Kernkompetenzen in digitalen Lebenswelten.

# Seamless Learning
Die Quelle verwendet den Begriff des Seamless Learning als Kernmodell für digitale Bildungsprozesse. Dadurch wird Lernen als durchgängiger, mobiler und kontextgebundener Prozess gedacht, der Schule, Freizeit, Arbeit und Alltag miteinander verbindet. Lernen verliert damit seine feste Verortung in einer einzelnen Institution oder in einer einzigen Zeitspanne [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=11|Q1]].

Seamless Learning meint nicht bloß, dass man überall über digitale Medien lernen kann. Es bedeutet vielmehr, dass Bildungsprozesse fließend zwischen verschiedenen Kontexten wechseln und sich an die Lebenswirklichkeit des Lernenden anpassen. Welche Lernform gerade relevant ist, hängt davon ab, was gerade gefragt ist, wo man sich befindet und welche Erfahrungen im Alltag gerade gemacht werden [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=11|Q2]]. In diesem Sinne überschreitet digitales Lernen die Trennung von formalen und informellen Lernsettings. Die Bildung wird Teil einer durchgehenden Lebenspraxis, in der Medien, Alltag, Selbststeuerung und Reflexion zusammenlaufen [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=12|Q3]].

Für die Bildungstheorie ist der Begriff deshalb so wichtig, weil er zeigt, dass moderne Bildung nicht mehr als getrennte Wissensvermittlung zwischen Institutionen gedacht werden kann. Die digitale Lebenswelt verlangt eine Bildungsform, die Lernprozesse im Wechsel von Gelegenheit, situierter Erfahrung und selbstorganisierter Reflexion organisiert. Genau darin liegt die zentrale Bildungsleistung des Seamless Learning: Lernen wird als kontinuierlicher, kontextbezogener und selbstverantworteter Prozess verstanden [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=12|Q4]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Sekundäre Radialsymmetrie der Echinodermen.md
--- BEGIN NOTE ---

# Sekundäre Radialsymmetrie der Echinodermen

**Ausgangslage:** Seesterne und andere Echinodermen wirken als klarer Gegenfall zur Bilateral-Regel — sie sind fünfarmig, ohne offensichtliches Vorn/Hinten (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=269s" title="00:04:29">(V)</a>). Eine ungerade Zahl von Spiegellinien ist dabei technisch möglich (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=269s" title="00:04:29">(V)</a>).

**Überraschung:** **Echinodermenlarven** (Seestern-, Seeigel-, Seegurken-Larven) sind tatsächlich **bilateral symmetrisch** mit normalem Links und Rechts (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=296s" title="00:04:56">(V)</a>). Erst beim Heranwachsen bauen sie sich in den fünfarmigen, **radialen Adulttier** um (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=296s" title="00:04:56">(V)</a>).

**Kladistische Konsequenz:** Echinodermen sind daher **kladistisch Bilateria** ([[Bilateria]]). Ihre **Radialsymmetrie** ([[Radiale Symmetrie]]) — Merkmale um eine zentrale Achse statt um eine zentrale Ebene — ist **sekundär** entstanden: Die Vorfahren waren spiegelsymmetrisch, die Fünfachigkeit ist eine spätere, "entsetzliche" Weiterentwicklung (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=315s" title="00:05:15">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Situs inversus.md
--- BEGIN NOTE ---

# Situs inversus

**Definition:** Situs inversus ist eine Erkrankung, bei der die Organe als **komplettes Spiegelbild** der üblichen Anordnung entstehen: Das Herz liegt nach rechts verlagert, das gesamte Magen-Darm-System ist gespiegelt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=234s" title="00:03:54">(V)</a>).

**Ursache:** Sie geht typischerweise auf **nicht funktionierende Cilien** ([[Nodal-Cilien]]) zurück, deren Strömung die [[Links-Rechts-Festlegung]] nicht mehr korrekt ausrichtet (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=234s" title="00:03:54">(V)</a>).

**Wichtige Einsicht:** Auch im Fall von Situs inversus zerfällt der Körper **nicht** in chaotische Asymmetrie — es entsteht eine **perfekte Spiegelkopie** der normalen Anordnung; jedes Organ liegt an der falschen, aber "exakt richtigen falschen" Stelle (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=258s" title="00:04:18">(V)</a>). Das belegt, wie robust die spiegelsymmetrische Baugrammatik des [[Bilaterale Symmetrie|bilateralen Bauplans]] programmiert ist.

--- END NOTE ---

--- FILENAME: 40-Permanent/Slab Breakoff und Exhumation.md
--- BEGIN NOTE ---

# Slab Breakoff und Exhumation

**Slab Breakoff** bezeichnet das Abreißen der subduzierten ozeanischen Lithosphäre und ihr Versinken in den Erdmantel — ein Schlüsselprozess der Exhumation der Ostalpen ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).

Vor etwa 30–40 Mio. Jahren riss die subduzierte ozeanische Lithosphäre unter den Ostalpen ab. In Folge des plötzlichen Verlusts der negativen Auftriebskraft stieg der zentrale Teil der Ostalpen **rasch um ~2 km** auf ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]). Der damit verbundene Aufstrom heißen Asthenosphärenmaterials erzeugte lokale Schmelzen in der tiefen Kruste: Granite, Tonalite und basische Gänge intrudierten vor ca. 40–30 Mio. Jahren entlang der Periadriatischen Störungen (Rieserferner an der Defereggen-Antholz-Vals-Störung, Rensen an der Pusteria-Störung, Adamello an der Judicarie-Störung) ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).

Der Slab Breakoff begann in der [[Alpine Deckentektonik|Deckentektonik]] die Exhumation des [[Tauernfenster|Tauernfensters]]: Auf die rasche Hebung folgten die Indentation der Adriatischen Platte und die [[Laterale Extrusion der Ostalpen|laterale Extrusion]], während die endgültige Freilegung durch O-W-Extension an der [[Brenner-Normalverwerfung|Brenner-Normalverwerfung]] erfolgte und die Frage nach der Interaktion dieser Mechanismen offen bleibt ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).

Verwandte Konzepte: [[Tauernfenster]], [[Alpine Metamorphose]], [[Laterale Extrusion der Ostalpen]]

## Einfach erklärt

*Slab Breakoff* heißt übersetzt "Abreißen der Platte". Wenn ein Ozeanboden in den Erdmantel abtaucht (Subduktion), zieht die schwere, kühle Platte wie ein verankertes Gewicht an dem Rest der Erdoberfläche nach unten. Irgendwann erreicht das Gestein an der Biegungsstelle seine Zugfestigkeit — und die Platte reißt ab. Dieser Moment ist wie das Durchschneiden des Seils in einem Aufzugssystem: Die Last ist weg, und der "Aufzug" (hier der mittlere Teil der Ostalpen) schnellt sichtbar nach oben — im Papier quantifiziert als rasche Hebung um ~2 km.

Das Abreißen öffnet außerdem ein "Fenster" im Erdmantel, durch das heißes, teilgeschmolzenes Material aufsteigen kann (analog zur Konvektionsdynamik in einer Flüssigkeit, die von unten erhitzt wird). Dieses Aufdringen erzeugt den Granit-/Tonaltmagmatismus, der an den Periadriatischen Störungen (Rieserferner, Rensen, Adamello) steckt. Der Breakoff ist damit der "Auslöser" der ganzen Spätphase: Er sorgt für die erste rasche Hebung, treibt danach die seitliche Extrusion und schließlich die Dehnungs-Exhumation an — ein energieintensiver, aber eindimensional-mechanisch gut fassbarer Prozess.

--- END NOTE ---

--- FILENAME: 40-Permanent/Speziation durch Habitatvariation.md
--- BEGIN NOTE ---

# Speziation durch Habitatvariation

**Kernidee:** Mehr Habitatvariation bedeutet mehr potenzielle Vorteile für einzelne Merkmale — und damit eine höhere Wahrscheinlichkeit, dass ein Merkmal selektiert wird und **neue Arten entstehen** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=406s" title="00:06:46">(V)</a>).

**Zusammenhang:** Wenn höhere Biodiversität beobachtet wird, sieht man möglicherweise den **erhaltenen Beleg dieser durch Habitatvariation verursachten Speziation** (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=417s" title="00:06:57">(V)</a>). Berge ([[Gebirge als Motoren der Biodiversität]]) bieten diese Variation im Quadratmeilen-Maßstab, weshalb in ihnen tendenziell mehr Arten und Speziation auftreten (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=424s" title="00:07:04">(V)</a>).

Dies ist ein Kernmechanismus dafür, warum [[Eozäne Primaten Nordamerikas|Primaten]] in mittleren Höhenlagen mehr Diversität zeigen als im Tiefland (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=424s" title="00:07:04">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Spätdevon-Extinktion.md
--- BEGIN NOTE ---

# Spätdevon-Extinktion

Die **Spätdevon-Extinktion** vor rund 375 Millionen Jahren löschte etwa 20 % der marinen Tierfamilien aus und reduzierte die [[Trilobiten]] auf nur noch vier Familien <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=305s" title="00:05:05">(V)</a>.

Die genaue Ursache ist ungeklärt, die Folgen sind es nicht: Innerhalb kurzer Zeit wurden große Mengen kohlenstoffreicher Sedimente abgelagert, der Sauerstoffgehalt im Wasser sank und Riffgemeinschaften brachen zusammen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=284s" title="00:04:44">(V)</a>. Während die neuen Kieferfische sowie die auf dem Land entstehenden Pflanzen und Insekten überlebten, verschwanden die meisten kieferlosen Bodenfresser — darunter die Trilobiten <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=284s" title="00:04:44">(V)</a>.

Der Fall zeigt eine wichtige Verschiebung der Ökosysteme: Überlebende waren nun Tiere mit aktiverer Lebensweise wie die Kieferfische sowie Organismen des neu besiedelten Festlands. Die Trilobiten als passive Bodenfresser ohne Kiefer gehörten zur Verliererseite — nach dem [[Evolutionäres Wettrüsten|evolutionären Wettrüsten]] mit den Fischen war ihre ökologische Nische bereits stark erodiert.

--- END NOTE ---

--- FILENAME: 40-Permanent/Symmetrie als Konsequenz der Bewegung.md
--- BEGIN NOTE ---

# Symmetrie als Konsequenz der Bewegung

**Kernidee:** Symmetrie ist keine Voreinstellung des Lebens, sondern die **logische Folge von Bewegung und Gravitation** — das "Standard-Ergebnis, nachdem man berücksichtigt hat, was sinnvoll ist".

**Ableitung über die Achsen:**
- **Schwerkraft** ergibt Oben/Unten ([[Cephalisation|Dorsoventral-Achse]]) (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=361s" title="00:06:01">(V)</a>).
- **Gerichtete Bewegung** ergibt Vorn/Hinten (Anterior/Posterior); das vordere Ende trifft zuerst auf Nahrung und Bedrohung, daher Cephalisation (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=375s" title="00:06:15">(V)</a>).
- **Links/Rechts** bleibt als "übrig gebliebene Achse" übrig ([[Körperachsen der Tiere]]) und fällt mangels Druck auf einen Spiegel zurück — das ist die [[Bilaterale Symmetrie]] (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=406s" title="00:06:46">(V)</a>).

**Hinweise aus dem Fossilbericht:** Der älteste bekannte Bilaterier [[Ikaria wutjita]] war mit Bewegung (Schlammgraben) verknüpft; die Bewegungshypothese ist aber nur die vorherrschende Erklärung — eine Alternative sieht Fluiddynamik im Körperinneren sessiler Tiere als Auslöser (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=637s" title="00:10:37">(V)</a>).

**Ergänzende Gründe:** Gerichtete Fortbewegung nutzt bilateral ([[Bilaterale Symmetrie]]) und das sparsame genetische Encoding ([[Symmetrie als sparsames genetisches Encoding]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Symmetrie als sparsames genetisches Encoding.md
--- BEGIN NOTE ---

# Symmetrie als sparsames genetisches Encoding

**Kernidee:** Ein gespiegelter Körper ist **billig zu kodieren**: Man schreibt die genetischen Instruktionen für **eine** Körperseite, und die andere läuft **von demselben Satz** ab — man erhält eine komplizierte Körperhälfte, ohne die Information doppelt zu bezahlen (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=545s" title="00:09:05">(V)</a>).

**Warum es sich auszahlt:** Jede Verbesserung oder Mutation im gemeinsamen Instruktionssatz zeigt sich **auf beiden Seiten zugleich** — man muss nicht auf dieselbe günstige Mutation an zwei getrennten Stellen warten; einmal genügt (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=545s" title="00:09:05">(V)</a>).

**Konsequenz:** Symmetrie fällt nicht nur aus der [[Symmetrie als Konsequenz der Bewegung|Bewegung heraus]], sondern passiert auch deshalb häufiger, weil sie billig ist. Umgekehrt erklärt das, warum [[Asymmetrie als abgeleitetes Merkmal|bewusste Asymmetrie]] etwas kostet: Sie muss den billigen Standard aktiv überschreiben (<a href="https://www.youtube.com/watch?v=DytckU8yfc8&t=664s" title="00:11:04">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Tauernfenster.md
--- BEGIN NOTE ---

# Tauernfenster

Das **Tauernfenster** ist das größte tektonische Fenster der Alpen: Es erstreckt sich vom Brennerpass im Westen über ~160 km bis zum Katschbergpass im Osten und umfasst eine Fläche von ~5600 km² ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).

Es ist der einzige Ort in den Ostalpen, an dem das **Europäische Grundgebirge** über eine Fläche von mehr als 100 km Breite an der Oberfläche aufgeschlossen ist — normalerweise ist dieses Grundgebirge unter den dicken Austroalpinen Decken und den ozeanischen Decken verborgen ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]). Seine heutige Struktur resultiert aus vier Prozessen: früher Ablösung und Faltung post-variszischer Deckschichten, Stapelung von Grundgebirgsdecken (Ahorn-, Tux-, Zillertal-, Eisbrugg-Gneise), Faltung des gesamten Deckenstapels in großräumige Kuppeln sowie einer Dreieckszone mit Rückfaltung am Nordrand ([[10-Raw/Field trip to the Tauern Window.pdf#page=5|Q1]]).

Das Fenster ist damit das Produkt tiefer Versenkung (bis zu 35–40 km) und mehrphasiger [[Slab Breakoff und Exhumation|Exhumation]] durch [[Laterale Extrusion der Ostalpen|laterale Extrusion]] und O-W-Extension an der [[Brenner-Normalverwerfung|Brenner-]] und Katschberg-Normalverwerfung — es dokumentiert einen kompletten Exhumationszyklus tief versenkter Kruste ([[10-Raw/Field trip to the Tauern Window.pdf#page=4|Q1]]).

Verwandte Konzepte: [[Alpine Deckentektonik]], [[Alpine Metamorphose]], [[Brenner-Normalverwerfung]], [[Laterale Extrusion der Ostalpen]]

## Einfach erklärt

Stellen Sie sich einen mehrschichtigen Kuchen vor, dessen oberste Schichten beim Kollidieren der Kontinente übereinander geschoben wurden. Das *Tauernfenster* ist dann die Stelle, an der eine Lücke in den oberen Schichten den Blick auf die tiefste Schicht freigibt — ursprünglich europäisches Grundgebirge, das sonst nirgends in den Ostalpen an der Oberfläche liegt. "Fenster" ist also ein Bild aus der Bergmannssprache: Man blickt durch die darüberliegenden Decken hindurch auf das, was normalerweise darunter verborgen ist.

Damit dieser "Blick" möglich wird, musste das Gestein erst 35–40 km nach unten gedrückt (versenkt) und dann durch mehrere Schübe wieder hochgeholt (exhumiert) werden: Auf- und Ab-Cyclen, die an einen geschlossenen thermodynamischen Kreisprozess erinnern, nur eben mit kontinentalen Platten statt eines Arbeitsgases. Für einen Physiker: Auch hier gilt Massen- und Impulserhaltung — was nach Süden verquetscht wird, muss seitlich (nach Osten) oder nach oben (Exhumation) ausweichen.

--- END NOTE ---

--- FILENAME: 40-Permanent/Time-Averaging in Sedimenten.md
--- BEGIN NOTE ---

# Time-Averaging in Sedimenten

**Definition:** Time-Averaging (Zeitmittelung) tritt auf, wenn statt eines einzigen, diskreten Zeitabschnitts **Sedimente verschiedenen Alters vermischt** werden (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=307s" title="00:05:07">(V)</a>).

**Wie es entsteht:** An einem Hügel können verschiedene Gesteins-/Sedimentschichten freiliegen, die der Regen auswäscht (erodiert); die Schuttablagerung am Hangfuß akkumuliert und bildet so eine neue Fossilfundstelle, die **alle am Hang freiliegenden Zeitperioden repräsentiert** — nicht nur eine (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=316s" title="00:05:16">(V)</a>). Ergebnis ist ein Sammelsurium von Tieren, die scheinbar nicht zusammenpassen — weil sie tatsächlich nicht zusammengehören (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=332s" title="00:05:32">(V)</a>).

**Abgrenzung im Eozän-Fall:** An den Wyominger Hochlagenfundstellen wurde Time-Averaging **ausgeschlossen**, weil gut datierte Schichten ober- und unterhalb der Sedimente lagen (<a href="https://www.youtube.com/watch?v=C6koLzdSves&t=339s" title="00:05:39">(V)</a>) — die ungewöhnliche Diversität war also real und auf [[Gebirge als Motoren der Biodiversität]] zurückzuführen.

--- END NOTE ---

--- FILENAME: 40-Permanent/Tiroler Grauvieh.md
--- BEGIN NOTE ---

# Tiroler Grauvieh

Das **Tiroler Grauvieh** ist eine Rinderrasse, die perfekt an die extremen Bedingungen des Hochgebirges angepasst ist: Die Tiere sind leicht und trittsicher und können selbst **steilste Schieferhänge beweiden** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]).

Seine wichtigste Funktion ist **Prävention durch Beweidung**: Indem das Grauvieh die Hänge abgrast, verhindert es die **Verbuschung** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]). Würde der Wald die instabilen Schieferhänge unkontrolliert überwuchern, stiege das Risiko von **Rutschungen und Lawinen** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]).

Das Grauvieh ist damit der wichtigste **biologische Partner der Talbewohner** ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 5: „Erbe und Zukunft – Bergbau, Grauvieh und sanfte Wege“|Q1]]): Es übernimmt eine Aufgabe, die früher die [[Bergmähder|Mahd]] der Bergmähder leistete — die Offenhaltung gefährdeter Hänge. Die Logik dahinter ist ökologisch wie technisch: Bäume und Sträucher erhöhen durch ihre Masse die Hanglast und ihre Wurzeln destabilisieren oberflächige Schuttlagen auf dem weichen Schiefer — beides Faktoren, die bei einem geologisch instabilen Hang wie dem [[Reissenschuh-Rutschung|Reissenschuh]] risikoverstärkend wirken.

--- END NOTE ---

--- FILENAME: 40-Permanent/Totenweg über das Tuxer Joch.md
--- BEGIN NOTE ---

# Totenweg über das Tuxer Joch

Der **Totenweg** war das letzte Geleit der Verstorbenen aus Hintertux über das [[Tuxer Joch]] zur Bestattung nach **Mauern** bei Steinach ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Ursache war die kirchliche Organisation der Schwaighof-Landschaft: Hintertux besaß kein eigenes Begräbnisrecht, alle Verstorbenen mussten auf den Friedhof der **Mutterpfarre** gebracht werden ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).

Die Route führte über den 2.338 Meter hohen Pass; die Särge wurden mühsam von **Trägern** über das Joch geschleppt ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Im Winter, wenn die Schneemassen am Joch meterhoch lagen und ein Übergang unmöglich war, war die Lösung so pragmatisch wie schaurig: Die Verstorbenen wurden **monatelang gefroren auf den Dachböden** der Bauernhäuser gelagert, bis der Frühling den Weg freigab ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]).

In Obern, beim Gasthof Steckholzer, existiert noch heute eine historische **Totenkammer**: Sie diente als letzte Station vor dem Joch oder als Zwischenlager, wenn ein Wettersturz die Träger zur Umkehr zwang ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 3: „Zwischen Leben und Tod – Die Schmirner Geschichte“|Q1]]). Der Totenweg zeigt exemplarisch, wie politische und kirchliche Grenzen das Alltagsleben — bis in den Tod hinein — bestimmten.

--- END NOTE ---

--- FILENAME: 40-Permanent/Trilobiten als biostratigraphisches Werkzeug.md
--- BEGIN NOTE ---

# Trilobiten als biostratigraphisches Werkzeug

Die Nutzung von **Trilobiten als biostratigraphisches Werkzeug** bezeichnet ihre Verwendung zur relativen Datierung und Korrelation von Gesteinsschichten. Die häufigen kambrischen Arthropoden begeisterten die Paläontologen des 19. Jahrhunderts gerade deshalb, weil ihre große Zahl und Vielfalt es erlaubte, Gesteinsschichten über weite Distanzen hinweg zeitlich zu ordnen und zu parallelisieren <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=107s" title="00:01:47">(V)</a>.

Diese Eigenschaft war die Grundlage von Walcotts Feldarbeit in Neufundland 1888: Er kartierte die Verbreitung verschiedener Trilobiten-Arten als geologisches Werkzeug <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=98s" title="00:01:38">(V)</a>. Die dabei entdeckte Diskrepanz der [[Atlantische und Pazifische Faunen|Atlantischen und Pazifischen Faunen]] zeigt die Doppelnatur dieses Werkzeugs: Trilobiten dienten nicht nur der Datierung, sondern wurden — über ihre Verteilungsmuster — zu einem Indiz für die Existenz geschlossener Ozeane und damit für die [[Kontinentaldrift]] und den [[Wilson-Zyklus]].

Trilobiten zählen zu den wichtigsten Leitfossilien der Erdgeschichte ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Leitfossilien|Q1]]). Ihre Überreste werden zur relativen Altersbestimmung von Sedimentgesteinen genutzt; diese Methodik nennt man Biostratigraphie ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Leitfossilien|Q1]]). Bestimmte Trilobitenarten kommen nur in engen zeitlichen Abschnitten vor und sind für die Ablagerungen dieser Zeit kennzeichnend — kombiniert mit ihrer weiten geographischen Ausdehnung macht das Trilobiten zu Leitfossilien des gesamten Paläozoikums, insbesondere des [[Ursprung der Trilobiten|Kambriums]] ([[10-Raw/Trilobiten (Quelle).md|Q1]]). Überliefert sind sie ausschließlich in Gesteinen des Erdaltertums; zu den ältesten gut erhaltenen gehören Arten der Gattung *Ellipsocephalus* mit ovalem Kopf ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Leitfossilien|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Trilobiten als Reliktgruppe.md
--- BEGIN NOTE ---

# Trilobiten als Reliktgruppe

**Trilobiten als Reliktgruppe** beschreibt das Endstadium ihrer Stammesgeschichte: Die spätere Evolution brachte zwar zahlreiche Neuerungen in Körperbau und Lebensweise, aber eine im Kern fast unveränderte Morphologie — die allerspätesten fossilen Trilobiten sehen den kambrischen Vertretern ausgesprochen ähnlich ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

Dem tatsächlichen Aussterben waren bereits mehrere „Beinahe-Aussterben“ bei früheren Aussterbewellen vorangegangen, die aber von wenigen Arten überlebt wurden, die sich anschließend wieder differenzieren konnten ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Anders als im Kambrium und Ordovizium, wo jeweils zahlreiche neue Arten mit unterschiedlicher Lebensweise entstanden, konnten die überlebenden Arten in den späteren Epochen nicht mehr zu vergleichbarer Vielfalt finden ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Vor ihrem endgültigen Aussterben waren die Trilobiten bereits **fast 100 Millionen Jahre lang eine artenarme Reliktgruppe** ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

Einige gut adaptierte Arten überlebten offenbar in speziellen ökologischen Nischen, die bei den Ereignissen des [[Perm-Trias-Massenaussterben|Perm-Trias-Massenaussterbens]] verloren gingen — bei diesem Ereignis starben schätzungsweise 95 % aller damals lebenden marinen Wirbellosen ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Ein Überleben einzelner Vertreter in unzugänglichen Lebensräumen wie der Tiefsee erscheint so gut wie ausgeschlossen ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Trilobiten.md
--- BEGIN NOTE ---

# Trilobiten

Die **Trilobiten** sind eine ausgestorbene Gruppe segmentierter Arthropoden, die vor rund 521 Millionen Jahren im heutigen Sibirien erstmals im Fossilbericht auftauchten <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=82s" title="00:01:22">(V)</a> und mehr als 270 Millionen Jahre lang zu den erfolgreichsten Tieren der Erde gehörten <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=24s" title="00:00:24">(V)</a>. Mit über 15.000 beschriebenen Arten zählen sie zu den vielfältigsten ausgestorbenen Organismengruppen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=361s" title="00:06:01">(V)</a>.

Ihr Erfolg beruhte auf einer Kombination anatomischer Neuheiten: bewegliche Beine, komplexe Augen, ein ausgefeilter Verdauungstrakt sowie ein Exoskelett aus Calcit und Chitin, das den gesamten Körper schützte <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=105s" title="00:01:45">(V)</a>. Diese Merkmale machten sie zu einem Gründungsmitglied der Arthropoden — der Gruppe, zu der heute Spinnentiere, Krebstiere und Insekten gehören — und ermöglichten ihnen, die kambrischen Meere zu dominieren und sich binnen 40 Millionen Jahren in mindestens 60 taxonomische Familien zu diversifizieren <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=127s" title="00:02:07">(V)</a>.

Trilobiten überlebten mehrere große Aussterbeereignisse und existierten länger als die Nicht-Vogel-Dinosaurier und länger als die Säugetiere <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=361s" title="00:06:01">(V)</a>. Sie starben schließlich im [[Perm-Trias-Massenaussterben]] vollständig aus, ohne direkte Nachfahren zu hinterlassen <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=52s" title="00:00:52">(V)</a> — ihr Ende war das Werk des größten Massensterbens der Erdgeschichte <a href="https://www.youtube.com/watch?v=Aji2VnQFUCs&t=323s" title="00:05:23">(V)</a>.

--- END NOTE ---

--- FILENAME: 40-Permanent/Truppendurchzüge und Plünderungen.md
--- BEGIN NOTE ---

# Truppendurchzüge und Plünderungen

**Truppendurchzüge und Plünderungen** beschreiben die Belastung der Zivilbevölkerung durch durchziehende Söldnerheere in der Frühen Neuzeit. Da sich Einheiten von mehreren tausend Mann nur selten selbst versorgen konnten, "organisierten" spezielle Plünderkommandos das Notwendige in der weiteren Umgebung — wenn der Kommandeur nicht zahlte, requirierten sie rücksichtslos ([[10-Raw/Inn Truppentransport.pdf#page=5|Q1]]). In Kriegszeiten uferten die Raubzüge in Gewalt aus; der Humanist Willibald Pirckheimer berichtete 1499 aus dem Engadinerkrieg von einem Weinraub im Lager bei Pfunds mit 50 Toten und über 100 Verwundeten ([[10-Raw/Inn Truppentransport.pdf#page=5|Q1]]). Auch das Passauer Kriegsvolk des Laurentius von Ramée (1609, über 10.000 Mann) brandschatzte ganze Gebiete, während die versprochenen Kompensationszahlungen ausblieben ([[10-Raw/Inn Truppentransport.pdf#page=6|Q1]]).

Zur Regulierung erließ der Tiroler Landtag 1557 die erste "ordnung der musterplätz, durchzüg und profiantheüser": Der Feldoberst musste bei seinen Soldaten bleiben, für die Nachtlager gab es Rastplätze mit Provianthäusern, und der Oberst haftete persönlich für Schäden ([[10-Raw/Inn Truppentransport.pdf#page=6|Q1]]). Seit den 1520er Jahren begleiteten Kommissare die Heeresverbände; damit konnten die gröbsten Ausschweifungen sowie Verletzte und Todesfälle reduziert werden ([[10-Raw/Inn Truppentransport.pdf#page=6|Q1]]). Der Inn war die wichtigste Alternative, um Plünderungen ganz zu vermeiden ([[10-Raw/Inn Truppentransport.pdf#page=6|Q1]], [[10-Raw/Inn Truppentransport.pdf#page=15|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Tuxer Joch.md
--- BEGIN NOTE ---

# Tuxer Joch

Das **Tuxer Joch** (2.338 m) ist ein Schlüsselpass zwischen dem **Wipptal** und dem **Zillertal** — und war über Jahrtausende die Lebensader zwischen den beiden Tälern ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]).

Die Nutzungsgeschichte reicht bis ins Mesolithikum zurück: Rund um den Pass fanden Archäologen **Jägerstationen** (Basislager), an denen Menschen rasteten und ihre Werkzeuge nachbesserten, während sie das Wild in die Hochlagen verfolgten ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Aus der **Bronzezeit** stammt eine bedeutende **Lochhalsnadel** — eine prachtvolle Gewandnadel, die belegt, dass der Pass auch von wohlhabenden Reisenden genutzt wurde ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Unter römischer Herrschaft riss die Bedeutung nie ab: Der Fund einer **römischen Goldmünze** im Passbereich sowie Hinweise auf alpine Weidewirtschaft belegen, dass das Joch eine vitale Verkehrsader im römischen Verkehrsnetz war ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]).

Für den prähistorischen Kristallhandel war das Joch der zentrale Transportweg der [[Bergkristallstraße]] ([[10-Raw/Schmirn Podcasts (Quelle).md#Podcast-Skript Episode 2: „Diamanten der Steinzeit – Das gläserne Erbe des Riepenkars“|Q1]]). Bis ins 20. Jahrhundert hinein behielt der Pass eine brisante Funktion: Über ihn führte der [[Totenweg über das Tuxer Joch|Totenweg]] der Schmirner Pfarre.

--- END NOTE ---

--- FILENAME: 40-Permanent/Ursprung der Nervensysteme.md
--- BEGIN NOTE ---

# Ursprung der Nervensysteme

**Zeitpunkt:** Molekulare Uhren ([[Molekulare Uhr]]) weisen die ersten Nervensysteme in das **Ediacarium**, vor etwa **625 Mio. Jahren** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=189s" title="00:03:09">(V)</a>). Davor waren die Vorfahren vermutlich mikroskopisch — bloße Zellbündel ohne Bedarf oder Platz für komplexe Nervensysteme (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=199s" title="00:03:19">(V)</a>).

**Ausgangsmechanismus:** Jedes Lebewesen muss seine Umwelt wahrnehmen und reagieren (Licht, Wasser, Nahrung, Konkurrenz) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=478s" title="00:07:58">(V)</a>). Einzellige Organismen tun das durch **chemisches Erkunden der Außenfläche** (ähnlich Riechen/Schmecken) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=489s" title="00:08:09">(V)</a>); einige koloniale Einzeller ([[Choanoflagellaten]]) nutzten schon primitive elektrische Signalgebung (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=496s" title="00:08:16">(V)</a>).

**Kooption:** Mit den ersten vielzelligen Organismen wurde die äußere Sensorik zur **inneren Sensorik** kooptiert, und die bewährten **elektrochemischen Signalgebungssysteme** wurden zu den **ersten Nervensystemen** (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=513s" title="00:08:33">(V)</a>).

**Fossilbericht-Herausforderung:** Im Ediacarium klaffen Gene und Fossilbericht auseinander — die molekulare Uhr sagt fortgeschrittene Cnidarier-Vorfahren voraus, aber es gibt kaum Fossilbelege; die Ediacarium-Organismen taten wenig (kaum Sinnesorgane, kaum Bewegung) (<a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=212s" title="00:03:32">(V)</a>, <a href="https://www.youtube.com/watch?v=mbG8-ejz-WE&t=239s" title="00:03:59">(V)</a>).

--- END NOTE ---

--- FILENAME: 40-Permanent/Ursprung der Trilobiten.md
--- BEGIN NOTE ---

# Ursprung der Trilobiten

Der **Ursprung der Trilobiten** liegt im Kambrium: Die ältesten Fossilien erscheinen mit Beginn der 2. Serie des Kambriums vor rund 521 Millionen Jahren ([[10-Raw/Trilobiten (Quelle).md|Q1]]). Damit ist ihr Erscheinen um die gesamte Dauer der ersten Serie (Terreneuvium) von den einschneidenden Ereignissen getrennt, die den Beginn des Kambriums markieren — der „kambrischen Explosion“ —, das sind etwa 13 Millionen Jahre ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

Die ältesten Trilobiten sind zugleich die ältesten unzweideutigen Körperfunde von Arthropoden überhaupt ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Sie treten in verschiedenen Erdregionen — den Flachmeeren der Kontinentalplatten des auseinanderbrechenden Superkontinents Rodinia — grob gleichzeitig auf, mit erkennbar verwandten, aber deutlich verschiedenen Formen ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

Dieses vikariierende Verbreitungsmuster zeigt, dass der tatsächliche Ursprung älter sein muss: Der Ausbreitung in die anderen Meeresregionen und der anschließenden evolutiven Auseinanderentwicklung musste ein gemeinsamer Ursprung vorausgegangen sein ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Diese nur erschlossene, nicht durch Fossilien belegbare Existenzperiode — als Ghost Range (Geisterlinie) bezeichnet — wird auf etwa 10 Millionen Jahre geschätzt ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

In den wenigen Konservatlagerstätten der frühen Kambrium-Formationen (etwa der chinesischen Chengjiang-Faunengemeinschaft) sind Trilobiten zwar nur eine Minderheit unter vielen unverkalkten, trilobiten-ähnlichen Arthropoden — aber genau diese Funde liefern den stammesgeschichtlichen Kontext des [[Trilobiten|Trilobiten-Ursprungs]] ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Vernetzung, Mobilität und Mit-Gestaltung.md
--- BEGIN NOTE ---

# Vernetzung, Mobilität und Mit-Gestaltung

> Die Quelle analysiert Digitalisierung als gesellschaftlichen Metaprozess, der Vernetzung, Mobilität und Mitgestaltung fördert. Digitale Medien reduzieren räumliche Distanzen, ermöglichen globale Kollaboration und verändern die Art, wie Menschen lernen und arbeiten. Bildung muss diese neuen Handlungsmuster integrieren.

# Vernetzung, Mobilität und Mit-Gestaltung
Die Quelle sieht Digitalisierung und Mediatisierung nicht bloß als technische Innovationen, sondern als gesellschaftliche Prozesse, die die Struktur des Alltags verändern. Ein zentrales Merkmal ist die Vernetzung: Digitale Medien reduzieren räumliche und zeitliche Distanz und verknüpfen Menschen, Informationen und Institutionen in komplexen Kommunikationsnetzen [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=13|Q1]]. Diese Vernetzung ist im Sinne Castells nicht nur ein technischer Effekt, sondern eine grundlegende Umformung der sozialen Ordnung, weil sie den Austausch von Informationen, Arbeit und Kommunikation in globalen Netzwerken organisiert [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=13|Q2]].

Ein zweites wichtiges Element ist Mobilität. Die Quelle betont, dass mobile digitale Endgeräte die Reichweite von Kommunikation und Zugang zu Informationen stark erweitern. Smartphones und Tablets ermöglichen jederzeit Zugang zu Daten, zu Kommunikationskanälen und zu Kollaborationsformen, unabhängig davon, wo sich der Nutzer gerade befindet [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=14|Q3]]. Die dadurch entstandenen „Freiheitsgeraden“ zeigen, dass digitale Technologien nicht nur das Handeln im Alltag erleichtern, sondern neue Muster von verteiltem, zeitlich flexiblen und ortsunabhängigem Lernen und Arbeiten hervorbringen [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=14|Q4]].

Der dritte Aspekt ist die (Mit-)Gestaltung von Welt. Die Quelle beschreibt, dass digitale Medien kulturelle Materialien nicht bloß speichern, sondern in einem größeren Maß reproducierbar, weiterverteilbar und kollaborativ bearbeitbar machen. Fotos, Texte, Audio- und Videodaten werden zunehmend digital verfügbar und können von vielen Akteuren geteilt, bearbeitet und neu verwendet werden [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=15|Q5]]. Dadurch entsteht eine Form von Teilhabe und gemeinschaftlicher Konstruktion, in der die Welt nicht nur konsumiert, sondern aktiv mitgestaltet wird. Genau hier zeigt sich die gesellschaftliche Konsequenz der Digitalisierung: Sie verändert nicht bloß Medien, sondern auch die Weise, wie Kultur, Öffentlichkeit und Alltag entstehen [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=15|Q6]].

Damit bildet dieser Bereich den Übergang zur Bildungsfrage: Wenn digitale Medien die Gesellschaft in Netzwerke, Mobilität und Teilhabe transformieren, dann verändert sich auch die Art und Weise, wie Bildung verläuft. Die Quelle macht damit deutlich, dass Digitalisierung und Mediatisierung nicht nur technische Rahmenbedingungen sind, sondern zentrale Strukturen der Gegenwartsgesellschaft, die für Lernen, Teilhabe und Selbstbildung unmittelbar relevant sind [[10-Raw/1_TFLE1 Bildung in der digitalisierten Gesellschaft.pdf#page=16|Q7]].

--- END NOTE ---

--- FILENAME: 40-Permanent/Verwandtschaft der Trilobiten.md
--- BEGIN NOTE ---

# Verwandtschaft der Trilobiten

Die **Verwandtschaft der Trilobiten** mit den lebenden (rezenten) Arthropodenordnungen der Spinnentiere und der Krebstiere ist durch neue Fossilfunde aus dem Kambrium zu einer offenen Frage geworden ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Sie hängt in kritischer Weise von der Interpretation der Homologie verschiedener Körpersegmente ab, insbesondere des Kopfes und der allerersten Extremitätenpaare ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

Zwei Positionen stehen sich gegenüber ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]):

- **Arachnata/Arachnomorpha**: Die traditionelle Auffassung, nach der Trilobiten gemeinsam mit den Spinnentieren diese Gruppe bilden ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).
- **Nähere Verwandte der Krebstiere**: vertreten von Forschern, die die Lage des Antennensegments anders interpretieren ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

Entscheidend ist die Deutung des Antennensegments: Die Antennen der Trilobiten sitzen am Kopfsegment des Deutocerebrums (zweiter Gehirnabschnitt) am Hypostom, während die Antennen der rezenten Stummelfüßer (Onychophora) am ersten Kopfabschnitt sitzen — je nach Interpretation der umstrittenen Antennenlage zahlreicher Fossilien verschieben sich die erschlossenen Verwandtschaftsverhältnisse ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

Unabhängig von dieser Frage gilt: Der dreilappige [[Körperbau der Trilobiten|Körperbau]], das Spaltbein sowie Kopf- und Schwanzschild sind gemeinsames Erbe der Arthropoden (Plesiomorphien) — Merkmale, die zuerst an Trilobiten beschrieben wurden, der Gruppe aber nicht eigentümlich sind, sondern von ihren Vorfahren vererbt wurden ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]). Dies belegen auch unverkalkte trilobiten-ähnliche Gruppen (Trilobitoidea, Trilobitomorpha, Lamellipedia) aus den Konservatlagerstätten des [[Ursprung der Trilobiten|frühen Kambriums]] ([[10-Raw/Trilobiten (Quelle).md#Trilobiten als Zeugen der Evolution|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Wiener Doppelhochzeit 1515.md
--- BEGIN NOTE ---

# Wiener Doppelhochzeit 1515

Die **Wiener Doppelhochzeit** (1515) war die Doppelverlobung zwischen den Enkeln Maximilians I. und den Kindern König Vladislavs II. von Böhmen und Ungarn: Erzherzog Ferdinand I. (alternativ Karl V.) mit Anna von Böhmen und Ungarn sowie Erzherzogin Maria mit Ludwig II. ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).

Sie war das Ergebnis des [[Pressburger Vertrag 1491|Pressburger Vertrags]] und des 1506 entwickelten Plans wechselseitiger Heiraten, mit dem Maximilian Böhmen und Ungarn für Habsburg sichern wollte ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]). Auf dem Wiener Fürstentag traf er sich 1515 mit den jagiellonischen Königen Vladislav II. und Sigismund I. von Polen, um den wachsenden Druck der Beistandsverträge Frankreichs, Polens, Ungarns, Böhmens und Russlands zu vermindern ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]).

Die 1521 vollzogenen Ehen zahlten sich aus: Nach dem Tod Ludwigs II. 1526 fielen die Kronen von Böhmen und Ungarn an das Haus Habsburg ([[10-Raw/Maximilian I. (HRR).md#Herr der Habsburgischen Erblande, regierender König und Kaiser|Q1]]). Die Doppelhochzeit ist damit das erfolgreichste Beispiel der [[Habsburgische Heiratspolitik|habsburgischen Heiratspolitik]] Maximilians.

Verwandte Konzepte: [[Pressburger Vertrag 1491]], [[Habsburgische Heiratspolitik]]

--- END NOTE ---

--- FILENAME: 40-Permanent/Wilhelm Biener.md
--- BEGIN NOTE ---

# Wilhelm Biener

**Wilhelm Biener** (um 1590–1651) war der letzte Kanzler von Tirol und dient in der Quelle als prominentes Beispiel für einen Gefangenen, dessen letzte Reise über den Inn führte ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]). Nach dem Studium der Rechtswissenschaft in Freiburg im Breisgau und Ingolstadt berief ihn Kaiser Ferdinand II. 1630 in den Reichshofrat; als Hofkanzler der österreichischen Vorlande beriet er Erzherzog Leopold V. und nach dessen Tod dessen Witwe Claudia de Medici und setzte sich für aufklärerische Ideen und eine von Korruption befreite Verwaltung ein ([[10-Raw/Inn Truppentransport.pdf#page=14|Q1]]).

Nach dem Tod der Landesfürstin 1648 übernahm Biener das Kanzleramt für den jungen Erzherzog Ferdinand Karl. Weil er dessen aufwändigen Lebensstil kritisierte, hetzten einflussreiche Gegner, die unter seiner Unbestechlichkeit gelitten hatten, den Landesfürsten gegen den Kanzler auf; ein äußerst einseitiger Schauprozess verurteilte ihn zum Tode ([[10-Raw/Inn Truppentransport.pdf#page=15|Q1]]). Seine letzte Reise trat Biener auf dem Inn an: unter strengster Bewachung von Hall nach Rattenberg gebracht, wurde er am 17. Juli 1651 im Innenhof der Burg Rattenberg enthauptet ([[10-Raw/Inn Truppentransport.pdf#page=15|Q1]]). Ein bereits unterzeichnetes kaiserliches Gnadengesuch hatte der Kammerpräsident Schmaus abgefangen — als der Bote die Burg erreichte, war es bereits zu spät ([[10-Raw/Inn Truppentransport.pdf#page=15|Q1]]).

--- END NOTE ---

--- FILENAME: 40-Permanent/Wilson-Zyklus.md
--- BEGIN NOTE ---

# Wilson-Zyklus

Der **Wilson-Zyklus** ist eine Kerntheorie der Plattentektonik, benannt nach dem kanadischen Geologen John Tuzo Wilson. Er beschreibt, wie Ozeanbecken sich entlang derselben Kollisionsgrenzen schließen und wieder öffnen — statt dass sich zusammengesetzte Kontinente jedes Mal auf neue Weise zerbrechen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=398s" title="00:06:38">(V)</a>.

1966 war Wilson der erste, der fragte, ob der Atlantik tatsächlich geschlossen und wieder geöffnet wurde <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=381s" title="00:06:21">(V)</a>. In den folgenden Jahrzehnten wurde diese Idee zur Kerntheorie der Plattentektonik ausgebaut <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=389s" title="00:06:29">(V)</a>. Der Zyklus umfasst acht Hauptstadien — von Dehnung und Rifting über Meeresbodenspreizung und reifen Ozean bis zu Subduktion, Schließung, Kollision und Stabilität ([[Die acht Phasen des Wilson-Zyklus]]) <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=410s" title="00:06:50">(V)</a>.

Der Zyklus hängt mit Superkontinent-Zyklen zusammen, läuft aber in kleinerem geografischem Maßstab und kürzerer geologischer Zeitspanne ab <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=571s" title="00:09:31">(V)</a>. Da Suturzonen Schwächezonen der Kruste sind, bleiben dieselben Plattengrenzen über hunderte Millionen Jahre erhalten <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=675s" title="00:11:15">(V)</a> — das erlaubt, vergangene und künftige Ozeane zu rekonstruieren bzw. vorherzusagen <a href="https://www.youtube.com/watch?v=BMJJoAtvHiY&t=689s" title="00:11:29">(V)</a>.

--- END NOTE ---

--- FILENAME: 40-Permanent/Wittelsbacher Hausvertrag von Pavia.md
--- BEGIN NOTE ---

# Wittelsbacher Hausvertrag von Pavia

Der **Wittelsbacher Hausvertrag von Pavia** regelte die Erbfolge im Haus Wittelsbach. Der Vertrag legte fest, dass bei Aussterben einer männlichen Linie die Besitzungen an die jeweils andere Linie fallen sollten ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]).

Herzog Georg der Reiche von Bayern-Landshut brach diese Regel mit seinem Testament vom 19. September 1496: Er setzte seine Tochter Elisabeth, deren Gemahl Ruprecht von der Pfalz und deren Söhne als Erben ein ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]). Dieser Vertragsbruch war die rechtliche Grundlage des Anspruchs von Albrecht IV. von Bayern-München, der die Erbregelung nicht akzeptierte und nach Georgs Tod am 1. Dezember 1503 den Landshuter Erbfolgekrieg auslöste ([[10-Raw/Landshuter Erbfolgekrieg (Quelle).md#Vorgeschichte|Q1]]). Der Hausvertrag war damit nicht nur ein privatrechtliches Instrument, sondern bestimmte die politische Ordnung des Reiches: Seine Verletzung eskalierte zum Krieg zwischen den wittelsbachischen Linien.

--- END NOTE ---

--- FILENAME: 40-Permanent/Zerrklüfte.md
--- BEGIN NOTE ---

# Zerrklüfte

**Zerrklüfte** sind Entspannungsrisse, die sich aufreißen, wenn ein Gebirge nach der tiefen Versenkung gehoben und der Druck entlastet wird — im Tauernfenster ein zentrales Phänomen der Spätphase der Deformationsgeschichte ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).

Im Tauernfenster öffneten sich die Zerrklüfte **genau in Ost-West-Richtung** und dokumentieren damit die regionale Dehnung: Alle Gesteine sind in diese Richtung gedehnt und gestreckt, Minerale parallel eingeregelt, und die Klüfte füllten sich mit Muskowit, Periklin, Bergkristall und anderen Mineralen, die erhöhte Temperaturen anzeigen ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]). Auch die Hornblendenädelchen der Amphibolite am Langsee sind streng parallel ausgerichtet — sie wuchsen während derselben Ost-West-Dehnungsphase; dort sind die Zerrklüfte meist mit Chlorit, Quarz und Periklin gefüllt ([[10-Raw/Tauernfenster (Quelle).md#Seite 10|Q1]]).

Zerrklüfte sind **Temperatur-Thermometer in der Landschaft**: Der derbe Quarz der meisten Klüfte entstand bei relativ geringer Temperatur während der Hebungsphase, ältere Klüfte mit Muskowit, Periklin und klarem Quarz bei höheren Temperaturen in einer Phase, in der das Gestein nicht mehr ganz plastisch reagierte ([[10-Raw/Tauernfenster (Quelle).md#Seite 8|Q1]]). Allgemein erklärt die Vielfalt an Mineralien (Quarz, Adular, Periklin; Muskowit, Biotit, Rutil, Titanit in höher temperierten; Chlorit/Pennin, Apatit, Laumontit, Pyrit in kühleren Klüften) sich daraus, dass die Spalten zu unterschiedlichen Zeiten und Temperaturen aufrissen und jedes Gestein etwas differierende Lösungen lieferte ([[10-Raw/Tauernfenster (Quelle).md#Seite 3|Q1]]).

Rare Mineralfunde wie **Lazulith, Manganepidot und Hämatit** in den Quarzschiefern am Pfitscher Joch gehören ebenfalls in diesen Klüfte-Kontext ([[10-Raw/Tauernfenster (Quelle).md#Seite 9|Q1]]).

--- END NOTE ---

# 50-MOC — Maps of Content (15 Notizen)

--- FILENAME: 50-MOC/_Index MOC.md
--- BEGIN NOTE ---

# 🗺 Index der Maps of Content (MOCs)

*Zentraler Überblick über alle entstehenden Themenkarten im Vault.*

---

## Großfachgebiete

*Umfassende MOCs für die Hauptdisziplinen im Vault.*

- [[Bildung]] — Bildungsforschung: Klassische und moderne Bildungsphilosophie, Digitalisierung, Mediatisierung
- [[Geschichte]] — Europäische Geschichte: Habsburgische Expansion, Landshuter Erbfolgekrieg, Reichsreformen, Inn-Militärwesen
- [[Geologie]] — Alpine Geologie: Tektonik, Tauernfenster, Trilobiten, Hangdeformationen

## Spezialisierte Themenbereiche

*Vertiefende MOCs zu einzelnen Themenfeldern.*

- [[Trilobiten als Fossilgruppe]] — Paläontologie: Anatomie, Lebensweise, Ursprung, Systematik und Aussterbeereignisse der Trilobiten
- [[Inn und Militärtransport]] — Geschichte Tirols: Innschifffahrt als Militärweg, Kufstein 1504, Galeerenstrafe
- [[Landshuter Erbfolgekrieg]] — Reichsgeschichte: Wittelsbacher Erbfolgekonflikt, Kölner Schiedsspruch, Habsburger Gebietsgewinne
- [[Reichsreform 1495]] — Rechtsgeschichte: Ewiger Landfrieden, Reichskammergericht, Reichskreise, Gemeiner Pfennig
- [[Aufstieg des Hauses Habsburg]] — Dynastiegeschichte: Heiratspolitik, Burgund, Spanien, Böhmen/Ungarn, Selbstinszenierung
- [[Wilson-Zyklus und Ozeanreinkarnation]] — Geologie/Paläontologie: Iapetus-Ozean, Kontinentaldrift, Trilobiten als Beleg
- [[Tauernfenster und Ostalpen]] — Alpengeologie: Tauernfenster, Deckentektonik, Alpine Metamorphose, Brenner-Normalverwerfung
- [[Schmirntal]] — Regionalgeschichte Tirols: Geologie des Tauernfensters, Bergkristallbergbau, Schwaighöfe, Bergsteigerdorf
- [[Symmetrie im Tierreich]] — Evolutionsbiologie: Körperachsen, bilaterale/radiale Symmetrie, Links-Rechts-Festlegung, Asymmetrie
- [[Evolution der Gehirne]] — Neurobiologie/Evolutionsbiologie: Nervensysteme, Gehirne, Haootia, fossile Hirne des Kambriums
- [[Eozäne Primaten und Gebirgsdiversität]] — Paläontologie/Mammalogie: eozäne Primaten, Omomyoiden, Gebirgsdiversität, Refugia

---

## System-MOCs

- [[Home]] — Zentrales Dashboard
- [[70-Meta/Vault Guide|Vault Guide]] — Workflow & Dokumentation
- [[70-Meta/KI-Anweisungen|KI-Anweisungen]] — Verbindliche KI-Regeln

--- END NOTE ---

--- FILENAME: 50-MOC/Aufstieg des Hauses Habsburg.md
--- BEGIN NOTE ---

# Aufstieg des Hauses Habsburg

*Map of Content — reiner Navigations-Hub, kein eigener Inhalt.*

## Permanent Notes

- [[Habsburgische Heiratspolitik]] — das zentrale Instrument des habsburgischen Aufstiegs
- [[Burgundisches Erbe Maximilians]] — der Erwerb Burgunds durch Heirat mit Maria
- [[Habsburgisch-französischer Gegensatz]] — die strukturelle Rivalität als Kehrseite des Aufstiegs
- [[Pressburger Vertrag 1491]] — der Erbvertrag für Böhmen und Ungarn
- [[Wiener Doppelhochzeit 1515]] — die Doppelverlobung, die 1526 die Kronen einbrachte
- [[Erwählter Römischer Kaiser]] — der Kaisertitel ohne päpstliche Krönung
- [[Maximilians Selbstinszenierung]] — der "letzte Ritter" als moderne Propagandastrategie
- [[Schulden Maximilians I.]] — die Finanznot hinter dem Prunk
- [[Collegium poetarum et mathematicorum]] — die Institutionalisierung des Humanismus

## Narrative Notes

- [[Aufstieg des Hauses Habsburg durch Heiratspolitik]] — Warum die Sonne im Habsburgerreich nicht mehr unterging
- [[Maximilians Selbstinszenierung als letzter Ritter]] — Wie ein moderner Herrscher sein ritterliches Image konstruierte

## Verwandte MOCs

- [[Reichsreform 1495]] — die innenpolitische Seite der Herrschaft Maximilians
- [[Landshuter Erbfolgekrieg]] — Maximilian als Schiedsrichter der Reichspolitik
- [[Inn und Militärtransport]] — die Tiroler Gebietsgewinne Maximilians am Inn
- [[_Index MOC]]

--- END NOTE ---

--- FILENAME: 50-MOC/Bildung.md
--- BEGIN NOTE ---

# Bildung MOC

Landkarte der Bildungsforschung und -konzepte in der digitalisierten Welt.

## Bildungskonzepte & Theorie

### Klassische Bildungsphilosophie
- [[Paideia]] - Antikes Bildungsideal
- [[Humboldt und die allgemeine Menschenbildung]] - Humboldts Bildungsbegriff
- [[Kant und die Autonomie der Bildung]] - Kant's Autonomie-Konzept
- [[Rousseau und die Erziehung zum Menschsein]] - Rousseaus Erziehungsphilosophie

### Bildung als Konzept
- [[Bildung als Deutungsmuster]] - Bildung als kulturelle Deutung
- [[Bildung als Subjektkonstitution]] - Bildung und Identität
- [[Bildung als historisches Gedächtnis]] - Bildung und historisches Bewusstsein
- [[Bildung als individueller Bestand und Vermögen]] - Bildung als Fähigkeiten
- [[Bildung als Selbstüberschreitung]] - Transformatives Bildungsverständnis

## Digitalisierung & Mediatisierung

### Grundkonzepte
- [[Mediatisierung und Digitalisierung]] - Überblick der Mediatisierung
- [[Mediatisierung als Metaprozess]] - Mediatisierung als strukturelles Phänomen
- [[Seamless Learning]] - Durchgängiges Lernen über Kontexte
- [[Vernetzung, Mobilität und Mit-Gestaltung]] - Zentrale Dimensionen digitaler Bildung

### Raum und Zeit
- [[Raum, Zeit und Entgrenzung in der digitalen Bildung]] - Transformation von Lernräumen

## Synthesedarstellungen

- [[Bildung zwischen Tradition und digitalem Wandel]] - Integration von Tradition und Innovation
- [[Bildung in einer vernetzten und mediatisierten Lebenswelt]] - Holistische Perspektive auf moderne Bildung

---

## Struktur dieser MOC

Diese MOC verbindet:
- **Philosophische Grundlagen**: Klassische Bildungsdenker
- **Moderne Konzepte**: Zeitgenössische Bildungstheorie
- **Digitale Transformation**: Mediatisierung und ihre Folgen
- **Synthesen**: Überblicksdarstellungen, die verschiedene Aspekte integrieren

## Nächste Schritte

- Weitere Facetten der digitalen Kompetenzentwicklung erforschen
- Kulturelle und gesellschaftliche Implikationen vertiefen
- Praktische Anwendungsszenarien dokumentieren

--- END NOTE ---

--- FILENAME: 50-MOC/Eozäne Primaten und Gebirgsdiversität.md
--- BEGIN NOTE ---

# Eozäne Primaten und Gebirgsdiversität

*MOC zu den eozänen Primaten Nordamerikas und der Rolle von Gebirgen für Speziation und Refugien.*

## Primaten Nordamerikas

- [[Eozäne Primaten Nordamerikas]]
- [[Omomyoiden]]
- [[Anaptomorphine und Omomyine]]
- [[Adapoidea]]

## Warum Berge Biodiversität erzeugen

- [[Gebirge als Motoren der Biodiversität]]
- [[Speziation durch Habitatvariation]]
- [[Refugia]]
- [[Time-Averaging in Sedimenten]]

## Höhenlage-Verfälschung des Fossilberichts

- [[Multituberculata]]

## Quellen

- [[How Mountains Make Evolution Weird]]

--- END NOTE ---

--- FILENAME: 50-MOC/Evolution der Gehirne.md
--- BEGIN NOTE ---

# Evolution der Gehirne

*MOC zu Entstehung und Evolution der Nervensysteme und Gehirne.*

## Grundlagen

- [[Nervensystem]]
- [[Neuronen-Netz]]
- [[Gehirn als zentraler Verarbeitungshub]]

## Ursprung und Evolution

- [[Ursprung der Nervensysteme]]
- [[Molekulare Uhr]]
- [[Choanoflagellaten]]
- [[Evolution des Nervensystems]]
- [[Kambrium-Explosion]]

## Gehirn und Muskeln

- [[Gehirne brauchen Muskeln]]
- [[Haootia]]

## Erhaltung im Fossilbericht

- [[Burgess Shale]]
- [[Fossile Hirne des Kambriums]]

## Quellen

- [[How Brawn Led to Brains]]

--- END NOTE ---

--- FILENAME: 50-MOC/Geologie.md
--- BEGIN NOTE ---

# Geologie MOC

Landkarte der alpinen Geologie, Tektonik und der Trilobiten als evolutionäre Zeugen.

## Alpine Tektonik & Orogenese

### Großräumliche Prozesse
- [[Kontinentaldrift]] - Plattenbewegung und Kontinente
- [[Penninisch-Ligurischer Ozean]] - Verschwundene ozeanische Lithosphäre
- [[Die acht Phasen des Wilson-Zyklus]] - Narrative zum Zyklus
- [[Wilson-Zyklus]] - Ozeanreinkarnation und Orogenese
- [[Wilson-Zyklus und Ozeanreinkarnation]] - MOC zum Konzept

### Ostalpen-Spezifik
- [[Entstehung der Ostalpen entlang des TRANSALP-Profils]] - Narrative zur Entstehung
- [[Eoalpine Orogenese]] - Frühe Orogenese-Phase
- [[Laterale Extrusion der Ostalpen]] - Horizontalverschiebungen
- [[Slab Breakoff und Exhumation]] - Prozesse der Krustenheraushebung
- [[Alpine Deckentektonik]] - Überschiebungstektonik
- [[Alpine Metamorphose]] - Metamorphe Umwandlungen

### Das Tauernfenster - Fenster in die Tiefe
- [[Tauernfenster]] - Fenster in metamorphe Kruste
- [[Das Tauernfenster als tektonisches Exhumationsfenster]] - Narrative
- [[Tauernfenster und Ostalpen]] - MOC zum Fenster
- [[Die Brenner-Normalverwerfung und die Exhumation der Ostalpen]] - Narrative
- [[Brenner-Normalverwerfung]] - Abschiebungstektonik
- [[Iapetus-Sutur]] - Alte Suturzone

## Das Schmirntal - Geologisches Laboratorium

### Tektonische Strukturen
- [[Das Schmirntal als geologisches Labor des Tauernfensters]] - Narrative
- [[Schmirntal]] - MOC zum Tal
- [[Die Deformationsgeschichte des Tauernfensters in vier Phasen]] - Narrative Synthese
- [[Metamorphe Schieferhülle (Tauernfenster)]] - Gesteine und Strukturen
- [[Furtschaglschiefer]] - Spezifisches Gestein
- [[Konglomeratgneis]] - Protolith und Metamorphose
- [[Geothermobarometrie]] - Druck-Temperatur-Rekonstruktion

### Gravitative Prozesse
- [[Der Reissenschuh als Referenzmodell tiefgreifender Hangdeformationen]] - Narrative
- [[Reissenschuh-Rutschung]] - Großflächige Deformation
- [[Gravitative Kaskadenprozesse am Reissenschuh]] - Prozessverkettung
- [[Der Pfitscher Bergsturz und der verschwundene Stausee]] - Narrative zum Bergsturz
- [[Pfitscher Bergsturz]] - Historischer Bergsturz
- [[Zerrklüfte]] - Strukturen in Hangdeformationen
- [[Monitoring gravitativer Hangdeformationen]] - Moderne Überwachung
- [[EMOD-SLAP]] - Monitoringmethode

### Hydrologie & Geochemie
- [[Quellhydrochemie des Tauernfensters]] - Wasser als Tracer
- [[Molybdänbergwerk Alpeiner Scharte]] - Hydrothermale Mineralisierung

### Kulturelle und Ethnobotanische Aspekte
- [[Ethnobotanik im Schmirntal]] - Pflanzliche Ressourcen und Nutzung
- [[Bergkristallstraße]] - Historische Handelswege
- [[Bergkristallbergbau am Riepenkar]] - Rohstoffabbau
- [[Wie der Bergkristall vom Riepenkar ein prähistorisches Handelsnetz erschloss]] - Narrative
- [[Totenweg über das Tuxer Joch]] - Sakrale Pfade
- [[Zwischen Pass und Pfarre - Wie politische Grenzen den Totenweg erzwangen]] - Narrative
- [[Alpenblumen- und Kräutergarten Toldern]] - Botanische Vielfalt
- [[Tiroler Grauvieh]] - Züchtung alpiner Rinder
- [[Bergmähder]] - Traditionelle Landwirtschaft
- [[Bergsteigerdorf]] - Moderne Nutzung
- [[Schwaighöfe]] - Alpenkultur
- [[Sakrale Landschaft des Schmirntals]] - Religiöse Topographie
- [[Tuxer Joch]] - Pass und historischer Ort

## Trilobiten - Zeugen der Evolution

### Evolutionäre Perspektive
- [[Trilobiten]] - Überblick der Arthropoden
- [[Entwicklung der Trilobiten]] - Evolutionsgeschichte
- [[Ursprung der Trilobiten]] - Früheste Formen
- [[Ordnungen der Trilobiten]] - Systematik und Vielfalt
- [[Verwandtschaft der Trilobiten]] - Phylogenetische Beziehungen
- [[Trilobiten als Reliktgruppe]] - Persistenz über geologische Zeit

### Morphologie & Biologie
- [[Körperbau der Trilobiten]] - Anatomie und Struktur
- [[Facettenaugen der Trilobiten]] - Optische Systeme
- [[Gesichtsnaht und Häutung der Trilobiten]] - Wachstum und Ecdysis
- [[Lebensweise der Trilobiten]] - Ökologie und Ethologie
- [[Schwarmintelligenz bei Trilobiten]] - Kollektives Verhalten

### Paläontologische Bedeutung
- [[Der Niedergang der Trilobiten]] - Narrative zum Aussterben
- [[Ordovizium-Silur-Extinktion]] - Massenaustauung
- [[Spätdevon-Extinktion]] - Weitere Krise
- [[Perm-Trias-Massenaussterben]] - Endkrise
- [[Trilobiten als biostratigraphisches Werkzeug]] - Zur Altersbestimmung
- [[Trilobiten als Fossilgruppe]] - MOC zur Paläontologie
- [[Trilobiten als Zeugen der Evolution]] - Narrative zur Evolution
- [[Wie Trilobiten den Wilson-Zyklus aufdeckten]] - Narrative zur Tektonik

## Historische Geologie & Umweltgeschichte

### Biografische Perspektive
- [[John Tuzo Wilson]] - Geologe und Theoretiker
- [[Wilhelm Biener]] - Lokaler Forscher

### Erdgeschichte & Ozeanzyklen
- Diese MOC verbindet Plattentektonik (Wilson-Zyklus), alpine Orogenese, quartäre Gletscher und Trilobiten als langfristige biostratigraphische Marker

---

## Struktur dieser MOC

Diese MOC verbindet:
- **Tektonische Prozesse**: Wilson-Zyklus, Orogenese, Exhumation
- **Regionale Fokus**: Tauernfenster und Schmirntal als Fallstudien
- **Moderne Prozesse**: Gravitative Hangdeformationen und ihre Überwachung
- **Biostratigraphie**: Trilobiten als Fenster in die Erdgeschichte
- **Kulturgeologie**: Integration von Geologie, Kulturlandschaft und Mensch

## Nächste Schritte

- Vertiefung der mikrostrukturellen Analyse
- Integration von Seismik und modernen Geophysik-Methoden
- Vergleich mit anderen tektonischen Fenstern weltweit
- Verbindung zu Klimageschichte und Eis-Pausen

--- END NOTE ---

--- FILENAME: 50-MOC/Geschichte.md
--- BEGIN NOTE ---

# Geschichte MOC

Landkarte der europäischen Geschichte im Fokus auf die Habsburgische Expansion und den Landshuter Erbfolgekrieg.

## Habsburgische Machtpolitik

### Heiratspolitik & Dynastische Strategie
- [[Habsburgische Heiratspolitik]] - Strategisches Heiraten als Machtinstrument
- [[Aufstieg des Hauses Habsburg durch Heiratspolitik]] - Narrative zur Machtentwicklung
- [[Wiener Doppelhochzeit 1515]] - Vertrag mit Polen-Litauen
- [[Burgundisches Erbe Maximilians]] - Erbschaft und deren Folgen
- [[Habsburgisch-französischer Gegensatz]] - Rivalität um europäische Hegemonie
- [[Pressburger Vertrag 1491]] - Frühe Verträge Maximilians

### Maximilian I. - Kaiser und Politiker
- [[Maximilians Selbstinszenierung als letzter Ritter]] - Narrative zur Inszenierung
- [[Erwählter Römischer Kaiser]] - Titel und Legitimation
- [[Schulden Maximilians I.]] - Finanzielle Realitäten
- [[Collegium poetarum et mathematicorum]] - Kulturelle Aktivitäten

## Der Landshuter Erbfolgekrieg (1504-1505)

### Ursachen & Ausgangslage
- [[Ursachen des Landshuter Erbfolgekriegs]] - Politische und persönliche Gründe
- [[Junge Pfalz]] - Pfalzische Konkurrenten
- [[Landshuter Erbfolgekrieg]] - MOC zum Krieg

### Militärische Dimensionen
- [[Belagerung von Kufstein 1504]] - Strategisches Schlüsselereignis
- [[Hall in Tirol als Zentrum der Militärschifffahrt]] - Logistische Basis

### Politische Folgen
- [[Maximilians Gebietsgewinne im Landshuter Erbfolgekrieg]] - Territoriale Expansion
- [[Der Kölner Schiedsspruch als territoriale Neuordnung]] - Narrative zum Friedensschluss
- [[Kölner Schiedsspruch 1505]] - Friedensvertrag
- [[Wittelsbacher Hausvertrag von Pavia]] - Weitere Verträge

## Reichsreform 1495

### Strukturelle Reformen
- [[Die Reichsreform von 1495]] - Narrative zur Reform
- [[Reichsreform von 1495]] - Permanent Note
- [[Reichskammergericht]] - Neue Justizinstitution
- [[Gemeiner Pfennig]] - Steuerreformen
- [[Reichskreise]] - Neue territoriale Ordnung
- [[Reichsregiment]] - Verwaltungsstruktur

### Innenpolitische Folgen
- [[Ewiger Landfrieden]] - Friedenswahrung und Konfliktregelung
- [[Reichsacht]] - Strafmechanismus

## Transportwege & Militärische Infrastruktur

### Der Inn als Logistisches Netzwerk
- [[Der Inn als militärischer Transportweg]] - Narrative zur Infrastruktur
- [[Innschifffahrt als militärischer Transportweg]] - Permanent Note
- [[Plätten und Schiffszug]] - Technologie des Schiffstransports
- [[Truppendurchzüge und Plünderungen]] - Auswirkungen auf die Bevölkerung

### Strafjustiz & Gefangenenwesen
- [[Gefangene und Galeeren auf dem Inn]] - Narrative zur Strafvollzug
- [[Galeerenstrafe]] - Strafform und Umsetzung

---

## Struktur dieser MOC

Diese MOC verbindet:
- **Dynastische Strategien**: Habsburgische Machtentwicklung durch Heirat und Krieg
- **Politische Militärgeschichte**: Landshuter Erbfolgekrieg als Fallstudie
- **Institutionelle Reformen**: Reichsreform 1495 und ihre Institutionen
- **Infrastruktur & Logistik**: Der Inn als militärisches und wirtschaftliches Netzwerk

## Nächste Schritte

- Vertiefung der Mediävistik und Frühneuzeit
- Kulturelle Aspekte der Habsburgischen Herrschaft
- Vergleich mit anderen europäischen Dynastien

--- END NOTE ---

--- FILENAME: 50-MOC/Inn und Militärtransport.md
--- BEGIN NOTE ---

# Inn und Militärtransport

*Map of Content — reiner Navigations-Hub, kein eigener Inhalt.*

## Permanent Notes

- [[Innschifffahrt als militärischer Transportweg]] — Kernkonzept: der Inn als schnelle, schadensarme Truppenroute
- [[Plätten und Schiffszug]] — Schiffstypen und Zugbetrieb auf dem Inn
- [[Hall in Tirol als Zentrum der Militärschifffahrt]] — logistischer Knotenpunkt mit Engpässen
- [[Truppendurchzüge und Plünderungen]] — Belastung der Bevölkerung und die Ordnung von 1557
- [[Belagerung von Kufstein 1504]] — der größte Artillerieeinsatz Maximilians I. am Inn
- [[Galeerenstrafe]] — Rudererbedarf der Seemächte nach Lepanto 1571
- [[Wilhelm Biener]] — letzter Kanzler Tirols, letzte Reise über den Inn

## Narrative Notes

- [[Der Inn als militärischer Transportweg]] — Warum der Inn Tirols Militärweg wurde
- [[Gefangene und Galeeren auf dem Inn]] — Gefangenentransporte und die Lehre von Lepanto

## Verwandte MOCs

- [[_Index MOC]]

--- END NOTE ---

--- FILENAME: 50-MOC/Landshuter Erbfolgekrieg.md
--- BEGIN NOTE ---

# Landshuter Erbfolgekrieg

*Map of Content — reiner Navigations-Hub, kein eigener Inhalt.*

## Permanent Notes

- [[Wittelsbacher Hausvertrag von Pavia]] — der Erbfolgeregel, deren Bruch den Krieg auslöste
- [[Reichsacht]] — politisches Druckmittel Maximilians gegen Ruprecht und Philipp
- [[Kölner Schiedsspruch 1505]] — der Friedensschluss und die territoriale Neuordnung
- [[Junge Pfalz]] — das neue Territorium für die Enkel Georgs des Reichen
- [[Maximilians Gebietsgewinne im Landshuter Erbfolgekrieg]] — Kufstein, Kitzbühel, Rattenberg an Habsburg

## Narrative Notes

- [[Ursachen des Landshuter Erbfolgekriegs]] — Wie ein Erbfall zum Reichskrieg wurde
- [[Der Kölner Schiedsspruch als territoriale Neuordnung]] — Wer gewann, wer verlor

## Literatur

- [[Landshuter Erbfolgekrieg (Wikipedia)]] — Experten-Exzerpt der Quellenquelle

## Verwandte MOCs

- [[Inn und Militärtransport]] — die Gebietsgewinne am Inn verbinden beide Themen
- [[_Index MOC]]

--- END NOTE ---

--- FILENAME: 50-MOC/Reichsreform 1495.md
--- BEGIN NOTE ---

# Reichsreform 1495

*Map of Content — reiner Navigations-Hub, kein eigener Inhalt.*

## Permanent Notes

- [[Reichsreform von 1495]] — das Bündel der Reformgesetze vom Wormser Reichstag
- [[Ewiger Landfrieden]] — das Fehdeverbot, das das Gewaltmonopol dem Reich zuordnet
- [[Reichskammergericht]] — die ständisch dominierte oberste Gerichtsbehörde
- [[Reichskreise]] — die neuen regionalen Verwaltungseinheiten (6 → 10)
- [[Gemeiner Pfennig]] — die erste reichsweite Steuer
- [[Reichsregiment]] — die gescheiterte ständische Reichsregierung
- [[Reichsacht]] — die höchste Strafe des Reichsrechts (Kontext aus dem Landshuter Erbfolgekrieg)

## Narrative Notes

- [[Die Reichsreform von 1495]] — Wie aus dem Wormser Reichstag ein Wendepunkt wurde

## Verwandte MOCs

- [[Landshuter Erbfolgekrieg]] — Reichsrecht und Acht in der Praxis
- [[_Index MOC]]

--- END NOTE ---

--- FILENAME: 50-MOC/Schmirntal.md
--- BEGIN NOTE ---

# Schmirntal

*Map of Content — reiner Navigations-Hub, kein eigener Inhalt.*

## Quellen

- [[Schmirn Podcasts]] — NotebookLM-Synthese: 5 Podcast-Skripte zum Schmirntal
- [[Reissenschuh (NotebookLM 2)]] — erweiterte 2. Ausgabe: EMOD-SLAP, Transferierbarkeit, Referenzmodell

## Permanent Notes

### Geologie

- [[Metamorphe Schieferhülle (Tauernfenster)]] — das weiche Fundament des Tals (Glockner-Decke)
- [[Reissenschuh-Rutschung]] — DSGSD durch lithologische Inversion und Porenwasserdruck
- [[Monitoring gravitativer Hangdeformationen]] — TLS, DGNSS, Luftbilder, KI-Nowcasting
- [[Quellhydrochemie des Tauernfensters]] — Arsen/Uran als geochemischer Fenster-Beweis
- [[Gravitative Kaskadenprozesse am Reissenschuh]] — von der DSGSD zur Mure: Akkumulation und Trigger
- [[EMOD-SLAP]] — Luftbild-Photogrammetrie verlängert Bewegungszeitreihen bis 1954

### Archäologie

- [[Bergkristallbergbau am Riepenkar]] — weltweit ältester Hochgebirgs-Bergbau (Mesolithikum)
- [[Bergkristallstraße]] — prähistorisches Handelsnetz vom Riepenkar bis zum Gardasee
- [[Tuxer Joch]] — Transitachse von der Steinzeit bis in die Römerzeit

### Siedlung & Kultur

- [[Schwaighöfe]] — mittelalterliche Alpwirtschaft (Vallis Smurne 1249)
- [[Totenweg über das Tuxer Joch]] — Bestattungslogistik über den Pass
- [[Sakrale Landschaft des Schmirntals]] — St. Joseph und die Kalte Herberge

### Botanik

- [[Bergmähder]] — extensive Kulturlandschaft als Biodiversitäts- und Lawinenschutz
- [[Ethnobotanik im Schmirntal]] — Enzian, Knabenkraut und Teufelskralle im Volksglauben
- [[Alpenblumen- und Kräutergarten Toldern]] — 420 Arten als lebendes Klassenzimmer

### Moderne & Zukunft

- [[Molybdänbergwerk Alpeiner Scharte]] — NS-Zwangsarbeit im höchstgelegenen Bergwerk Europas
- [[Tiroler Grauvieh]] — Verbuschungsprävention durch Beweidung
- [[Bergsteigerdorf]] — sanfter Tourismus im Sinne der Alpenkonvention

## Narrative Notes

- [[Das Schmirntal als geologisches Labor des Tauernfensters]] — von der Exhumation bis zur Quellenchemie
- [[Der Reissenschuh als Referenzmodell tiefgreifender Hangdeformationen]] — von der Tektonik zum Risikomanagement
- [[Wie der Bergkristall vom Riepenkar ein prähistorisches Handelsnetz erschloss]] — vom Rohstoff zum Exportgut
- [[Zwischen Pass und Pfarre - Wie politische Grenzen den Totenweg erzwangen]] — von der Schwaige zum Totenweg

## Verwandte MOCs

- [[Tauernfenster und Ostalpen]] — die geologische Tiefenstruktur hinter dem Schmirntal
- [[_Index MOC]]

--- END NOTE ---

--- FILENAME: 50-MOC/Symmetrie im Tierreich.md
--- BEGIN NOTE ---

# Symmetrie im Tierreich

*MOC zu den Körperbauplänen der Tiere und ihrer evolutionsbiologischen Erklärung.*

## Grundlegende Baupläne

- [[Körperachsen der Tiere]]
- [[Bilaterale Symmetrie]]
- [[Radiale Symmetrie]]
- [[Cnidarier]]

## Wie Symmetrie entsteht

- [[Symmetrie als Konsequenz der Bewegung]]
- [[Cephalisation]]
- [[Hox-Gene]]
- [[Links-Rechts-Festlegung]]
- [[Nodal-Cilien]]

## Symmetrie brechen und Störungen

- [[Asymmetrie als abgeleitetes Merkmal]]
- [[Sekundäre Radialsymmetrie der Echinodermen]]
- [[Situs inversus]]

## Systematik und Ursprung

- [[Bilateria]]
- [[Ikaria wutjita]]

## Ergänzende Erklärungsmechanismen

- [[Symmetrie als sparsames genetisches Encoding]]

## Quellen

- [[Warum 99% aller Tiere symmetrisch sind]]

--- END NOTE ---

--- FILENAME: 50-MOC/Tauernfenster und Ostalpen.md
--- BEGIN NOTE ---

# Tauernfenster und Ostalpen

*Map of Content — reiner Navigations-Hub, kein eigener Inhalt.*

## Permanent Notes

- [[Tauernfenster]] — das größte tektonische Fenster der Alpen
- [[Alpine Deckentektonik]] — wie Deckenstapelung die Alpen strukturierte
- [[Alpine Metamorphose]] — Versenkung bis 35–40 km und ihr Höhepunkt bei ~25–30 Ma
- [[Brenner-Normalverwerfung]] — O-W-Extension und Footwall-Uplift im Miozän
- [[Slab Breakoff und Exhumation]] — Abreißen der Platte, ~2 km Hebung, Magmatismus
- [[Laterale Extrusion der Ostalpen]] — Adriatischer Indenter und O-W-Extension
- [[Penninisch-Ligurischer Ozean]] — die magmatisch "arme" Alpine Tethys
- [[Eoalpine Orogenese]] — die kretazische Vorläufer-Orogenese in den Austroalpinen Decken
- [[Metamorphe Schieferhülle (Tauernfenster)]] — das weiche Fundament des Schmirntals
- [[Reissenschuh-Rutschung]] — DSGSD durch lithologische Inversion und Porenwasserdruck
- [[Monitoring gravitativer Hangdeformationen]] — Messtechnik gegen die langsame Katastrophe
- [[Quellhydrochemie des Tauernfensters]] — Arsen/Uran als geochemischer Fenster-Beweis
- [[EMOD-SLAP]] — Luftbild-Photogrammetrie verlängert Bewegungszeitreihen bis 1954
- [[Geothermobarometrie]] — Minerale als Thermometer und Uhren des P-T-Zeit-Pfads
- [[Zerrklüfte]] — Dehnungsklüfte der Hebungsphase als Mineral-Fenster
- [[Konglomeratgneis]] — unreifes Perm-Sediment als Deformationsmessgerät
- [[Furtschaglschiefer]] — >700 Mio. Jahre alte Schwarzschiefer der Greiner Serie
- [[Diskordanz am Pfitscher Joch]] — der Viertelmilliarden-Jahre-Sprung im Gelände
- [[Pfitscher Bergsturz]] — nacheiszeitliche Talverriegelung mit katastrophalem Dammbruch um 1100 n. Chr.

## Narrative Notes

- [[Entstehung der Ostalpen entlang des TRANSALP-Profils]] — sieben Schritte von Pangaea zum Orogen
- [[Das Tauernfenster als tektonisches Exhumationsfenster]] — wie tief versenktes Grundgebirge an die Oberfläche kam
- [[Die Brenner-Normalverwerfung und die Exhumation der Ostalpen]] — Extension parallel zur Kompression
- [[Das Schmirntal als geologisches Labor des Tauernfensters]] — die lokale Manifestation der Exhumation
- [[Der Reissenschuh als Referenzmodell tiefgreifender Hangdeformationen]] — von der Tektonik zum Risikomanagement
- [[Die Deformationsgeschichte des Tauernfensters in vier Phasen]] — von der Überschiebung zur Caterpillar-Kompression
- [[Der Pfitscher Bergsturz und der verschwundene Stausee]] — eine Katastrophe, die die Landschaft prägte

## Literatur

- [[Reissenschuh (NotebookLM 2)]] — erweiterte 2. Ausgabe: EMOD-SLAP-Details, Transferierbarkeit, Referenzmodell
- [[Tauernfenster (Exkursion Pfitschtal)]] — Exkursionsführer Pfitschtal: Deckenbau, Methodik, 4-Phasen-Geschichte

## Verwandte MOCs

- [[Wilson-Zyklus und Ozeanreinkarnation]] — die Alpen als Wilson-Zyklus: Ozeanöffnung und -schließung
- [[Schmirntal]] — Regionalgeschichte Tirols am Westrand des Tauernfensters
- [[_Index MOC]]

--- END NOTE ---

--- FILENAME: 50-MOC/Trilobiten als Fossilgruppe.md
--- BEGIN NOTE ---

# Trilobiten als Fossilgruppe

*Map of Content — reiner Navigations-Hub, kein eigener Inhalt.*

## Permanent Notes

- [[Trilobiten]] — Anatomie, Dominanz und Langlebigkeit der Trilobiten
- [[Körperbau der Trilobiten]] — Loben, Tagmata, Glabella und Spaltbeine
- [[Facettenaugen der Trilobiten]] — calcitische Sehorgane in drei Bauformen
- [[Gesichtsnaht und Häutung der Trilobiten]] — Sollbruchstelle für die Häutung, fünf Grundtypen
- [[Entwicklung der Trilobiten]] — Protaspis, Meraspis und Holaspis (Anamorphose)
- [[Lebensweise der Trilobiten]] — Benthos, pelagiale Formen und Ernährungstypen
- [[Ursprung der Trilobiten]] — kambrische Explosion, Ghost Range und Vikariismus
- [[Verwandtschaft der Trilobiten]] — Arachnata vs. Krebstiere, Plesiomorphien
- [[Ordnungen der Trilobiten]] — die neun anerkannten Ordnungen der Klasse
- [[Schwarmintelligenz bei Trilobiten]] — 480 Mio. Jahre alte Reihenformation von Ampyx priscus
- [[Trilobiten als Reliktgruppe]] — fast 100 Mio. Jahre artenarm vor dem Aussterben
- [[Trilobiten als biostratigraphisches Werkzeug]] — Trilobiten zur relativen Datierung von Schichten
- [[Enrollierung]] — Einroll-Verhalten als Verteidigung gegen kambrische Prädation
- [[Evolutionäres Wettrüsten]] — Wettrüstenspirale zwischen Räubern und Beute
- [[Ordovizium-Silur-Extinktion]] — klimatischer Doppelschlag vor 445 Mio. Jahren
- [[Spätdevon-Extinktion]] — Sauerstoffverlust und Zusammenbruch der Riffe
- [[Perm-Trias-Massenaussterben]] — das größte Massensterben der Erdgeschichte

## Narrative Notes

- [[Der Niedergang der Trilobiten]] — Warum endete die Erfolgsgeschichte der Trilobiten?
- [[Trilobiten als Zeugen der Evolution]] — vom kambrischen Ursprung bis zur Reliktgruppe

## Verwandte MOCs

- [[Wilson-Zyklus und Ozeanreinkarnation]] — die Trilobiten als Brücke zwischen beiden Themen
- [[_Index MOC]]

--- END NOTE ---

--- FILENAME: 50-MOC/Wilson-Zyklus und Ozeanreinkarnation.md
--- BEGIN NOTE ---

# Wilson-Zyklus und Ozeanreinkarnation

*Map of Content — reiner Navigations-Hub, kein eigener Inhalt.*

## Permanent Notes

- [[Wilson-Zyklus]] — Kerntheorie: Ozeanbecken schließen und öffnen sich entlang derselben Grenzen
- [[Iapetus-Sutur]] — Rest des geschlossenen Iapetus-Ozeans, der Linie des Atlantiks folgt
- [[Atlantische und Pazifische Faunen]] — Walcotts Trilobiten-Rätsel in Neufundland
- [[Kontinentaldrift]] — Wegeners Theorie und ihr langer Weg zur Anerkennung
- [[Trilobiten als biostratigraphisches Werkzeug]] — Trilobiten zur relativen Datierung von Schichten
- [[John Tuzo Wilson]] — der Geologe, der das Rätsel auflöste

## Narrative Notes

- [[Wie Trilobiten den Wilson-Zyklus aufdeckten]] — die hundertjährige Entdeckungsgeschichte
- [[Die acht Phasen des Wilson-Zyklus]] — von der Dehnung bis zur Kollision

## Verwandte MOCs

- [[Trilobiten als Fossilgruppe]] — die Trilobiten als Brücke zwischen beiden Themen
- [[_Index MOC]]

--- END NOTE ---

---

# Anhang: Kurzbeschreibungen (60-PARA, 70-Meta)

Diese Dateien sind Anweisungen und Resources, keine Wissens-Notizen. Sie werden nur zur Orientierung aufgelistet und sind KEINE gueltigen Link-Ziele.

## 60-PARA — Projekte / Areas / Resources (5)

- **`60-PARA/Projects/Zettelkasten Aufbau/_Roadmap.md`** (project) — Zentrale Roadmap für das PARA-Projekt Zettelkasten Aufbau: Aufsetzen, Befüllen und Systematisieren der Verzeichnis-, Regel- und Multi-Vault-Architektur für LLMWikiV4 (basierend auf dem Template Ar9av/
- **`60-PARA/Projects/Zettelkasten Aufbau/Log.md`** (project_log) — Vollständiges Chronologie-Protokoll aller im Vault LLMWikiV4 umgesetzten Einrichtungsschritte, Systemanpassungen, Regel-Konsolidierungen und Skript-Implementierungen für das PARA-Projekt Zettelkasten 
- **`60-PARA/Projects/Zettelkasten Aufbau/Master-Kinder-Vault-Architektur.md`** (ai_instruction) — Portable KI-Spezifikation: Diese Datei beschreibt die vollständige technische Architektur, Vererbung und Entkopplungslogik zwischen einem Master-Vault und mehreren Kinder-Vaults. Jede KI (unabhängig v
- **`60-PARA/Resources/Anweisungen für andere KIs/Kommunikation mit dem Nutzer.md`** — Halte dich für eine möglichst effiziente Gestaltung der Kommunikation mit dem Benutzer an folgende Regeln:
- **`60-PARA/Resources/NotebookLM Ingester.md`** — Dieser Prompt wird zu Beginn einer neuen NotebookLM-Session eingegeben. Er richtet NotebookLM als Denkpartner für den Obsidian-Zettelkasten ein und definiert das /produce-Kommando.

## 70-Meta — KI-Anweisungen, Skills, Dokumentation (6)

- **`70-Meta/KI-Anweisungen.md`** (ai_instruction) — Diese Datei ist die verbindliche und höchstpriorisierte Anweisung für alle KI-Interaktionen in diesem Vault. Sie hat Vorrang vor allen anderen Quellen, Notizen oder früheren Anweisungen.
- **`70-Meta/Nutzerprofil.md`** (meta) — Diese Datei speichert dauerhaft alle Informationen über den Nutzer, die für die weitere Zusammenarbeit von Bedeutung sein können (fachlicher Hintergrund, Vorlieben, Konventionen, Projektkontext). Sie 
- **`70-Meta/Skills/ZK-ingest.md`** (ai_instruction) — Hinweis: Diese Datei ist die verbindliche und einzige Skill-Anweisung für die Zettelkasten-Ingestion in diesem Vault. Die KI nutzt diese Anweisung zur automatischen Verarbeitung von Rohquellen aus 10-
- **`70-Meta/System-Skills-Register.md`** (ai_instruction) — Verbindliche KI-Anweisung: Diese Datei beschreibt alle 40 externen System-Skills unter C:\Users\Martin Huber\.agents\skills\. Jede KI, die in diesem Vault arbeitet, muss sich der Existenz dieser Skill
- **`70-Meta/Tag-Taxonomie.md`** (ai_instruction) — Diese Datei ist das kanonische Referenz-Register für alle Frontmatter-Tags im Vault LLMWikiV4. Sie ist von der KI vor jeder Notiz-Erstellung und vor jedem Ingest zwingend einzusehen.
- **`70-Meta/Vault Guide.md`** (meta) — Ein molekularer Zettelkasten für gemischte Wissensquellen (PDFs, Videos, Bücher, KI-Chats, Urlaubs-Notizen, Transkripte), kombiniert mit PARA-Projektverwaltung. Alle Notizen werden KI-generiert und vo

---

_Fulltext-Summe: 191 Notizen im Volltext, 11 Kurzbeschreibungen._
