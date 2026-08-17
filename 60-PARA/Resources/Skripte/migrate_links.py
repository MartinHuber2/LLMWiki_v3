#!/usr/bin/env python3
"""
migrate_links.py
Konvertiert alle Vault-Notizen von flachen `related:` / `relationships:`
Root-Feldern auf das neue verschachtelte `links:` Schema:

  links:
    uses: [...]
    extends: [...]
    derived_from: [...]
    contradicts: [...]
    related: [...]

Leere Unterlisten werden weggelassen.
Bestehende `links:` Einträge werden nicht überschrieben.

Aufruf: python migrate_links.py [vault_path]
"""

import os, re, sys
from pathlib import Path

VAULT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
    r"g:\Meine Ablage\Hidden\Synch\Obsidian\LLMWiki_V4"
)

SKIP_DIRS = {'.git', '.obsidian', '.venv', 'node_modules'}
SKIP_FILES = {'index.md', 'log.md', 'hot.md'}

KNOWN_TYPES = {'uses', 'extends', 'derived_from', 'contradicts', 'replaces', 'implements', 'related_to', 'related'}

# Regex to detect YAML frontmatter
FM_RE = re.compile(r'^---\r?\n(.*?)\r?\n---', re.DOTALL)

def parse_yaml_list(raw: str) -> list[str]:
    """Parse a simple YAML list value like '["[[A]]", "[[B]]"]' or block style."""
    raw = raw.strip()
    items = []
    # Inline list: ["[[A]]", "[[B]]"]
    if raw.startswith('[') and raw.endswith(']'):
        inner = raw[1:-1]
        for part in re.split(r',\s*', inner):
            part = part.strip().strip('"').strip("'")
            if part:
                items.append(part)
    return items

def parse_relationships_block(value_lines: list[str]) -> dict[str, list[str]]:
    """
    Parse an old-style relationships: block that may be a list of objects:
      - target: "[[X]]"
        type: uses
    or a flat list:
      - "[[X]]"
    Returns dict {type: [targets]}
    """
    result: dict[str, list[str]] = {}
    i = 0
    while i < len(value_lines):
        line = value_lines[i].strip()
        if line.startswith('- '):
            entry = line[2:].strip()
            # Could be "[[X]]" directly → related
            if entry.startswith('"[[') or entry.startswith('[['):
                target = entry.strip('"')
                result.setdefault('related', []).append(target)
                i += 1
            elif entry.startswith('target:') or (i + 1 < len(value_lines) and 'target:' in value_lines[i+1]):
                # Object-style: collect target + type from next lines
                obj: dict[str, str] = {}
                if 'target:' in entry:
                    obj['target'] = entry.split('target:', 1)[1].strip().strip('"')
                if 'type:' in entry:
                    obj['type'] = entry.split('type:', 1)[1].strip().strip('"')
                i += 1
                while i < len(value_lines):
                    sub = value_lines[i].strip()
                    if sub.startswith('- ') or not sub:
                        break
                    if sub.startswith('target:'):
                        obj['target'] = sub.split('target:', 1)[1].strip().strip('"')
                    elif sub.startswith('type:'):
                        obj['type'] = sub.split('type:', 1)[1].strip().strip('"')
                    i += 1
                rel_type = obj.get('type', 'related')
                if rel_type not in KNOWN_TYPES:
                    rel_type = 'related'
                if 'target' in obj:
                    result.setdefault(rel_type, []).append(obj['target'])
            else:
                i += 1
        else:
            i += 1
    return result

def render_links(links: dict[str, list[str]]) -> str:
    """Render the links: block as YAML string (no trailing newline)."""
    order = ['uses', 'extends', 'derived_from', 'contradicts', 'implements', 'replaces', 'related_to', 'related']
    lines = ['links:']
    for key in order:
        vals = links.get(key, [])
        if vals:
            items_str = ', '.join(f'"{v}"' for v in vals)
            lines.append(f'  {key}: [{items_str}]')
    # Any extra keys not in order
    for key, vals in links.items():
        if key not in order and vals:
            items_str = ', '.join(f'"{v}"' for v in vals)
            lines.append(f'  {key}: [{items_str}]')
    return '\n'.join(lines)

def migrate_frontmatter(fm_text: str) -> tuple[str, bool]:
    """
    Given raw frontmatter text (between ---), return (new_fm_text, changed).
    """
    lines = fm_text.split('\n')
    new_lines = []
    collected_links: dict[str, list[str]] = {}
    has_links_already = any(l.startswith('links:') for l in lines)
    changed = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip old top-level `related:` field
        if re.match(r'^related:\s*', line):
            raw_val = line.split(':', 1)[1].strip()
            items = parse_yaml_list(raw_val)
            if items:
                collected_links.setdefault('related', []).extend(items)
            # consume continuation lines (block list)
            j = i + 1
            while j < len(lines) and lines[j].startswith('  - '):
                item = lines[j].strip().lstrip('- ').strip().strip('"')
                if item:
                    collected_links.setdefault('related', []).append(item)
                j += 1
            if j > i + 1:
                i = j
            else:
                i += 1
            changed = True
            continue

        # Skip old top-level `relationships:` field
        if re.match(r'^relationships:\s*', line):
            raw_val = line.split(':', 1)[1].strip()
            # Collect block-style sub-lines
            sub_lines = []
            if raw_val and raw_val != '[]':
                sub_lines.append(raw_val)
            j = i + 1
            while j < len(lines) and (lines[j].startswith('  ') or lines[j].startswith('- ')):
                sub_lines.append(lines[j].strip())
                j += 1
            parsed = parse_relationships_block(sub_lines)
            for rel_type, targets in parsed.items():
                collected_links.setdefault(rel_type, []).extend(targets)
            i = j
            changed = True
            continue

        new_lines.append(line)
        i += 1

    if collected_links and not has_links_already:
        # Insert links: block after tags: block or after type:
        insert_after = 0
        for idx, l in enumerate(new_lines):
            if l.startswith('tags:') or l.startswith('type:') or l.startswith('sources:'):
                insert_after = idx
        # Consume any continuation of tags block
        j = insert_after + 1
        while j < len(new_lines) and (new_lines[j].startswith('  ') or new_lines[j].startswith('- ')):
            insert_after = j
            j += 1
        links_block = render_links(collected_links)
        new_lines.insert(insert_after + 1, links_block)

    return '\n'.join(new_lines), changed

def process_file(path: Path) -> bool:
    text = path.read_text(encoding='utf-8', errors='ignore')
    m = FM_RE.match(text)
    if not m:
        return False

    fm_raw = m.group(1)
    new_fm, changed = migrate_frontmatter(fm_raw)
    if not changed:
        return False

    new_text = text[:m.start(1)] + new_fm + text[m.end(1):]
    path.write_text(new_text, encoding='utf-8')
    return True

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
                if process_file(fp):
                    rel = fp.relative_to(VAULT)
                    modified.append(str(rel))
            except Exception as e:
                skipped.append(f'{fp}: {e}')

    print(f'\nmigrate_links.py abgeschlossen')
    print(f'   Modifizierte Dateien: {len(modified)}')
    for f in modified:
        print(f'   OK {f}')
    if skipped:
        print(f'   Fehler: {len(skipped)}')
        for s in skipped:
            print(f'   ERR {s}')

if __name__ == '__main__':
    main()
