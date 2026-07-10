#!/usr/bin/env python3
"""Eval script for a Jekyll static-site project.

Runs six dimensions — three hygiene (build, validation, config) and three
growth (capability surface, content freshness, architecture) — and prints
a JSON results array to stdout.

Output format:
    {"results": [{"name": str, "score": float, "weight": float, "passed": bool, "details": str}, ...]}
"""

import datetime
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# HYGIENE dimensions
# ---------------------------------------------------------------------------

def eval_jekyll_build() -> dict:
    """Run 'bundle exec jekyll b -d _site' and check exit code."""
    try:
        result = subprocess.run(
            ["bundle", "exec", "jekyll", "b", "-d", "_site"],
            capture_output=True,
            text=True,
            timeout=300,
        )
        passed = result.returncode == 0
        detail = (result.stderr or result.stdout).strip()[-500:]
        return {
            "name": "jekyll_build",
            "score": 1.0 if passed else 0.0,
            "weight": 0.25,
            "passed": passed,
            "details": detail or ("Build succeeded" if passed else "Build failed"),
        }
    except subprocess.TimeoutExpired:
        return {
            "name": "jekyll_build",
            "score": 0.0,
            "weight": 0.25,
            "passed": False,
            "details": "Timed out after 300s",
        }
    except FileNotFoundError:
        return {
            "name": "jekyll_build",
            "score": 0.0,
            "weight": 0.25,
            "passed": False,
            "details": "bundle not found — is Ruby/Bundler installed?",
        }


def eval_html_validation() -> dict:
    """Run htmlproofer on _site and check exit code."""
    cmd = [
        "bundle", "exec", "htmlproofer", "_site",
        "--disable-external",
        "--ignore-urls",
        "/^http:\\/\\/127.0.0.1/,/^http:\\/\\/0.0.0.0/,/^http:\\/\\/localhost/",
        "--ignore-empty-alt",
        "--ignore-missing-alt",
    ]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
        )
        passed = result.returncode == 0
        detail = (result.stderr or result.stdout).strip()[-500:]
        return {
            "name": "html_validation",
            "score": 1.0 if passed else 0.0,
            "weight": 0.20,
            "passed": passed,
            "details": detail or ("Validation passed" if passed else "Validation failed"),
        }
    except subprocess.TimeoutExpired:
        return {
            "name": "html_validation",
            "score": 0.0,
            "weight": 0.20,
            "passed": False,
            "details": "Timed out after 300s",
        }
    except FileNotFoundError:
        return {
            "name": "html_validation",
            "score": 0.0,
            "weight": 0.20,
            "passed": False,
            "details": "bundle not found — is Ruby/Bundler installed?",
        }


def eval_config_parser() -> dict:
    """Verify _config.yml is valid YAML and has required keys."""
    config_path = Path("_config.yml")
    required_keys = {"baseurl", "url", "markdown", "plugins"}

    if not config_path.exists():
        return {
            "name": "config_parser",
            "score": 0.0,
            "weight": 0.05,
            "passed": False,
            "details": "_config.yml not found",
        }

    try:
        data = yaml.safe_load(config_path.read_text())
    except yaml.YAMLError as exc:
        return {
            "name": "config_parser",
            "score": 0.0,
            "weight": 0.05,
            "passed": False,
            "details": f"Invalid YAML: {exc}",
        }

    if not isinstance(data, dict):
        return {
            "name": "config_parser",
            "score": 0.0,
            "weight": 0.05,
            "passed": False,
            "details": "_config.yml does not parse as a mapping",
        }

    missing = required_keys - set(data.keys())
    if missing:
        return {
            "name": "config_parser",
            "score": 0.0,
            "weight": 0.05,
            "passed": False,
            "details": f"Missing required keys: {', '.join(sorted(missing))}",
        }

    return {
        "name": "config_parser",
        "score": 1.0,
        "weight": 0.05,
        "passed": True,
        "details": f"Valid YAML with all required keys ({', '.join(sorted(required_keys))})",
    }


# ---------------------------------------------------------------------------
# GROWTH dimensions
# ---------------------------------------------------------------------------

def _count_files(directory: str, extensions: tuple | None = None) -> int:
    d = Path(directory)
    if not d.is_dir():
        return 0
    if extensions:
        return sum(1 for f in d.rglob("*") if f.is_file() and f.suffix in extensions)
    return sum(1 for f in d.rglob("*") if f.is_file())


def eval_capability_surface() -> dict:
    """Count pages, posts, data files, layouts, includes."""
    pages = _count_files("_pages", (".html", ".md"))
    posts = _count_files("_posts", (".md", ".html"))
    data = _count_files("_data", (".yml", ".yaml", ".json", ".csv"))
    layouts = _count_files("_layouts", (".html",))
    includes = _count_files("_includes", (".html", ".scss"))

    total = pages + posts + data + layouts + includes
    score = min(1.0, total / 50)

    detail = f"pages={pages}, posts={posts}, data={data}, layouts={layouts}, includes={includes}, total={total}"
    return {
        "name": "capability_surface",
        "score": round(score, 3),
        "weight": 0.20,
        "passed": score > 0,
        "details": detail,
    }


def eval_content_freshness() -> dict:
    """Score based on how recent the newest post is."""
    posts_dir = Path("_posts")
    if not posts_dir.is_dir():
        return {
            "name": "content_freshness",
            "score": 0.0,
            "weight": 0.15,
            "passed": False,
            "details": "_posts/ directory not found",
        }

    date_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2})-")
    newest = None
    for f in posts_dir.iterdir():
        m = date_pattern.match(f.name)
        if m:
            try:
                d = datetime.date.fromisoformat(m.group(1))
                if newest is None or d > newest:
                    newest = d
            except ValueError:
                continue

    if newest is None:
        return {
            "name": "content_freshness",
            "score": 0.0,
            "weight": 0.15,
            "passed": False,
            "details": "No dated posts found in _posts/",
        }

    age_days = (datetime.date.today() - newest).days
    if age_days <= 90:
        score = 1.0
    elif age_days <= 180:
        score = 0.7
    elif age_days <= 365:
        score = 0.4
    else:
        score = 0.2

    return {
        "name": "content_freshness",
        "score": score,
        "weight": 0.15,
        "passed": score >= 0.4,
        "details": f"Newest post: {newest} ({age_days} days ago)",
    }


def eval_architecture() -> dict:
    """Check for proper Jekyll directory structure."""
    expected_dirs = ["_layouts", "_includes", "_data", "_posts", "_sass"]
    present = 0
    details = []

    for d in expected_dirs:
        p = Path(d)
        if p.is_dir() and any(p.iterdir()):
            present += 1
            details.append(f"{d}: ok")
        elif p.is_dir():
            details.append(f"{d}: empty")
        else:
            details.append(f"{d}: missing")

    score = present / len(expected_dirs) if expected_dirs else 0.0

    return {
        "name": "architecture",
        "score": round(score, 3),
        "weight": 0.15,
        "passed": score >= 0.6,
        "details": ", ".join(details),
    }


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

EVALS = [
    eval_jekyll_build,
    eval_html_validation,
    eval_config_parser,
    eval_capability_surface,
    eval_content_freshness,
    eval_architecture,
]


def main() -> None:
    results = [fn() for fn in EVALS]
    output = {"results": results}
    json.dump(output, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
