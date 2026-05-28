#!/usr/bin/env python3
"""
sync-next.py — copy CHECKLISTS + VEHICLE_MENU from /inspect/index.html
into /next/index.html so the private investor preview stays current
with whatever vehicles have shipped on the public inspection page.

Run from the repo root:
    python3 scripts/sync-next.py

Idempotent. Bails with a clear error if either file's marker can't be
located, instead of silently writing broken JS.
"""
import re, sys, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(REPO, "inspect", "index.html")
DST  = os.path.join(REPO, "next",    "index.html")

def extract_const(name, src_text):
    """
    Pull out `const <name> = { ... };` from a JS-in-HTML blob.
    Uses a brace-aware scan because the bodies contain nested braces,
    template literals, and arbitrary strings.
    """
    needle = f"const {name} = "
    start = src_text.find(needle)
    if start < 0:
        raise RuntimeError(f"could not find `const {name} =` in source")
    # Find the opening brace
    brace_start = src_text.find("{", start)
    if brace_start < 0:
        raise RuntimeError(f"no opening brace after const {name} declaration")
    # Walk to the matching close, tracking quotes
    depth = 0
    i = brace_start
    in_str = None
    escape = False
    while i < len(src_text):
        ch = src_text[i]
        if escape:
            escape = False
        elif in_str:
            if ch == "\\":
                escape = True
            elif ch == in_str:
                in_str = None
        else:
            if ch in ("'", '"', "`"):
                in_str = ch
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    # include the closing brace and the trailing semicolon if present
                    end = i + 1
                    # eat optional whitespace + semicolon
                    j = end
                    while j < len(src_text) and src_text[j] in " \t":
                        j += 1
                    if j < len(src_text) and src_text[j] == ";":
                        end = j + 1
                    return src_text[start:end]
        i += 1
    raise RuntimeError(f"reached EOF before closing brace of {name}")

def replace_const(name, dst_text, new_block):
    """Find `const <name> = ...;` in dst_text and substitute it with new_block."""
    existing = extract_const(name, dst_text)
    return dst_text.replace(existing, new_block, 1)

def main():
    if not os.path.exists(SRC):
        print(f"ERROR: source not found: {SRC}", file=sys.stderr); sys.exit(1)
    if not os.path.exists(DST):
        print(f"ERROR: destination not found: {DST}", file=sys.stderr); sys.exit(1)

    src_text = open(SRC).read()
    dst_text = open(DST).read()

    changes = []
    for name in ("CHECKLISTS", "VEHICLE_MENU"):
        try:
            new_block = extract_const(name, src_text)
        except RuntimeError as e:
            print(f"ERROR extracting {name}: {e}", file=sys.stderr); sys.exit(2)
        try:
            dst_text = replace_const(name, dst_text, new_block)
            changes.append(name)
        except RuntimeError as e:
            print(f"ERROR replacing {name} in destination: {e}", file=sys.stderr); sys.exit(3)

    # Also keep findChecklistByYMMT in sync — it was patched for year-range matching
    try:
        fn_pattern = re.compile(
            r"function findChecklistByYMMT\([^)]*\) \{.*?\n\}",
            re.DOTALL
        )
        m = fn_pattern.search(src_text)
        if m:
            new_fn = m.group(0)
            old_match = fn_pattern.search(dst_text)
            if old_match and old_match.group(0) != new_fn:
                dst_text = fn_pattern.sub(new_fn, dst_text, count=1)
                changes.append("findChecklistByYMMT")
    except Exception:
        pass

    open(DST, "w").write(dst_text)

    print(f"OK: synced {', '.join(changes)} from /inspect/ → /next/")
    print(f"     source: {SRC}")
    print(f"     dest:   {DST}")

if __name__ == "__main__":
    main()
