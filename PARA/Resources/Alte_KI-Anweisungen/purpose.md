---
type: ai_instruction
created: 2026-08-08
updated: 2026-08-08
---

# Projektzweck — Second Brain (Martin Huber)

> **Hinweis zur Nutzung dieser Datei:** Dieser Vault ist *kein* klassisches
> Ein-Fragen-Forschungsprojekt, sondern ein themenübergreifendes, dauerhaft
> genutztes "Second Brain" nach dem LLM-Wiki-Pattern (Karpathy): nashsu
> übernimmt die automatische Ingestion aus `raw/sources/` und generiert daraus
> verlinkte Wiki-Seiten nach `schema.md`. Statt einer einzigen Forschungsfrage
> verfolgt dieser Vault mehrere parallele Themenbereiche (siehe unten), die
> sich einen gemeinsamen Wiki-Baum teilen und ausschließlich über das
> `tags:`-Frontmatter-Feld auseinandergehalten werden.

## Themenbereiche

Der Vault deckt aktuell vier parallele Bereiche ab. Neue Quellen sollten,
wo sinnvoll, einem oder mehreren dieser Bereiche über `tags:` zugeordnet
werden:

1. **Unterrichtsmaterial (HTL, Elektrotechnik/Programmieren)** — fachliche
   Konzepte, Quellen und Referenzmaterial für den laufenden Unterricht.
2. **Diplomarbeitsbetreuung** — Wissen zur Betreuung mehrerer, thematisch
   unterschiedlicher Diplomarbeiten, schwerpunktmäßig aus dem Bereich
   Mikroelektronik/Embedded Programming. Nicht auf ein einzelnes Thema
   festgelegt: neue Diplomarbeitsthemen kommen laufend hinzu.
3. **Privates Wissensmanagement** — freie Lerninteressen ohne beruflichen
   Zweck (u.a. Geschichte, Paläontologie, Naturwissenschaft allgemein), wie
   bereits an den bisherigen Test-Ingests (Säugetier-Evolution, Perm-Trias-
   Massenaussterben, Wilhelm Biener) erkennbar.
4. **Rechtsfall Hochbehälter Reith** — Rechtsstreit mit der Gemeinde Reith,
   die einen Hochbehälter vertragswidrig nicht von Martins Grundstück
   entfernt. Aktuell **inaktiv**, wird erst zu einem späteren Zeitpunkt
   aufgenommen; bis dahin keine gezielte Recherche oder Ingestion zu diesem
   Thema.

## Hintergrund

Martin ist HTL-Lehrer für Elektrotechnik/Programmieren und betreut
regelmäßig Diplomarbeiten. Statt für jede Anfrage neu aus Rohdaten zu
recherchieren (klassisches RAG-Muster), soll ein dauerhaftes, strukturiertes
Wiki inkrementell aufgebaut werden, das über die Zeit wächst und als
persönliches Nachschlagewerk dient — fachlich wie privat.

## Offene Punkte / Platzhalter

<!-- Diese Punkte sind bewusst noch nicht ausformuliert und werden ergänzt, sobald sie aktuell werden. -->

- Diplomarbeitsbetreuung: konkrete Einzelthemen werden fortlaufend ergänzt,
  sobald sie feststehen; kein Versuch, sie hier vorab vollständig zu listen.
- Rechtsfall Reith: Details, Chronologie und relevante Dokumente folgen erst,
  wenn das Thema aktiv bearbeitet wird.

## Scope

**In scope:**
- Alle vier oben genannten Themenbereiche, auch thematisch weit auseinander
  liegende Inhalte (z. B. Paläontologie neben Mikroelektronik) — bewusst
  keine inhaltliche Eingrenzung.
- Sowohl beruflich zweckgebundene Inhalte (Unterricht, Diplomarbeiten,
  Rechtsfall) als auch rein private Lerninteressen.

**Out of scope:**
- Keine bewusste Ausschlussliste vorhanden. Grundsätzlich offen für nahezu
  alle Inhalte; sollte sich das ändern, wird dieser Abschnitt aktualisiert.

## Methodik

- **Automatische Ingestion:** nashsu verarbeitet Rohquellen aus
  `raw/sources/` (PDF, Web-Clips, Video-Transkripte, Artikel etc.) gemäß den
  Regeln in `schema.md` und generiert daraus Wiki-Seiten inkl. Verlinkung.
- **Gezielte Recherche zu offenen Queries:** In `wiki/queries/` gesammelte
  offene Fragen werden fallweise aktiv weiterverfolgt, indem gezielt neue
  Quellen dazu gesucht und ingestiert werden.
- **Manuelle Relevanzbewertung (`Rel_MH`):** Martin vergibt `Rel_MH`
  punktuell bei einzelnen Seiten — insbesondere wenn ihm ein Artikel
  besonders wichtig oder unwichtig erscheint, oder wenn seine eigene
  Einschätzung deutlich von der KI-Bewertung (`Rel_KI`) abweicht. Keine
  systematische Durchsicht aller Seiten geplant.

## Erfolgskriterien

- **Aktiv genutztes Nachschlagewerk:** Martin greift beim Unterrichten und
  Arbeiten regelmäßig auf die Notizen zurück, statt Dinge neu zu
  recherchieren.
- **Sichtbare Wissensvernetzung:** Der Wissensgraph zeigt sinnvolle
  Verbindungen zwischen Themen, die vorher nicht bewusst waren — das
  Kernversprechen des LLM-Wiki-Ansatzes.
- **Gepflegte Ingestion-Pipeline:** nashsu und `schema.md` funktionieren
  technisch zuverlässig und werden bei Bedarf weiter nachgeschärft.

## Aktueller Stand

> Vault-Infrastruktur (Ordnerstruktur, `schema.md`, nashsu-Anbindung) steht.
> Bisherige Ingests dienten überwiegend als Tests (Säugetier-Evolution,
> Wilhelm Biener) und spiegeln noch nicht die vier oben definierten
> Themenbereiche vollständig wider. Diplomarbeits- und Unterrichtsinhalte
> sowie der Rechtsfall Reith wurden noch nicht aktiv eingepflegt.
</content>
