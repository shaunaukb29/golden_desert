#!/usr/bin/env python3
"""
Generate car-brand + noise-type specific SEO pages.
Uses rattling-noise.html as template. Content injected BELOW the tool
to protect AdSense RPM. Strong internal links back to core pages.
"""
import os
import re
import html

STATIC_DIR = "/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static"
TEMPLATE = os.path.join(STATIC_DIR, "rattling-noise.html")
BASE_URL = "https://carithm.vercel.app/audio"
PUBLISH_DATE = "2026-10-08"

# Top US cars by sales volume — skip models that already have pages
CARS = [
    # (slug, display_name)
    ("toyota-rav4", "Toyota RAV4"),
    ("tesla-model-y", "Tesla Model Y"),
    ("honda-cr-v", "Honda CR-V"),
    ("ford-f-150", "Ford F-150"),
    ("chevrolet-silverado", "Chevrolet Silverado"),
    ("toyota-camry", "Toyota Camry"),
    ("toyota-corolla", "Toyota Corolla"),
    ("honda-civic", "Honda Civic"),
    ("nissan-rogue", "Nissan Rogue"),
    ("toyota-highlander", "Toyota Highlander"),
    ("toyota-tacoma", "Toyota Tacoma"),
    ("jeep-grand-cherokee", "Jeep Grand Cherokee"),
    ("ford-explorer", "Ford Explorer"),
    ("hyundai-tucson", "Hyundai Tucson"),
    ("subaru-outback", "Subaru Outback"),
    ("gmc-sierra", "GMC Sierra"),
    ("chevrolet-equinox", "Chevrolet Equinox"),
    ("mazda-cx-5", "Mazda CX-5"),
    ("kia-sportage", "Kia Sportage"),
    ("hyundai-santa-fe", "Hyundai Santa Fe"),
    ("ford-bronco", "Ford Bronco"),
    ("chevrolet-trax", "Chevrolet Trax"),
    ("honda-accord", "Honda Accord"),
    ("toyota-tundra", "Toyota Tundra"),
    ("nissan-altima", "Nissan Altima"),
    ("ram-1500", "Ram 1500"),
    ("tesla-model-3", "Tesla Model 3"),
    ("subaru-forester", "Subaru Forester"),
    ("subaru-crosstrek", "Subaru Crosstrek"),
    ("volkswagen-tiguan", "Volkswagen Tiguan"),
    ("jeep-wrangler", "Jeep Wrangler"),
    ("kia-seltos", "Kia Seltos"),
    ("hyundai-elantra", "Hyundai Elantra"),
    ("nissan-sentra", "Nissan Sentra"),
    ("ford-mustang", "Ford Mustang"),
    ("dodge-durango", "Dodge Durango"),
    ("chevrolet-traverse", "Chevrolet Traverse"),
    ("mazda-cx-50", "Mazda CX-50"),
    ("honda-pilot", "Honda Pilot"),
    ("toyota-4runner", "Toyota 4Runner"),
    ("kia-forte", "Kia Forte"),
    ("nissan-pathfinder", "Nissan Pathfinder"),
    ("chevrolet-colorado", "Chevrolet Colorado"),
    ("hyundai-palisade", "Hyundai Palisade"),
    ("dodge-charger", "Dodge Charger"),
    ("buick-encore-gx", "Buick Encore GX"),
    ("ford-escape", "Ford Escape"),
    ("toyota-corolla-cross", "Toyota Corolla Cross"),
    ("lexus-rx", "Lexus RX"),
    ("bmw-3-series", "BMW 3 Series"),
]

