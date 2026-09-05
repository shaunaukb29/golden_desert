import os

cars = [
    "Ford F-150", "Chevrolet Silverado", "Ram 1500", "Toyota RAV4", 
    "Tesla Model Y", "Honda CR-V", "Toyota Camry", "GMC Sierra", 
    "Nissan Rogue", "Jeep Grand Cherokee", "Toyota Corolla", "Honda Civic",
    "Subaru Outback", "Hyundai Tucson", "Ford Explorer", "Nissan Altima"
]

noises = [
    "rattling noise", "ticking noise", "squealing noise", 
    "grinding noise", "knocking noise", "whining noise"
]

with open('rattling-noise.html', 'r') as f:
    base_html = f.read()

count = 0
for car in cars:
    for noise in noises:
        filename = f"{car.lower().replace(' ', '-').replace('.', '')}-{noise.replace(' ', '-')}"
        
        # Check if already exists
        if os.path.exists(f"{filename}.html"):
            continue
            
        html = base_html
        
        # Generic replacement
        html = html.replace("<title>Why Is My Car Making a Rattling Noise?", f"<title>Why Is My {car} Making a {noise.title()}? Free AI Diagnosis")
        html = html.replace("Why is your car making a rattling noise", f"Why is your {car} making a {noise.lower()}")
        html = html.replace("Car Making a Rattling Noise?", f"{car} Making a {noise.title()}?")
        html = html.replace("car making a rattling noise", f"{car} making a {noise.lower()}")
        html = html.replace("rattling-noise", filename)
        
        with open(f"{filename}.html", "w") as f:
            f.write(html)
        count += 1
        
print(f"Generated {count} mass car pages.")
