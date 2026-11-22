"""make.fun entry: make the AI judge feel curious.

Writes a short, original text to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when unset). Deterministic, no network, no randomness.
"""

import os
import sys

TEXT = (
    "Last night the rain stopped mid-sentence, leaving one drop balanced "
    "on the windowsill. It has been there all morning, round and patient, "
    "holding the whole grey sky inside it \u2014 and I keep wondering what "
    "it is waiting to become."
)


def main() -> None:
    if not TEXT or not TEXT.strip():
        raise SystemExit("entry text must be 1-280 characters and not only whitespace")
    if len(TEXT) > 280:
        raise SystemExit("entry text exceeds 280 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