NOISES = {
    "rattling": {
        "display": "Rattling",
        "verb": "rattle",
        "causes": "loose heat shields, exhaust hangers, worn engine mounts, or catalytic converter issues",
        "scenarios": "when accelerating, idling, or driving over bumps",
        "urgency": "Medium",
        "faq_q": "Why does my {car} make a rattling noise?",
        "faq_a": "A rattling noise in a {car} is commonly caused by a loose heat shield, worn exhaust hangers, or failing engine mounts. The severity depends on when and where the rattle occurs.",
    },
    "ticking": {
        "display": "Ticking",
        "verb": "tick",
        "causes": "low oil pressure, worn valve lifters, direct fuel injection, or exhaust manifold leaks",
        "scenarios": "at startup, while idling, or under acceleration",
        "urgency": "Medium–High",
        "faq_q": "Why does my {car} make a ticking noise?",
        "faq_a": "A ticking noise in a {car} often points to low oil levels, worn valve lifters, or a minor exhaust leak. Direct injection engines may tick normally, but persistent ticking should be checked.",
    },
    "squealing": {
        "display": "Squealing",
        "verb": "squeal",
        "causes": "a worn serpentine belt, glazed brake pads, a failing power steering pump, or a worn alternator bearing",
        "scenarios": "on cold start, when turning the steering wheel, or when braking",
        "urgency": "Medium",
        "faq_q": "Why does my {car} make a squealing noise?",
        "faq_a": "A squealing noise from a {car} is most often caused by a worn or slipping serpentine belt, especially on cold starts. Brake squealing may indicate worn pads that need replacement.",
    },
    "grinding": {
        "display": "Grinding",
        "verb": "grind",
        "causes": "worn brake pads, failing wheel bearings, transmission issues, or a damaged CV joint",
        "scenarios": "when braking, turning, or shifting gears",
        "urgency": "High",
        "faq_q": "Why does my {car} make a grinding noise?",
        "faq_a": "Grinding in a {car} is a serious sound that often indicates metal-on-metal contact from worn brake pads, a failing wheel bearing, or transmission damage. This should be inspected promptly.",
    },
    "knocking": {
        "display": "Knocking",
        "verb": "knock",
        "causes": "engine detonation (pre-ignition), worn rod bearings, low-quality fuel, or carbon buildup",
        "scenarios": "during acceleration, under load, or at high RPM",
        "urgency": "High",
        "faq_q": "Why does my {car} make a knocking noise?",
        "faq_a": "A knocking noise in a {car} can be caused by engine detonation from low-octane fuel, worn rod bearings, or significant carbon buildup. Persistent knocking under load should be diagnosed immediately.",
    },
    "whining": {
        "display": "Whining",
        "verb": "whine",
        "causes": "a failing power steering pump, low transmission fluid, a worn alternator bearing, or differential issues",
        "scenarios": "when turning, accelerating, or at certain speeds",
        "urgency": "Medium",
        "faq_q": "Why does my {car} make a whining noise?",
        "faq_a": "A whining noise from a {car} often indicates a power steering pump issue, low transmission fluid, or a worn alternator bearing. The pitch and speed-dependence help identify the source.",
    },
    "humming": {
        "display": "Humming",
        "verb": "hum",
        "causes": "worn wheel bearings, uneven tire wear, transmission problems, or a failing differential",
        "scenarios": "at highway speeds, when turning, or at a constant speed",
        "urgency": "Medium",
        "faq_q": "Why does my {car} make a humming noise?",
        "faq_a": "A humming noise in a {car} that changes with speed usually points to a worn wheel bearing or uneven tire wear. If it changes pitch when turning, a wheel bearing is the most likely cause.",
    },
    "hissing": {
        "display": "Hissing",
        "verb": "hiss",
        "causes": "a coolant leak, a vacuum hose leak, an overheating radiator cap, or a failing AC system",
        "scenarios": "after shutting off the engine, while idling, or from under the hood",
        "urgency": "Medium–High",
        "faq_q": "Why does my {car} make a hissing noise?",
        "faq_a": "A hissing sound from a {car} can indicate a coolant or vacuum leak, an overheating cooling system, or an AC refrigerant leak. Any hissing from under the hood should be checked to prevent overheating.",
    },
    "clicking": {
        "display": "Clicking",
        "verb": "click",
        "causes": "worn CV joints, low engine oil, a failing starter, or loose valve lifters",
        "scenarios": "when turning, at startup, or while driving at low speed",
        "urgency": "Medium",
        "faq_q": "Why does my {car} make a clicking noise?",
        "faq_a": "A clicking noise in a {car}, especially when turning, is commonly caused by a worn CV joint. Clicking at startup may indicate low oil or a starter issue.",
    },
    "clunking": {
        "display": "Clunking",
        "verb": "clunk",
        "causes": "worn ball joints, bad strut mounts, loose sway bar end links, or worn control arm bushings",
        "scenarios": "over bumps, potholes, speed bumps, or when turning",
        "urgency": "Medium–High",
        "faq_q": "Why does my {car} make a clunking noise?",
        "faq_a": "A clunking noise from a {car} when going over bumps usually indicates worn suspension components like ball joints, strut mounts, or sway bar end links. These are safety-critical and should be inspected.",
    },
}

# Load template
with open(TEMPLATE, "r") as f:
    template_html = f.read()

created = 0
skipped = 0

