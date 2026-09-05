import os
import glob
import re
import shutil

# Target cars and noises from the search console data
targets = [
    ("Honda Odyssey", "wheel bearing noise", "honda-odyssey-wheel-bearing-noise"),
    ("Ford Fiesta", "rattling noise when accelerating", "ford-fiesta-rattling-noise-when-accelerating"),
    ("Jeep Compass", "rattling noise", "jeep-compass-rattling-noise"),
    ("Nissan Altima", "humming noise when accelerating", "nissan-altima-humming-noise-when-accelerating"),
    ("Renault Kwid", "rattling noise", "renault-kwid-rattling-noise"),
    ("VW Caddy", "rattling noise", "vw-caddy-rattling-noise"),
    ("Audi A8", "rattling noise", "audi-a8-rattling-noise"),
    ("Toyota Camry", "ticking noise", "toyota-camry-ticking-noise"),
    ("Honda Civic", "rattling at idle", "honda-civic-rattling-at-idle"),
    ("Fiat Egea", "ticking noise", "fiat-egea-ticking-noise")
]

# We will use rattling-noise.html as a base template because it is well-formatted and generic
with open('rattling-noise.html', 'r') as f:
    base_html = f.read()

for car, noise, filename in targets:
    html = base_html
    
    # Simple replace to make the page specific
    html = html.replace("<title>Why Is My Car Making a Rattling Noise?", f"<title>Why Is My {car} Making a {noise.title()}?")
    html = html.replace("Why is your car making a rattling noise", f"Why is your {car} making a {noise}")
    html = html.replace("Car Making a Rattling Noise?", f"{car} Making a {noise.title()}?")
    html = html.replace("car making a rattling noise", f"{car} making a {noise}")
    html = html.replace("rattling-noise", filename)
    
    with open(f"{filename}.html", "w") as f:
        f.write(html)
        
print("Generated high traffic pages.")
