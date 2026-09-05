import os

# Specific symptom-based targets from the search console data
targets = [
    # Component based
    ("Heat Shield", "Rattling Noise", "heat-shield-rattling-noise"),
    ("Exhaust", "Rattling At Idle", "exhaust-rattling-at-idle"),
    ("Muffler", "Rattling When Accelerating", "muffler-rattling-when-accelerating"),
    ("Lifter", "Tick Sound", "lifter-tick-sound"),
    ("Valvetrain", "Tick", "valvetrain-tick-noise"),
    ("Direct Injection", "Ticking Noise", "direct-injection-ticking-noise"),
    
    # Condition based
    ("Car", "Rattling Noise When Driving Slow", "car-making-rattling-noise-when-driving-slow"),
    ("Engine", "Rattling When Idle", "engine-rattling-when-idle"),
    ("Car", "Rattling Noise Underneath", "rattling-noise-underneath-car"),
    ("Engine", "Rattling Noise When Accelerating", "engine-rattling-noise-when-accelerating"),
    ("Engine", "Tick at Idle", "engine-tick-at-idle"),
    ("Car", "High Pitched Ticking", "high-pitched-ticking-noise"),
    ("Car", "Metallic Rattle", "metallic-rattle-noise")
]

with open('rattling-noise.html', 'r') as f:
    base_html = f.read()

for component, noise, filename in targets:
    html = base_html
    
    # Generic replacement
    html = html.replace("<title>Why Is My Car Making a Rattling Noise?", f"<title>{component} {noise.title()}? Free AI Diagnosis")
    html = html.replace("Why is your car making a rattling noise", f"Is your {component.lower()} making a {noise.lower()}")
    html = html.replace("Car Making a Rattling Noise?", f"{component} {noise.title()}?")
    html = html.replace("car making a rattling noise", f"{component.lower()} making a {noise.lower()}")
    html = html.replace("rattling-noise", filename)
    
    with open(f"{filename}.html", "w") as f:
        f.write(html)
        
print("Generated symptom pages.")
