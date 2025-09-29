import os
import requests
import re
from pathlib import Path
from dotenv import load_dotenv

# Load API key
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/your-username/your-model"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

# --- Helpers ---
def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def query_model(prompt):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    return response.json()[0]['generated_text'] if isinstance(response.json(), list) else str(response.json())

def build_html(query, answer):
    slug = slugify(query)
    meta_desc = (answer[:150] + "...") if len(answer) > 150 else answer
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>{query} | Carithm AI Diagnosis</title>
  <meta name="description" content="{meta_desc}" />
  <link rel="canonical" href="https://carithm.vercel.app/examples/{slug}.html" />
</head>
<body>
  <h1>{query}</h1>
  <h2>Carithm AI Diagnosis</h2>
  <p>{answer}</p>
</body>
</html>""", slug

# --- Main ---
def main():
    Path("examples").mkdir(exist_ok=True)
    with open("queries.txt") as f:
        queries = [line.strip() for line in f if line.strip()]

    sitemap_entries = []
    for q in queries:
        print(f"Generating page for: {q}")
        answer = query_model(q)
        html, slug = build_html(q, answer)

        out_file = Path("examples") / f"{slug}.html"
        out_file.write_text(html, encoding="utf-8")

        sitemap_entries.append(f"<url><loc>https://carithm.vercel.app/examples/{slug}.html</loc></url>")

    # update sitemap.xml
    sitemap = "<?xml version='1.0' encoding='UTF-8'?>\n<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>\n"
    sitemap += "\n".join(sitemap_entries)
    sitemap += "\n</urlset>"
    Path("public/sitemap.xml").write_text(sitemap, encoding="utf-8")

if __name__ == "__main__":
    main()
