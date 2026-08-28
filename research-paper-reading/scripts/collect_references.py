#!/usr/bin/env python3
"""Copy local paper inputs and download URL sources into a references folder."""

from __future__ import annotations

import argparse
import json
import mimetypes
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def safe_name(value: str, fallback: str) -> str:
    value = Path(value).name.strip()
    cleaned = "".join(ch if ch.isalnum() or ch in ".-_" else "_" for ch in value)
    return cleaned or fallback


def unique_path(directory: Path, filename: str) -> Path:
    candidate = directory / filename
    stem = candidate.stem
    suffix = candidate.suffix
    index = 2
    while candidate.exists():
        candidate = directory / f"{stem}-{index}{suffix}"
        index += 1
    return candidate


def load_manifest(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Cannot read {path}: {exc}") from exc
    if not isinstance(data, list):
        raise RuntimeError(f"Expected {path} to contain a JSON list")
    return data


def write_manifest(path: Path, entries: list[dict[str, object]]) -> None:
    path.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n")


def add_local(source: Path, output: Path) -> dict[str, object]:
    if not source.is_file():
        raise FileNotFoundError(f"Not a file: {source}")
    destination = unique_path(output, safe_name(source.name, "source"))
    shutil.copy2(source, destination)
    return {
        "input": str(source),
        "kind": "local",
        "status": "downloaded",
        "path": str(destination),
    }


def add_url(url: str, output: Path, timeout: int) -> dict[str, object]:
    request = urllib.request.Request(url, headers={"User-Agent": "Codex research-paper-reading"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
            content_type = response.headers.get_content_type()
            final_url = response.geturl()
            parsed = urllib.parse.urlparse(final_url)
            filename = safe_name(Path(parsed.path).name, "article")
            if "." not in filename:
                extension = mimetypes.guess_extension(content_type) or ".bin"
                filename += extension
            destination = unique_path(output, filename)
            destination.write_bytes(body)
            return {
                "input": url,
                "final_url": final_url,
                "kind": "url",
                "status": "downloaded",
                "content_type": content_type,
                "path": str(destination),
                "bytes": len(body),
            }
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
        return {"input": url, "kind": "url", "status": "failed", "error": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", help="URLs or local files")
    parser.add_argument("--output", default="references", help="Reference directory")
    parser.add_argument("--timeout", type=int, default=30, help="URL timeout in seconds")
    args = parser.parse_args()

    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    manifest_path = output / "manifest.json"
    entries = load_manifest(manifest_path)
    timestamp = datetime.now(timezone.utc).isoformat()
    failures = 0

    for raw_input in args.inputs:
        if urllib.parse.urlparse(raw_input).scheme in {"http", "https"}:
            entry = add_url(raw_input, output, args.timeout)
        else:
            try:
                entry = add_local(Path(raw_input).expanduser().resolve(), output)
            except (FileNotFoundError, OSError) as exc:
                entry = {"input": raw_input, "kind": "local", "status": "failed", "error": str(exc)}
        entry["collected_at"] = timestamp
        entries.append(entry)
        if entry["status"] == "failed":
            failures += 1
            print(f"FAILED: {raw_input}: {entry['error']}", file=sys.stderr)
        else:
            print(f"SAVED: {entry['path']}")

    write_manifest(manifest_path, entries)
    print(f"Manifest: {manifest_path}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
