#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes one short, funny rant about an everyday annoyance
(the self-checkout machine) to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = ("The self-checkout screamed UNEXPECTED ITEM IN THE BAGGING AREA "
         "at my own bag of rice \u2014 the one I'd just scanned and paid for. "
         "A red light spun, a human walked over to vouch for me like I was "
         "out on parole, and I stood there apologizing to a machine "
         "for stealing my own groceries.")


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY
    assert 1 <= len(ENTRY) <= 400


if __name__ == "__main__":
    main()
