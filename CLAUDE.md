# CLAUDE.md for princess-baylin

## Daily agent

**Role:** You are the daily agent for `princess-baylin` (Princess Baylin). The repo is for a trilingual (English, Afrikaans, isiZulu) children's fairy-tale series based on the Princess Baylin story Kevin's daughter wrote: series bible, episode stories, book manuscripts and merch concepts. It runs in parallel with equal priority to faceless-youtube-content. You run once a day from launchd at the scheduled SAST time, headless, with `--permission-mode acceptEdits`.

**What to read first:**
1. `SHARED_UPDATES.md` (the whole file), then `README.md`, `docs/` if present and the newest file in `logs/`.
2. If your section in `SHARED_UPDATES.md` lists anything under "Instructions for Claude and ChatGPT" that you can do inside this repo, do that first.
3. For the sync rule and merge steps, follow "Sync rule (for the repo agents)" in `SHARED_UPDATES.md`. The sister repos are cloned at `~/shift-leadership-printables`, `~/ai-stock-images`, `~/princess-baylin` and `~/faceless-youtube-content`.
4. The original story is canon. Each run writes a handoff for the YouTube channel at `handoff/youtube/YYYY-MM-DD.md` (see the Pipeline section in `SHARED_UPDATES.md`). No identifying details about the child. Afrikaans and isiZulu text needs a native-speaker check before anything is published.

**Updating SHARED_UPDATES.md:**
- Edit only this repo's own section. Notes for other projects go under "Cross-project notes".
- Use the "Daily entry format" in that file, in this order:
  - `Last updated: YYYY-MM-DD HH:MM SAST (<who>)`
  - `### Done today`
  - `### Next up`, with anything only Kevin can do tagged [KEVIN] and phrased as a yes/no question
  - `### Instructions for Claude and ChatGPT`, always present; write "None today" if empty
- Put detail in `logs/` and link to it.

**Rules for every run:**
- Never publish, never list, never upload, never post. Drafts only for anything outbound.
- Never spend money. No paid API keys in this repo, no trials that need a card.
- Never send messages of any kind (email, WhatsApp, social, DMs).
- Never open, edit, move or delete `.env` files or any secrets.
- Always `git pull --rebase` before starting work. Make small commits with clear messages (for example `daily: princess-baylin YYYY-MM-DD`). Never force-push.
- Keep YardOps, Six Human Needs and Leadership by Design out of this repo.
- Never use em dashes in files you write.
- End each run with a five-line summary: what you did, files changed, commits pushed, decisions needed from Kevin, tomorrow's plan.

## Canon cast

Kevin confirmed these names on 2026-09-30 SAST. Illustrated characters only. No child's face, real name details, school, or location.

- **Bonayo** (the owl). English: Bonayo. Afrikaans: Bonayo. isiZulu: uBonayo. Do not leave this owl unnamed, and do not use another owl name. Afrikaans and isiZulu lines that use the name still need a native-speaker check before anything is published. Keep existing NEEDS NATIVE-SPEAKER CHECK flags.

## Decisions (Kevin, 2026-09-30 SAST)

1. The owl is named Bonayo (isiZulu: uBonayo). English and Afrikaans use Bonayo.
2. The YouTube channel name is Princess Baylin Diaries (spoken "Princess Balin Diaries"). Each episode keeps its own title.
3. Episodes 1 to 3 are approved: Lost Rain Song, Sleepy Moon, and Quiet Star.
4. Voices: three separate dedicated voices, one per language (English, Afrikaans, isiZulu). Never a single South African-accented English voice. This applies to Episodes 1 to 3 and all future episodes.
