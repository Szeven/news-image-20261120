# The World in One Day — 20 November 2026

Infographic (`entry.png`, 1024×1024) summing up Friday 20 November 2026.
All six stories were reported on 20 November 2026.

## Stories

1. **Peace summit — Trump, Putin & Xi sign peace declaration.**
   First-ever trilateral talks in Shenzhen (APEC) end with a four-point
   declaration: UN reform, energy cooperation, official immunity and
   nuclear-risk dialogue.
   Sources: https://jabulaniradio.com/rss/top-international-news-17
   (BBC headlines), https://tuttiquotidiani.it/en/news/latest?author=Le%20Monde&page=1

2. **Markets — AI selloff deepens: Dow drops below 50,000.**
   S&P 500 −2.02%, Nasdaq −2.25%; Taiwan stocks plunge more than 2,200
   points intraday in a week-long rout.
   Sources: https://www.instagram.com/p/Df8wnOcl4Kx/ (The Daily Brief),
   https://simplelife.news/regions/tw/en/latest.html

3. **Tech — Anthropic soars on Nasdaq debut.**
   The first frontier AI company to go public jumps 17% on day one under
   ticker ANT, on record trading volume.
   Sources: https://jabulaniradio.com/rss/top-international-news-17
   (BBC), https://simplelife.news/regions/tw/en/latest.html

4. **Ukraine — Ukraine hits Crimean Bridge a third time.**
   Neptune missiles briefly halt trains; Putin vows a "far more painful"
   response and rejects ceasefire talks.
   Source: https://www.instagram.com/p/Df8wnOcl4Kx/ (The Daily Brief)

5. **Climate — COP31 draft drops fossil-fuel phase-out.**
   Australia's draft text promotes electrification and renewables instead,
   drawing outcry from negotiators.
   Source: https://tuttiquotidiani.it/en/news/latest?author=Le%20Monde&page=1

6. **Middle East — Houthi attack damages Riyadh's PIF tower.**
   Saudi Arabia confirms windows blown out of the 80-storey tower; no
   injuries reported.
   Source: https://simplelife.news/regions/tw/en/latest.html

## Build notes

- Image drawn fresh with Python + Pillow (DejaVu Sans), no copied artwork.
- `main.ts` copies `entry.png` to the output directory; paths resolve from
  the script's own folder, never from the working directory.
- Verified: `node --check main.ts` passes; the program runs in the repo
  directory and as uid 65534 from a foreign working directory, writing a
  byte-identical `entry.png` both times.
- The 19 November ICJ ruling on Myanmar was deliberately left out: it was
  first reported on 19 November, so it belongs to the previous day's edition.
