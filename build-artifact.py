#!/usr/bin/env python3
"""Generate the Claude Artifact body from index.html.

The Artifact runtime wraps the file it is given in its own
<!doctype html><head>...</head><body> skeleton, so the published file must
carry page content only. This strips index.html's document skeleton and the
meta tags the skeleton already supplies, keeping index.html as the single
source of truth.

Usage: build-artifact.py [OUTPUT]   (default: dist/artifact.html)
"""
import os
import re
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")


def build(src_html):
    head = re.search(r"<head>(.*?)</head>", src_html, re.S)
    body = re.search(r"<body[^>]*>(.*?)</body>", src_html, re.S)
    if not head or not body:
        raise SystemExit("index.html: expected a <head> and a <body>")

    title = re.search(r"<title>.*?</title>", head.group(1), re.S)
    style = re.search(r"<style>.*?</style>", head.group(1), re.S)
    if not title or not style:
        raise SystemExit("index.html: expected a <title> and a <style> in <head>")

    parts = [title.group(0), style.group(0), body.group(1).strip(), ""]
    return "\n".join(parts)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(SRC), "dist", "artifact.html")
    with open(SRC, encoding="utf-8") as fh:
        html = build(fh.read())
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("%s (%d bytes)" % (out, len(html)))


if __name__ == "__main__":
    main()
