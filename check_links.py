from pathlib import Path
import re

root = Path(".")

href_pattern = re.compile(r'href=["\']([^"\']+)["\']', re.I)

broken = []

def resolve(base, href):
    href = href.split("#")[0].split("?")[0]

    if href.startswith(("http", "mailto:", "tel:", "javascript:", "#")):
        return None

    # absolute route
    if href.startswith("/"):
        path = href.lstrip("/")
        p1 = root / path / "index.html"
        p2 = root / (path + ".html")
    else:
        # relative route
        p1 = (base / href).resolve()
        if p1.is_dir():
            p1 = p1 / "index.html"
        p2 = None

    if p1.exists():
        return p1
    if p2 and p2.exists():
        return p2

    return None


for html in root.rglob("*.html"):
    if ".git" in str(html) or "node_modules" in str(html):
        continue

    text = html.read_text(errors="ignore")

    for href in href_pattern.findall(text):
        target = resolve(html.parent, href)

        if target is None:
            continue

        if not target.exists():
            broken.append((html, href))

print("\nBroken links:", len(broken))

for b in broken[:50]:
    print(b)
