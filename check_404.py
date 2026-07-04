from pathlib import Path
import re

root = Path(".")

href_pattern = re.compile(r'href=["\']([^"\']+)["\']', re.I)

broken_links = []

def resolve_target(base_file, href):
    # remove query/hash
    href = href.split("#")[0].split("?")[0]

    if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
        return None

    # external links ignored
    if href.startswith(("http://", "https://")):
        return None

    # absolute site path like /bmw/x5
    if href.startswith("/"):
        target = root / href.lstrip("/")
    else:
        target = base_file.parent / href

    # if it's a folder → index.html
    if target.is_dir():
        target = target / "index.html"

    # if no extension → try .html fallback
    if target.suffix == "":
        html_version = target.with_suffix(".html")
        if html_version.exists():
            return html_version
        return target

    return target


for html_file in root.rglob("*.html"):
    if ".git" in str(html_file) or "node_modules" in str(html_file):
        continue

    content = html_file.read_text(errors="ignore")

    links = href_pattern.findall(content)

    for href in links:
        target = resolve_target(html_file, href)

        if target is None:
            continue

        if not target.exists():
            broken_links.append((html_file.relative_to(root), href))

print("\n🚨 BROKEN LINKS REPORT")
print(f"Total broken links: {len(broken_links)}\n")

for page, link in broken_links[:100]:
    print(f"{page}  ->  {link}")
