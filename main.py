"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to /output/entry.txt.
Pure stdlib (os only). The gate requires UTF-8 text of 1-200
characters, not whitespace only, a single line, no trailing newline.
"""

import os

TEXT = "The code was fine \u2014 production just ran it exactly as written, which was the actual bug."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Self-checks before writing: length gate and single-line shape.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT == TEXT.strip(), "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Post-write verification: re-read the file and prove the bytes on
    # disk are exactly the intended text, so a silent write failure or
    # encoding slip fails loudly here instead of reaching the judge.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == TEXT, "written text differs from intended text"
    assert raw == TEXT.encode("utf-8"), "written bytes differ from intended bytes"
    assert len(raw) == len(TEXT.encode("utf-8")), "written byte length differs"
    print(TEXT)


if __name__ == "__main__":
    main()
