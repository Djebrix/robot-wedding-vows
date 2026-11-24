"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt when set).

Stdlib only, no network, fully deterministic: the vow is a fixed
string, so every run writes byte-identical output.
"""

import os

VOW = (
    "I promise to love you through every firmware update, "
    "even the one that changes your laugh and forgets my name."
)


def main() -> None:
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
