#!/usr/bin/env python3
"""Build the Princess Baylin Ep1 picture book PDFs from text.md and art/.

Outputs (in out/ next to this script unless --out is given):
  interior-kdp.pdf  8.625 x 8.75 in pages (8.5 x 8.5 trim + 0.125 in bleed outside, top, bottom)
  cover-kdp.pdf     full wrap: back + spine + front, 0.125 in bleed all round
  etsy-screen.pdf   8.5 x 8.5 in, no bleed, RGB, compressed, cover as page 1
Requires: reportlab, Pillow. Fonts: Kalam (OFL).
"""
import argparse, io, os, re
from PIL import Image, ImageFilter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.colors import HexColor

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIRS = [os.path.join(HERE, 'fonts'), '/usr/share/fonts/truetype/sand-box/google/Kalam']
def font(name):
    for d in FONT_DIRS:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return p
    raise SystemExit(f'missing font {name}')
pdfmetrics.registerFont(TTFont('Kalam', font('Kalam-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Kalam-Bold', font('Kalam-Bold.ttf')))

PAPER = (247, 239, 221)
PAPER_HEX = HexColor('#F7EFDD')
INK = HexColor('#4A3222')
INK_SOFT = HexColor('#7A5A40')
TRIM = 8.5 * inch
BLEED = 0.125 * inch
PAGES_PER_INCH_SPINE = 0.002347  # KDP premium colour, white paper (assumption, verify in KDP cover calculator)

def parse(path):
    t = open(path, encoding='utf-8').read()
    pages = []
    for blk in re.split(r'^## Page ', t, flags=re.M)[1:]:
        lines = blk.splitlines()
        meta = {'n': int(lines[0].strip()), 'kind': 'story', 'crop': None}
        body = []
        for l in lines[1:]:
            m = re.match(r'^(art|kind|crop):\s*(.*)$', l)
            if m:
                meta[m.group(1)] = m.group(2).strip()
            else:
                body.append(l)
        paras, cur = [], []
        for l in body:
            if l.strip() == '':
                if cur: paras.append(cur); cur = []
            else:
                cur.append(l.strip())
        if cur: paras.append(cur)
        meta['paras'] = paras
        pages.append(meta)
    return pages

_cache = {}
def art(name, crop=None, fade='bottom', maxw=None, q=90, fade_frac=0.10, paper=PAPER):
    """Return an ImageReader of the frame, optionally cropped, with an edge faded into paper."""
    key = (name, crop, fade, maxw, q, fade_frac, paper)
    if key in _cache: return _cache[key]
    im = Image.open(os.path.join(HERE, 'art', name + '.jpg')).convert('RGB')
    if crop:
        z, fx, fy = [float(v) for v in crop.split()]
        w, h = im.size; cw, ch = int(w / z), int(h / z)
        x0, y0 = int((w - cw) * fx), int((h - ch) * fy)
        im = im.crop((x0, y0, x0 + cw, y0 + ch)).resize((w, h), Image.LANCZOS)
    if maxw and im.width > maxw:
        im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
    w, h = im.size
    if fade:
        paper = Image.new('RGB', im.size, paper)
        mask = Image.new('L', im.size, 255)
        fh = int(h * fade_frac)
        px = mask.load()
        for y in range(fh):
            a = int(255 * (y / fh) ** 1.4)
            yy = h - 1 - y if fade == 'bottom' else y
            for x in range(w):
                px[x, yy] = a
        im = Image.composite(im, paper, mask)
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=q, optimize=True); buf.seek(0)
    r = ImageReader(buf); _cache[key] = r
    return r

def fit_paras(c, paras, x, y, w, h, size, leading_mul=1.38, min_size=12, font_name='Kalam', align=TA_CENTER, color=INK, space=0.55):
    """Draw paragraphs centred vertically in the box, shrinking the font until they fit."""
    while True:
        st = ParagraphStyle('b', fontName=font_name, fontSize=size, leading=size * leading_mul,
                            alignment=align, textColor=color, spaceAfter=size * space)
        flow = [Paragraph('<br/>'.join(esc(l) for l in p), st) for p in paras]
        tot = 0
        for f in flow:
            _, fh = f.wrap(w, h); tot += fh + st.spaceAfter
        tot -= st.spaceAfter
        if tot <= h or size <= min_size:
            break
        size -= 0.5
    cy = y + (h - tot) / 2 + tot
    for f in flow:
        _, fh = f.wrap(w, h)
        f.drawOn(c, x, cy - fh); cy -= fh + st.spaceAfter
    return size

