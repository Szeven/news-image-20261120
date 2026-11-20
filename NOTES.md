# The World in One Day — 20 November 2026

Round-2 rebuild of the news-image-20261120 entry, drawn fresh with Python +
Pillow (DejaVu fonts) in `draw.py`. `main.ts` copies `entry.png` into the
output directory. All six stories were researched from live news coverage of
Friday 20 November 2026 and verified against multiple outlets before drawing.

## The six stories

1. **World Court: Myanmar committed genocide** (Justice · The Hague)
   The International Court of Justice ruled 9–6 that Myanmar's 2017 campaign
   against the Rohingya was genocide — the first time the court has held a
   state responsible for genocide. Case brought by The Gambia (2019); over
   1.3 million Rohingya remain displaced.
   Sources: BBC News, UN News, PBS NewsHour —
   https://oneturn.news/day/2026-11-20/

2. **Trump, Xi and Putin sign peace declaration** (Diplomacy · Shenzhen)
   The leaders of the US, China and Russia met in Shenzhen and signed a
   four-point joint declaration covering nuclear risk, UN reform, energy
   supply stability and ICC jurisdiction. No mention of Ukraine or Iran;
   the talks lasted about 70 minutes.
   Sources: BBC News, The Guardian, Euronews —
   https://oneturn.news/day/2026-11-20/

3. **Anthropic soars 17% on debut as markets sink** (Markets · New York)
   Anthropic closed near $97 on its Nasdaq debut (IPO price $83), a record
   $81.3bn listing at a valuation near $1.5 trillion, ticker ANT. The S&P 500
   fell about 2%, its fifth straight loss; Japan's Nikkei dropped 4.8% on
   Friday and SoftBank fell more than 16%.
   Sources: BBC News, CNBC, The Hindu —
   https://oneturn.news/day/2026-11-20/

4. **Houthi missile hits Riyadh's PIF Tower** (Conflict · Riyadh)
   Houthi missiles hit Riyadh's financial district, damaging the Public
   Investment Fund tower and other buildings. No injuries reported; Saudi
   Arabia said it will not tolerate attacks on its territory.
   Sources: Sky News, Middle East Eye, The Hindu —
   https://oneturn.news/day/2026-11-20/

5. **Russian strike kills 3 in Kyiv, hits bridges** (War · Kyiv)
   An overnight Russian missile and drone attack on Kyiv killed three people
   and damaged three bridges across the Dnipro river. Ukraine's allies met in
   Berlin the same day to discuss security guarantees for Ukraine.
   Sources: BBC News, Augerton Morning Edition —
   https://augerton.com/digest/2026/11/20/morning/

6. **COP31 draft drops fossil-fuel phase-out** (Climate · Antalya)
   Negotiators removed any reference to ending fossil fuel use — and net-zero
   dates — from the slimmed-down draft deal at COP31 in Antalya. Pacific
   nations such as Vanuatu demanded a phase-out as talks entered their
   final day.
   Sources: Japan Times, CBC News, The Hindu —
   https://oneturn.news/day/2026-11-20/

## Build notes

- `draw.py` renders the 1024×1024 PNG with Pillow: navy masthead with the
  title and date, then a 2×3 grid of story cards (tag, headline, summary).
  Re-run with `python3 draw.py`.
- `entry.png` was visually checked: all six panels render complete sentences
  with no truncation or garbled text.
- `main.ts` resolves paths from its own location (never the working
  directory), creates the output directory, never deletes it, and copies
  `entry.png` into it. Verified with `node --check`, a repo-dir run, and a
  run as user 65534 from a foreign working directory.
