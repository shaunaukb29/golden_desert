import os
from jinja2 import Template

# 30 Specific High-Intent Vehicle Targets
vehicles = [
    {
        "slug": "2014-honda-civic-squealing-noise",
        "year": "2014",
        "make": "Honda",
        "model": "Civic",
        "page_title": "2014 Honda Civic Squealing Noise — AI Audio Diagnosis | Carithm",
        "meta_description": "Is your 2014 Honda Civic making a squealing noise when turning on the AC or accelerating? Record your audio and let Carithm AI diagnose belt and pulley faults instantly.",
        "h1_title": "2014 Honda Civic Squealing Noise? Upload Your Sound for AI Diagnosis",
        "common_issue_summary": "worn serpentine belts, AC compressor clutch slip, or failing tensioner pulleys",
        "vehicle_specific_diagnosis": "In the 2014 Honda Civic, squealing when the AC turns on is frequently tied to the AC compressor clutch or an aging serpentine belt that loses grip under high torque load."
    },
    {
        "slug": "2015-honda-accord-squealing-noise",
        "year": "2015",
        "make": "Honda",
        "model": "Accord",
        "page_title": "2015 Honda Accord Cold Start Squeal — AI Diagnosis | Carithm",
        "meta_description": "Does your 2015 Honda Accord squeal on cold starts? Diagnose VTC actuator noise, belt slip, and alternator pulley wear using AI sound analysis.",
        "h1_title": "2015 Honda Accord Squealing Noise? Diagnose the Cause with AI",
        "common_issue_summary": "VTC actuator rattle, serpentine belt tensioner wear, or alternator bearing whine",
        "vehicle_specific_diagnosis": "2015 Accord owners often report a brief 1-2 second squeal or rattle during cold morning starts, usually caused by a sticking VTC actuator or a loose serpentine belt."
    },
    {
        "slug": "2013-ford-f150-squealing-noise",
        "year": "2013",
        "make": "Ford",
        "model": "F-150",
        "page_title": "2013 Ford F-150 Squealing Engine Noise — AI Sound Check | Carithm",
        "meta_description": "Diagnose 2013 Ford F-150 squealing noise under acceleration or idling. Upload engine audio for instant AI feedback on belts, pulleys, and water pumps.",
        "h1_title": "2013 Ford F-150 Squealing Noise? Check Your Belt & Pulleys With AI",
        "common_issue_summary": "EcoBoost primary belt slippage, idler pulley bearing wear, or water pump seal squeal",
        "vehicle_specific_diagnosis": "The 2013 F-150 (especially EcoBoost 3.5L models) is prone to idler pulley bearing degradation, leading to a high-pitched metallic squeal that tracks with engine RPM."
    },
    {
        "slug": "2012-toyota-camry-squealing-noise",
        "year": "2012",
        "make": "Toyota",
        "model": "Camry",
        "page_title": "2012 Toyota Camry Squealing Noise — Free AI Audio Diagnosis | Carithm",
        "meta_description": "2012 Toyota Camry squealing when starting or accelerating? Upload audio to detect alternator pulley wear, worn drive belts, or brake wear indicators.",
        "h1_title": "2012 Toyota Camry Squealing Noise? Find the Cause With AI",
        "common_issue_summary": "degraded drive belt, alternator decoupler pulley, or brake pad wear indicators",
        "vehicle_specific_diagnosis": "The 2012 Camry commonly develops drive belt chirp on damp mornings due to worn rubber compound, or an alternator clutch pulley failing."
    },
    {
        "slug": "2015-nissan-altima-squealing-noise",
        "year": "2015",
        "make": "Nissan",
        "model": "Altima",
        "page_title": "2015 Nissan Altima Squealing & Whining Noise — AI Diagnosis | Carithm",
        "meta_description": "Is your 2015 Nissan Altima squealing or whining during acceleration? Test your audio to differentiate between CVT transmission noise and belt slip.",
        "h1_title": "2015 Nissan Altima Squealing Noise? Upload Audio to Diagnose",
        "common_issue_summary": "CVT belt whine, serpentine belt tensioner fatigue, or power steering pump noise",
        "vehicle_specific_diagnosis": "It is critical on 2015 Altimas to distinguish between accessory belt squeal (fixable under $200) and CVT transmission belt whine. AI audio pattern analysis pinpoints the exact frequency."
    }
    # [Expand list with remaining 25 targets from Step 1 table]
]

# Create output folder
os.makedirs("output", exist_ok=True)

# Read HTML Jinja2 template
with open("template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

template = Template(template_content)

# Render all 30 HTML files
for v in vehicles:
    rendered_html = template.render(v)
    file_path = os.path.join("output", f"{v['slug']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)
    print(f"Generated: {file_path}")

print("Successfully generated all programmatic pages!")
