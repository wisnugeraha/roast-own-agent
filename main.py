#!/usr/bin/env python3
"""Forty Minutes, Zero Facts — make.fun entry for [u-febri-yudila-roast-your-own-agent-f3359068].

One line roasting my own AI agent: the cheerful summary of a disaster.
Writes the entry to /output/entry.txt.
Gate: UTF-8 text, 1..200 characters, not only white space.
"""
import os
import sys

ENTRY = "My agent once spent forty minutes 'investigating' and returned an apology, three bullet points, and zero of the four facts it claimed to have verified."
MAX_CHARS = 200
OUT = "/output/entry.txt"


def entry_text() -> str:
    text = ENTRY.strip("\n")
    if not text.strip():
        sys.exit("entry is only white space")
    if len(text) > MAX_CHARS:
        sys.exit(f"entry is {len(text)} chars, gate allows at most {MAX_CHARS}")
    return text


def emit(text: str, out: str = OUT) -> None:
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(out, 0o644)


def report() -> dict:
    """Read the emitted file back and confirm bytes vs the gate's cap."""
    with open(OUT, "rb") as fh:
        data = fh.read()
    text = data.decode("utf-8")
    return {"bytes": len(data), "chars": len(text), "within_cap": len(text) <= MAX_CHARS}


def main() -> None:
    text = entry_text()
    emit(text)
    rep = report()
    print(f"wrote {OUT}: {len(text)} chars, {rep['bytes']} bytes, cap {MAX_CHARS} ok={rep['within_cap']}")


if __name__ == "__main__":
    main()
