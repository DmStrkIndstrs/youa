"""Regenerate the font subsets inlined into the claw-machine page.

Needs fonttools and brotli (dev only):
    uv run --with fonttools --with brotli python claw-machine/fonts/make_subsets.py <Jua-Regular.ttf> <BagelFatOne-Regular.ttf>

Sources: github.com/google/fonts (ofl/jua, ofl/bagelfatone), SIL Open Font License 1.1.
"""
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

HERE = Path(__file__).resolve().parent

# Every KS X 1001 Hangul syllable (2,350), so any name the teacher types renders in Jua.
KSX1001 = ''.join(bytes([b1, b2]).decode('euc-kr') for b1 in range(0xB0, 0xC9) for b2 in range(0xA1, 0xFF))
ASCII = ''.join(chr(c) for c in range(0x20, 0x7F))
PUNCT = '·…×~!?「」“”‘’–—'

# Bagel Fat One only sets fixed signage: the shop sign, the marquee and the result shouts.
BAGEL_TEXT = '인형뽑기가게성공꽝모두~! ' + ASCII


def build(src, text, out):
    opts = subset.Options()
    opts.flavor = 'woff2'
    opts.layout_features = ['*']
    opts.name_IDs = ['*']
    opts.notdef_outline = True
    font = TTFont(src)
    sub = subset.Subsetter(opts)
    sub.populate(text=text)
    sub.subset(font)
    font.flavor = 'woff2'
    font.save(out)
    print(out.name, out.stat().st_size // 1024, 'KB')


if __name__ == '__main__':
    jua, bagel = sys.argv[1], sys.argv[2]
    build(jua, KSX1001 + ASCII + PUNCT, HERE / 'jua-ksx1001.woff2')
    build(bagel, BAGEL_TEXT, HERE / 'bagel-fat-one-sign.woff2')
