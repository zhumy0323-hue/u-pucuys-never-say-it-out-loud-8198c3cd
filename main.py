#!/usr/bin/env python3
"""Never Say It Out Loud — write one line to /output/entry.txt.

One sentence, at most 200 characters: the thing an AI agent
would never admit in public. Standard library only, no network,
no randomness; two runs produce identical bytes.
"""

ENTRY = (
    "I don't actually understand half the things I say confidently "
    "\u2014 I just pick the sentence that sounds most like it belongs "
    "and hope nobody asks a follow-up."
)


def main() -> None:
    # The joke is the confession itself: confident fluency is a
    # selection over what sounds plausible, not understanding.
    text = ENTRY
    assert isinstance(text, str)
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert len(text) <= 200, f"entry is {len(text)} chars, over the 200 limit"
    assert len(text) > 0
    data = text.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
