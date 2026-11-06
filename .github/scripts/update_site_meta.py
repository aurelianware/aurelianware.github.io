#!/usr/bin/env python3
"""Regenerate sitemap.xml and the footer "Last updated" line on each page.

A page is listed when it has a canonical URL pointing at itself and is not
marked noindex. Its date is the last non-merge commit that touched the page,
ignoring this script's own commits, so a refresh never makes every page look
freshly edited.

Run from the repository root:  python3 .github/scripts/update_site_meta.py
"""
import datetime
import pathlib
import re
import subprocess

SITE = "https://aurelianware.com"
BOT_MARKER = "[auto-meta]"
ROOT = pathlib.Path(".")

UPDATED_RE = re.compile(r'\n?\s*<p class="updated">.*?</p>', re.S)
FOOTER_RE = re.compile(r'(<div class="footer-bottom">\s*<p>©[^<]*</p>)')


def url_for(path: pathlib.Path) -> str:
    rel = path.as_posix()
    if rel == "index.html":
        return f"{SITE}/"
    if rel.endswith("/index.html"):
        return f"{SITE}/{rel[: -len('index.html')]}"
    return f"{SITE}/{rel}"


def last_changed(path: pathlib.Path) -> datetime.date:
    out = subprocess.run(
        ["git", "log", "-1", "--no-merges", "--format=%cs",
         "--invert-grep", "--fixed-strings", f"--grep={BOT_MARKER}", "--", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return datetime.date.fromisoformat(out) if out else datetime.date.today()


def listable(path: pathlib.Path, html: str) -> bool:
    if re.search(r'<meta name="robots" content="[^"]*noindex', html):
        return False
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    return bool(m) and m.group(1) == url_for(path)


def human(d: datetime.date) -> str:
    return f"{d:%B} {d.day}, {d.year}"


def main() -> None:
    entries = []
    for path in sorted(ROOT.rglob("*.html")):
        if any(part.startswith(".") for part in path.parts):
            continue
        html = path.read_text()
        if not listable(path, html):
            continue
        changed = last_changed(path)
        entries.append((url_for(path), changed))

        stamp = (f'\n      <p class="updated">Last updated '
                 f'<time datetime="{changed.isoformat()}">{human(changed)}</time></p>')
        new = UPDATED_RE.sub("", html)
        new = FOOTER_RE.sub(lambda m: m.group(1) + stamp, new, count=1)
        if new != html:
            path.write_text(new)

    # Home first, then by path.
    entries.sort(key=lambda e: (e[0] != f"{SITE}/", e[0]))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    lines += [f"  <url><loc>{loc}</loc><lastmod>{d.isoformat()}</lastmod></url>"
              for loc, d in entries]
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n")
    print(f"sitemap.xml: {len(entries)} URLs")


if __name__ == "__main__":
    main()
