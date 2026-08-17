"""
fix_floating_links.py
Findet Notizen im Vault, bei denen Wikilinks als parentlose Listen-Elemente
im YAML-Frontmatter stehen (kein übergeordneter Schlüssel), und verschiebt
diese unter links: related:.

Beispiel vorher:
  tier: core
  - '[[KoerpΕrperplaene]]'
  - '[[Bilaterale Symmetrie]]'
  Rel_AI: 1

Beispiel nachher:
  tier: core
  links:
    related:
      - '[[KoerpΕrperplaene]]'
      - '[[Bilaterale Symmetrie]]'
  Rel_AI: 1
"""

import sys, io, os, re
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

VAULT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
    r"g:\Meine Ablage\Hidden\Synch\Obsidian\LLMWiki_V4"
)

SKIP_DIRS = {'.git', '.obsidian', '.venv', 'node_modules'}
SKIP_FILES = {'index.md', 'log.md', 'hot.md'}

FM_RE = re.compile(r'^---\r?\n(.*?)\r?\n---', re.DOTALL)
WIKILINK_LINE = re.compile(r"^-\s+['\"]?(\[\[.*?\]\])['\"]?\s*$")

# Keys that introduce a list block (next lines with '- ' belong to them)
LIST_KEYS = {'tags', 'sources', 'related', 'links', 'provenance',
             'pages_created', 'pages_updated', 'relationships'}


def fix_floating_links(fm_text: str) -> tuple[str, bool]:
    lines = fm_text.split('\n')
    result_lines = []
    floating = []
    in_list_key = False
    last_insert_idx = 0   # after which result_line to insert links block
    changed = False

    for line in lines:
        stripped = line.rstrip()

        # A YAML key at root level
        key_match = re.match(r'^([a-zA-Z_][a-zA-Z0-9_-]*):', stripped)
        if key_match:
            key = key_match.group(1)
            in_list_key = key in LIST_KEYS
            result_lines.append(line)
            # Track insert position: after tier/summary/type/... single-value keys
            if key not in LIST_KEYS:
                last_insert_idx = len(result_lines) - 1
            continue

        # Indented continuation of a multi-line value (e.g. summary block)
        if stripped.startswith('  ') and not stripped.startswith('  - '):
            result_lines.append(line)
            last_insert_idx = len(result_lines) - 1
            continue

        # List item under a known list key — keep
        if in_list_key and stripped.startswith('- '):
            result_lines.append(line)
            continue

        # List item NOT under a known list key — floating wikilink?
        wl_match = WIKILINK_LINE.match(stripped)
        if wl_match and not in_list_key:
            floating.append(wl_match.group(1))
            changed = True
            continue

        # Everything else
        if not stripped:
            in_list_key = False
        result_lines.append(line)

    if floating and changed:
        # Build links: related block
        block_lines = ['links:', '  related:']
        for lnk in floating:
            block_lines.append(f"    - '{lnk}'")
        links_block = '\n'.join(block_lines)
        result_lines.insert(last_insert_idx + 1, links_block)

    return '\n'.join(result_lines), changed


def main():
    modified = []
    skipped = []

    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fname in files:
            if not fname.endswith('.md') or fname in SKIP_FILES:
                continue
            fp = Path(root) / fname
            try:
                text = fp.read_text(encoding='utf-8', errors='ignore')
                m = FM_RE.match(text)
                if not m:
                    continue
                fm_raw = m.group(1)
                new_fm, changed = fix_floating_links(fm_raw)
                if changed:
                    new_text = text[:m.start(1)] + new_fm + text[m.end(1):]
                    fp.write_text(new_text, encoding='utf-8')
                    modified.append(str(fp.relative_to(VAULT)))
            except Exception as e:
                skipped.append(f'{fp.name}: {e}')

    print(f'fix_floating_links.py done')
    print(f'  Modified: {len(modified)} files')
    for f in modified:
        print(f'  OK {f}')
    if skipped:
        print(f'  Errors: {len(skipped)}')
        for s in skipped:
            print(f'  ERR {s}')


if __name__ == '__main__':
    main()
