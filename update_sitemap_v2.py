import os
import glob

sitemap_path = "/Users/shaunaukbasu/Desktop/golden_desert/sitemap_v4.xml"
static_dir = "/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static"
base_url = "https://carithm.vercel.app/audio"

html_files = glob.glob(os.path.join(static_dir, "*.html"))

with open(sitemap_path, "r") as f:
    sitemap_content = f.read()

urls_to_add = []
for filepath in html_files:
    filename = os.path.basename(filepath)
    if filename in ["index.html"]: continue
    
    url_slug = filename.replace(".html", "")
    full_url = f"{base_url}/{url_slug}"
    
    if f"<loc>{full_url}</loc>" not in sitemap_content:
        urls_to_add.append(full_url)

if urls_to_add:
    new_urls_xml = ""
    for url in urls_to_add:
        new_urls_xml += f"""
  <url>
    <loc>{url}</loc>
    <lastmod>2026-10-08</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>"""
    
    sitemap_content = sitemap_content.replace('</urlset>', f"{new_urls_xml}\n</urlset>")
    
    with open(sitemap_path, "w") as f:
        f.write(sitemap_content)
    
    print(f"Added {len(urls_to_add)} new URLs to sitemap.")
else:
    print("No new URLs to add.")
