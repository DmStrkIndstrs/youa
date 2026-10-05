"""Build claw-machine/index.html from src/app.html with the fonts inlined.

The page must work from a USB stick or a school network that blocks web fonts,
so the subset fonts in fonts/ are embedded as data URIs. Standard library only:
    python3 claw-machine/build.py
"""
import base64
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTS = [
    ('Jua Local', 'jua-ksx1001.woff2'),
    ('Bagel Local', 'bagel-fat-one-sign.woff2'),
]


def font_faces():
    rules = []
    for family, file in FONTS:
        data = base64.b64encode((HERE / 'fonts' / file).read_bytes()).decode('ascii')
        rules.append(
            '@font-face{font-family:"%s";src:url(data:font/woff2;base64,%s) format("woff2");'
            'font-weight:400;font-style:normal;font-display:block}' % (family, data)
        )
    return ''.join(rules)


def main():
    src = (HERE / 'src' / 'app.html').read_text(encoding='utf-8')
    marker = '/*@@FONTS@@*/'
    if marker not in src:
        raise SystemExit('font marker missing from src/app.html')
    out = src.replace(marker, font_faces())
    (HERE / 'index.html').write_text(out, encoding='utf-8')
    print('index.html', len(out.encode('utf-8')) // 1024, 'KB')


if __name__ == '__main__':
    main()