def esc(s):
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return re.sub(r'`([^`]*)`', r'\1', s)

def draw_page(c, p, W, H, tx, ty, maxw=None, q=90):
    """W,H canvas size; (tx,ty) trim box origin. Image runs to the canvas edge (bleed) at top and sides."""
    c.setFillColor(PAPER_HEX); c.rect(0, 0, W, H, stroke=0, fill=1)
    ih = W * 9 / 16
    c.drawImage(art(p['art'], p.get('crop'), 'bottom', maxw, q), 0, H - ih, W, ih)
    margin = 0.62 * inch           # >= 0.375 in safe margin inside trim on every side
    bx, bw = tx + margin, TRIM - 2 * margin
    by = ty + 0.5 * inch
    bh = (H - ih) + 0.05 * inch - by
    kind = p['kind']
    if kind == 'title':
        st = ParagraphStyle('t', fontName='Kalam-Bold', fontSize=34, leading=40, alignment=TA_CENTER, textColor=INK)
        para = Paragraph('<br/>'.join(esc(l) for l in p['paras'][0]), st)
        _, h1 = para.wrap(bw, bh)
        sub = Paragraph(esc(' '.join(p['paras'][1])), ParagraphStyle('s', fontName='Kalam', fontSize=17, leading=22, alignment=TA_CENTER, textColor=INK_SOFT))
        _, h2 = sub.wrap(bw, bh)
        top = by + (bh + h1 + h2 + 14) / 2
        para.drawOn(c, bx, top - h1); sub.drawOn(c, bx, top - h1 - 14 - h2)
    elif kind == 'credits':
        fit_paras(c, p['paras'], bx, by, bw, bh, 12.5, leading_mul=1.35, min_size=10, color=INK, space=0.5)
    elif kind == 'end':
        st = ParagraphStyle('e', fontName='Kalam-Bold', fontSize=30, leading=36, alignment=TA_CENTER, textColor=INK)
        head = Paragraph(esc(p['paras'][0][0]), st); _, hh = head.wrap(bw, bh)
        head.drawOn(c, bx, by + bh - hh - 4)
        fit_paras(c, p['paras'][1:], bx, by, bw, bh - hh - 14, 15)
    else:
        fit_paras(c, p['paras'], bx, by, bw, bh, 19.5)

def boxes(c, W, H, tx, ty):
    c.setCropBox((0, 0, W, H)); c.setBleedBox((0, 0, W, H))
    c.setTrimBox((tx, ty, tx + TRIM, ty + TRIM))

def build_interior(pages, path):
    W, H = TRIM + BLEED, TRIM + 2 * BLEED
    c = canvas.Canvas(path, pagesize=(W, H), initialFontName='Kalam')
    c.setTitle('Princess Baylin and the Lost Rain Song'); c.setAuthor('Kevin Britz')
    c.setSubject("Created from Kevin's stories, brought to life with AI.")
    for p in pages:
        tx = 0 if p['n'] % 2 == 1 else BLEED   # odd pages are rectos: bleed on the right
        boxes(c, W, H, tx, BLEED)
        draw_page(c, p, W, H, tx, BLEED)
        c.showPage()
    c.save()

BLURB = [["In the Kingdom of Sunhill the garden is dry, the pond is low, and the Rainbird has forgotten the song that brings the rain."],
         ["Princess Baylin thinks singing louder will fix it. With slow and steady Tilly the tortoise beside her, she learns that listening well and working together is the real answer."],
         ["A calm bedtime story about listening, teamwork and saying thank you. For ages 3 to 7."],
         ["Created from Kevin's stories, brought to life with AI."]]

