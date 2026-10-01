# KDP readiness: Princess Baylin and the Lost Rain Song (Episode 1)

Status: DRAFT fix list, nothing uploaded to KDP. Written 2026-10-01 SAST.
All prices are **estimates**, checked on the web on 2026-10-01 SAST, converted at **USD/ZAR 16.44** (market quote, 1 Oct 2026) and rounded. Prices change; check the vendor page before paying. No money has been spent.

Applies to the build in this folder: `out/interior-kdp.pdf` (26 pages, 8.5 x 8.5 in trim, bleed), `out/cover-kdp.pdf` (full wrap), from `build.py` at commit 730f0ee.

## Summary of decisions Kevin needs to make

1. **Art resolution:** approve the free upscale (recommended below), or pay for a commercial upscaler. Yes/no on the free route?
2. **Author and copyright name:** "Kevin Britz" personally, a pen name, or a company or imprint? This name goes on the cover, the title page, the credits page and the KDP Author field, and they must match.
3. **ISBN:** free KDP ISBN (publisher shows as "Independently published", only usable on Amazon) or a free South African ISBN from the National Library of South Africa (NLSA), with your own imprint name and legal deposit duties.
4. **KDP AI questions:** KDP asks whether text, images or translations are AI-generated. For this book the honest answer is that the images are AI-generated (Canva) and the text was expanded with AI from Kevin's stories. Kevin answers this in the KDP form himself.

---

## (a) Art resolution (KDP recommends 300 ppi)

### Where the book is today

| Item | Pixels used | Printed width | Effective ppi |
|---|---|---|---|
| Interior pages (full frame) | 1920 px wide | 8.625 in (with bleed) | about **223** |
| Page 6 (1.35x crop of the Rainbird frame) | about 1422 px wide | 8.625 in | about **165** |
| Front cover (frame enlarged to 6.1 in tall, sides cropped) | 1920 px across 10.84 in | | about **177** (not flagged before; it is the lowest after page 6) |
| Back cover | 1920 px wide | 8.625 in | about **223** |

KDP accepts images under 300 ppi but warns, and they print softer. The art has to reach at least 2588 px across the 8.625 in bleed width for 300 ppi.

### Option 1: original source stills (checked first)

- Checked `/workspace/princess-baylin/` on the box: only the video, thumbnail (1280x720), audio and notes are there. The `build/` folder with the original stills (`img2/`) is no longer on the box.
- The production notes say the originals were **1680 x 944** (Canva image generator). That is smaller than the 1920 x 1080 video frames we already use (the video upscaled them). Originals would print at about **195 ppi**, so they alone do **not** fix the problem. They would be a slightly cleaner starting point for an upscale (no video compression), if they can be re-downloaded from Kevin's Canva account.
- Cost: free. Effort: find and download 13 images from Canva. Not done here.

### Option 2: free local upscaler on the box (tested)

**Tested: Real-ESRGAN (ncnn-vulkan build, BSD-3 licence, free), running on the box CPU through the free Mesa "lavapipe" Vulkan driver (no GPU).**

| Model | Scale | Time per 1920x1080 frame on the box | Result |
|---|---|---|---|
| `realesr-animevideov3` | 2x, to 3840 x 2160 | about **50 to 55 s** (tested on 2 frames: `s2_128.75` the page 6 and 7 Rainbird frame, and `s0_21.25` the cover frame) | Clean, crisp pencil lines; removes video compression blocks; slightly smooths the paper grain. Looks like the same drawing, just sharper. **Good for print.** |
| `realesrgan-x4plus` | 4x | about 105 s for a 400 x 300 crop, so roughly 30 min per full frame on CPU | Sharper, but adds crunchy over-sharpened texture in the hair. Too slow and less faithful to the soft style. Not recommended. |
| Lanczos (plain resize, for comparison) | 2x | instant | Soft and blocky. No real gain. |

Effective ppi after the 2x `realesr-animevideov3` upscale:

| Item | Before | After |
|---|---|---|
| Interior pages | 223 | **445** |
| Page 6 crop | 165 | **330** |
| Front cover | 177 | **354** |
| Back cover | 223 | **445** |

