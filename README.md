# Princess Baylin: Trilingual Fairy-Tale YouTube Series (English, Afrikaans, isiZulu)
> **Start here:** read [SHARED_UPDATES.md](SHARED_UPDATES.md) for the status of all four sister projects, and write your update back into it.

_Repo: `princess-baylin`. Side venture, separate from YardOps, 6HN and LBD. Background research: `blackvault/new-income-ideas-2026-09-27.md` (27 Sep 2026)._

## The idea
A children's fairy-tale YouTube series based on **'Princess Baylin', a story written by Kevin's daughter**. Princess Baylin is the hero of a consistent world with a recurring supporting cast. Each story becomes an illustrated, narrated episode, produced in **three languages: English, Afrikaans and isiZulu**, for South African children and families (ages 4–8). Later the stories can become picture books. The priority is high-effort, original storytelling that stays true to her original story: real plots, character growth, a recurring world, and hand-directed art and narration. We don't mass-produce templated AI videos.

The original story is the canon. Keep a copy in `assets/story/` (Kevin to add it) and build the series bible from it.

## Target platform
YouTube, with long-form episodes (8+ minutes so mid-roll ads can run, if monetised) and Shorts only as trailers. Language format to decide in week 1: separate uploads per language (possibly separate playlists or channels), or one video with multi-language audio tracks if that feature is available to the channel (check). Later: trilingual picture books (with AI disclosure where required) and colouring pages (can share the Etsy shop from `shift-leadership-printables`).

## How money is made
- YouTube Partner Program ad revenue. Kids content has a low RPM (about $0.30–4), and SA audiences earn a fraction of that. Afrikaans and isiZulu audiences are smaller but far less served, which is the opportunity.
- Monetisation thresholds need checking: research notes (27 Sep 2026, not yet verified) say the ad tier is 1,000 subscribers + 4,000 watch hours today, rising to **1,000 subscribers + 8,000 watch hours for new applicants from 1 Feb 2027**. Verify on YouTube's official help pages and plan for the higher bar.
- Later income: book sales, colouring and activity printables, and licensing. Realistic estimate: R0 for the first 6+ months. This is a long bet on building a family IP.

## First 30 days
- **Days 1–5:** Write the series bible from the original story: Baylin's personality, goals and flaws, the kingdom and map, recurring cast, tone, age range (4–8), the values each story teaches, a trilingual name and glossary list (character names, places, catchphrases in English, Afrikaans and isiZulu), and the visual style guide (palette, character sheets). Decide the language format. **[KEVIN and his daughter approve.]**
- **Days 6–12:** Write the first 4 original story scripts in all three languages (1,200–1,800 words each in English, about 8–12 minutes narrated). Each needs a distinct plot and outcome. Line up native-speaker reviewers for Afrikaans and isiZulu. **[KEVIN]**
- **Days 13–22:** Produce episode 1 end to end in all three languages: illustrations to a consistent character design, narration (native-speaker voices or Kevin's family where possible), gentle music, edit, thumbnails and a Short trailer per language. Native-speaker check, then Kevin reviews as the quality gate.
- **Days 23–30:** Publish episode 1 (three language versions) and episode 2 if ready, set the channel as 'made for kids' with correct AI-disclosure labels, and draft episodes 3–4. Log views, retention and subscribers per language.

## Success and kill criteria
**Success (keep going and scale):**
- Day 30: series bible done, episode 1 published in all three languages after native-speaker review, and average view duration of 40% or more on at least one version.
- Month 3: 6+ episodes (all three languages), 100+ subscribers, retention holding up. Month 6: on course for the watch-hours threshold within 12 months.

**Kill (stop or change direction):**
- Any 'inauthentic content' or reused-content warning from YouTube: stop, review the format with Kevin, and appeal if it's wrong.
- After 12 episodes: under 50 subscribers or average view duration under 25%. Rethink the format (for example drop to the best-performing languages), or focus on books and printables.
- If no native-speaker reviewer can be found for a language, don't publish that language version until one is.

## What only Kevin can do
- Own the Google/YouTube account with 2FA, AdSense (ID and address), and tax info (W-8BEN).
- Add his daughter's original story to `assets/story/`, and approve the series bible with her.
- Find and brief native-speaker reviewers (and ideally narrators) for Afrikaans and isiZulu.
- Review each episode before it's published (the quality gate YouTube expects). Optionally record English narration himself.

## Risks and policy rules
- **Native-speaker check:** isiZulu and Afrikaans scripts, titles and on-screen text must be checked by a native speaker before publishing. Machine translation of children's content can be wrong or culturally off.
- **YouTube AI-content and 'inauthentic content' policy (2026) needs checking.** Research notes describe a 16 July 2026 update that won't monetise generic, repetitive or template-based content, including templated storylines and mass-produced AI content, reviewed across the whole channel. Every episode must be a genuinely original story with its own plot, visuals and editorial care. Three language versions of one episode should be real adaptations, and disclosed as versions of the same story.
- Kids content must be set as 'made for kids' (COPPA): no personalised ads, no comments, lower RPM. Disclose realistic AI content where YouTube requires it.
- Family privacy: don't show Kevin's daughter's face, full name, school or location in videos or metadata. Credit her only as Kevin decides.
- Don't use copyrighted fairy-tale IP or recognisable branded characters.

## Repo layout
- `README.md`: this plan
- `assets/`: source files and exports (keep large binaries out of git where you can)
- `prompts/`: plain-markdown prompts that work pasted into Claude, ChatGPT or any other assistant
  - `daily-progress-check.md` and `daily-next-content.md` run every day
  - `weekly-metrics-review.md` is run by hand once a week
- `from-cto-new/`: material carried over from cto.new (the prompt runner includes any text files here as context)
- `scripts/run_prompts.py`: runs prompts through OpenAI or Anthropic and appends the output to `logs/YYYY-MM-DD.md`
- `logs/`: one file per day (`YYYY-MM-DD.md`). Agents append output; Kevin pastes real metrics in by hand.
- `.github/workflows/daily-prompts.yml`: runs the two daily prompts at 04:17 UTC (06:17 SAST) every day, or by hand from the Actions tab

## Automation
The daily workflow only calls an LLM if a repo secret `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` exists. Without one it prints `skipped: no API key` and finishes cleanly without committing anything. To switch it on, add one of the secrets under Settings → Secrets and variables → Actions. Optional repo variables: `OPENAI_MODEL` or `ANTHROPIC_MODEL` to pick the model, and `LLM_PROVIDER=anthropic` to prefer Anthropic when both keys are set.

Run locally: `python scripts/run_prompts.py` (daily prompts), `python scripts/run_prompts.py weekly-metrics-review`, or `python scripts/run_prompts.py --all`.

The prompts can only reason over the README, logs and `from-cto-new/`. They can't see platform dashboards, so paste real numbers into the day's log, or the reviews will say "unknown".