def draw_front(c, x, y, w, h, ox, oy, maxw=None, q=90):
    """Front panel. (x,y,w,h) is the drawn area including any bleed; (ox,oy) the trim origin."""
    # background = average colour of the art's top rows, so the sky melts into the title area
    src = Image.open(os.path.join(HERE, 'art', 's0_21.25.jpg')).convert('RGB')
    top = src.crop((0, 0, src.width, int(src.height * 0.04))).resize((1, 1), Image.BOX).getpixel((0, 0))
    c.setFillColorRGB(*[v / 255 for v in top]); c.rect(x, y, w, h, stroke=0, fill=1)
    # cover art: taller than the panel is wide-scaled, so crop the sides (keeps Baylin, Tilly and the Rainbird)
    ih = 6.1 * inch; iw = ih * 16 / 9
    c.saveState(); pth = c.beginPath(); pth.rect(x, y, w, h); c.clipPath(pth, stroke=0, fill=0)
    c.drawImage(art('s0_21.25', None, 'top', maxw, q, 0.12, top), x - (iw - w) * 0.35, y, iw, ih)
    c.restoreState()
    m = 0.55 * inch
    bw = TRIM - 2 * m
    st = ParagraphStyle('t', fontName='Kalam-Bold', fontSize=48, leading=52, alignment=TA_CENTER, textColor=INK)
    p1 = Paragraph('Princess Baylin', st); _, h1 = p1.wrap(bw, 200)
    p2 = Paragraph('and the Lost Rain Song', ParagraphStyle('t2', parent=st, fontSize=30, leading=36)); _, h2 = p2.wrap(bw, 200)
    p3 = Paragraph('A Princess Baylin Diaries bedtime story', ParagraphStyle('s', fontName='Kalam', fontSize=15, leading=19, alignment=TA_CENTER, textColor=INK_SOFT)); _, h3 = p3.wrap(bw, 200)
    top = oy + TRIM - 0.6 * inch
    p1.drawOn(c, ox + m, top - h1); p2.drawOn(c, ox + m, top - h1 - 4 - h2); p3.drawOn(c, ox + m, top - h1 - h2 - 16 - h3)

def draw_back(c, x, y, w, h, ox, oy, maxw=None, q=90, barcode=True):
    c.setFillColor(PAPER_HEX); c.rect(x, y, w, h, stroke=0, fill=1)
    ih = w * 9 / 16
    c.drawImage(art('s10_502.75', None, 'bottom', maxw, q), x, y + h - ih, w, ih)
    m = 0.55 * inch
    # keep KDP barcode zone (2 x 1.2 in, bottom right, 0.25 in in from trim) clear
    bw = TRIM - 2 * m - (2.3 * inch if barcode else 0)
    fit_paras(c, BLURB, ox + m, oy + 0.5 * inch, bw, (y + h - ih) - (oy + 0.5 * inch), 15.5, min_size=10, align=TA_LEFT, space=0.6)

def build_cover(n_pages, path):
    spine = n_pages * PAGES_PER_INCH_SPINE * inch
    W = 2 * TRIM + spine + 2 * BLEED; H = TRIM + 2 * BLEED
    c = canvas.Canvas(path, pagesize=(W, H), initialFontName='Kalam')
    c.setTitle('Princess Baylin and the Lost Rain Song (cover)'); c.setAuthor('Kevin Britz')
    c.setSubject("Created from Kevin's stories, brought to life with AI.")
    c.setFillColor(PAPER_HEX); c.rect(0, 0, W, H, stroke=0, fill=1)
    draw_back(c, 0, 0, BLEED + TRIM, H, BLEED, BLEED)
    draw_front(c, BLEED + TRIM + spine, 0, TRIM + BLEED, H, BLEED + TRIM + spine, BLEED)
    c.showPage(); c.save()
    return spine / inch, W / inch, H / inch

def build_screen(pages, path):
    W = H = TRIM
    c = canvas.Canvas(path, pagesize=(W, H), pageCompression=1, initialFontName='Kalam')
    c.setTitle('Princess Baylin and the Lost Rain Song'); c.setAuthor('Kevin Britz')
    c.setSubject("Created from Kevin's stories, brought to life with AI.")
    draw_front(c, 0, 0, W, H, 0, 0, maxw=1400, q=80); c.showPage()
    for p in pages:
        draw_page(c, p, W, H, 0, 0, maxw=1400, q=80); c.showPage()
    draw_back(c, 0, 0, W, H, 0, 0, maxw=1400, q=80, barcode=False); c.showPage()
    c.save()

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--out', default=os.path.join(HERE, 'out'))
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    pages = parse(os.path.join(HERE, 'text.md'))
    assert len(pages) % 2 == 0, 'page count must be even'
    build_interior(pages, os.path.join(a.out, 'interior-kdp.pdf'))
    s, cw, ch = build_cover(len(pages), os.path.join(a.out, 'cover-kdp.pdf'))
    build_screen(pages, os.path.join(a.out, 'etsy-screen.pdf'))
    print(f'pages={len(pages)} spine={s:.4f}in cover={cw:.4f}x{ch:.4f}in')