Test files on the box (not committed): `/workspace/princess-baylin-book/upscale/` (`s2_128.75_animev3x2.png`, `s0_21.25_animev3x2.png`, side-by-side crops `compare.jpg` and `compare_zoom.jpg`, left to right: Lanczos, animevideov3 2x, x4plus).

Other free option: **Upscayl** (free desktop app for Mac, Windows and Linux, uses the same Real-ESRGAN models) would do the same job faster on a computer with a GPU. waifu2x (free) is an alternative, but Real-ESRGAN already gives good results here, so it was not tested.

Cost: **0 USD / R0**. Box time for all 25 frames: about 22 minutes.

### Option 3: paid upscalers (estimates, 2026-10-01)

| Tool | Plan | Price USD | Price ZAR (16.44) | Notes |
|---|---|---|---|---|
| Topaz Gigapixel Personal | monthly, no commitment | 29 per month | about R477 per month | Desktop app, unlimited local renders; "limited commercial use" for organisations under 1 million USD revenue. Source: topazlabs.com/pricing |
| Topaz Gigapixel Personal | annual | 149 per year | about R2,450 per year | Same as above |
| Topaz Gigapixel Pro | annual | 499 per year | about R8,204 per year | Full commercial use |
| Let's Enhance Starter | monthly | 12 per month (100 images) | about R197 per month | 25 frames fit in one month; cancel after. Source: letsenhance.io/pricing plus 2026 review sites |
| Let's Enhance Starter | annual | 9 per month billed yearly | about R148 per month | |
| Let's Enhance free | 10 credits at signup | 0 | R0 | Output limited to 8 MP and watermarked per 2026 review sites, so not usable for print |

### Recommendation (a)

**Use the free Real-ESRGAN `realesr-animevideov3` 2x upscale on the box (tested, R0).** It takes every page above 300 ppi (lowest is page 6 at about 330 ppi) and keeps the hand-drawn look. Only pay for Topaz (from 29 USD, about R477, for one month) if a printed proof looks wrong.

To apply it (not done yet; the current PDFs are untouched):
1. Upscale the 25 frames in `art/` at 2x with `realesr-animevideov3` (about 22 min on the box).
2. In `build.py`, embed images at about 2600 to 2700 px wide (just over 300 ppi) with JPEG quality 88 so the interior PDF stays well under 50 MB (at full 3840 px it would be about 60 to 70 MB; KDP accepts up to 650 MB, but the repo is easier at under 50 MB).
3. Rebuild, keep the old PDFs as `out/v1/`, then check one page at 100% zoom.

---

## (b) Spine width

- **KDP formula (premium colour, white paper):** spine width = page count x 0.002347 in (0.0596 mm per page). Source: KDP Help "Paperback Submission Guidelines" (topic G201857950), checked 2026-10-01.
- **This book:** 26 pages x 0.002347 in = **0.0610 in (about 1.55 mm)**.
- **Full cover size:** 0.125 + 8.5 + 0.061 + 8.5 + 0.125 = **17.311 in wide x 8.75 in tall** (matches `out/cover-kdp.pdf`).
- **Spine text:** KDP only prints spine text on books with more than 79 pages (Cover Creator needs 80). This book has **no spine text**, which is correct. KDP also allows 0.0625 in of variance either side of each fold, so the cover has no hard lines on the folds.

**Exact verification step (Kevin or an agent, before upload):**
1. Open KDP's cover calculator and template tool (linked from the KDP Help page "Create a Paperback Cover", under "cover calculator" / "cover templates").
2. Enter: Binding **Paperback**, Interior **Premium color**, Paper **White**, Trim **8.5 x 8.5 in**, Page count **26** (must equal the final interior PDF page count), Units **inches**.
3. Download the template ZIP. Check that the template's full width is 17.311 in (spine 0.061 in) and height 8.75 in.
4. Overlay `out/cover-kdp.pdf` on the template PNG (for example in Canva or any image editor at the same size). The barcode box on the template should land in the clear area at the bottom right of the back cover.
5. If the page count changes (for example to 28 or 32), change it in `text.md` and rebuild. `build.py` recalculates the spine automatically from the page count.

