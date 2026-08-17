import os
import re
import yaml

MAPPING = {
    # Geowissenschaften
    "Geologie": "geowissenschaften/geologie",
    "geologie": "geowissenschaften/geologie",
    "Paläontologie": "geowissenschaften/palaeontologie",
    "palaeontologie": "geowissenschaften/palaeontologie",
    "Tirol": "geowissenschaften/regionen/tirol",
    "Inn": "geowissenschaften/hydrologie",

    # Biowissenschaften
    "Biologie": "biowissenschaften",
    "Botanik": "biowissenschaften/botanik",
    "Entwicklungsbiologie": "biowissenschaften/entwicklungsbiologie",
    "Evolution der Erhaltung": "biowissenschaften/evolutionsbiologie",
    "Evolutionsbiologie": "biowissenschaften/evolutionsbiologie",
    "Genetik": "biowissenschaften/genetik",
    "Mammalogie": "biowissenschaften/mammalogie",
    "Medizin": "biowissenschaften",
    "Mikrobiologie": "biowissenschaften/mikrobiologie",
    "Neurobiologie": "biowissenschaften/neurobiologie",
    "Zoologie": "biowissenschaften/zoologie",
    "Ökologie": "biowissenschaften/oekologie",

    # Geisteswissenschaften
    "Allgemeinbildung": "geisteswissenschaften/paedagogik/allgemeinbildung",
    "Antike": "geisteswissenschaften/geschichte/antike",
    "Archäologie": "geisteswissenschaften/archaeologie",
    "Autonomie": "geisteswissenschaften/philosophie",
    "Bildung": "geisteswissenschaften/paedagogik",
    "bildung": "geisteswissenschaften/paedagogik",
    "Erinnerung": "geisteswissenschaften/philosophie",
    "Geschichte": "geisteswissenschaften/geschichte",
    "geschichte": "geisteswissenschaften/geschichte",
    "Humanität": "geisteswissenschaften/philosophie",
    "Humboldt": "geisteswissenschaften/paedagogik/selbstbildung",
    "Kant": "geisteswissenschaften/philosophie",
    "Kompetenz": "geisteswissenschaften/paedagogik",
    "Lernen": "geisteswissenschaften/paedagogik",
    "Militärgeschichte": "geisteswissenschaften/geschichte/militaergeschichte",
    "Philosophie": "geisteswissenschaften/philosophie",
    "Pädagogik": "geisteswissenschaften/paedagogik",
    "Raum": "geisteswissenschaften/philosophie",
    "Rechtsgeschichte": "geisteswissenschaften/geschichte/rechtsgeschichte",
    "Renaissance": "geisteswissenschaften/geschichte/renaissance",
    "Rousseau": "geisteswissenschaften/paedagogik",
    "Selbstbildung": "geisteswissenschaften/paedagogik/selbstbildung",
    "Subjekt": "geisteswissenschaften/philosophie",
    "Theorie": "geisteswissenschaften/philosophie",
    "Zeit": "geisteswissenschaften/philosophie",

    # Gesellschaft & Digitales
    "Digitalisierung": "gesellschaft/digitalisierung",
    "Gesellschaft": "gesellschaft",
    "Mediatisierung": "gesellschaft/mediatisierung",
    "Medien": "gesellschaft/medien",

    # Meta
    "clippings": "meta/clippings",
    "index": "meta/index",
    "meta": "meta/instruction",
    "moc": "meta/moc",
    "skill": "meta/skill",
    "zettelkasten": "meta/zettelkasten",
    "expert": "meta/zettelkasten",
    "Rules": "meta/instruction",
    "AI_Instruction": "meta/instruction",
    "Agents": "meta/instruction",
    "Workflow": "meta/instruction",

    # User / Ad-hoc
    "Allgemein": "u/general",
    "general": "u/general",
    "General": "u/general",
}

TARGET_DIRS = ["10-Raw", "20-Literature", "30-Narrative", "40-Permanent", "50-MOC", "70-Meta", "gemini-scribe"]

def migrate_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return False, "no frontmatter"

    parts = content.split("---", 2)
    if len(parts) < 3:
        return False, "invalid frontmatter"

    frontmatter_str = parts[1]
    body = parts[2]

    try:
        data = yaml.safe_load(frontmatter_str)
    except Exception as e:
        return False, f"yaml parse error: {e}"

    if not isinstance(data, dict) or "tags" not in data:
        return False, "no tags field"

    raw_tags = data["tags"]
    if raw_tags is None:
        raw_tags = []
    elif isinstance(raw_tags, str):
        raw_tags = [raw_tags]

    new_tags = []
    changed = False

    for t in raw_tags:
        if not t:
            continue
        t_str = str(t).strip()
        
        # If already starts with u/ or a valid domain, keep (or normalize)
        if t_str.startswith("u/"):
            normalized_u = "u/" + t_str[2:].lower().replace(" ", "-")
            new_tags.append(normalized_u)
            if normalized_u != t_str:
                changed = True
        elif t_str in MAPPING:
            new_tags.append(MAPPING[t_str])
            changed = True
        else:
            # Fallback: if lowercased in mapping
            if t_str.lower() in MAPPING:
                new_tags.append(MAPPING[t_str.lower()])
                changed = True
            else:
                # Keep as lower-kebab-case or u/ tag
                norm = t_str.lower().replace(" ", "-")
                new_tags.append(norm)
                if norm != t_str:
                    changed = True

    # Deduplicate while preserving order
    seen = set()
    dedup_tags = []
    for t in new_tags:
        if t not in seen:
            seen.add(t)
            dedup_tags.append(t)

    if len(dedup_tags) != len(raw_tags):
        changed = True

    if not changed:
        return False, "no changes needed"

    data["tags"] = dedup_tags

    # Dump updated frontmatter safely
    new_fm = yaml.dump(data, allow_unicode=True, sort_keys=False).strip()
    new_content = f"---\n{new_fm}\n---" + body

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True, f"migrated: {raw_tags} -> {dedup_tags}"

def main():
    modified_count = 0
    total_scanned = 0
    for d in TARGET_DIRS:
        if not os.path.exists(d):
            continue
        for root, _, files in os.walk(d):
            for file in files:
                if file.endswith(".md"):
                    total_scanned += 1
                    filepath = os.path.join(root, file)
                    success, msg = migrate_file(filepath)
                    if success:
                        modified_count += 1
                        print(f"[UPDATED] {filepath}: {msg}")

    print(f"\nDone! Scanned {total_scanned} files, updated {modified_count} files.")

if __name__ == "__main__":
    main()
