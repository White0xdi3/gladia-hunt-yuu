#!/usr/bin/env python3
"""Upsert dedup facts into knowledge/facts.json and regenerate knowledge/index.md.

Replaces the old naive "append if exact string not already in file" dedup,
which let knowledge/index.md and reports/hypotheses.md grow unboundedly
(400KB+ / 1.6MB+) because every cycle's LLM output rewords the same fact
slightly differently, so exact-string matching never caught the duplicate.

Reads text on stdin. Recognizes two shapes:
  1. Structured (from hunt.yml analyst 8-step output):
     "[LEARN] ACCEPTED|REJECTED <CLASS> @ <asset>: <reason>"
  2. Loose (from triage.yml's free-text verdicts): any line starting with
     VALID/INVALID/HOLD plus a trailing reason -- keyed by asset host (if
     recognizable) plus a hash of the normalized reason, so near-duplicate
     restatements collapse instead of accumulating forever.

Each fact is keyed so the newest verdict replaces the old one in place;
first_seen is preserved across updates so history isn't lost, it's just
not repeated every cycle.
"""
import json, os, re, sys, datetime, hashlib

FACTS_PATH = 'knowledge/facts.json'
INDEX_PATH = 'knowledge/index.md'
KNOWN_HOSTS = ('api.gladia.io', 'app.gladia.io', 'gladia.io', 'npm', 'pypi', 'sdk')

STRUCTURED_RE = re.compile(r'^\[LEARN\]\s+(ACCEPTED|REJECTED)\s+(\S+)\s+@\s+([^:]+):\s*(.*)$', re.I | re.M)
LOOSE_RE = re.compile(r'(?im)^\s*(VALID|INVALID|HOLD)\b.*?[-:]\s*(.{10,220})')

# The model spells the same asset/class inconsistently cycle to cycle
# ("api" vs "api.gladia.io", "OATH" vs "OAUTH"); normalize so those collapse
# to one fact instead of sitting as separate near-duplicate keys.
ASSET_ALIASES = {
    'api': 'api.gladia.io', 'app': 'app.gladia.io',
    'npm': 'sdk', 'pypi': 'sdk', 'npm registry': 'sdk',
}
CLASS_ALIASES = {'OATH': 'OAUTH'}


def normalize_asset(asset):
    a = asset.strip().strip('`').rstrip('.,;:')
    if a.lower() in ASSET_ALIASES:
        return ASSET_ALIASES[a.lower()]
    if re.match(r'(?i)^npm\b', a) or re.match(r'(?i)^pypi\b', a):
        return 'sdk'
    return a


def normalize_class(cls):
    c = cls.strip().upper()
    return CLASS_ALIASES.get(c, c)


def load_facts():
    if os.path.exists(FACTS_PATH):
        try:
            return json.load(open(FACTS_PATH))
        except Exception:
            return {}
    return {}


def save_facts(facts):
    os.makedirs(os.path.dirname(FACTS_PATH) or '.', exist_ok=True)
    json.dump(facts, open(FACTS_PATH, 'w'), indent=1, sort_keys=True)
    open(FACTS_PATH, 'a').write('\n')


def render_index(facts):
    os.makedirs(os.path.dirname(INDEX_PATH) or '.', exist_ok=True)
    lines = ['# Knowledge Base (deduped facts -- one row per class@asset, updated in place)', '']
    for key in sorted(facts):
        f = facts[key]
        lines.append(f"- [{f['verdict']}] {key}: {f['reason']} (first {f['first_seen']}, last {f['last_seen']})")
    open(INDEX_PATH, 'w').write('\n'.join(lines) + '\n')


def upsert(facts, verdict, key, reason, stamp):
    prior = facts.get(key)
    facts[key] = {
        'verdict': verdict.upper(),
        'reason': reason.strip()[:220],
        'first_seen': prior['first_seen'] if prior else stamp,
        'last_seen': stamp,
    }


def main():
    text = sys.stdin.read()
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    facts = load_facts()
    changed = 0

    for verdict, cls, asset, reason in STRUCTURED_RE.findall(text):
        key = f"{normalize_class(cls)}@{normalize_asset(asset)}"
        upsert(facts, verdict, key, reason, stamp)
        changed += 1

    if not changed:
        for verdict, reason in LOOSE_RE.findall(text):
            host = next((h for h in KNOWN_HOSTS if h in reason.lower()), 'unspecified')
            norm = re.sub(r'[^a-z0-9]+', ' ', reason.lower()).strip()
            reason_hash = hashlib.sha1(norm[:80].encode()).hexdigest()[:10]
            key = f"TRIAGE@{host}#{reason_hash}"
            mapped_verdict = 'REJECTED' if verdict.upper() == 'INVALID' else verdict.upper()
            upsert(facts, mapped_verdict, key, reason, stamp)
            changed += 1

    if changed:
        save_facts(facts)
        render_index(facts)
    print(f'upserted {changed} facts, {len(facts)} total in {FACTS_PATH}')


if __name__ == '__main__':
    main()