---

## (c) Copyright line, author name and ISBN

### What is on the book now

Credits page (page 2): "Text copyright 2026 Kevin Britz. All rights reserved." and "First edition, 2026. ISBN to be assigned." There is no author name on the front cover.

### What KDP requires (checked 2026-10-01)

- KDP does not demand a copyright page, but one is standard and expected.
- The title (and author, if shown) on the cover must match the KDP book details. Decide the author name and add it to the cover and title page for consistency.
- **ISBN:** every paperback needs one. Two routes:
  - **Free KDP ISBN:** KDP registers it with Bowker (US). The publisher field shows "Independently published" and cannot be changed. It can only be used on Amazon KDP. Source: KDP Help "Get an ISBN" (GTJ8LBXL6Z4WV5QX).
  - **Own ISBN:** the imprint name entered in KDP must match the ISBN agency record exactly (spaces and capitals count), or KDP blocks publishing. Source: KDP Help "What is an ISBN and Imprint?" (G201834170).
- **AI disclosure to Amazon:** KDP's publishing form asks whether content is AI-generated (text, images, translations). Answer truthfully; the book already carries "Created from Kevin's stories, brought to life with AI."

### South African ISBN through NLSA (verified 2026-10-01)

- The National Library of South Africa is the official ISBN agency for South Africa and issues ISBNs **free of charge** to South African authors and publishers. Online form at nlsa.ac.za/isbn. Processing takes **5 to 14 working days**. Source: NLSA ISBN page.
- The form asks whether to register the ISBN against **the author or the publisher**, and which platforms (for example Amazon) will be used.
- NLSA's form says that for **print on demand from Amazon**, they need **a physical print copy before you publish on Amazon** (e-books must be sent to them before going to Amazon).
- **Legal deposit** (Legal Deposit Act 54 of 1997): under 100 printed copies, deposit 1 copy with the NLSA (Pretoria or Cape Town); 100 or more, 1 copy to each legal deposit library. Source: NLSA Legal Deposit page.
- Cost: ISBN R0. Estimated cost of the required copy: one KDP proof or author copy, about 4.20 USD print cost (about R69) plus international shipping to South Africa (estimate R300 to R600, not checked) plus local courier to NLSA.
- Each format needs its own ISBN (paperback, hardcover, e-book).

### Copyright line options

| Option | Copyright line | Publisher / imprint | Notes |
|---|---|---|---|
| A. Kevin personally, free KDP ISBN (simplest) | "Text copyright 2026 Kevin Britz. All rights reserved." | "Independently published" | Fastest. Amazon only. Kevin's legal name appears publicly on the book and Amazon page. |
| B. Kevin personally, NLSA ISBN | same | Imprint "Kevin Britz" or a chosen imprint name | Free ISBN, usable on other platforms and in SA bookshops. Needs the print copy to NLSA before publishing, plus legal deposit. |
| C. Company or imprint, NLSA ISBN | "Text copyright 2026 [Company name]. All rights reserved." | the company / imprint name | Only if the company actually owns the rights (written assignment from Kevin to the company). Keeps Kevin's personal name off the imprint. The imprint name must match NLSA records exactly in KDP. |
| D. Pen name as author (with A, B or C) | copyright holder stays the real owner | as chosen | Pen name on cover and KDP Author field; copyright line still names the legal owner. |

Notes:
- In South Africa copyright exists automatically on creation; no registration needed.
- The pictures are AI-generated. In some places (notably the US) purely AI-generated images may not be protected by copyright, so "Text copyright" (as now) is the accurate wording. Kevin's selection, arrangement and text are his.
- Never put the child's name, school or location on the credits page.

### Recommendation (c)

For a fast first edition: **Option A** (Kevin Britz, free KDP ISBN). If the series will also sell in South African bookshops or on other platforms, **Option B or C with a free NLSA ISBN** is better long term, but it adds about 1 to 3 weeks (ISBN processing plus getting a print copy to NLSA). Kevin decides the name (personal, pen name or imprint) first; everything else follows from that.
