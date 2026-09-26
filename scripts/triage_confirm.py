"""File one markdown record per confirmed-VALID bug under triage/, instead
of only a free-text line in reports/valid-bugs.md.

Reads a triage cycle's full 7-Question-Gate output on stdin. For each
genuine "Verdict: VALID" segment, derives a slug from the package/asset
it's about (e.g. "gladia@0.1.3" -> gladia-0-1-3) and writes/updates
triage/<slug>.md. Re-confirmations of an already-known bug append a dated
section to the existing file instead of creating a duplicate -- same
finding, same file, growing evidence trail.

Uses the same VALID/NOT_VALID detection as scripts/watchdog.py (see that
file's comment on why "NO NEW VALID" must not match).
"""
import os
import re
import sys
import datetime

TRIAGE_DIR = "triage"

VALID_RE = re.compile(r'^\s*(?:-\s*)?\**Verdict:?\**\s*VALID\b(?!\s*\()', re.M | re.I)
NOT_VALID_NEARBY = re.compile(r'\bNO\s+(NEW\s+)?VALID\b|\bINVALID\b', re.I)

PKG_RE = re.compile(r'\b([a-zA-Z0-9@/_.-]{2,40})@(\d+\.\d+\.\d+)\b')
HOST_RE = re.compile(r'\b(api\.gladia\.io|app\.gladia\.io|gladia\.io)\b', re.I)


def slugify(text):
    s = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    return s[:60] or "finding"


def derive_slug(block):
    m = PKG_RE.search(block)
    if m:
        return slugify(f"{m.group(1)}-{m.group(2)}")
    m = HOST_RE.search(block)
    if m:
        return slugify(m.group(1))
    return None


def split_lead_blocks(text):
    # triage answers Q1-Q7 per lead; blank-line-separated paragraphs are a
    # reasonable best-effort block boundary for free-form LLM output.
    return re.split(r'\n\s*\n', text)


def main():
    text = sys.stdin.read()
    os.makedirs(TRIAGE_DIR, exist_ok=True)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    created = updated = 0
    for block in split_lead_blocks(text):
        hits = [l for l in block.splitlines() if VALID_RE.search(l) and not NOT_VALID_NEARBY.search(l)]
        if not hits:
            continue
        slug = derive_slug(block) or slugify(re.sub(r'[^a-z0-9 ]', '', hits[0].lower())[:40])
        path = os.path.join(TRIAGE_DIR, f"{slug}.md")
        excerpt = block.strip()[:2000]
        if os.path.exists(path):
            with open(path, "a") as f:
                f.write(f"\n\n## Re-confirmed {stamp}\n{excerpt}\n")
            updated += 1
        else:
            with open(path, "w") as f:
                f.write(f"# Confirmed finding: {slug}\n\n## Confirmed {stamp}\n{excerpt}\n")
            created += 1
    print(f"triage_confirm: {created} new confirmed-bug file(s), {updated} re-confirmed this cycle")


if __name__ == "__main__":
    main()
