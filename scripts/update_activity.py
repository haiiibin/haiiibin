"""Rewrite the Recent Activity section of README.md from the GitHub public events API.

Runs inside GitHub Actions on a daily schedule. No third-party dependencies.
"""
import json
import os
import re
import urllib.request
from datetime import datetime
from pathlib import Path

USER = "haiiibin"
START = "<!--RECENT_ACTIVITY:start-->"
END = "<!--RECENT_ACTIVITY:end-->"
MAX_ITEMS = 5


def fetch_events():
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}/events/public?per_page=60",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "User-Agent": USER,
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


# Lower rank = higher priority. Contributions and releases outrank bare pushes
# so a day of portfolio commits cannot bury a merged PR or a release.
RANK = {"PullRequestEvent": 0, "ReleaseEvent": 0, "CreateEvent": 1, "PushEvent": 2}


def describe(event):
    repo = event["repo"]["name"]
    url = f"https://github.com/{repo}"
    date = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
    t = event["type"]
    p = event["payload"]
    if t == "PushEvent":
        n = len(p.get("commits", [])) or 1
        noun = "commit" if n == 1 else "commits"
        return date, f"- `{date}` Pushed {n} {noun} to [{repo}]({url})"
    if t == "CreateEvent" and p.get("ref_type") == "repository":
        return date, f"- `{date}` Created repository [{repo}]({url})"
    if t == "PullRequestEvent" and p.get("action") in ("opened", "closed"):
        action = "Merged PR in" if p.get("pull_request", {}).get("merged") else f"{p['action'].capitalize()} PR in"
        return date, f"- `{date}` {action} [{repo}]({url})"
    if t == "ReleaseEvent" and p.get("action") == "published":
        return date, f"- `{date}` Published release in [{repo}]({url})"
    return None


def main():
    candidates, seen = [], set()
    # Events arrive newest-first; keep that order as the tiebreaker within a rank.
    for order, event in enumerate(fetch_events()):
        item = describe(event)
        if item is None or item[1] in seen:
            continue
        seen.add(item[1])
        candidates.append((RANK.get(event["type"], 3), order, item[1]))
    candidates.sort(key=lambda c: (c[0], c[1]))
    lines = [c[2] for c in candidates[:MAX_ITEMS]]
    if not lines:
        lines = ["- Quiet week: nothing public to report"]

    readme = Path("README.md")
    text = readme.read_text(encoding="utf-8")
    block = START + "\n" + "\n".join(lines) + "\n" + END
    new_text = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S)
    if new_text != text:
        readme.write_text(new_text, encoding="utf-8")
        print("README updated")
    else:
        print("No changes")


if __name__ == "__main__":
    main()
