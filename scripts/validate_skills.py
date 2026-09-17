#!/usr/bin/env python3
"""Validate Blackbook's metadata, local Markdown links, and installable layout."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import yaml

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools'}


def validate(root=ROOT):
    errors = []
    skills = list((root / 'skills').iterdir())
    for skill in sorted(skills):
        if not skill.is_dir():
            continue
        entry = skill / 'SKILL.md'
        if not entry.is_file():
            errors.append(f'{skill.name}: missing SKILL.md')
            continue
        text = entry.read_text()
        match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        try:
            data = yaml.safe_load(match.group(1)) if match else None
        except yaml.YAMLError:
            data = None
        if not isinstance(data, dict):
            errors.append(f'{skill.name}: invalid frontmatter')
            continue
        if set(data) - ALLOWED:
            errors.append(f'{skill.name}: unsupported frontmatter keys')
        name = data.get('name', '')
        if not isinstance(name, str) or name != skill.name or len(name) > 64 or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            errors.append(f'{skill.name}: invalid or mismatched name')
        for field, limit in (('description', 1024), ('compatibility', 500)):
            if field == 'compatibility' and field not in data:
                continue
            value = data.get(field)
            if not isinstance(value, str) or not 1 <= len(value.strip()) <= limit:
                errors.append(f'{skill.name}: invalid {field}')
        metadata = data.get('metadata', {})
        if not isinstance(metadata, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in metadata.items()):
            errors.append(f'{skill.name}: metadata must map strings to strings')
        for doc in skill.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
                link = urlsplit(target)
                if link.scheme or not link.path:
                    continue
                resolved = (doc.parent / unquote(link.path)).resolve()
                if not resolved.is_relative_to(skill.resolve()) or not resolved.exists():
                    errors.append(f'{doc.relative_to(root)}: missing or nonportable link {target}')
    return errors


if __name__ == '__main__':
    errors = validate()
    print('\n'.join(errors) if errors else 'All skills passed metadata and local-link checks.')
    sys.exit(bool(errors))
