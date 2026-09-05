import glob
import os

# Get all html files in static dir
files = glob.glob('audio/src/cardiag/web/static/*.html')
slugs = sorted([os.path.basename(f).replace('.html', '') for f in files if os.path.basename(f) != 'app.html' and os.path.basename(f) != 'landing.html'])

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>All Supported Vehicles & Noises | Carithm</title>
<meta name="description" content="Browse our complete directory of supported vehicles and specific car noises for free AI diagnosis.">
<link rel="canonical" href="https://carithm.vercel.app/audio/all-models">
<style>
  body { font-family: system-ui, sans-serif; background: #0c0d0e; color: #f5f4f2; line-height: 1.6; padding: 40px; max-width: 900px; margin: 0 auto; }
  a { color: #2f81f7; text-decoration: none; }
  a:hover { text-decoration: underline; }
  h1 { font-size: 2rem; margin-bottom: 20px; }
  ul { columns: 2; list-style-type: none; padding: 0; }
  @media (max-width: 600px) { ul { columns: 1; } }
  li { margin-bottom: 8px; }
</style>
</head>
<body>
  <h1>All Supported Vehicles & Noises</h1>
  <p>Select your vehicle and specific symptom to get a free AI-assisted diagnosis.</p>
  <ul>
"""

for slug in slugs:
    title = slug.replace('-', ' ').title()
    html_content += f'    <li><a href="https://carithm.vercel.app/audio/{slug}">{title}</a></li>\n'

html_content += """
  </ul>
  <div style="margin-top: 40px;">
    <a href="https://carithm.vercel.app/">&larr; Back to Home</a>
  </div>
</body>
</html>
"""

with open('audio/src/cardiag/web/static/all-models.html', 'w') as f:
    f.write(html_content)

print("Directory page created.")
