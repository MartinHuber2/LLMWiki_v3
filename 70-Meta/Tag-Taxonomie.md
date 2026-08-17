---
type: ai_instruction
created: 2026-08-17 13:23:00
updated: 2026-08-17 13:23:00
---

# Tag-Taxonomie — LLMWiki_V4

Diese Datei ist das kanonische Referenz-Register für alle Frontmatter-Tags im Vault `LLMWiki_V4`. Sie ist von der KI vor jeder Notiz-Erstellung und vor jedem Ingest zwingend einzusehen.

---

## Nomenklatur- & Schreibweisen-Regeln

1. **Format**: Ausnahmslos Kleinschreibung und Kebab-Case (z. B. `geowissenschaften/geologie`, `u/urlaub-2026`). Keine Leerzeichen, keine Großbuchstaben.
2. **Ohne Raute**: In YAML-Frontmattern stehen Tags ohne `#`-Zeichen (z. B. `- geowissenschaften/geologie`).
3. **Zwei Tag-Kategorien**:
   - **Hierarchische Domain-Tags**: Systematische Einordnung des Notiz-Fachinhalts (Wissensstruktur).
   - **Nutzer-Tags (`u/`)**: Ad-hoc-, Projekt-, Event- oder Kontext-Tags mit dem Präfix `u/` (sowohl flach als auch hierarchisch).

---

## 1. Domain-Hierarchie (Fachwissen)

Die folgenden Stamm-Domains bilden die Fachstruktur des Vaults. Neue Sub-Tags werden unter den passenden Oberknoten eingeordnet. Neue Wurzel-Domains entstehen nur bei grundlegend neuen Wissensgebieten.

### `geowissenschaften/`
* `geowissenschaften/geologie`
* `geowissenschaften/geologie/tektonik`
* `geowissenschaften/geologie/geomorphologie`
* `geowissenschaften/palaeontologie`
* `geowissenschaften/hydrologie`
* `geowissenschaften/regionen/tirol`
* `geowissenschaften/regionen/alpen`

### `biowissenschaften/`
* `biowissenschaften/evolutionsbiologie`
* `biowissenschaften/zoologie`
* `biowissenschaften/botanik`
* `biowissenschaften/neurobiologie`
* `biowissenschaften/mikrobiologie`
* `biowissenschaften/genetik`
* `biowissenschaften/oekologie`
* `biowissenschaften/entwicklungsbiologie`
* `biowissenschaften/mammalogie`

### `geisteswissenschaften/`
* `geisteswissenschaften/paedagogik`
* `geisteswissenschaften/paedagogik/allgemeinbildung`
* `geisteswissenschaften/paedagogik/selbstbildung`
* `geisteswissenschaften/bildung/digitalisierung`
* `geisteswissenschaften/geschichte`
* `geisteswissenschaften/geschichte/antike`
* `geisteswissenschaften/geschichte/renaissance`
* `geisteswissenschaften/geschichte/militaergeschichte`
* `geisteswissenschaften/geschichte/rechtsgeschichte`
* `geisteswissenschaften/philosophie`
* `geisteswissenschaften/archaeologie`

### `gesellschaft/`
* `gesellschaft/medien`
* `gesellschaft/mediatisierung`
* `gesellschaft/digitalisierung`
* `gesellschaft/politik`
* `gesellschaft/soziologie`

### `meta/`
* `meta/skill`
* `meta/instruction`
* `meta/template`
* `meta/moc`
* `meta/clippings`
* `meta/zettelkasten`

---

## 2. Register bekannter Nutzer-Tags (`u/`)

Jedes Tag mit dem Präfix `u/` ist ein Nutzer-Tag. Die KI **löscht oder verändert bestehende `u/`-Tags niemals**.

Wenn die KI beim Ingest eine Rohquelle verarbeitet, gleicht sie deren Kontext mit diesem Register ab und vergibt passende `u/`-Tags proaktiv. Neue `u/`-Tags, die vom Nutzer oder im Ingest erzeugt werden, werden hier eingetragen.

### Bekannte Nutzer-Tags:
* `u/general`
* `u/clippings`

*(Dieses Register wird bei neuen Nutzer-Tags durch die KI kontinuierlich erweitert.)*
