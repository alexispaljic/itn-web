
from pathlib import Path
import re

ROOT = "https://boisgera.github.io/itn-web"

for path in Path("dist").rglob("*.html"):
    with path.open(mode="r", encoding="utf-8") as f:
        src = f.read()
    src = src.replace('href="/', f'href="{ROOT}/')
    src = src.replace('src="/', f'src="{ROOT}/')
    while match := re.search(r'srcset="/[^"]*"', src): # ⚠️ Hack
        content = match.group(0)
        start, end = match.span(0)
        prefix, string = content[:7], content[7:]
        assert prefix == "srcset="
        srcset_paths = string[1:-1].split(",")
        #print(srcset_paths)
        srcset_paths = [f"{ROOT}{p}" for p in srcset_paths if p.startswith("/")]
        srcset =  f'srcset="{" ".join(srcset_paths)}"'
        src = src[:start] + srcset + src[end:]
    with path.open(mode="w", encoding="utf-8") as f:
        f.write(src)