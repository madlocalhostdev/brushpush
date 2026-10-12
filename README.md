# BrushPush site

Support page and privacy policy of the BrushPush mobile game, served by GitHub Pages, in the game's six languages.

Edit `source/<lang>/{support,privacy}.html` (English in `source/en`), then run `python3 build.py`: it writes `index.html` and
`privacy.html` (English, at the root: the stores and the game link there) and `zh/`, `hi/`, `es/`, `fr/`, `uk/`.
Commit the built pages too.
