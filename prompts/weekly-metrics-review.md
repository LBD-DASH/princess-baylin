# Weekly metrics review: Princess Baylin: Trilingual Fairy-Tale YouTube Series (English, Afrikaans, isiZulu)

_Run once a week (Mondays suggested). It isn't part of the daily schedule: paste it into a chat assistant, or run `python scripts/run_prompts.py weekly-metrics-review`._

## Inputs
Use the repo's `README.md` (the plan, money model, 30-day plan and success/kill criteria), the most recent files in `logs/` (newest first) and anything in `from-cto-new/`. If you're pasting this prompt into a chat assistant, paste or attach those files below it. If no logs are supplied, treat today as Day 1 of the 30-day plan.

## Language rule (applies to everything below)
- Every script, story and content item you write must be given in **all three languages: English, Afrikaans and isiZulu**, as three clearly labelled versions (`### English`, `### Afrikaans`, `### isiZulu`). This includes titles, descriptions, on-screen text, songs and Short scripts. Don't give English only, and don't say "translate later".
- Adapt rather than translate word for word: use natural phrasing, names, rhymes and humour that work for young children in each language.
- Keep all three versions culturally appropriate for children aged 4–8: gentle and age-appropriate, no stereotypes, no frightening or violent content, and respectful portrayal of South African cultures, languages, traditions and families.

## Task
1. Pull these metrics from the logs for the last 7 days and the 7 days before that: episodes published per language, scripts drafted per language, native-speaker checks done, views, watch hours (cumulative and last 12 months), average view duration %, subscribers, Shorts views, click-through rate, production hours per episode, any policy notices.
2. Show them as a small table with week-on-week change. Write "unknown" where a number is missing.
3. Break views, retention and subscribers down by language (English, Afrikaans, isiZulu). Flag any content published without all three versions or without a native-speaker check, and any sign that a language version isn't landing culturally.
4. Say what worked, what didn't, and one experiment for next week.
5. Measure progress against the success/kill criteria in the README. Recommend **continue**, **adjust** or **kill**, with a one-line reason.
6. List the metrics Kevin should paste into next week's logs so the next review has real numbers.

## Output
Reply with a single markdown section that starts with the heading `## Weekly metrics review`. It gets appended to `logs/YYYY-MM-DD.md` (today's date), either by the daily workflow or by Kevin pasting it in.

Rules:
- Don't make up numbers. If a metric isn't in the logs, write "unknown" and say who needs to supply it.
- Keep it short and specific. Kevin should be able to act on it in under 5 minutes.
- Mark anything that needs Kevin personally (accounts, KYC, payments, approvals, reviews) with **[KEVIN]**.
- End with this flag, every time: **[KEVIN] Native-speaker check needed: the isiZulu and Afrikaans versions must be reviewed by a native speaker before anything is published.**
