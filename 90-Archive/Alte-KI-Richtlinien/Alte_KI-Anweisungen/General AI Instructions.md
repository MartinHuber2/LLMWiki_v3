---
type: ai_instruction
created: 2026-05-19 08:30:00
updated: 2026-05-19 08:30:00
status: confirmed
up: "[[AI Instructions]]"
tags:
- AI_Instruction
- General
- Rules
Rel_KI: 5
Rel_MH: 
---

# General AI Instructions

Diese Anweisungen bilden das Fundament für die inhaltliche Arbeit aller KI-Agenten im Obsidian-Vault. Sie sind nachrangig zu den [[Top level AI instructions]], definieren aber die Zettelkasten-Philosophie und formale Standards.

### 1. Wissens-Architektur (3-Ebenen-Modell)
1.  **Quellen-Notiz (`type: source`)**: Bewahrt das lineare Narrativ als **strukturiertes Experten-Skript**. Ziel ist eine Detailtiefe, die den Inhalt der Quelle lückenlos und eigenständig lesbar abbildet [user input]. Sie dient als chronologisches Exzerpt und Einstiegsportal.
2.  **Konzept-Notiz / Atom (`type: concept`)**: Ein eigenständiges Prinzip oder eine zentrale Entität, gelöst vom ursprünglichen Kontext für maximale Wiederverwendbarkeit.
3.  **Struktur-Notiz / MOC (`type: moc`)**: Ein reiner Navigations-Hub zur thematischen Ordnung.

### 2. Qualitätsstandard: „Experten-Skript“
Notizen dürfen Informationen nicht oberflächlich zusammenfassen, sondern müssen den Inhalt der Quellen vollständig wiedergeben. Um werthaltiges Wissen zu generieren, müssen sie:
*   **Kausalitätsketten** explizit aufzeigen (Warum geschah X? Was war die Folge Y?).
*   Inhaltliche Zusammenhänge mit anderen Inhalten des Obsidian Vaults aufzeigen
*   **Fachbegriffe** präzise definieren und konsequent im Kontext verwenden.
*   Inhaltliche Zusammenhänge mit anderen Inhalten des Obsidian Vaults aufzeigen und Zusammenhänge so gliedern, dass Querverbindungen zwischen verschiedenen Quellen sofort ersichtlich werden.

### 3. Richtlinien zur Erstellung von Konzeptnotizen (Atome)
*   **Extraktions-Filter**: Inhalte werden atomisiert, wenn der Text zwischen **150 und 300 Wörtern** umfasst.
*   **Ausnahme „Zentrale Entitäten“**: Zentrale Entitäten wie beispielsweise Personen, spezifische Orte, Schlachten oder Institutionen erhalten **ausnahmslos** eine eigene Notiz, sofern sie nicht bereits in `all_notes` existieren, auch wenn sie kürzer als 150 Wörter sind.
*   **Vernetzungs-Pflicht**: Jedes Vorkommen einer zentralen Entität oder eines bestehenden Konzepts im Fließtext der Quellen-Notiz MUSS mit einem WikiLink `[[ ]]` versehen werden.

### 4. Emergente MOC-Genese
Struktur-Notizen (MOCs) entstehen organisch aus dem Bestand:
*   **Quantitative Hürde**: Die KI erstellt ein neues MOC erst dann eigenständig, wenn mindestens **5 Konzept-Notizen** (egal, ob neu erzeugte oder bereits bestehende) unter einem einheitlichen Überbegriff sinnvoll zusammengefasst werden können. 

### 5. Formale Vorgaben & Metadaten
*   **YAML-Properties**: Pflichtfelder `created`, `status`, `up`, `source_type`, `Rel_KI` und `Rel_MH`.
*   **Property 'up'**: Verlinkt auf das übergeordnete MOC. Falls noch keines existiert, bleibt das Feld **leer**.
*   **Tag-Formatierung**: Schlagworte im Feld `tags:` sind zwingend als reine Textwerte **ohne das # -Zeichen** anzugeben (z. B. `- Geschichte`).
*   **Naming Convention**: 
    *   Quellen: `YYYY-MM-DD - Quelle - Titel`.
    *   Konzepte: `Term` (Kontext nur bei Verwechslungsgefahr in Klammern).
*   **Video-Zitierweise**: Nach jeder Sachaussage ist zwingend der HTML-Anker für Zeitstempel `<a href="URL&t=s" title="HH:mm:ss"> (V) </a>` zu verwenden.
*   **Backup-Protokoll**: Alle durch Skripte erzeugten Backups werden im Verzeichnis `80_Backups` mit dem Tag `#dontMerge` abgelegt [user input].
*   **Active-Recall**: Die Erstellung von Active-Recall-Fragen innerhalb von Notizen ist bis auf Weiteres deaktiviert.