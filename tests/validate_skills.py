#!/usr/bin/env python3
"""Validate every skill in skills/. Exits non-zero on any error.

Checks:
  1. SKILL.md exists in each skill directory
  2. YAML frontmatter present, with name + description
  3. frontmatter `name` matches the directory name
  4. description length within the 1024-char limit
  5. every cross-skill reference resolves to a skill in this repo
  6. no absolute host paths (/mnt/skills/user/...) left behind
"""
import os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")
MAX_DESC = 1024

REF = re.compile(r'\$\{CLAUDE_PLUGIN_ROOT\}/skills/([a-z0-9-]+)')
ABS = re.compile(r'/mnt/skills/user/([a-z0-9-]+)')

def frontmatter(text):
    m = re.match(r'---\n(.*?)\n---', text, re.S)
    if not m: return None
    block = m.group(1)
    name = re.search(r'^name:\s*(.+)$', block, re.M)
    desc = re.search(r'^description:\s*(>-?|\|)?\s*\n?(.*?)(?=\n[a-z_-]+:|\Z)', block, re.S | re.M)
    desc_text = " ".join(desc.group(2).split()) if desc else None
    if desc_text and len(desc_text) >= 2 and desc_text[0] == desc_text[-1] and desc_text[0] in ('"', "'"):
        desc_text = desc_text[1:-1]
    return {
        "name": name.group(1).strip() if name else None,
        "description": desc_text,
    }

def main():
    errors, warnings = [], []
    present = sorted(d for d in os.listdir(SKILLS_DIR)
                     if os.path.isdir(os.path.join(SKILLS_DIR, d)))
    if not present:
        print("no skills found"); return 1

    for s in present:
        path = os.path.join(SKILLS_DIR, s, "SKILL.md")
        if not os.path.exists(path):
            errors.append(f"{s}: missing SKILL.md"); continue
        text = open(path, encoding="utf-8").read()

        fm = frontmatter(text)
        if fm is None:
            errors.append(f"{s}: no YAML frontmatter"); continue
        if not fm["name"]:
            errors.append(f"{s}: frontmatter missing `name`")
        elif fm["name"] != s:
            errors.append(f"{s}: frontmatter name is '{fm['name']}' but directory is '{s}'")
        if not fm["description"]:
            errors.append(f"{s}: frontmatter missing `description`")
        elif len(fm["description"]) > MAX_DESC:
            errors.append(f"{s}: description is {len(fm['description'])} chars (max {MAX_DESC})")

        for dirpath, _, files in os.walk(os.path.join(SKILLS_DIR, s)):
            for f in files:
                if not f.endswith(".md"): continue
                body = open(os.path.join(dirpath, f), encoding="utf-8").read()
                rel = os.path.relpath(os.path.join(dirpath, f), ROOT)
                for target in set(REF.findall(body)):
                    if target not in present:
                        errors.append(f"{rel}: references '{target}', which is not in this repo")
                for target in set(ABS.findall(body)):
                    warnings.append(f"{rel}: absolute host path to '{target}' (not portable)")

    print(f"skills checked: {len(present)}")
    for w in sorted(set(warnings)): print(f"  WARN  {w}")
    for e in errors: print(f"  ERROR {e}")
    print(f"\n{len(errors)} error(s), {len(set(warnings))} warning(s)")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
