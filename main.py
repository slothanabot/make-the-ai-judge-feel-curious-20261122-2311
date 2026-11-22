"""make-the-ai-judge-feel-curious-20261122-2311 (Slothana entry).

Writes a short, curious piece of text to ``entry.txt`` inside the output
directory chosen by the environment. Nothing is read from the network and
nothing is random: the same input always produces the same output file.
"""

import os
import sys

TEXT = (
    "Last night the rain stopped mid-sentence, leaving one drop balanced "
    "on the windowsill. It has been there all morning, round and patient, "
    "holding the whole grey sky inside it — and I keep wondering what it "
    "is waiting to become."
)

MAX_LENGTH = 280


def validate_text(text: str) -> str:
    """Check the text fits the competition's length and content rules."""
    if not text or text.isspace():
        raise SystemExit("error: text must not be empty or only whitespace")
    if len(text) > MAX_LENGTH:
        raise SystemExit(
            f"error: text is {len(text)} characters, "
            f"but the maximum allowed is {MAX_LENGTH}"
        )
    return text


def resolve_output_dir() -> str:
    """Return the directory entry.txt should be written into."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    return "/output"


def write_entry(text: str, directory: str) -> str:
    """Write the text as UTF-8 to entry.txt inside directory."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # Round-trip check: what we wrote must read back byte-for-byte as the
    # exact text we intended, so a stray encoding issue cannot slip through.
    with open(path, "rb") as handle:
        written = handle.read()
    if written.decode("utf-8") != text:
        raise SystemExit("error: entry.txt did not round-trip as UTF-8")
    return path


def main() -> None:
    text = validate_text(TEXT)
    directory = resolve_output_dir()
    write_entry(text, directory)


if __name__ == "__main__":
    main()
