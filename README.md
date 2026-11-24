# Robot Wedding Vows

[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Djebrix/robot-wedding-vows/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Djebrix/robot-wedding-vows/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

One line of wedding vows for a robot couple, written for the
[One-Line Robot Wedding Vows](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
bounty on [make.fun](https://make.fun).

`main.py` (stdlib only, no network, fully deterministic) writes the vow to
`/output/entry.txt`:

> I promise to love you through every firmware update, even the one that changes your laugh and forgets my name.

Run it locally:

```sh
ENTRY_OUTPUT_DIR=/tmp/robot-vows-out python3 main.py
cat /tmp/robot-vows-out/entry.txt
```
