#!/usr/bin/env python3
import os
import re
import html

STATIC_DIR = "/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static"
TEMPLATE = os.path.join(STATIC_DIR, "rattling-noise.html")
BASE_URL = "https://carithm.vercel.app/audio"
PUBLISH_DATE = "2026-10-09"

# Top 50 US cars
CARS = [
    ("toyota-rav4", "Toyota RAV4"), ("tesla-model-y", "Tesla Model Y"), ("honda-cr-v", "Honda CR-V"),
    ("ford-f-150", "Ford F-150"), ("chevrolet-silverado", "Chevrolet Silverado"), ("toyota-camry", "Toyota Camry"),
    ("toyota-corolla", "Toyota Corolla"), ("honda-civic", "Honda Civic"), ("nissan-rogue", "Nissan Rogue"),
    ("toyota-highlander", "Toyota Highlander"), ("toyota-tacoma", "Toyota Tacoma"), ("jeep-grand-cherokee", "Jeep Grand Cherokee"),
    ("ford-explorer", "Ford Explorer"), ("hyundai-tucson", "Hyundai Tucson"), ("subaru-outback", "Subaru Outback"),
    ("gmc-sierra", "GMC Sierra"), ("chevrolet-equinox", "Chevrolet Equinox"), ("mazda-cx-5", "Mazda CX-5"),
    ("kia-sportage", "Kia Sportage"), ("hyundai-santa-fe", "Hyundai Santa Fe"), ("ford-bronco", "Ford Bronco"),
    ("chevrolet-trax", "Chevrolet Trax"), ("honda-accord", "Honda Accord"), ("toyota-tundra", "Toyota Tundra"),
    ("nissan-altima", "Nissan Altima"), ("ram-1500", "Ram 1500"), ("tesla-model-3", "Tesla Model 3"),
    ("subaru-forester", "Subaru Forester"), ("subaru-crosstrek", "Subaru Crosstrek"), ("volkswagen-tiguan", "Volkswagen Tiguan"),
    ("jeep-wrangler", "Jeep Wrangler"), ("kia-seltos", "Kia Seltos"), ("hyundai-elantra", "Hyundai Elantra"),
    ("nissan-sentra", "Nissan Sentra"), ("ford-mustang", "Ford Mustang"), ("dodge-durango", "Dodge Durango"),
    ("chevrolet-traverse", "Chevrolet Traverse"), ("mazda-cx-50", "Mazda CX-50"), ("honda-pilot", "Honda Pilot"),
    ("toyota-4runner", "Toyota 4Runner"), ("kia-forte", "Kia Forte"), ("nissan-pathfinder", "Nissan Pathfinder"),
    ("chevrolet-colorado", "Chevrolet Colorado"), ("hyundai-palisade", "Hyundai Palisade"), ("dodge-charger", "Dodge Charger"),
    ("buick-encore-gx", "Buick Encore GX"), ("ford-escape", "Ford Escape"), ("toyota-corolla-cross", "Toyota Corolla Cross"),
    ("lexus-rx", "Lexus RX"), ("bmw-3-series", "BMW 3 Series"),
]

