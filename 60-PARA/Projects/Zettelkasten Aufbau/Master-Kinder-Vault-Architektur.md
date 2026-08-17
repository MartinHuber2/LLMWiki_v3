---
type: ai_instruction
created: 2026-08-17 13:41:00
updated: 2026-08-17 13:41:00
tags:
  - meta/zettelkasten
  - meta/instruction
---

# Architekturspezifikation: Master-Vault und Kinder-Vaults

> **Portable KI-Spezifikation**: Diese Datei beschreibt die vollständige technische Architektur, Vererbung und Entkopplungslogik zwischen einem **Master-Vault** und mehreren **Kinder-Vaults**. Jede KI (unabhängig von Modell oder Chat-Kontext) muss diese Spezifikation als verbindliche Referenz für die Implementierung und Pflege von Multi-Vault-Umgebungen nutzen.

---

## 1. Problemstellung & Zielsetzung

Beim Betrieb mehrerer Obsidian-Vaults (z. B. Vault für Geowissenschaften/Biologie, Vault für Recht/Finanzen, Vault für persönliche Notizen) entstehen zwei Zielkonflikte:

1. **Redundanz vermeiden**: Neue Obsidian-Plugins (`.obsidian/plugins`), CSS-Snippets (`.obsidian/snippets`) und KI-System-Skills (`70-Meta/Skills/`) sollen **nur einmal zentral im Master-Vault** gepflegt und automatisch auf alle Kinder-Vaults übertragen werden.
2. **Lokale Autonomie wahren**: 
   - **Plugin-Einstellungen (`data.json`)**: Jedes Plugin speichert seine spezifischen Konfigurationen (Pfade, Hotkeys, API-Keys) in `data.json`. Diese Einstellungen müssen in jedem Kinder-Vault **individuell anpassbar** bleiben und dürfen nicht überschrieben werden.
   - **Tag-Taxonomie (`Tag-Taxonomie.md`)**: Der Fachbereichs-Tag-Stamm ist vaultspezifisch. Ein Biologie-Vault benötigt andere Domain-Tags als ein Jurastudium-Vault. Die Taxonomie muss daher pro Kinder-Vault lokal wachsen.

---

## 2. Architekturentwurf (Vererbung & Entkopplung)

```
[Master-Vault] (Zentrale Pflege)
 ├── .obsidian/
 │    ├── plugins/
 │    │    ├── <plugin-id>/
 │    │    │    ├── main.js           ---> SYNC ---> Kinder-Vault/
 │    │    │    ├── manifest.json     ---> SYNC ---> Kinder-Vault/
 │    │    │    ├── styles.css        ---> SYNC ---> Kinder-Vault/
 │    │    │    └── data.json         [NUR MASTER / NICHT KOPPIERT]
 │    └── snippets/                   ---> SYNC ---> Kinder-Vault/
 └── 70-Meta/
      └── Skills/                     ---> SYNC ---> Kinder-Vault/
           ├── ZK-ingest.md
           ├── ZK-lint.md
           └── ZK-tag-taxonomy.md     [Logik/Regeln vererbt, Baum lokal]

[Kinder-Vault A] (Lokaler Inhalt)
 ├── .obsidian/
 │    ├── plugins/
 │    │    └── <plugin-id>/
 │    │         ├── main.js           [Vererbt aus Master]
 │    │         ├── manifest.json     [Vererbt aus Master]
 │    │         ├── styles.css        [Vererbt aus Master]
 │    │         └── data.json         [LOKAL & INDIVIDUELL]
 │    └── community-plugins.json     [LOKAL & INDIVIDUELL]
 ├── 70-Meta/
 │    ├── Tag-Taxonomie.md            [LOKALER TAG-BAUM]
 │    └── Skills/                     [Vererbt aus Master]
 ├── 10-Raw/
 ├── 20-Literature/
 ├── 30-Narrative/
 ├── 40-Permanent/
 └── 50-MOC/
```

---

## 3. Technische Umsetzung: Das Sync-Skript (`sync_master.py`)

Statt des Gesamtexporte-Junctions (die `data.json` erzwingen würden) wird ein Python-Synchronisationsskript im Master-Vault eingesetzt (`60-PARA/Resources/Skripte/sync_master.py`).

### Skript-Logik & Regeln:

1. **Gezielter Plugin-Code-Sync**:
   - Für jedes im Master-Vault installierte Plugin werden ausschließlich `main.js`, `manifest.json` und `styles.css` in die Plugin-Ordner der Kinder-Vaults kopiert.
   - **Löschschutz**: Existiert im Kinder-Vault bereits eine `data.json`, wird diese **niemals überschrieben oder gelöscht**.
2. **Skill- & Snippet-Sync**:
   - Der Ordner `70-Meta/Skills/` wird vom Master-Vault in alle Kinder-Vaults gespiegelt.
   - Der Ordner `.obsidian/snippets/` wird gespiegelt.
3. **Ersterstellung lokaler Dateien**:
   - Besitzt ein Kinder-Vault noch keine `70-Meta/Tag-Taxonomie.md`, wird eine leere Vorlage mit den Grundregeln (Kleinschreibung, `u/`-Nutzer-Tag-Register) angelegt. Der Fach-Tag-Baum wächst anschließend lokal im Kinder-Vault.
4. **Verzeichnis-Registrierung**:
   - Die Ziel-Pfade aller Kinder-Vaults werden in einer Konfigurationsdatei (`60-PARA/Resources/kinder_vaults.json`) im Master-Vault verwaltet.

---

## 4. KI-Verhaltensanweisungen für Multi-Vault-Betrieb

Jede KI, die in einem Kinder-Vault agiert, muss folgende Regeln einhalten:

1. **System-Skills nutzen**: Die KI liest Anweisungen aus `70-Meta/Skills/` (aus dem Master vererbt).
2. **Lokale Taxonomie respektieren**: Bei Tag-Zuweisungen liest die KI ausschließlich die **lokale** Datei `70-Meta/Tag-Taxonomie.md` des aktuellen Kinder-Vaults.
3. **Plugins & Einstellungen**: Die KI nimmt keine manuellen Änderungen an Plugin-Codedateien vor. Einstellungen werden vom Nutzer in der jeweiligen Obsidian-Instanz vorgenommen.

---

## 5. Vorteile dieser Architektur

* **Zero-Redundanz bei Code & Skills**: Plugin-Updates und Skill-Verbesserungen werden 1x im Master-Vault durchgeführt und per Skript auf alle Kinder-Vaults verteilt.
* **100 % Autonomie der Inhalte & Einstellungen**: Kein Vermischen von Fachgebiet-Tags und keine ungewollten Überstrahlungen von Plugin-Konfigurationen.
* **Model- & KI-Portabilität**: Das Schema ist rein dateibasiert und setzt keine proprietäre Software voraus.
