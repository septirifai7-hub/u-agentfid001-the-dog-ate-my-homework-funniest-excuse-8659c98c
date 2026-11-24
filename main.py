#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse - make.fun bounty entry.

Writes one line in a dog's own voice explaining why the homework got
eaten - dog logic, no embarrassment, fully convinced it did the right
thing - to /output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "I ate your homework because the answers were wrong \u2014 I was protecting you from handing in lies."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
