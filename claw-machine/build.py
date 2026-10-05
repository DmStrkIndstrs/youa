"""Build the pages with the fonts inlined:
    claw-machine/src/app.html -> claw-machine/index.html  (the claw game)
    town/src/app.html         -> index.html               (the 우리동네 map, the site's front page)

The pages must work from a USB stick or a school network that blocks web fonts,
so the subset fonts in fonts/ are embedded as data URIs. Standard library only:
    python3 claw-machine/build.py
"""
import base64
import csv
import json
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


TARGETS = [
    (HERE / 'src' / 'app.html', HERE / 'index.html'),
    (HERE.parent / 'town' / 'src' / 'app.html', HERE.parent / 'index.html'),
]


VOICE_DIR = HERE.parent / 'town' / 'voices'
VOICE_EXTS = ('.mp3', '.m4a', '.wav', '.ogg', '.webm')


def voices():
    """Map each line in town/voices/lines.csv to its recording, if one has been added.

    A recording is any file named after the line's number (001.mp3, 001.m4a, ...).
    Lines without a file are left out, so the page reads them with the device voice.
    """
    found = {}
    with open(VOICE_DIR / 'lines.csv', encoding='utf-8-sig', newline='') as f:
        for row in csv.DictReader(f):
            for ext in VOICE_EXTS:
                if (VOICE_DIR / (row['번호'] + ext)).exists():
                    found[row['대사']] = 'town/voices/' + row['번호'] + ext
                    break
    return found


def main():
    faces = font_faces()
    marker = '/*@@FONTS@@*/'
    voice_marker = '/*@@VOICES@@*/{}'
    recorded = voices()
    for src_path, out_path in TARGETS:
        src = src_path.read_text(encoding='utf-8')
        if marker not in src:
            raise SystemExit('font marker missing from %s' % src_path)
        out = src.replace(marker, faces)
        if voice_marker in out:
            out = out.replace(voice_marker, json.dumps(recorded, ensure_ascii=False))
            print('voices: %d recorded lines' % len(recorded))
        out_path.write_text(out, encoding='utf-8')
        print(out_path.relative_to(HERE.parent), len(out.encode('utf-8')) // 1024, 'KB')


if __name__ == '__main__':
    main()
