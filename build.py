#!/usr/bin/env python3
"""Builds the site's pages from source/<lang>/{support,privacy}.html: python3 build.py

English stays at the root (index.html, privacy.html: the stores and the game link there); every other language goes
into its own folder (zh/, hi/, es/, fr/, uk/). The pages are committed as built: GitHub Pages serves them as they are.
"""
from pathlib import Path

SITE = "https://madlocalhostdev.github.io/brushpush/"
ROOT = Path(__file__).parent

# Code, folder ("" = the root), the name in its own language (as in the game), and the words the template needs.
LANGS = [
    ("en", "", "English", {
        "support": "Support", "privacy": "Privacy policy", "contact": "Contact",
        "support_title": "BrushPush Support", "privacy_title": "BrushPush Privacy Policy",
        "support_desc": "Help and contact for BrushPush, a push puzzle that paints the world's landmarks layer by layer.",
        "privacy_desc": "How BrushPush and its ad partner handle your data.",
        "tagline": "A push puzzle that paints the world's landmarks, one layer at a time.",
        "languages": "Languages",
    }),
    ("zh-CN", "zh", "中文", {
        "support": "支持", "privacy": "隐私政策", "contact": "联系我们",
        "support_title": "BrushPush 支持", "privacy_title": "BrushPush 隐私政策",
        "support_desc": "BrushPush 的帮助与联系方式。这是一款推方块解谜游戏，一层一层画出世界名胜。",
        "privacy_desc": "BrushPush 及其广告合作伙伴如何处理你的数据。",
        "tagline": "推方块解谜，一层一层画出世界名胜。",
        "languages": "语言",
    }),
    ("hi", "hi", "हिन्दी", {
        "support": "सहायता", "privacy": "गोपनीयता नीति", "contact": "संपर्क",
        "support_title": "BrushPush सहायता", "privacy_title": "BrushPush गोपनीयता नीति",
        "support_desc": "BrushPush के लिए सहायता और संपर्क: एक पुश पहेली, जो परत-दर-परत दुनिया की मशहूर जगहें रंगती है।",
        "privacy_desc": "BrushPush और उसका विज्ञापन साझेदार आपके डेटा के साथ क्या करते हैं।",
        "tagline": "एक पुश पहेली, जो परत-दर-परत दुनिया की मशहूर जगहें रंगती है।",
        "languages": "भाषाएँ",
    }),
    ("es", "es", "Español", {
        "support": "Ayuda", "privacy": "Política de privacidad", "contact": "Contacto",
        "support_title": "Ayuda de BrushPush", "privacy_title": "Política de privacidad de BrushPush",
        "support_desc": "Ayuda y contacto de BrushPush, un puzle de empujar que pinta los monumentos del mundo capa a capa.",
        "privacy_desc": "Cómo tratan tus datos BrushPush y su socio publicitario.",
        "tagline": "Un puzle de empujar que pinta los monumentos del mundo, capa a capa.",
        "languages": "Idiomas",
    }),
    ("fr", "fr", "Français", {
        "support": "Assistance", "privacy": "Politique de confidentialité", "contact": "Contact",
        "support_title": "Assistance BrushPush", "privacy_title": "Politique de confidentialité de BrushPush",
        "support_desc": "Aide et contact pour BrushPush, un puzzle de poussée qui peint les monuments du monde couche par couche.",
        "privacy_desc": "Comment BrushPush et son partenaire publicitaire traitent vos données.",
        "tagline": "Un puzzle de poussée qui peint les monuments du monde, couche après couche.",
        "languages": "Langues",
    }),
    ("uk", "uk", "Українська", {
        "support": "Підтримка", "privacy": "Політика конфіденційності", "contact": "Контакт",
        "support_title": "Підтримка BrushPush", "privacy_title": "Політика конфіденційності BrushPush",
        "support_desc": "Допомога й контакти BrushPush — головоломки зі штовханням, що шар за шаром малює визначні місця світу.",
        "privacy_desc": "Як BrushPush і її рекламний партнер поводяться з вашими даними.",
        "tagline": "Головоломка зі штовханням, що шар за шаром малює визначні місця світу.",
        "languages": "Мови",
    }),
]

# The extra Google Font a script needs beyond Noto Sans.
FONTS = {"hi": "Noto+Sans+Devanagari:wght@400;700;800", "zh-CN": "Noto+Sans+SC:wght@400;700;800"}

PAGES = {"support": "index.html", "privacy": "privacy.html"}

TEMPLATE = """<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#2E2042">
  <link rel="canonical" href="{canonical}">
{alternates}
  <link rel="icon" type="image/png" href="{up}img/favicon.png">
  <link rel="apple-touch-icon" href="{up}img/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{up}style.css">
</head>
<body>
  <main class="{page}">
    <header class="hero">
      <a href="./"><img src="{up}img/logo.png" width="640" height="640" alt="BrushPush"></a>
{tagline}    </header>
{body}
  </main>

  <footer>
    <nav>
      <a href="./">{support}</a>
      <a href="privacy.html">{privacy}</a>
      <a href="mailto:madlocalhostdev@gmail.com">{contact}</a>
    </nav>
    <nav class="langs" aria-label="{languages}">
{langs}
    </nav>
    © 2026 madlocalhostdev
  </footer>
  <script src="{up}backdrop.js"></script>
</body>
</html>
"""


def path_of(folder: str, page: str) -> str:
    """The page's path from the site's root, "" for the English support page."""
    name = "" if page == "support" else PAGES[page]
    return (folder + "/" if folder else "") + name


def build() -> None:
    for code, folder, _name, words in LANGS:
        up = "../" if folder else ""
        fonts = "family=Noto+Sans:wght@400;700;800" + (f"&family={FONTS[code]}" if code in FONTS else "")
        for page, file in PAGES.items():
            body = (ROOT / "source" / (folder or "en") / f"{page}.html").read_text().rstrip("\n")
            alternates = "\n".join(
                f'  <link rel="alternate" hreflang="{c}" href="{SITE}{path_of(f, page)}">' for c, f, _n, _w in LANGS
            ) + f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}{path_of("", page)}">'
            langs = "\n".join(
                f'      <a href="{up + path_of(f, page) or "./"}" hreflang="{c}" lang="{c}"'
                + (' aria-current="page"' if c == code else "") + f">{n}</a>"
                for c, f, n, _w in LANGS
            )
            tagline = f'      <p>{words["tagline"]}</p>\n' if page == "support" else ""
            html = TEMPLATE.format(
                lang=code, title=words[page + "_title"], desc=words[page + "_desc"],
                canonical=SITE + path_of(folder, page), alternates=alternates, up=up, fonts=fonts, page=page,
                tagline=tagline, body=body, langs=langs, **{k: words[k] for k in ("support", "privacy", "contact", "languages")},
            )
            out = ROOT / folder / file if folder else ROOT / file
            out.parent.mkdir(exist_ok=True)
            out.write_text(html)
            print(out.relative_to(ROOT))


if __name__ == "__main__":
    build()
