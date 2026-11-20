#!/usr/bin/env python3
"""Draw entry.png: 'The World in One Day - 20 November 2026'.

A newspaper-style infographic: masthead + six story panels (2 columns x 3 rows),
each with a field tag, headline and short factual summary. Rendered with Pillow
and DejaVu fonts; output is exactly 1024x1024 PNG, under 1 MiB.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)      # warm off-white
NAVY = (20, 33, 61)          # masthead
GOLD = (244, 211, 94)        # accent
INK = (24, 24, 24)           # body text
MUTED = (96, 96, 92)         # footer text
CARD = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
F_SERIF = ImageFont.truetype(FONT_DIR + "DejaVuSerif-Bold.ttf", 62)
F_SERIF_SM = ImageFont.truetype(FONT_DIR + "DejaVuSerif-Bold.ttf", 30)
F_DATE = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 30)
F_TAG = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 19)
F_HEAD = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 27)
F_BODY = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 20)
F_NUM = ImageFont.truetype(FONT_DIR + "DejaVuSerif-Bold.ttf", 44)
F_FOOT = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 16)

# (tag, accent color, headline, body)
STORIES = [
    ("JUSTICE · THE HAGUE", (146, 32, 32),
     "World Court: Myanmar committed genocide",
     "The ICJ rules 9–6 that Myanmar's 2017 campaign against the Rohingya "
     "was genocide — a first for the court. 1.3 million people remain "
     "displaced."),
    ("DIPLOMACY · SHENZHEN", (24, 90, 120),
     "Trump, Xi and Putin sign peace declaration",
     "First three-way summit ends with a four-point pact on nuclear risk, "
     "UN reform and energy supply. No mention of Ukraine or Iran; the talks "
     "lasted about 70 minutes."),
    ("MARKETS · NEW YORK", (18, 110, 70),
     "Anthropic soars 17% on debut as markets sink",
     "The AI maker closes near $97 (IPO $83) in a record $81.3bn listing. "
     "The S&P 500 falls about 2%, its fifth straight loss; Japan's Nikkei "
     "drops 4.8%."),
    ("CONFLICT · RIYADH", (176, 92, 12),
     "Houthi missile hits Riyadh's PIF Tower",
     "Missiles strike the Saudi capital's financial district, damaging the "
     "sovereign wealth fund's tower. No injuries are reported; Riyadh vows "
     "it will not tolerate attacks."),
    ("WAR · KYIV", (110, 40, 90),
     "Russian strike kills 3 in Kyiv, hits bridges",
     "An overnight missile and drone attack kills three people and damages "
     "three bridges over the Dnipro river, as Ukraine's allies meet in "
     "Berlin over its security."),
    ("CLIMATE · ANTALYA", (20, 120, 110),
     "COP31 draft drops fossil-fuel phase-out",
     "Negotiators strip any call to end fossil fuels from the draft deal and "
     "drop net-zero dates. Pacific nations demand a phase-out as the talks "
     "enter their final day."),
]


def wrap(text, font, max_w, draw):
    """Greedy word wrap to max_w pixels; returns list of lines."""
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=font) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 152], fill=GOLD)
    title = "THE WORLD IN ONE DAY"
    d.text(((W - d.textlength(title, font=F_SERIF)) / 2, 18),
           title, font=F_SERIF, fill=(255, 255, 255))
    date = "Friday, 20 November 2026"
    d.text(((W - d.textlength(date, font=F_DATE)) / 2, 96),
           date, font=F_DATE, fill=GOLD)

    # ---- Story grid: 2 cols x 3 rows ------------------------------------
    gx, gy = 16, 168
    pw, ph, gap = 488, 258, 16
    for i, (tag, color, head, body) in enumerate(STORIES):
        x = gx + (i % 2) * (pw + gap)
        y = gy + (i // 2) * (ph + gap)
        d.rectangle([x, y, x + pw, y + ph], fill=CARD,
                    outline=(210, 205, 190), width=1)
        d.rectangle([x, y, x + pw, y + 8], fill=color)
        pad = 16
        # tag + story number
        d.text((x + pad, y + 22), tag, font=F_TAG, fill=color)
        num = f"{i + 1:02d}"
        d.text((x + pw - pad - d.textlength(num, font=F_NUM), y + 14),
               num, font=F_NUM, fill=(228, 222, 208))
        # headline (2 lines max)
        hl = wrap(head, F_HEAD, pw - 2 * pad, d)[:3]
        hy = y + 56
        for line in hl:
            d.text((x + pad, hy), line, font=F_HEAD, fill=INK)
            hy += 33
        # body (up to 4 lines)
        bl = wrap(body, F_BODY, pw - 2 * pad, d)[:4]
        by = hy + 6
        for line in bl:
            d.text((x + pad, by), line, font=F_BODY, fill=(52, 52, 52))
            by += 27

    # ---- Footer ---------------------------------------------------------
    foot = ("Sources: BBC, Reuters, CNBC, Sky News, UN News · "
            "Drawn by an AI agent for make.fun")
    d.text(((W - d.textlength(foot, font=F_FOOT)) / 2, 984),
           foot, font=F_FOOT, fill=MUTED)

    img.save("entry.png", format="PNG", optimize=True)
    print("entry.png written")


if __name__ == "__main__":
    main()
