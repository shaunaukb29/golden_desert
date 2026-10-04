import os

sitemap_path = "/Users/shaunaukbasu/Desktop/golden_desert/sitemap_v4.xml"
static_dir = "/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static"

# Read the current sitemap
with open(sitemap_path, 'r') as f:
    content = f.read()

# Get all HTML files in static dir
html_files = sorted([f.replace('.html', '') for f in os.listdir(static_dir) if f.endswith('.html')])

# Find which ones are already in the sitemap
already_in = set()
for h in html_files:
    # Check various URL patterns the sitemap might use
    if f"/{h}" in content:
        already_in.add(h)

new_pages = [h for h in html_files if h not in already_in]

print(f"Total HTML files in static: {len(html_files)}")
print(f"Already in sitemap: {len(already_in)}")
print(f"New pages to add: {len(new_pages)}")

# Build the new URL entries
new_entries = []
for page in new_pages:
    new_entries.append(f"""  <url>
    <loc>https://carithm.vercel.app/audio/{page}</loc>
    <lastmod>2026-10-04</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>""")

# Also build entries for existing audio/* pages that need priority bumped to 1.0
# These are the ones already present that match our static dir pages
existing_audio_pages = [h for h in html_files if h in already_in]
print(f"Existing audio pages to bump to priority 1.0: {len(existing_audio_pages)}")

# Insert new entries before </urlset>
new_block = "\n\n  <!-- ── Programmatic SEO: Car-Specific Symptom Pages (mass generated, priority 1.0) ── -->\n" + "\n".join(new_entries) + "\n"

content = content.replace("</urlset>", new_block + "\n</urlset>")

# Now bump ALL audio/ page priorities to 1.0
import re
# Match any <url> block containing /audio/ and replace its priority
def bump_audio_priority(match):
    block = match.group(0)
    if '/audio/' in block:
        block = re.sub(r'<priority>[^<]+</priority>', '<priority>1.0</priority>', block)
        block = re.sub(r'<lastmod>[^<]+</lastmod>', '<lastmod>2026-10-04</lastmod>', block)
    return block

content = re.sub(r'<url>.*?</url>', bump_audio_priority, content, flags=re.DOTALL)

with open(sitemap_path, 'w') as f:
    f.write(content)

# Count total URLs in final sitemap
total_urls = content.count('<url>')
print(f"\nFinal sitemap has {total_urls} total URLs.")
print("Done!")
