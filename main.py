"""Funniest Lost Sock Status Update — make.fun entry.

Writes exactly one original status update, in the voice of a lost sock
that ended up somewhere it should not be, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt). Pure
standard library, deterministic: the same bytes on every run. Never
deletes or recreates the output directory, and writes nothing
anywhere else.
"""

import os

STATUS = (
    "Somehow I'm in the freezer now. The peas won't stop staring. "
    "I was made for a foot, not a shelf next to the ice cream."
)


def main() -> None:
    assert len(STATUS) <= 120, "status update must fit 120 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STATUS + "\n")


if __name__ == "__main__":
    main()
