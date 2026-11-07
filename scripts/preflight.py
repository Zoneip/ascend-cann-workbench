#!/usr/bin/env python3
"""Read-only screening of tracked and untracked publishable files; not a full audit."""
import ast
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES = {'candidate', 'blocked', 'ready', 'in_progress', 'submitted', 'done', 'deferred'}
REQUIRED = {'id', 'title', 'track', 'priority', 'status', 'owner', 'sources', 'last_checked', 'evidence', 'blockers', 'next_action', 'acceptance', 'tested_commit', 'submission_url', 'reward_status'}

def validate_tasks(data):
    errors = []
    if data.get('schema_version') != 1 or not isinstance(data.get('tasks'), list):
        return ['Invalid task schema']
    ids = set()
    for task in data['tasks']:
        if not isinstance(task, dict) or not REQUIRED <= task.keys():
            errors.append('Task missing required fields')
            continue
        ident = task['id']
        if ident in ids:
            errors.append(f'Duplicate task: {ident}')
        ids.add(ident)
        if task['status'] not in STATES:
            errors.append(f'Invalid status: {ident}')
        if task['status'] == 'blocked' and not task['blockers']:
            errors.append(f'Blocked task without blockers: {ident}')
        if task['status'] == 'submitted' and not task['submission_url']:
            errors.append(f'Submitted task without URL: {ident}')
        if task['status'] == 'done' and not task['evidence']:
            errors.append(f'Done task without evidence: {ident}')
        if not task['sources'] or not task['acceptance'] or not task['next_action']:
            errors.append(f'Missing source/acceptance/next action: {ident}')
    return errors

def main():
    raw = subprocess.check_output(['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=ROOT)
    files = sorted(set(raw.decode().split('\0')) - {''})
    errors = []
    secrets = re.compile(r'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|-----BEGIN (?:OPENSSH|RSA|EC) PRIVATE KEY-----)')
    for name in files:
        path = ROOT / name
        if path.is_symlink():
            errors.append(f'Symlink requires review: {name}')
            continue
        if not path.is_file():
            errors.append(f'Missing candidate file: {name}')
            continue
        if name.split('/')[0] in {'forks', 'repos', 'models', 'workspace'} and path.name != '.gitkeep':
            errors.append(f'External artifact exposed: {name}')
        if path.stat().st_size > 2 * 1024 * 1024:
            errors.append(f'Large candidate file: {name}')
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeError:
            errors.append(f'Binary candidate requires review: {name}')
            continue
        if secrets.search(text):
            errors.append(f'Potential secret in {name} (value redacted)')
        if path.suffix == '.py':
            ast.parse(text, filename=name)
        if path.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', text):
                target = target.strip('<>').split('#')[0]
                if not target or '://' in target or target.startswith('mailto:'):
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.is_relative_to(ROOT) or not resolved.exists():
                    errors.append(f'Broken/nonportable link: {name}: {target}')
    errors += validate_tasks(json.loads((ROOT / 'tasks/candidates.json').read_text()))
    workflow = (ROOT / '.github/workflows/mirror.yml').read_text()
    for unsafe in ('--force', '--prune', 'schedule:'):
        if unsafe in workflow:
            errors.append(f'Unsafe/unapproved mirror operation: {unsafe}')
    print(f'Scanned {len(files)} tracked/untracked non-ignored candidates')
    for error in errors:
        print('FAIL:', error)
    print('PASS' if not errors else 'FAILED')
    return bool(errors)

if __name__ == '__main__':
    raise SystemExit(main())
