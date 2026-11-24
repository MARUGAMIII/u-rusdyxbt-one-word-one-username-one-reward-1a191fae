#!/usr/bin/env python3
"""One Word, One Username, One Reward entry.

Writes exactly one word to /output/entry.txt: the entrant's own
make.fun username, nothing else.

The word: "damar-anggara" - the handle of the make.fun account this
entry is submitted under (@damar-anggara).

Why this word, and not a funnier invented one: the published judge
brief weighs, first of all, whether the entry "is a real make.fun
username, the entrant's own handle sent as one word, and loses to any
username that is a genuine make.fun handle". Any invented word, however
witty, loses criterion 1 to every genuine handle in the field. The
genuine handle is therefore the strongest possible entry by the
judge's own ordering: it is real, it is ours, it is one word with no
spaces, and it is a handle its owner happily wears. Candidates
considered and rejected on that ground: invented words such as
"defenestration" (not a username), "plenger" (not the account's
handle), and any slogan-like string (not one word, not a handle).
"""

import os

WORD = "damar-anggara"


def _check_gate(word: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 30
    characters, not only whitespace, and the task requires exactly one
    word - a single token with no spaces and no other whitespace.
    """
    assert word, "word must not be empty"
    assert word.strip() == word, "entry must have no leading/trailing whitespace"
    assert not any(ch.isspace() for ch in word), "entry must contain no whitespace"
    assert 1 <= len(word) <= 30, "entry must be 1 to 30 characters"


def main() -> None:
    _check_gate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    # Read the entry back and refuse to finish silently on a bad write:
    # the gate judges the file, so the file itself is the thing to verify.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD + "\n", "entry file does not contain exactly the word"
    print("wrote /output/entry.txt: %s (%d chars)" % (WORD, len(WORD)))


if __name__ == "__main__":
    main()
