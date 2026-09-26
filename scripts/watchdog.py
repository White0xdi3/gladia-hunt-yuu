"""Watchdog: surface overdue human follow-ups and new VALID findings as
GitHub Issues instead of leaving them buried in markdown logs.

Two checks:
1. Overdue follow-ups: any leads/*.md file with a "FOLLOW-UP DUE: YYYY-MM-DD"
   marker that has passed with no later "## YYYY-MM-DD STATUS:" checkpoint.
2. New VALID findings: genuine "Verdict: VALID" lines appended to
   reports/valid-bugs.md since this script's last run.

Check 1 is idempotent via a `<!-- watchdog:<key> -->` marker in the issue
body (same pattern scripts/sync-issues.py uses). Check 2 is idempotent via a
byte offset persisted in reports/.watchdog-state.json: valid-bugs.md is
append-only and the same underlying finding gets re-confirmed with
differently-worded VALID lines across many triage cycles (the npm
impersonation bug alone produced 6+ distinct wordings over 6 weeks), so
content-based fuzzy dedup of free text doesn't converge cleanly -- tracking
"already seen up to byte N" sidesteps that entirely instead of trying to
NLP-dedupe prose. First run intentionally does NOT backfill 6 weeks of
history for an already-known, already human-reported finding (the
overdue-followup check already surfaces that); it only alerts on genuinely
new content going forward.
"""
import os
import re
import json
import datetime
from pathlib import Path
from github import Github

REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GITHUB_TOKEN"]
TODAY = datetime.date.today()
STATE_PATH = Path("reports/.watchdog-state.json")

DUE_RE = re.compile(r'FOLLOW-UP DUE:\s*(\d{4}-\d{2}-\d{2})')
STATUS_RE = re.compile(r'^##\s*(\d{4}-\d{2}-\d{2})\s+STATUS:', re.M)
# Deliberately excludes "NO NEW VALID" / "INVALID" -- see triage.yml's
# valid-bugs counter, which had the same false-positive bug this avoids.
VALID_RE = re.compile(
    r'^\s*(?:-\s*)?\**Verdict:?\**\s*VALID\b(?!\s*\()', re.M | re.I)
NOT_VALID_NEARBY = re.compile(r'\bNO\s+(NEW\s+)?VALID\b|\bINVALID\b', re.I)


def ensure_label(repo, name, color):
    try:
        repo.get_label(name)
    except Exception:
        repo.create_label(name, color)


def find_marker(repo, marker, state="all"):
    for iss in repo.get_issues(state=state, labels=["watchdog"]):
        if marker in (iss.body or ""):
            return iss
    return None


def check_overdue_followups(repo):
    ensure_label(repo, "watchdog", "e11d21")
    ensure_label(repo, "overdue-followup", "d93f0b")
    for path in sorted(Path("leads").glob("*.md")):
        text = path.read_text(errors="ignore")
        dues = DUE_RE.findall(text)
        if not dues:
            continue
        latest_due = max(datetime.date.fromisoformat(d) for d in dues)
        statuses = STATUS_RE.findall(text)
        latest_status = max((datetime.date.fromisoformat(d) for d in statuses), default=None)
        overdue = TODAY > latest_due and (latest_status is None or latest_status <= latest_due)
        marker = f"<!-- watchdog:followup:{path.name} -->"
        existing = find_marker(repo, marker, state="all")

        if overdue:
            days_over = (TODAY - latest_due).days
            body = (f"{marker}\n\n"
                    f"## Overdue follow-up\n`{path}`\n\n"
                    f"## Due\n{latest_due.isoformat()} ({days_over} days ago)\n\n"
                    f"## Last status checkpoint\n{latest_status.isoformat() if latest_status else 'none found'}\n\n"
                    f"_auto-flagged by scripts/watchdog.py -- update the STATUS line in "
                    f"`{path}` once you've followed up, and this closes itself next run._")
            if existing is None:
                repo.create_issue(
                    title=f"Overdue follow-up: {path.stem}",
                    body=body, labels=["watchdog", "overdue-followup"])
                print(f"opened overdue-followup issue for {path}")
            elif existing.state != "open":
                existing.edit(state="open", body=body)
                existing.create_comment("Still overdue -- reopening.")
                print(f"reopened overdue-followup issue for {path}")
            else:
                if existing.body != body:
                    existing.edit(body=body)
        elif existing is not None and existing.state == "open":
            existing.edit(state="closed")
            existing.create_comment("Status checkpoint now newer than the due date -- closing.")
            print(f"closed resolved overdue-followup issue for {path}")


def load_state():
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text())
        except Exception:
            return {}
    return {}


def save_state(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=1, sort_keys=True) + "\n")


def check_new_valid_findings(repo):
    path = Path("reports/valid-bugs.md")
    if not path.exists():
        return
    ensure_label(repo, "watchdog", "e11d21")
    ensure_label(repo, "valid-finding", "0e8a16")

    state = load_state()
    size = path.stat().st_size
    offset = state.get("valid_bugs_offset")
    if offset is None:
        state["valid_bugs_offset"] = size
        save_state(state)
        print("watchdog: first run, baselining valid-bugs.md offset (no backfill)")
        return

    with open(path, "rb") as f:
        f.seek(min(offset, size))
        new_text = f.read().decode("utf-8", "ignore")
    state["valid_bugs_offset"] = size
    save_state(state)

    if not new_text.strip():
        print("no new valid-bugs.md content since last run")
        return

    hits, seen = [], set()
    for l in new_text.splitlines():
        if VALID_RE.search(l) and not NOT_VALID_NEARBY.search(l):
            clean = re.sub(r'^\s*-\s*', '', l.strip())
            key = re.sub(r'\s+', ' ', clean.lower())[:60]
            if key in seen:
                continue
            seen.add(key)
            hits.append(clean[:300])
    if not hits:
        print("no genuine VALID verdicts in new content")
        return

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    body = ("## New VALID verdict(s) since last watchdog run\n\n"
            + "\n".join(f"- {h}" for h in hits[:15])
            + f"\n\n_auto-flagged by scripts/watchdog.py from reports/valid-bugs.md at {stamp}. "
              f"Cross-check leads/lead-human.md before acting -- this may restate an "
              f"already-tracked/already-reported finding rather than a new one._")
    repo.create_issue(title=f"New VALID verdict(s) - {stamp}", body=body,
                       labels=["watchdog", "valid-finding", "high-confidence"])
    print(f"opened valid-finding issue with {len(hits)} new verdict line(s)")


def main():
    g = Github(TOKEN)
    repo = g.get_repo(REPO)
    check_overdue_followups(repo)
    check_new_valid_findings(repo)


if __name__ == "__main__":
    main()
