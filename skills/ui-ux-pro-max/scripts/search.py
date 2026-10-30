#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI/UX Pro Max Search - BM25 search over the UI/UX CSV database.

Usage (run with `python3 -I`, from the project root):
  search.py "<query>" [--domain <domain>] [--max-results 3] [--json]
  search.py "<query>" --stack <stack> [--max-results 3] [--json]
  search.py "<query>" --design-system [-p "Project Name"] [-f ascii|markdown]
  search.py "<query>" --design-system --persist -p "Project Name" [--page "dashboard"] [-o <dir>] [--force]

Domains: style, color, chart, landing, product, ux, typography, icons
Stacks:  html-tailwind, react, nextjs, astro, vue, nuxtjs, nuxt-ui, svelte,
         swiftui, react-native, flutter, shadcn, jetpack-compose

Persistence (Master + Overrides): --persist writes design-system/<slug>/MASTER.md
and, with --page, design-system/<slug>/pages/<page>.md. Existing files are kept
unless --force is given.
"""

import argparse
import io
import json
import sys
from pathlib import Path

# `python3 -I` drops the script directory from sys.path: add this skill's own
# scripts/ directory explicitly (and only it) so the sibling modules resolve.
sys.path.insert(0, str(Path(__file__).resolve().parent))
# The skill folder is shared (symlinked) into runtimes: never write __pycache__ there.
sys.dont_write_bytecode = True

from core import CSV_CONFIG, AVAILABLE_STACKS, MAX_RESULTS, search, search_stack  # noqa: E402
from design_system import generate_design_system_with_files  # noqa: E402

# Force UTF-8 for stdout/stderr (Windows consoles default to cp1252)
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def format_output(result):
    """Format results for model consumption (token-optimized)"""
    if "error" in result:
        return f"Error: {result['error']}"

    output = []
    if result.get("stack"):
        output.append("## UI Pro Max Stack Guidelines")
        output.append(f"**Stack:** {result['stack']} | **Query:** {result['query']}")
    else:
        output.append("## UI Pro Max Search Results")
        output.append(f"**Domain:** {result['domain']} | **Query:** {result['query']}")
    output.append(f"**Source:** {result['file']} | **Found:** {result['count']} results\n")

    if not result['results']:
        output.append("No match: retry with other or more specific keywords.")

    for i, row in enumerate(result['results'], 1):
        output.append(f"### Result {i}")
        for key, value in row.items():
            value_str = str(value)
            if len(value_str) > 300:
                value_str = value_str[:300] + "..."
            output.append(f"- **{key}:** {value_str}")
        output.append("")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="UI Pro Max Search")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()), help="Search domain (auto-detected when omitted)")
    parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, help="Stack-specific guidelines")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help=f"Max results (default: {MAX_RESULTS})")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    # Design system generation
    parser.add_argument("--design-system", "-ds", action="store_true", help="Generate a complete design system recommendation")
    parser.add_argument("--project-name", "-p", type=str, default=None, help="Project name for the design system")
    parser.add_argument("--format", "-f", choices=["ascii", "markdown"], default="ascii", help="Output format for the design system")
    # Persistence (Master + Overrides pattern)
    parser.add_argument("--persist", action="store_true", help="Save to design-system/<slug>/MASTER.md")
    parser.add_argument("--page", type=str, default=None, help="Also create design-system/<slug>/pages/<page>.md")
    parser.add_argument("--output-dir", "-o", type=str, default=None, help="Root directory for persisted files (default: current directory)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing persisted files")

    args = parser.parse_args()

    if not args.query.strip():
        parser.error("query must not be empty")
    if args.max_results < 1:
        parser.error("--max-results must be >= 1")
    if args.persist and not args.design_system:
        parser.error("--persist requires --design-system")
    if (args.page or args.force or args.output_dir) and not args.persist:
        parser.error("--page, --force and --output-dir require --persist")
    if args.design_system and (args.stack or args.domain):
        parser.error("--design-system cannot be combined with --stack or --domain")

    if args.design_system:
        try:
            text, files = generate_design_system_with_files(
                args.query,
                args.project_name,
                args.format,
                persist=args.persist,
                page=args.page,
                output_dir=args.output_dir,
                force=args.force,
            )
        except OSError as exc:
            print(f"Error: cannot write design-system files: {exc}", file=sys.stderr)
            return 2
        print(text)
        if files:
            print("\n" + "=" * 60)
            print(f"Design system directory: {files['design_system_dir']}")
            for path in files["created_files"]:
                print(f"  written: {path}")
            for path in files["skipped_files"]:
                print(f"  kept (exists, use --force to regenerate): {path}")
            print("Usage: read MASTER.md, then pages/<page>.md if it exists (page rules override Master).")
            print("=" * 60)
        return 0

    if args.stack:
        result = search_stack(args.query, args.stack, args.max_results)
    else:
        result = search(args.query, args.domain, args.max_results)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_output(result))
    return 1 if "error" in result else 0


if __name__ == "__main__":
    sys.exit(main())