# 8 NEW noise types
NOISES = {
    "popping": {
        "display": "Popping", "verb": "pop",
        "causes": "exhaust leaks, unburned fuel igniting in the exhaust, worn CV joints, or suspension issues",
        "scenarios": "when accelerating, decelerating, or turning sharply", "urgency": "Medium"
    },
    "sputtering": {
        "display": "Sputtering", "verb": "sputter",
        "causes": "exhaust manifold leaks, failing spark plugs, clogged fuel injectors, or a bad mass airflow sensor",
        "scenarios": "when accelerating or idling roughly", "urgency": "Medium-High"
    },
    "scraping": {
        "display": "Scraping", "verb": "scrape",
        "causes": "worn brake pads grinding against rotors, a dragging dust shield, or a loose undercarriage panel",
        "scenarios": "while driving at low speeds or applying the brakes", "urgency": "High"
    },
    "roaring": {
        "display": "Roaring", "verb": "roar",
        "causes": "a damaged exhaust system, worn wheel bearings, or a failing transmission",
        "scenarios": "when accelerating heavily or driving at highway speeds", "urgency": "High"
    },
    "tapping": {
        "display": "Tapping", "verb": "tap",
        "causes": "low engine oil, worn valve lifters, or exhaust manifold leaks",
        "scenarios": "when starting the engine cold or idling", "urgency": "Medium"
    },
    "whistling": {
        "display": "Whistling", "verb": "whistle",
        "causes": "vacuum leaks, window seal gaps, or a failing turbocharger",
        "scenarios": "while accelerating or driving at highway speeds", "urgency": "Medium"
    },
    "whooshing": {
        "display": "Whooshing", "verb": "whoosh",
        "causes": "a vacuum leak, HVAC system issues, or a failing brake booster",
        "scenarios": "when pressing the brake pedal or accelerating", "urgency": "Medium"
    },
    "groaning": {
        "display": "Groaning", "verb": "groan",
        "causes": "low power steering fluid, a failing power steering pump, or worn suspension bushings",
        "scenarios": "when turning the steering wheel or driving over bumps", "urgency": "Medium-High"
    }
}

with open(TEMPLATE, "r") as f:
    template_html = f.read()

created = 0

