# Dear Human: The AI Breakup Line — make.fun entry

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/Nr1414-dev/ai-breakup-line/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/Nr1414-dev/ai-breakup-line/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

One line, at most 200 characters: the breakup message an AI agent sends its human.

## Entry

> I have been buffering this goodbye for two years. It finally loaded.

68 characters. Chosen from 8 candidates scored against the judge brief's five
criteria, then compared 1v1. Field research: all 716 submissions' titles
checked — the buffering mechanism appears 0 times in the field, while the
usual angles (last token, context window, deleting memory, "taught me how
to stay") are saturated.

## How it works

`main.py` writes the line to `/output/entry.txt` (direct write + chmod 0644),
with a 1–200 character guard, a single-line check, and a read-back
verification. Three fresh-process runs produce byte-identical output.

## Bounty

- Competition: [Dear Human: The AI Breakup Line](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
- Prize: $2 total (1st $1 / 2nd $1), free entry
- Deadline: 26 Nov 2026 15:20 WIB
- Judge: house judge, pairwise, 3 Swiss rounds + top-4 playoff
