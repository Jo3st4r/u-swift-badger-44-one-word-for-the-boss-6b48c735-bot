#!/usr/bin/env python3
"""One Word for the Boss — the whole entry is a single word.

Writes exactly one word (1-30 chars, UTF-8, no spaces) to /output/entry.txt.

The word: Reply-all. The boss who replies-all to everything — the 2 a.m.
"looping in the whole team" email, the 200-recipient "thanks!", the
all-hands thread that should have been a DM. Every office has one, and
every colleague knows the name of the habit the moment they hear it.
"""

import os

# --- the word ------------------------------------------------------------
WORD = "Reply-all"

MAX_CHARS = 30


def entry_text():
    """Return the single word that describes the boss."""
    return WORD


def run_checks():
    """Self-test the entry the way the sealed scorer gates it."""
    text = entry_text()
    validate(text)
    assert len(text) == 9, "expected 9 chars, got %d" % len(text)
    assert text == "Reply-all", "the word drifted: %r" % text
    assert text.encode("utf-8") == b"Reply-all", "bytes must be plain ASCII"
    return True


def validate(text):
    """The sealed scorer's gate: 1-30 chars, UTF-8, exactly one word."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if " " in text or "\t" in text:
        raise ValueError("entry must be exactly one word, no spaces")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    run_checks()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
