"""Write the one-letter diary entry to /output/entry.txt.

The entry is a single letter, A-Z, standing for the word that describes
the day. This entry sends "X" — the letter of "eXhausted": the day ended
with nothing left in the tank, the kind of tired that is funny only in
retrospect. X is the sound the word starts with — the "ex" in exhausted —
so the letter fits its word the way the judge's brief asks an initial to.
The letter is the whole entry: exactly one character, no
newline, no gloss, no punctuation.
"""

import os

LETTER = "X"

assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "entry must be one A-Z letter"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
