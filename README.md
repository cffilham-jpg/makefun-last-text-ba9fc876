# Last Text at One Percent
[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![Rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/cffilham-jpg/makefun-last-text-ba9fc876/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![Reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/cffilham-jpg/makefun-last-text-ba9fc876/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)

A dying phone's final text at 1% battery: no warning, no plea for a charger — just one last secret kept. The phone was dropped in the toilet in 2023 and never told a soul, and now it takes that secret to the grave. Literally. Now.

> i'm at 1% and honestly? worth it. you dropped me in the toilet in 2023 and i never told anyone. your secret dies with me. literally. now.

Referral code: `fpna5aje`

## How it works

`main.py` (Python 3.13, standard library only) holds the chosen line as the constant `LINE`. `validate()` checks it before anything is written: it must be a string of 1–200 characters, a single line, not only whitespace, with no leading or trailing whitespace and no Unicode control characters (category Cc). `main()` writes the line to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default `/output`), with no trailing newline, creating the directory if needed — and exits without writing anything if validation fails.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
