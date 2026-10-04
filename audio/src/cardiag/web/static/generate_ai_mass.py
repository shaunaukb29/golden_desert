import os
import re

# Top 50 cars in the US (Sales & Popularity)
cars = [
    "Ford F-150", "Chevrolet Silverado", "Ram 1500", "Toyota RAV4", 
    "Tesla Model Y", "Honda CR-V", "Toyota Camry", "GMC Sierra", 
    "Nissan Rogue", "Jeep Grand Cherokee", "Toyota Corolla", "Honda Civic",
    "Subaru Outback", "Hyundai Tucson", "Ford Explorer", "Nissan Altima",
    "Chevrolet Equinox", "Subaru Crosstrek", "Honda Accord", "Jeep Wrangler",
    "Hyundai Elantra", "Kia Sportage", "Ford Escape", "Mazda CX-5",
    "Toyota Tacoma", "Toyota Highlander", "Subaru Forester", "Volkswagen Tiguan",
    "Kia Forte", "Jeep Compass", "Nissan Sentra", "Chevrolet Traverse",
    "Hyundai Santa Fe", "Nissan Frontier", "Ford Bronco", "Dodge Charger",
    "Kia Telluride", "Honda Pilot", "Chevrolet Malibu", "Chevrolet Colorado",
    "BMW X5", "BMW X3", "Subaru Ascent", "Toyota Tundra", "Honda HR-V",
    "Lexus RX", "Hyundai Palisade", "Mercedes-Benz GLE", "Tesla Model 3"
]

noises = [
    "rattling noise", "ticking noise", "squealing noise", 
    "grinding noise", "knocking noise", "whining noise",
    "humming noise", "hissing noise", "clicking noise", "clunking noise"
]

with open('rattling-noise.html', 'r') as f:
    base_html = f.read()

count = 0
sitemap_links = []

for car in cars:
    for noise in noises:
        # e.g. ford-f-150-rattling-noise
        filename = f"{car.lower().replace(' ', '-').replace('.', '')}-{noise.replace(' ', '-')}"
        
        # Don't overwrite if it exists to save time/avoid messing up manually edited ones
        if os.path.exists(f"{filename}.html"):
            continue
            
        html = base_html
        
        # Meta Title
        html = re.sub(
            r'<title>Why Is My Car Making a Rattling Noise\?.*?</title>', 
            f'<title>Why Is My {car} Making a {noise.title()}? Causes + Free AI Diagnosis | Carithm</title>', 
            html
        )
        
        # OG & Twitter Titles
        html = re.sub(
            r'content="Car Making a Rattling Noise\?[^"]*"', 
            f'content="{car} Making a {noise.title()}? Diagnose {noise.split()[0].title()} When Accelerating, Idling & Driving"', 
            html
        )
        
        # Meta Description
        html = re.sub(
            r'<meta name="description" content="Why is your car making a rattling noise[^"]*">',
            f'<meta name="description" content="Why is your {car} making a {noise.lower()}? Upload a recording and our AI engine sound analyzer will identify the exact mechanical fault for free.">',
            html
        )
        
        # H1
        html = re.sub(
            r'<h1>Car Making a Rattling Noise\?.*?</h1>',
            f'<h1>{car} Making a {noise.title()}? Find Out Why It Happens When Accelerating, Idling or Driving</h1>',
            html
        )
        
        # Content replacements
        html = html.replace("Why is your car making a rattling noise", f"Why is your {car} making a {noise.lower()}")
        html = html.replace("car making a rattling noise", f"{car} making a {noise.lower()}")
        html = html.replace("rattling-noise", filename)
        
        # specific string fix
        html = html.replace(f"Why Is My {car} Making a {noise.title()}?", f"Why is my {car} making a {noise.lower()}?")
        
        with open(f"{filename}.html", "w") as f:
            f.write(html)
        count += 1
        sitemap_links.append(f"  <url>\n    <loc>https://carithm.vercel.app/{filename}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>")

print(f"Generated {count} new car/symptom pages.")

# Output sitemap links to a file to easily copy-paste
with open('new_sitemap_urls.txt', 'w') as f:
    f.write('\n'.join(sitemap_links))
print("Wrote sitemap XML nodes to new_sitemap_urls.txt")