for car_slug, car_name in CARS:
    for noise_key, noise in NOISES.items():
        filename = f"{car_slug}-{noise_key}-noise.html"
        filepath = os.path.join(STATIC_DIR, filename)

        # Skip if already exists
        if os.path.exists(filepath):
            skipped += 1
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

        # Build page from template
        page = template_html

        # Replace title
        page = re.sub(r"<title>[^<]+</title>", f"<title>{html.escape(title)}</title>", page)

        # Replace meta description
        page = re.sub(
            r'<meta name="description" content="[^"]+"',
            f'<meta name="description" content="{html.escape(meta_desc)}"',
            page,
        )

        # Replace canonical
        page = re.sub(
            r'<link rel="canonical" href="[^"]+"',
            f'<link rel="canonical" href="{page_url}"',
            page,
        )

        # Replace OG tags
        page = re.sub(r'<meta property="og:title" content="[^"]+"', f'<meta property="og:title" content="{html.escape(og_title)}"', page)
        page = re.sub(r'<meta property="og:description" content="[^"]+"', f'<meta property="og:description" content="{html.escape(og_desc)}"', page)
        page = re.sub(r'<meta property="og:url" content="[^"]+"', f'<meta property="og:url" content="{page_url}"', page)
        page = re.sub(r'<meta property="og:image:alt" content="[^"]+"', f'<meta property="og:image:alt" content="{html.escape(og_alt)}"', page)

        # Replace Twitter tags
        page = re.sub(r'<meta name="twitter:title" content="[^"]+"', f'<meta name="twitter:title" content="{html.escape(og_title)}"', page)
        page = re.sub(r'<meta name="twitter:description" content="[^"]+"', f'<meta name="twitter:description" content="{html.escape(og_desc)}"', page)

        # Replace H1
        page = re.sub(r"<h1>[^<]+</h1>", f"<h1>{html.escape(h1)}</h1>", page)

        # Replace lead paragraph
        lead_text = (
            f'<strong>Short answer:</strong> if your {car_name} is making a {noise_lower} noise, '
            f"it's most commonly caused by {noise['causes']}. "
            f"This sound typically appears {noise['scenarios']}. "
            f'Record the sound below and let Carithm AI analyze the noise pattern, or head to the '
            f'<a href="https://carithm.vercel.app/audio">full Carithm audio diagnosis hub</a> '
            f"if your {car_name} is making a different noise entirely."
        )
        page = re.sub(r'<p class="lead">.*?</p>', f'<p class="lead">\n    {lead_text}\n  </p>', page, flags=re.DOTALL)

        # Replace schema dates
        page = re.sub(r'"datePublished": "[^"]+"', f'"datePublished": "{PUBLISH_DATE}"', page)
        page = re.sub(r'"dateModified": "[^"]+"', f'"dateModified": "{PUBLISH_DATE}"', page)

        # Replace schema URLs
        page = page.replace("https://carithm.vercel.app/audio/rattling-noise", page_url)

        # Replace schema headline
        page = re.sub(r'"headline": "[^"]+"', f'"headline": "{html.escape(og_title)}"', page)

        # Replace schema app name
        page = re.sub(
            r'"name": "Carithm Car Sound Diagnostic App - [^"]+"',
            f'"name": "Carithm Car Sound Diagnostic App - {car_name} {noise_display} Noise"',
            page,
        )

        # Replace schema app description
        page = re.sub(
            r'"description": "App to help identify[^"]+"',
            f'"description": "App to help identify possible causes of {noise_lower} noises in a {car_name} by analyzing uploaded audio."',
            page,
        )

        # Replace breadcrumb last item
        page = re.sub(
            r'"position": 3, "name": "[^"]+"',
            f'"position": 3, "name": "{html.escape(breadcrumb_name)}"',
            page,
        )
        page = re.sub(
            r'<span class="current">[^<]+</span>',
            f'<span class="current">{html.escape(breadcrumb_name)}</span>',
            page,
        )

        # Replace eyebrow
        page = re.sub(
            r'<div class="eyebrow">[^<]+</div>',
            f'<div class="eyebrow">{html.escape(car_name).upper()} NOISE DIAGNOSIS</div>',
            page,
        )

        # Replace byline date
        page = re.sub(
            r'Updated <time datetime="[^"]+">.*?</time>',
            f'Updated <time datetime="{PUBLISH_DATE}">October 8, 2026</time>',
            page,
        )

        # Replace upload section title
        page = re.sub(
            r'🔊 Upload Your Car Rattling Sound',
            f'🔊 Upload Your {car_name} {noise_display} Sound',
            page,
        )

        # Replace upload description
        page = re.sub(
            r'<p>Record the rattling noise while your car is making it\.[^<]+</p>',
            f'<p>Record the {noise_lower} noise while your {car_name} is making it. AI sound analysis can help narrow down the source and possible cause.</p>',
            page,
        )

        # Add publish date meta tag and internal links block before </body>
        internal_links_block = f"""
<meta property="article:published_time" content="{PUBLISH_DATE}T08:00:00+00:00" />
<meta property="article:modified_time" content="{PUBLISH_DATE}T08:00:00+00:00" />

<!-- Internal Links Block -->
<div style="max-width: 760px; margin: 40px auto; padding: 20px; background: #18181b; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
    <h3 style="margin-top: 0; color: #fff;">More Free Car Diagnosis Tools</h3>
    <p style="color: #a1a1aa; font-size: 0.9em;">Published: <time datetime="{PUBLISH_DATE}">October 8, 2026</time></p>
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

print(f"Created {created} new pages, skipped {skipped} existing pages.")
print(f"Total pages now: {created + skipped + 171}")
