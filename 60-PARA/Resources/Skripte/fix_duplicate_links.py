"""
fix_duplicate_links.py
Repariert YAML-Frontmatter in dem:
1. Ein malformierter inline links:-Block (mit 'type:' Resten) entfernt wird
2. Doppelte links:-Schluessel zu einem einzigen Block zusammengefuehrt werden
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


def collect_links_blocks(fm_text: str) -> tuple[dict[str, list[str]], list[str]]:
    """
    Parse all links: blocks from frontmatter.
    Returns (merged_links_dict, clean_lines_without_links_blocks).
    """
    lines = fm_text.split('\n')
    merged: dict[str, list[str]] = {}
    clean: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()

        # Detect start of a links: block
        if re.match(r'^links:', stripped):
            # Check if it's an inline malformed line
            rest = stripped[len('links:'):].strip()
            if rest and not rest.startswith('#'):
                # Malformed inline — skip the whole line, discard
                i += 1
                # consume any indented sub-lines (there usually are none for inline)
                while i < len(lines) and (lines[i].startswith('  ') or lines[i].startswith('\t')):
                    i += 1
                continue

            # Normal block-style: consume sub-lines
            i += 1
            current_subkey = None
            while i < len(lines):
                sub = lines[i]
                sub_stripped = sub.rstrip()

                # End of links block: non-indented non-empty line that isn't a list item
                if sub_stripped and not sub_stripped.startswith('  ') and not sub_stripped.startswith('\t') and not sub_stripped.startswith('- '):
                    break

                # Sub-key like '  related:' or '  uses:'
                sub_key_match = re.match(r'^\s{2}([a-z_]+):\s*$', sub_stripped)
                if sub_key_match:
                    current_subkey = sub_key_match.group(1)
                    i += 1
                    continue

                # Inline sub-key like '  related: ["[[A]]", "[[B]]"]'
                inline_sub_match = re.match(r'^\s{2}([a-z_]+):\s*\[(.+)\]\s*$', sub_stripped)
                if inline_sub_match:
                    current_subkey = inline_sub_match.group(1)
                    raw_items = inline_sub_match.group(2)
                    # Parse items
                    for part in re.split(r',\s*', raw_items):
                        part = part.strip().strip('"').strip("'")
                        # Filter out garbled tokens like 'type: extends}'"
                        if part.startswith('[[') and part.endswith(']]'):
                            merged.setdefault(current_subkey, []).append(part)
                    i += 1
                    continue

                # List item like '    - "[[X]]"'
                list_item_match = re.match(r'^\s+- ["\']?(\[\[.*?\]\])["\']?\s*$', sub_stripped)
                if list_item_match and current_subkey:
                    merged.setdefault(current_subkey, []).append(list_item_match.group(1))
                    i += 1
                    continue

                # Empty line inside block
                if not sub_stripped:
                    i += 1
                    continue

                # Anything else — end of block
                break
            continue

        # Regular frontmatter line
        clean.append(line)
        i += 1

    return merged, clean


def render_links(links: dict[str, list[str]]) -> str:
    order = ['uses', 'extends', 'derived_from', 'contradicts', 'implements', 'replaces', 'related_to', 'related']
    lines = ['links:']
    for key in order:
        vals = links.get(key, [])
        if vals:
            lines.append(f'  {key}:')
            for v in vals:
                lines.append(f"    - '{v}'")
    for key, vals in links.items():
        if key not in order and vals:
            lines.append(f'  {key}:')
            for v in vals:
                lines.append(f"    - '{v}'")
    return '\n'.join(lines)


def fix_file(fp: Path) -> bool:
    text = fp.read_text(encoding='utf-8', errors='ignore')
    m = FM_RE.match(text)
    if not m:
        return False

    fm_raw = m.group(1)

    # Quick check: does this file have a problem?
    links_count = len(re.findall(r'^links:', fm_raw, re.MULTILINE))
    has_malformed = bool(re.search(r'^links:\s*\[', fm_raw, re.MULTILINE))
    if links_count <= 1 and not has_malformed:
        return False

    merged, clean_lines = collect_links_blocks(fm_raw)
    if not merged:
        return False

    links_block = render_links(merged)
    # Append links block at end of clean frontmatter
    clean_lines.append(links_block)
    new_fm = '\n'.join(clean_lines)

    new_text = text[:m.start(1)] + new_fm + text[m.end(1):]
    fp.write_text(new_text, encoding='utf-8')
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
                if fix_file(fp):
                    modified.append(str(fp.relative_to(VAULT)))
            except Exception as e:
                skipped.append(f'{fp.name}: {e}')

    print(f'fix_duplicate_links.py done')
    print(f'  Fixed: {len(modified)} files')
    for f in modified:
        print(f'  OK {f}')
    if skipped:
        print(f'  Errors: {len(skipped)}')
        for s in skipped:
            print(f'  ERR {s}')


if __name__ == '__main__':
    main()