for car_slug, car_name in CARS:
    for noise_key, noise in NOISES.items():
        filename = f"{car_slug}-{noise_key}-noise.html"
        filepath = os.path.join(STATIC_DIR, filename)

        if os.path.exists(filepath):
            continue

        page_slug = filename.replace(".html", "")
        page_url = f"{BASE_URL}/{page_slug}"
        noise_display = noise["display"]
        noise_lower = noise_display.lower()

        title = f"{car_name} {noise_display} Noise? Causes + Free AI Diagnosis | Carithm"
        meta_desc = f"Is your {car_name} making a {noise_lower} noise {noise['scenarios']}? Common causes include {noise['causes']}. Upload your recording for a free AI diagnosis."
        h1 = f"{car_name} Making a {noise_display} Noise? Here's What It Could Mean"
        og_title = f"{car_name} {noise_display} Noise — Diagnose {noise_display} Sound in {car_name}"
        og_desc = f"Upload a recording of your {car_name}'s {noise_lower} noise and get a free AI-assisted analysis of possible causes, urgency, and cost."
        og_alt = f"{car_name} engine bay being inspected for {noise_lower} noise"
        breadcrumb_name = f"{car_name} {noise_display}"

        page = template_html
        page = re.sub(r"<title>[^<]+</title>", f"<title>{html.escape(title)}</title>", page)
        page = re.sub(r'<meta name="description" content="[^"]+"', f'<meta name="description" content="{html.escape(meta_desc)}"', page)
        page = re.sub(r'<link rel="canonical" href="[^"]+"', f'<link rel="canonical" href="{page_url}"', page)
        page = re.sub(r'<meta property="og:title" content="[^"]+"', f'<meta property="og:title" content="{html.escape(og_title)}"', page)
        page = re.sub(r'<meta property="og:description" content="[^"]+"', f'<meta property="og:description" content="{html.escape(og_desc)}"', page)
        page = re.sub(r'<meta property="og:url" content="[^"]+"', f'<meta property="og:url" content="{page_url}"', page)
        page = re.sub(r'<meta property="og:image:alt" content="[^"]+"', f'<meta property="og:image:alt" content="{html.escape(og_alt)}"', page)
        page = re.sub(r'<meta name="twitter:title" content="[^"]+"', f'<meta name="twitter:title" content="{html.escape(og_title)}"', page)
        page = re.sub(r'<meta name="twitter:description" content="[^"]+"', f'<meta name="twitter:description" content="{html.escape(og_desc)}"', page)
        page = re.sub(r"<h1>[^<]+</h1>", f"<h1>{html.escape(h1)}</h1>", page)

        lead_text = (
            f'<strong>Short answer:</strong> if your {car_name} is making a {noise_lower} noise, '
            f"it's most commonly caused by {noise['causes']}. "
            f"This sound typically appears {noise['scenarios']}. "
            f'Record the sound below and let Carithm AI analyze the noise pattern, or head to the '
            f'<a href="https://carithm.vercel.app/audio">full Carithm audio diagnosis hub</a> '
            f"if your {car_name} is making a different noise entirely."
        )
        page = re.sub(r'<p class="lead">.*?</p>', f'<p class="lead">\n    {lead_text}\n  </p>', page, flags=re.DOTALL)
        page = re.sub(r'"datePublished": "[^"]+"', f'"datePublished": "{PUBLISH_DATE}"', page)
        page = re.sub(r'"dateModified": "[^"]+"', f'"dateModified": "{PUBLISH_DATE}"', page)
        page = page.replace("https://carithm.vercel.app/audio/rattling-noise", page_url)
        page = re.sub(r'"headline": "[^"]+"', f'"headline": "{html.escape(og_title)}"', page)
        page = re.sub(r'"name": "Carithm Car Sound Diagnostic App - [^"]+"', f'"name": "Carithm Car Sound Diagnostic App - {car_name} {noise_display} Noise"', page)
        page = re.sub(r'"description": "App to help identify[^"]+"', f'"description": "App to help identify possible causes of {noise_lower} noises in a {car_name} by analyzing uploaded audio."', page)
        page = re.sub(r'"position": 3, "name": "[^"]+"', f'"position": 3, "name": "{html.escape(breadcrumb_name)}"', page)
        page = re.sub(r'<span class="current">[^<]+</span>', f'<span class="current">{html.escape(breadcrumb_name)}</span>', page)
        page = re.sub(r'<div class="eyebrow">[^<]+</div>', f'<div class="eyebrow">{html.escape(car_name).upper()} NOISE DIAGNOSIS</div>', page)
        page = re.sub(r'Updated <time datetime="[^"]+">.*?</time>', f'Updated <time datetime="{PUBLISH_DATE}">October 9, 2026</time>', page)
        page = re.sub(r'🔊 Upload Your Car Rattling Sound', f'🔊 Upload Your {car_name} {noise_display} Sound', page)
        page = re.sub(r'<p>Record the rattling noise while your car is making it\.[^<]+</p>', f'<p>Record the {noise_lower} noise while your {car_name} is making it. AI sound analysis can help narrow down the source and possible cause.</p>', page)

        internal_links_block = f"""
<meta property="article:published_time" content="{PUBLISH_DATE}T08:00:00+00:00" />
<meta property="article:modified_time" content="{PUBLISH_DATE}T08:00:00+00:00" />

<!-- Internal Links Block -->
<div style="max-width: 760px; margin: 40px auto; padding: 20px; background: #18181b; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
    <h3 style="margin-top: 0; color: #fff;">More Free Car Diagnosis Tools</h3>
    <p style="color: #a1a1aa; font-size: 0.9em;">Published: <time datetime="{PUBLISH_DATE}">October 9, 2026</time></p>
    <p style="color: #d4d4d8;">Need a broader analysis? Try our main AI tools:</p>
    <ul style="line-height: 1.8;">
        <li><strong><a href="https://carithm.vercel.app/" style="color: #60a5fa; text-decoration: none;">Carithm AI — Free Engine Noise Identifier</a></strong></li>
        <li><strong><a href="https://carithm.vercel.app/audio" style="color: #60a5fa; text-decoration: none;">Car Sound Diagnosis App — Upload Any Recording</a></strong></li>
        <li><strong><a href="https://carithm.vercel.app/app" style="color: #60a5fa; text-decoration: none;">Engine Noise Analysis App — No Download Required</a></strong></li>
    </ul>
</div>
"""
        page = page.replace("</body>", f"{internal_links_block}\n</body>")

        with open(filepath, "w") as f:
            f.write(page)
        created += 1

print(f"Successfully generated {created} NEW pages.")
