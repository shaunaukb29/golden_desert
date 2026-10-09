#!/usr/bin/env python3
"""
Randomly assign one of 3 Streamlit app URLs to each car-model-sound page.
Only targets car-specific pages (brand-model-noise pattern), not generic topic pages.
"""
import os
import re
import random
import glob

STATIC_DIR = "/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static"

STREAMLIT_URLS = [
    "https://hadi10973-nmanvbz9onaxzbwzdmnjku.streamlit.app/",
    "https://heidi23982-5vovybvpxghzdhuduaairo.streamlit.app/",
    "https://heimi34505-3aue9zwjqykkgwxjwnemcy.streamlit.app/",
]

# Pattern to match car-model-noise files (e.g. toyota-rav4-rattling-noise.html)
# These have at least 3 hyphens and end with -noise.html
# Exclude generic pages like rattling-noise.html, squealing-noise.html, app.html, ac.html, all-models.html, etc.
CAR_PAGE_PATTERN = re.compile(
    r"^(?!rattling-noise|squealing-noise|grinding-noise|knocking-noise|ticking-noise|"
    r"whining-noise|humming-noise|hissing-noise|clicking-noise|clunking-noise|"
    r"popping-noise|sputtering-noise|scraping-noise|roaring-noise|tapping-noise|"
    r"whistling-noise|whooshing-noise|groaning-noise|app|ac|all-models|free-ai|"
    r"can-chatgpt|ai-|car-|engine-|what-|why-|how-|is-my|my-car|shazam|drive-|"
    r"noise-|diagnos|direct-|exhaust-|heat-|high-)"
    r".+-noise\.html$"
)

html_files = glob.glob(os.path.join(STATIC_DIR, "*.html"))

# The old Streamlit URL pattern in the iframe src
OLD_SRC_PATTERN = re.compile(
    r'src="https://[^"]*\.streamlit\.app/[^"]*"'
)

updated = 0
distribution = {url: 0 for url in STREAMLIT_URLS}

random.seed(42)  # Reproducible randomness

for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    
    if not CAR_PAGE_PATTERN.match(filename):
        continue
    
    with open(filepath, "r") as f:
        content = f.read()
    
    # Pick a random URL
    chosen_url = random.choice(STREAMLIT_URLS)
    new_src = f'src="{chosen_url}?embed=true"'
    
    # Replace the streamlit iframe src
    new_content = OLD_SRC_PATTERN.sub(new_src, content)
    
    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
        updated += 1
        distribution[chosen_url] += 1

print(f"Updated {updated} car-model-sound pages with randomized Streamlit URLs.")
print(f"\nDistribution:")
for url, count in distribution.items():
    short = url.split("//")[1].split("-")[0]
    print(f"  {short}...: {count} pages")
