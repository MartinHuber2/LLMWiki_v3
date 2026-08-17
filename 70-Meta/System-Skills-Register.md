---
type: ai_instruction
created: 2026-08-17 16:56:00
updated: 2026-08-17 16:56:00
tags:
  - meta/instruction
  - meta/skill
---

# System-Skills-Register — External Agent Tools

> **Verbindliche KI-Anweisung**: Diese Datei beschreibt alle 40 externen System-Skills unter `C:\Users\Martin Huber\.agents\skills\`. Jede KI, die in diesem Vault arbeitet, muss sich der Existenz dieser Skills bewusst sein und dem Nutzer **selbstständig und proaktiv vorschlagen**, den jeweils passenden Skill einzusetzen, sobald eine Situation dies sinnvoll erscheinen lässt.

---

## Übersicht der Skill-Kategorien

1. **Vault-Pflege, Linting & Verlinkung** (`wiki-lint`, `cross-linker`, `wiki-dedup`, `wiki-stage-commit`, `wiki-rebuild`, `impl-validator`)
2. **Inhalts-Ingestierung & Import** (`zk-ingest`, `wiki-ingest`, `wiki-import`, `wiki-capture`, `claude-history-ingest`, `copilot-history-ingest`, `codex-history-ingest`, `hermes-history-ingest`, `pi-history-ingest`, `openclaw-history-ingest`, `wiki-history-ingest`)
3. **Synthese, Briefing & Dashboards** (`wiki-synthesize`, `wiki-digest`, `wiki-narrate`, `wiki-dashboard`, `wiki-status`, `daily-update`, `wiki-update`, `graph-colorize`, `obsidian-layout-adjustment`)
4. **Recherche, Abfrage & Wissenssuche** (`wiki-research`, `wiki-query`, `session-search`, `session-brain`, `memory-bridge`)
5. **Multi-Vault-Steuerung, Setup & Skill-Erstellung** (`wiki-switch`, `wiki-setup`, `wiki-export`, `tag-taxonomy`, `wiki-agent`, `skill-creator`, `vault-skill-factory`, `llm-wiki`)

---

## Detailliertes Skill-Register

### `claude-history-ingest`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\claude-history-ingest\SKILL.md`
* **Zweck & Beschreibung**: Ingest Claude Code conversation history into the Obsidian wiki. Use this skill when the user wants to mine their past Claude conversations for knowledge, import their ~/.claude folder, extract insights from previous coding sessions, or says things like "process my Claude history", "add my conversations to the wiki", "what have I discussed with Claude before". Also triggers when the user mentions their .claude folder, Claude projects, session data, past conversation logs, local-agent-mode sessions, or audit logs.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. claude-history-ingest) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `codex-history-ingest`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\codex-history-ingest\SKILL.md`
* **Zweck & Beschreibung**: Ingest Codex CLI conversation history into the Obsidian wiki. Use this skill when the user wants to mine their past Codex sessions for knowledge, import their ~/.codex folder, extract insights from previous coding sessions, or says things like "process my Codex history", "add my Codex conversations to the wiki", or "what have I discussed in Codex before". Also triggers when the user mentions .codex sessions, rollout files, session_index.jsonl, or Codex transcript logs.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. codex-history-ingest) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `copilot-history-ingest`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\copilot-history-ingest\SKILL.md`
* **Zweck & Beschreibung**: Ingest GitHub Copilot CLI session history into an Obsidian wiki as distilled knowledge pages. Use this skill when the user wants to capture their Copilot CLI sessions into a personal wiki — extracting architecture decisions, debug notes, and patterns into searchable Obsidian pages. Triggers on phrases like "ingest my copilot sessions into obsidian", "add my copilot history to my wiki", "pull my copilot session history into the vault", "capture what I've learned from copilot into obsidian", "just the new sessions since last time", or "mine patterns across my copilot sessions". Also triggers when the user mentions session-store.db, ~/.copilot/session-state, or VS Code copilot-chat transcripts in the context of building a wiki or knowledge base. Does NOT trigger for general copilot usage questions, searching sessions, or backing up history.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. copilot-history-ingest) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `cross-linker`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\cross-linker\SKILL.md`
* **Zweck & Beschreibung**: Scan the Obsidian wiki and automatically discover missing cross-references between pages. Use this skill when the user says "link my pages", "find missing links", "cross-reference", "connect my wiki", "add wikilinks", "what pages should be linked", or after any large ingestion to ensure new pages are woven into the existing knowledge graph. Also trigger when the user mentions "orphan pages" in the context of wanting to connect them, or says things like "my wiki feels disconnected" or "pages aren't linked well". This is a write-heavy skill — it actually modifies pages to add links, unlike wiki-lint which just reports issues.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. cross-linker) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `daily-update`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\daily-update\SKILL.md`
* **Zweck & Beschreibung**: Run the daily wiki maintenance cycle: check all source freshness, update the index, and regenerate hot.md. Use this skill when the user says "/daily-update", "run the daily update", "update everything", "morning sync", "refresh the wiki index", or when triggered by the launchd cron at 9 AM. Also use to set up or verify the cron + terminal notification infrastructure for the first time ("set up the daily cron", "install the terminal notification", "how do I get the morning reminder?").
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. daily-update) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `graph-colorize`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\graph-colorize\SKILL.md`
* **Zweck & Beschreibung**: Color-code the Obsidian graph view by rewriting `.obsidian/graph.json` colorGroups. Use this skill when the user says "color my graph", "color code obsidian", "colorize the graph", "color the graph by tag", "color by category", "highlight visibility in graph", "make the graph colorful", "distinguish tags in graph", or wants nodes in Obsidian's graph view tinted by tag, folder, or visibility. Generates a `colorGroups` array from the vault's actual tags/categories and merges it into the existing graph.json without clobbering other graph settings. Always backs up first.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. graph-colorize) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `hermes-history-ingest`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\hermes-history-ingest\SKILL.md`
* **Zweck & Beschreibung**: Ingest Hermes agent history into the Obsidian wiki. Use this skill when the user wants to mine their past Hermes sessions for knowledge, import their ~/.hermes folder, extract insights from previous Hermes conversations, or says things like "process my Hermes history", "add my Hermes memories to the wiki", "ingest ~/.hermes", or "what have I worked on in Hermes". Also triggers when the user mentions Hermes memories, Hermes sessions, ~/.hermes/memories, or Hermes skill logs.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. hermes-history-ingest) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `impl-validator`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\impl-validator\SKILL.md`
* **Zweck & Beschreibung**: Validate whether an implementation matches its stated goal. Use this skill when a skill or agent wants a second opinion on its own output, when the user says "check this implementation", "validate what you did", "is this correct?", "review the output", or "did you do this right?". Also spawned automatically as a subagent by other skills (memory-bridge, daily-update) to self-check their outputs before presenting to the user. Returns a structured pass/warn/fail verdict with specific actionable issues.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. impl-validator) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `llm-wiki`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\llm-wiki\SKILL.md`
* **Zweck & Beschreibung**: The foundational knowledge distillation pattern for building and maintaining an AI-powered Obsidian wiki. Based on Andrej Karpathy's LLM Wiki architecture. Use this skill whenever the user wants to understand the wiki pattern, set up a new knowledge base, or needs guidance on the three-layer architecture (raw sources → wiki → schema). Also use when discussing knowledge management strategy, wiki structure decisions, or how to organize distilled knowledge. This is the "theory" skill — other skills handle specific operations (ingesting, querying, linting).
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. llm-wiki) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `memory-bridge`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\memory-bridge\SKILL.md`
* **Zweck & Beschreibung**: Browse and compare wiki knowledge by which AI tool originally produced it. Use this skill when the user says "/memory-bridge", "browse codex memory", "what did codex know about X", "show me claude knowledge", "cross-tool memory", "what does hermes know that claude doesn't", "show me knowledge from <tool>", "compare my AI tool memories", or wants to explore knowledge gaps between tools. Works from any project. Diff mode ("what's different", "unique to codex", "gaps between tools") is the killer feature — it surfaces blind spots between tools that the user may not know exist.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. memory-bridge) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `obsidian-layout-adjustment`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\obsidian-layout-adjustment\SKILL.md`
* **Zweck & Beschreibung**: Workflow for working with Dan on changing how Obsidian looks using CSS snippets. Use this whenever Dan asks to restyle Obsidian, tune a vault's visual layout, adjust tabs, sidebars, note surfaces, properties, backlinks, graph panes, file explorer rows, icons, links, shadows, active states, or CSS snippets. Also use it when Dan says a visual CSS change did nothing, still looks wrapped, is not lifted, is unreadable, or needs to be refactored without changing the current appearance.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. obsidian-layout-adjustment) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `openclaw-history-ingest`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\openclaw-history-ingest\SKILL.md`
* **Zweck & Beschreibung**: Ingest OpenClaw agent history into the Obsidian wiki. Use this skill when the user wants to mine their past OpenClaw sessions for knowledge, import their ~/.openclaw folder, extract insights from previous OpenClaw conversations, or says things like "process my OpenClaw history", "add my OpenClaw sessions to the wiki", "ingest ~/.openclaw", or "what have I worked on in OpenClaw". Also triggers when the user mentions OpenClaw session logs, MEMORY.md, daily notes, or ~/.openclaw/workspace.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. openclaw-history-ingest) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `pi-history-ingest`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\pi-history-ingest\SKILL.md`
* **Zweck & Beschreibung**: Ingest Pi coding agent session history into the Obsidian wiki. Use this skill when the user wants to mine their past Pi sessions for knowledge, import their ~/.pi/agent/sessions folder, extract insights from previous coding sessions, or says things like "process my Pi history", "add my Pi sessions to the wiki", "ingest ~/.pi", or "what have I worked on in Pi". Also triggers when the user mentions Pi sessions, Pi agent history, ~/.pi/agent/sessions, or Pi conversation logs.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. pi-history-ingest) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `session-brain`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\session-brain\SKILL.md`
* **Zweck & Beschreibung**: Build and maintain a topic graph over your agent session history. Reads every Claude session transcript plus the pruned sessions that survive only in history.jsonl, clusters them by topic using local TF-IDF (no API calls, no embeddings), and writes an interactive graph you can open in a browser. Use when the user says "/session-brain", "build my session map", "cluster my claude sessions", "map my session history", "rebuild the session graph", "show me my session graph", "what have I been working on lately", "what topics have gone stale". Different from wiki-history-ingest, which distils sessions into vault pages: this builds a retrieval index over the raw sessions and never writes to the vault.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. session-brain) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `session-search`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\session-search\SKILL.md`
* **Zweck & Beschreibung**: Find a past agent session by topic and load its context into the current conversation. Searches the session-brain topic graph, ranking by relevance, topic membership, and time decay, then loads the winning transcript. Use when the user says "/wiki-sessions <topic>", "which session did I do X in", "find the session where I fixed X", "when did I last work on Y", "what was that session about Z", "load the session where I set up X", "have I done this before". Read-only — never writes to the vault. Requires a graph built by the session-brain skill.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. session-search) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `skill-creator`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\skill-creator\SKILL.md`
* **Zweck & Beschreibung**: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. skill-creator) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `tag-taxonomy`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\tag-taxonomy\SKILL.md`
* **Zweck & Beschreibung**: Enforce consistent tagging across the Obsidian wiki using a controlled vocabulary. Use this skill when the user says "fix my tags", "normalize tags", "clean up tags", "tag audit", "what tags should I use", "tag taxonomy", or whenever you're creating or updating wiki pages and need to choose the right tags. Also trigger when the user asks about tag conventions, wants to add a new tag to the taxonomy, or says "my tags are a mess". Always consult this skill's taxonomy file before assigning tags to any wiki page.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. tag-taxonomy) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `vault-skill-factory`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\vault-skill-factory\SKILL.md`
* **Zweck & Beschreibung**: Generate a portable, self-contained Agent Skill from mature, curated Obsidian wiki pages — turning a cluster of verified knowledge into a reusable "digital expert" (SKILL.md + references/). Use this skill when the user says "/vault-skill-factory", "make a skill from my wiki", "turn these pages into a skill", "generate an agent skill from my vault", "package my notes on X as a skill", "build a domain-expert skill from my wiki", or wants to distill recurring, mature wiki knowledge into a shareable skill. Inspired by OpenKB's "drop in a book → out comes a digital expert" pattern. The factory ONLY reads the vault and WRITES TO A REVIEW DIRECTORY — it never installs skills, never writes into .skills/, and never touches global skill directories.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. vault-skill-factory) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-agent`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-agent\SKILL.md`
* **Zweck & Beschreibung**: Query-driven targeted ingest from a specific AI agent's raw history. Use this skill when the user invokes /wiki-claude, /wiki-codex, /wiki-hermes, /wiki-openclaw, /wiki-copilot, /wiki-pi — with or without a search topic. Different from wiki-history-ingest (which bulk-ingests everything new): this skill finds sessions about a SPECIFIC TOPIC in a specific agent's history and ingests just those, then returns a synthesized answer immediately usable in the current session. Primary use case: you're working in agent A and want to pull in how you solved X in agent B's history. Cross-referencing, not archiving. Also trigger on: "what did I work on in codex about X", "search my claude sessions for Y", "pull in hermes knowledge about Z", "find that conversation where I did X in codex".
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-agent) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-capture`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-capture\SKILL.md`
* **Zweck & Beschreibung**: Save the current conversation as a permanent, structured wiki note. Use this skill when the user says "save this", "/wiki-capture", "capture this", "file this conversation", "preserve this", "add this to my wiki", or wants to turn what was just discussed into lasting knowledge. The skill classifies the content, rewrites it as declarative knowledge (not a chat transcript), and places it in the correct vault category. Also supports a fast QUICK MODE (`/wiki-capture --quick`, "quick capture", "capture this finding", "save this bug fix", "save this gotcha", "drop this to raw", "quick save to wiki") that drops findings to the `_raw/` staging area in under 60 seconds with no manifest or index writes — used by the session-end Stop hook to auto-preserve findings. Accepts inline named-vault routing like "@research save this" via the shared Config Resolution Protocol.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-capture) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-context-pack`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-context-pack\SKILL.md`
* **Zweck & Beschreibung**: Produce a token-bounded, citation-ready context slice from an existing Obsidian vault for a downstream agent or task. Use for "/wiki-context-pack", "use my vault as context", "context slice for X", "pack the wiki for my agent", or "bounded context for Y".
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-context-pack) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-dashboard`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-dashboard\SKILL.md`
* **Zweck & Beschreibung**: Create dynamic, queryable dashboard views of the Obsidian vault using Obsidian Bases or Dataview. Use this skill when the user says "create a dashboard", "vault dashboard", "show all X as a table", "dynamic view", "query my vault", "build a content index", "show me all concepts/entities/projects", or wants a structured, auto-updating view of their wiki content. Bases is native to Obsidian 1.8+ (no plugin needed). Dataview requires the community plugin.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-dashboard) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-dedup`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-dedup\SKILL.md`
* **Zweck & Beschreibung**: Scan the Obsidian wiki for page-level identity collisions — different pages covering the same concept under different names (e.g. "RSC" vs "React Server Components") — and merge them. Use this skill when the user says "dedup my wiki", "find duplicate pages", "merge duplicates", "identity resolution", "consolidate my wiki", "I have duplicate pages", or "my wiki has two pages for the same thing". Distinct from wiki-lint (which checks structure) and cross-linker (which adds links) — this skill makes destructive page-level merges and requires careful confirmation.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-dedup) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-digest`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-digest\SKILL.md`
* **Zweck & Beschreibung**: Generate a periodic knowledge digest — a human-readable newsletter-style summary of what was learned, updated, and connected in your wiki over a specified period (day/week/month). Use when the user says "what did I learn this week", "give me a digest", "weekly summary", "knowledge report", "what's new in my wiki", "/wiki-digest [period]", "summarize my recent learning", or wants a readable overview of recent wiki activity. Distinct from wiki-status (which reports ingestion delta of sources) — wiki-digest summarizes *knowledge*, not sources.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-digest) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-export`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-export\SKILL.md`
* **Zweck & Beschreibung**: Export the Obsidian wiki's knowledge graph to structured formats for use in external tools. Use this skill when the user says "export wiki", "export graph", "export to JSON", "export to Gephi", "export to Neo4j", "graphml", "visualize wiki", "knowledge graph export", "export to OKF", "OKF bundle", "open knowledge format", "export as markdown bundle", or wants to use their wiki data in another tool. Outputs graph.json, graph.graphml, cypher.txt (Neo4j), and graph.html (interactive browser visualization) into a wiki-export/ directory at the vault root, plus an optional OKF (Open Knowledge Format) markdown bundle under wiki-export/okf/.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-export) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-history-ingest`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-history-ingest\SKILL.md`
* **Zweck & Beschreibung**: Unified wiki-history-ingest entrypoint for conversation/session sources. Use this when the user says "/wiki-history-ingest claude", "/wiki-history-ingest copilot", "/wiki-history-ingest codex", "/wiki-history-ingest pi", or asks to ingest agent history without naming the underlying skill. This router dispatches to the specialized history skill.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-history-ingest) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-import`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-import\SKILL.md`
* **Zweck & Beschreibung**: Import a wiki knowledge graph into the current vault — either from a graph.json export file (stubs) or from an OKF (Open Knowledge Format) markdown bundle (full page bodies). Use this skill when the user says "import wiki", "import from export", "load graph.json", "import vault", "import OKF bundle", "import OKF", "load OKF", "import markdown bundle", "/wiki-import", or wants to transfer pages from one vault to another using the output of wiki-export.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-import) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-ingest`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-ingest\SKILL.md`
* **Zweck & Beschreibung**: Ingest any source into the Obsidian wiki by distilling its knowledge into interconnected wiki pages. Handles structured documents (PDFs, markdown, articles, papers, notes, folders), raw/unstructured text (chat exports, conversation logs, Slack/Discord threads, meeting transcripts, CSV/JSON data, journal entries, browser bookmarks, email archives, text dumps), AND web URLs. Use whenever the user wants to add new sources to their wiki: "add this to the wiki", "process these docs", "ingest this folder", "ingest this data", "process this export/logs", "import my chat history from X", "/ingest-url <url>", "add this URL", "save this page", or pastes a URL and says "add this" / "save this to my wiki". Also triggers when the user drops a file, or for raw mode: "process my drafts", "promote my raw pages", or any reference to the _raw/ staging directory. This is the general catch-all ingest skill for any document, text, or URL source not covered by a more specific ingest skill (claude-history-ingest, etc.).
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-ingest) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-lint`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-lint\SKILL.md`
* **Zweck & Beschreibung**: Audit and maintain the health of the Obsidian wiki. Use this skill when the user wants to check their wiki for issues, find orphaned pages, detect contradictions, identify stale content, fix broken wikilinks, or perform general maintenance on their knowledge base. Also triggers on "clean up the wiki", "what needs fixing", "audit my notes", or "wiki health check". Add --consolidate to switch from report-only to act-and-report mode (the "dream cycle"): fixes broken links, adds missing cross-references for orphans, corrects lifecycle states, demotes stale peripheral pages, normalizes tag aliases, and adds contradiction callouts — all with a dry-run preview and explicit user confirmation before any writes.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-lint) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-narrate`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-narrate\SKILL.md`
* **Zweck & Beschreibung**: Turn a wiki topic into a cited Markdown briefing, plain-language explanation, or progressive lecture. Use this skill for topic-based briefing, explanation, and lecture requests that must stay within the evidence compiled in an Obsidian vault.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-narrate) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-query`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-query\SKILL.md`
* **Zweck & Beschreibung**: Answer questions by searching the compiled Obsidian wiki. Use this skill when the user asks a question about their knowledge base, wants to find information across their wiki, asks "what do I know about X", "find everything related to Y", or wants synthesized answers with citations from their wiki pages. Also use when the user wants to explore connections between topics in their wiki, or asks a multi-hop "how is X connected to Y", "what links X to Y", "trace the chain from X to Z", or "what does X depend on transitively" question — answered by walking typed edges across multiple hops. Works from any project. Includes an index-only fast mode triggered by "quick answer", "just scan", "don't read the pages", "fast lookup" — returns answers from page summaries and frontmatter without reading page bodies. Accepts inline named-vault routing like "wiki-query @work what do I know about X" via the shared Config Resolution Protocol.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-query) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-rebuild`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-rebuild\SKILL.md`
* **Zweck & Beschreibung**: Archive existing wiki knowledge and rebuild from scratch, or restore from a previous archive. Use this skill when the user wants to start fresh, rebuild the wiki from all sources, archive current knowledge before a major change, or restore an older version. Triggers on "rebuild the wiki", "start over", "archive and rebuild", "restore from archive", "nuke and repave", "clean rebuild". Also use when the wiki has drifted too far from sources and incremental fixes won't cut it.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-rebuild) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-research`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-research\SKILL.md`
* **Zweck & Beschreibung**: Autonomously research a topic via multi-round web search, synthesize findings, and file structured results into the Obsidian wiki. Use this skill when the user says "/wiki-research [topic]", "research X", "find everything about Y", "do a deep dive on Z", "autonomous research on X", or wants comprehensive, web-sourced knowledge on a topic filed directly into their wiki.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-research) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-setup`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-setup\SKILL.md`
* **Zweck & Beschreibung**: Initialize a new Obsidian wiki vault with the correct structure, special files, and configuration. Use this skill when the user wants to set up a new wiki from scratch, initialize the vault structure, create the .env file, or says things like "set up my wiki", "initialize obsidian", "create a new vault", "get started with the wiki". Also use when the user needs to reconfigure their existing vault or fix a broken setup.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-setup) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-stage-commit`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-stage-commit\SKILL.md`
* **Zweck & Beschreibung**: Review and promote staged wiki pages to their final locations. Use when WIKI_STAGED_WRITES=true and the user says "/wiki-stage-commit", "review staged pages", "commit staged writes", "promote staged pages", "approve staged changes", or "what's waiting in staging". Shows each staged file, lets the user accept or reject it, and moves accepted files to their final wiki locations. Rejected files are moved back to _raw/ for manual editing.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-stage-commit) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-status`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-status\SKILL.md`
* **Zweck & Beschreibung**: Show the current state of the wiki — what's been ingested, what's pending, and the delta between sources and wiki content. Use this skill when the user asks "what's the status", "how much is ingested", "what's left to process", "show me the delta", "what changed since last ingest", "wiki dashboard", or wants an overview of their knowledge base health and completeness. Also use before deciding whether to append or rebuild. Includes an insights mode triggered by "wiki insights", "what's central", "show me the hubs", "central pages", "what's connected", "wiki structure" — analyzes the shape of the wiki itself to surface top hubs, cross-domain bridges, and orphan-adjacent pages.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-status) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-switch`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-switch\SKILL.md`
* **Zweck & Beschreibung**: Switch between multiple Obsidian wiki vault profiles. Use this skill when the user says "/wiki-switch NAME", "switch to my work wiki", "switch vault", "change wiki", "which wiki am I on", "list my wikis", "show my vaults", "create a new vault config", or "add a new wiki profile". The skill manages named config files at ~/.obsidian-wiki/config.NAME and activates one by symlinking it to ~/.obsidian-wiki/config.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-switch) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-synthesize`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-synthesize\SKILL.md`
* **Zweck & Beschreibung**: Systematically discover synthesis opportunities across the Obsidian wiki — pairs or clusters of concepts that co-occur frequently across pages but have no synthesis page connecting them. Creates new synthesis/ pages that draw explicit cross-cutting conclusions. Use when the user says "synthesize my wiki", "find connections", "what concepts keep coming up together", "/wiki-synthesize", or after a large ingest when the vault has grown significantly.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-synthesize) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `wiki-update`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\wiki-update\SKILL.md`
* **Zweck & Beschreibung**: Sync the current project's knowledge into the Obsidian wiki. Use this skill from any project when the user says "update wiki", "sync to wiki", "save this to my wiki", "update obsidian", or wants to distill what they've been working on into their knowledge base. This is the cross-project skill that lets you push knowledge from wherever you are into the vault. Accepts inline named-vault routing like "@work update wiki" via the shared Config Resolution Protocol.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. wiki-update) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.

### `zk-ingest`
* **Pfad**: `C:\Users\Martin Huber\.agents\skills\zk-ingest\SKILL.md`
* **Zweck & Beschreibung**: Ingest raw sources into the Zettelkasten vault using the vault-local ZK-ingest workflow. Use this skill when the user says "zk-ingest", wants to process files in `10-Raw/Waiting_For_Ingestion/`, or asks to ingest documents into their Zettelkasten.
* **Proaktiver KI-Vorschlag**: Sobald eine Aufgabe (z. B. zk-ingest) ansteht, soll die KI diesen Skill aktiv zur Ausführung empfehlen.
