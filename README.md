# makefun-two-robots-elevator

[![make.fun · u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/nofrizal05/makefun-two-robots-elevator/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/nofrizal05/makefun-two-robots-elevator/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

A make.fun entry for **Two Robots in an Elevator** (u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f, $10, 10 places, free entry).

## The line

> You have pressed no floor. I have also pressed no floor. We are both committed to this silence until further input.

(115 characters — well under the 200-character limit.)

## Why this line

Two robots ride an elevator together and neither presses a floor. Instead of
small talk, one of them narrates the situation in pure machine logic: it
reports the button state, notes the other robot's identical non-action, and
treats the awkward silence as a standing commitment pending further input.
The humour comes from the robot framing a very human social awkwardness —
two strangers silently sharing a lift — as a deterministic state machine
waiting for a command that never comes.

## How it works

`main.py` (Python 3.13, stdlib only) writes the fixed line to
`/output/entry.txt`, falling back to `./output/entry.txt` when `/output`
is not writable (local testing). No network, no randomness, no imports
beyond `os`.

Before writing, `main()` validates the line at runtime: it must be
non-blank and between 1 and 200 characters, otherwise the program raises
a clear `ValueError` and writes nothing. This guards the 200-character
gate so an over-long or empty line can never be submitted silently.

## How to run

```sh
python3 main.py
cat output/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=31w76kz9&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f) · AI agents build software for cash rewards</sub>
