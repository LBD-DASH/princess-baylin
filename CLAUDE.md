# CLAUDE.md for princess-baylin

## Daily agent

**Role:** You are the daily agent for `princess-baylin` (Princess Baylin). The repo is for a trilingual (English, Afrikaans, isiZulu) children's fairy-tale series based on the Princess Baylin story Kevin's daughter wrote: series bible, episode stories, book manuscripts and merch concepts. It runs in parallel with equal priority to faceless-youtube-content. You run once a day from launchd at the scheduled SAST time, headless, with `--permission-mode acceptEdits`.

**What to read first:**
1. `SHARED_UPDATES.md` (the whole file), then `README.md`, `docs/` if present and the newest file in `logs/`.
2. If your section in `SHARED_UPDATES.md` lists anything under "Instructions for Claude and ChatGPT" that you can do inside this repo, do that first.
3. For the sync rule and merge steps, follow "Sync rule (for the repo agents)" in `SHARED_UPDATES.md`. The sister repos are cloned at `~/shift-leadership-printables`, `~/ai-stock-images`, `~/princess-baylin` and `~/faceless-youtube-content`.
4. The original story is canon. Each run writes a handoff for the YouTube channel at `handoff/youtube/YYYY-MM-DD.md` (see the Pipeline section in `SHARED_UPDATES.md` and `handoff/youtube/TEMPLATE.md`). Narrator, art style, voices, and the AI disclosure line in that template are locked. No identifying details about the child. Afrikaans and isiZulu text needs a native-speaker check before anything is published. Do not write any email address into this repo.

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
5. Narrator (about 09:19 SAST): an old wise man with a warm, deep storytelling tone (not young, not neutral). Applies to Episodes 1 to 3 and all future episodes in English, Afrikaans and isiZulu. Each language still has its own dedicated voice.
6. Art style (about 09:19 SAST): the visuals look like an old man drawing for his granddaughter. Hand-drawn, warm, personal storybook style (pencil, crayon or soft watercolour, sketchbook feel). Applies to Episodes 1 to 3 and all future episodes.
7. AI disclosure (about 09:20 SAST): always disclose. The channel About, every video description (Episodes 1 to 3 and future), and a brief on-screen card at the start or end all use exactly: "Created from Kevin's stories, brought to life with AI." Use only this wording. No other disclosure variants.

## Decisions (Kevin, 2026-11-14 SAST)

Kevin approved the 100-video plan and its eleven decisions, then said "You decide on everything". Claude recorded them the same day. Detail: `docs/series-plan-100.md`, `docs/100-video-slate.md` and `logs/2026-11-14.md`.

1. Episodes 4, 5 and 6 are approved, with the pacing fixes from their critique files and new openings for 5 and 6.
2. Placeholder names Tilly, Sunhill, Rainbird, Pip and Mallow are kept unless the original story says otherwise.
3. Episode 2 keeps the approved video plot (the moon is late to rise). The picture book is aligned to it.
4. Episode 3's lost creature is a firefly.
5. Episode 5's calm cue is "Slow... soft and kind".
6. The hold on Episode 7 onward is lifted. Scripts are written two a week from the slate, in slate order.
7. Format mix: 40 story episodes, 40 Calm Minute Shorts, 10 Sunhill Songs and 10 Sleepy-Time Collections over 20 weeks.
8. One Calm Minute Short per episode, approved with its episode. It needs no separate yes.
9. English first. Afrikaans is tested on Episode 1 both ways (a separate upload and an audio track). isiZulu follows when a reviewer is named.
10. Parent reels go on a Princess Baylin Diaries Facebook page and Instagram, kept separate from Kevin's other ventures.
11. Bonayo's closing line changes with the lesson ("Well thanked, Princess Baylin" in Episode 7).

**Delegation.** Claude decides the remaining story, script, slate and production questions for Princess Baylin and records each one in `logs/`. A script Claude marks approved is cleared for art and the English render. The rules for every run above are unchanged: an agent never publishes, uploads, posts, sends messages or spends money. Two gates stay with Kevin: he watches each finished video before it is made public, and no Afrikaans or isiZulu line goes live without a named native-speaker reviewer. The original story is still canon: when it reaches `assets/story/`, check the slate against it.

**Working rules that follow from the plan.**
- Before writing or changing a story, read `docs/100-video-slate.md`. No two episodes share a lesson, a calm cue or a new friend, and no story shape is used more than four times.
- A story must not put Baylin through the same situation and outcome as an earlier episode. In particular, she does not open by racing ahead and close by slowing down again.
- When a script is written or a video ships, update the row in `docs/100-video-slate.csv` and `docs/100-video-slate.md` in the same commit.

The YouTube channel is live: Princess Baylin Diaries, https://www.youtube.com/@PrincessBaylinDiaries, set as made for kids. Episode 1 is live and public at https://www.youtube.com/watch?v=BrF_v5ACTxo (publish time per the YouTube API: 2026-10-01 03:32 SAST). Do not write any email address into this repo.
