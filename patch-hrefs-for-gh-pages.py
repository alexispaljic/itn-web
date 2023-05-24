
from pathlib import Path

ROOT = "https://boisgera.github.io/itn-web"

for path in Path("dist").rglob("*.html"):
    with path.open(mode="r", encoding="utf-8") as f:
        src = f.read()
    src = src.replace('href="/', f'href="{ROOT}/')
    src = src.replace('srcset="/', f'srcset="{ROOT}/')
    with path.open(mode="w", encoding="utf-8") as f:
        f.write(src)