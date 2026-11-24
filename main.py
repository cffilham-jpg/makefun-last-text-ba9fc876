"""Last Text at One Percent.

Writes the phone's final text message to entry.txt inside
MAKEFUN_OUTPUT_DIR (default /output). Standard library only.
"""

import os
import sys
import unicodedata

LINE = "i'm at 1% and honestly? worth it. you dropped me in the toilet in 2023 and i never told anyone. your secret dies with me. literally. now."


def validate(text):
    """Return True only if text is a valid entry line.

    Valid means: a string, 1-200 characters, a single line, not only
    whitespace, and containing no Unicode control characters
    (category Cc).
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if text.strip() == "":
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(unicodedata.category(ch) == "Cc" for ch in text):
        return False
    return True


def main():
    if not validate(LINE):
        print("invalid entry line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
