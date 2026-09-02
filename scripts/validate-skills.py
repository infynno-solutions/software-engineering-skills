#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT=Path(__file__).resolve().parents[1] / 'skills'
errors=[]
skills=list(ROOT.glob('*/*/SKILL.md'))

if len(skills) != 138:
    errors.append(f'Expected 138 skills, found {len(skills)}')

seen=set()
for p in skills:
    skill_dir=p.parent.name
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', skill_dir):
        errors.append(f'Invalid skill directory name: {p}')
    text=p.read_text()
    if not text.startswith('---\n'):
        errors.append(f'Missing YAML frontmatter: {p}')
        continue
    parts=text.split('---\n',2)
    if len(parts)!=3:
        errors.append(f'Malformed frontmatter: {p}')
        continue
    fm=parts[1]
    name_m=re.search(r'^name:\s*(\S+)\s*$', fm, re.M)
    desc_m=re.search(r'^description:\s*(.+)$', fm, re.M)
    if not name_m or not desc_m:
        errors.append(f'Missing name/description: {p}')
        continue
    name=name_m.group(1)
    if name != skill_dir:
        errors.append(f'name does not match directory: {p} ({name} != {skill_dir})')
    if name in seen:
        errors.append(f'Duplicate skill name: {name}')
    seen.add(name)
    desc=desc_m.group(1).strip()
    if len(desc)>1024:
        errors.append(f'Description > 1024 chars: {p}')
    body=parts[2]
    if not re.search(r'^#\s+[^#]', body, re.M):
        errors.append(f'Missing H1: {p}')
    if re.search(r'^(id|category|type|status|version|tags):', fm, re.M):
        errors.append(f'Nonstandard frontmatter fields remain: {p}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'OK: {len(skills)} skills validated')
