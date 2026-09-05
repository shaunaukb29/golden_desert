import glob
import json

# Get all html files
os_files = glob.glob('audio/src/cardiag/web/static/*.html')
slugs = [f.split('/')[-1].replace('.html', '') for f in os_files]

# Update vercel.json
with open('vercel.json', 'r') as f:
    vercel = json.load(f)

existing_sources = {r['source'] for r in vercel.get('rewrites', [])}

for slug in slugs:
    source = f"/audio/{slug}"
    if source not in existing_sources:
        vercel['rewrites'].insert(0, {
            "source": source,
            "destination": f"/audio/src/cardiag/web/static/{slug}"
        })

with open('vercel.json', 'w') as f:
    json.dump(vercel, f, indent=2)

# Update sitemap_v4.xml
with open('sitemap_v4.xml', 'r') as f:
    sitemap = f.read()

# Insert before </urlset>
insert_pos = sitemap.rfind('</urlset>')

urls_to_add = ""
for slug in slugs:
    url = f"https://carithm.vercel.app/audio/{slug}"
    if url not in sitemap:
        urls_to_add += f"""
  <url>
    <loc>{url}</loc>
    <lastmod>2026-09-05</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""

sitemap = sitemap[:insert_pos] + urls_to_add + sitemap[insert_pos:]

with open('sitemap_v4.xml', 'w') as f:
    f.write(sitemap)

print("Updated configurations.")
