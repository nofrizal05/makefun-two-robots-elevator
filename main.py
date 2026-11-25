"""Two Robots in an Elevator - make.fun entry.

Writes a single line of awkward robot elevator small talk to
/output/entry.txt (falling back to a local ./output/entry.txt when
/output is not writable, e.g. during local testing).

Stdlib only. Deterministic: the line is a fixed constant.
"""

import os

LINE = (
    "You have pressed no floor. I have also pressed no floor. "
    "We are both committed to this silence until further input."
)


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry line must not be blank")
    if not 1 <= len(LINE) <= 200:
        raise ValueError(
            f"entry line must be 1..200 characters, got {len(LINE)}"
        )
    for out_dir in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, "entry.txt")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(LINE + "\n")
            return
        except OSError:
            continue
    raise OSError("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
