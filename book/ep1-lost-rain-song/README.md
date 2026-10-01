# Princess Baylin and the Lost Rain Song: picture book (Episode 1, English)

Draft built 2026-10-01 SAST. Nothing has been published, listed or uploaded anywhere (no KDP, no Etsy, no YouTube).
English only. Afrikaans and isiZulu are left out until the native-speaker checks are done.

## Files

| File | What it is |
|---|---|
| `text.md` | Read-aloud text, 26 pages, ages 3 to 7 (about 40 to 65 words per story page). The build script reads it. |
| `build.py` | Builds all three PDFs from `text.md` and `art/` (Python 3, reportlab, Pillow, Kalam font, OFL). Run `python3 build.py`. Output goes to `out/`. |
| `art-manifest.md` | Every picture used, which page it is on, and where it came from. |
| `extract_art.sh` | Re-creates `art/` from the Episode 1 video if the JPEGs are missing. |
| `art/` | The 25 frames used (1920x1080 JPEG). Kept on the box at `/workspace/princess-baylin-book/book/ep1-lost-rain-song/art/` (about 20 MB). |
| `out/interior-kdp.pdf` | KDP interior: 26 pages at 8.625 x 8.75 in (8.5 x 8.5 in trim plus 0.125 in bleed on the outside edge, top and bottom). Odd pages are right-hand pages. Fonts embedded (Kalam, subset). |
| `out/cover-kdp.pdf` | KDP full-wrap cover: back, spine, front at 17.311 x 8.75 in. |
| `out/etsy-screen.pdf` | Screen PDF for Etsy: 8.5 x 8.5 in, no bleed, RGB, compressed images, cover as page 1, back cover as last page (28 pages). |

If `art/` and `out/` are not in this folder in the repo, they live on the shared box under `/workspace/princess-baylin-book/` (they are binary files and could not be pushed with the text-only GitHub tool).

## Layout

- Every page has a picture and text. The picture runs to the bleed at the top and both sides; its bottom edge fades into warm paper, and the text sits below it on the paper.
- Text is kept at least 0.62 in inside the trim on every side (KDP minimum is 0.375 in), so nothing important is near the trim or the gutter.
- Page 1 is the title page, page 2 the credits page, page 26 "The End".
- The disclosure line "Created from Kevin's stories, brought to life with AI." is on the credits page (2), the end page (26) and the back cover.

## Pages needing new art

None. All 26 pages and both covers use existing Episode 1 art (frames from the rendered episode video). Optional upgrades only:

- Optional, page 25: Bonayo the owl is heard ("Hoo-hoo") from the fig tree but not shown, because no Episode 1 picture has an owl. A future picture of Bonayo in the fig tree at dusk would let Bonayo appear on that page. Bonayo is canon; Episode 1's video did not include the owl, so the book adds Bonayo in text only.
- Optional, page 6: this is a 1.35x zoom of the page 7 picture (the only Rainbird frame), so it is softer (about 165 ppi at print size).
- Several pictures come from the same video scene: pages 3 to 5; 6 and 7; 8 and 9; 10 and 11; 12, 13 and 26; 14 and 15; 16 and 17; 18 and 19; 20 and 21; 2, 24 and 25. The pan and zoom make each frame a little different, but a reader will notice the pairs. Fresh pictures for one page of each pair would make the book richer.

## Things to check before any KDP upload (KEVIN)

1. Resolution: the frames are 1920x1080, about 223 ppi across the 8.625 in bleed width (KDP recommends 300 ppi). KDP may warn. Higher-resolution exports of the original Canva images, or an upscale, would fix it.
2. Spine: 26 pages x 0.002347 in (premium colour, white paper) = 0.061 in. This is an assumption. Download KDP's cover template for 8.5 x 8.5 in, 26 pages, premium colour, and compare before uploading. There is no spine text (KDP needs 79 or more pages for spine text).
3. Barcode: the back cover keeps the bottom-right area (about 2.3 x 1.4 in) clear for KDP's barcode.
4. Credits page says "Text copyright 2026 Kevin Britz. All rights reserved." and "ISBN to be assigned". Change the copyright holder if it should be a company name.
5. Placeholder cast still flagged in canon: Tilly the tortoise, Kingdom of Sunhill, the Rainbird, the Grandmother Tree.

## Price estimates (estimates only, not decided)

Rate used: USD/ZAR 16.44 (market quote for 1 Oct 2026). Rounded.

KDP paperback (Amazon.com), 8.5 x 8.5 in counts as a large trim (wider than 6.12 in). KDP's published printing cost for premium colour, 24 to 40 pages, large trim, is a flat 4.20 USD per book (fixed cost, no per-page cost). Royalty at 60% = 0.6 x list price minus printing cost.

| List price | Printing cost | Royalty per copy (60%) | Expanded distribution (40%) |
|---|---|---|---|
| 11.99 USD (about R197) | 4.20 USD | 2.99 USD | 0.60 USD |
| **12.99 USD (about R214), suggested** | 4.20 USD | **3.59 USD (about R59)** | 1.00 USD |
| 14.99 USD (about R246) | 4.20 USD | 4.79 USD | 1.80 USD |

Amazon has no ZAR paperback store, so the ZAR figures are equivalents. For selling author copies locally, about R229 to R249 covers printing, shipping in and a margin.

Etsy digital PDF: suggested **4.99 USD (about R82)**, or R85 if listed in rand. Etsy fees are about 0.20 USD listing, 6.5% transaction and roughly 3% plus 0.25 USD payment processing (varies by country), leaving roughly 4.05 USD (about R67) per sale. Selling AI-assisted art on Etsy needs the AI disclosure in the listing.
