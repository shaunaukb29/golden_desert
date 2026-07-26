import os

# Set target directory relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(script_dir, "template.html")

# 30 High-Intent Vehicle & Sound Targets
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
        "slug": "2016-honda-crv-squealing-noise",
        "year": "2016",
        "make": "Honda",
        "model": "CR-V",
        "page_title": "2016 Honda CR-V Squealing Noise — AI Audio Diagnosis | Carithm",
        "meta_description": "Is your 2016 Honda CR-V squealing under acceleration or morning start? Test audio to detect belt slippage or tensioner pulley issues.",
        "h1_title": "2016 Honda CR-V Squealing Noise? Find the Source With AI",
        "common_issue_summary": "accessory drive belt slip, belt tensioner misalignment, or alternator pulley wear",
        "vehicle_specific_diagnosis": "High-pitched squealing under acceleration in the 2016 CR-V typically points toward accessory drive belt slippage or a tensioner losing spring tension."
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
        "slug": "2015-toyota-corolla-squealing-noise",
        "year": "2015",
        "make": "Toyota",
        "model": "Corolla",
        "page_title": "2015 Toyota Corolla Cold Start Belt Squeal — AI Check | Carithm",
        "meta_description": "Squealing noise from your 2015 Toyota Corolla engine bay? Upload engine audio for instant AI feedback on water pump bearings and belt tension.",
        "h1_title": "2015 Toyota Corolla Squealing Noise? Upload Engine Audio",
        "common_issue_summary": "water pump bearing failure, serpentine belt glaze, or idler pulley squeak",
        "vehicle_specific_diagnosis": "In 2015 Corollas, persistent engine squealing is frequently caused by early water pump bearing weep/failure or a dry serpentine belt."
    },
    {
        "slug": "2016-toyota-rav4-squealing-noise",
        "year": "2016",
        "make": "Toyota",
        "model": "RAV4",
        "page_title": "2016 Toyota RAV4 Squealing Noise Diagnosis | Carithm",
        "meta_description": "Hear squealing from your 2016 RAV4 when braking or steering? Use AI sound analysis to separate belt noise from brake pad wear indicators.",
        "h1_title": "2016 Toyota RAV4 Squealing Noise? Analyze Engine Audio",
        "common_issue_summary": "serpentine belt slippage, brake indicator wear, or AC clutch pulley drag",
        "vehicle_specific_diagnosis": "Squealing on 2016 RAV4s is commonly traced to drive belt slippage during heavy electrical load or worn front brake pad wear indicators."
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
        "slug": "2016-ford-explorer-squealing-noise",
        "year": "2016",
        "make": "Ford",
        "model": "Explorer",
        "page_title": "2016 Ford Explorer AC Squeal — AI Sound Diagnosis | Carithm",
        "meta_description": "2016 Ford Explorer making a high-pitched squeal when AC turns on? Upload audio to test for AC clutch slip and tensioner failure.",
        "h1_title": "2016 Ford Explorer Squealing Noise? Test Audio with AI",
        "common_issue_summary": "AC compressor clutch slipping, stretch belt wear, or belt tensioner fatigue",
        "vehicle_specific_diagnosis": "2016 Explorers frequently experience high-pitched squeal upon AC compressor activation due to clutch plate slipping or a worn stretch belt."
    },
    {
        "slug": "2014-ford-focus-squealing-noise",
        "year": "2014",
        "make": "Ford",
        "model": "Focus",
        "page_title": "2014 Ford Focus Serpentine Belt Squeal — AI Check | Carithm",
        "meta_description": "Is your 2014 Ford Focus engine squealing or chirping? Upload engine sound to diagnose power steering, belt stretch, and pulley noise.",
        "h1_title": "2014 Ford Focus Squealing Noise? Identify the Fault with AI",
        "common_issue_summary": "serpentine belt stretching, alternator decoupler pulley wear, or idler pulley failure",
        "vehicle_specific_diagnosis": "A loud squeal on acceleration in 2014 Focus models is usually linked to a stretched main serpentine belt or dry idler bearings."
    },
    {
        "slug": "2015-ford-escape-squealing-noise",
        "year": "2015",
        "make": "Ford",
        "model": "Escape",
        "page_title": "2015 Ford Escape Belt Tensioner Squeal — AI Diagnosis | Carithm",
        "meta_description": "2015 Ford Escape squealing on startup or load? Check tensioner pulley and belt slipping frequencies with AI audio analysis.",
        "h1_title": "2015 Ford Escape Squealing Noise? Diagnose Instantly",
        "common_issue_summary": "belt tensioner arm wear, AC belt stretch, or water pump bearing noise",
        "vehicle_specific_diagnosis": "2015 Escapes commonly develop belt squeal due to weak automatic belt tensioners losing tension, causing belt flutter and slippage."
    },
    {
        "slug": "2014-chevrolet-silverado-1500-squealing-noise",
        "year": "2014",
        "make": "Chevrolet",
        "model": "Silverado 1500",
        "page_title": "2014 Chevy Silverado 1500 Squealing Noise — AI Audio Check | Carithm",
        "meta_description": "2014 Chevy Silverado engine squealing under load? Upload recording to test idler pulley wear, main belt glazing, and alternator bearings.",
        "h1_title": "2014 Chevrolet Silverado 1500 Squealing Noise? AI Diagnosis",
        "common_issue_summary": "idler pulley bearing failure, main drive belt glazing, or water pump squeal",
        "vehicle_specific_diagnosis": "The 5.3L V8 in the 2014 Silverado 1500 often suffers from dry upper/lower idler pulley bearings that produce a persistent high-pitched squeal."
    },
    {
        "slug": "2015-chevrolet-equinox-squealing-noise",
        "year": "2015",
        "make": "Chevrolet",
        "model": "Equinox",
        "page_title": "2015 Chevy Equinox High-Pitched Cold Start Squeal — AI Check | Carithm",
        "meta_description": "Does your 2015 Chevrolet Equinox squeal during cold engine starts? Test your sound file to diagnose belt and alternator pulley issues.",
        "h1_title": "2015 Chevrolet Equinox Squealing Noise? Test Audio with AI",
        "common_issue_summary": "serpentine belt alignment, alternator pulley wear, or exhaust heat shield rattle/squeak",
        "vehicle_specific_diagnosis": "Cold start squeal on 2015 Equinox 2.4L models is typical of belt glazing or misaligned alternator pulleys under initial charge load."
    },
    {
        "slug": "2016-chevrolet-malibu-squealing-noise",
        "year": "2016",
        "make": "Chevrolet",
        "model": "Malibu",
        "page_title": "2016 Chevy Malibu Engine Belt Squeal — AI Sound Analysis | Carithm",
        "meta_description": "Squealing engine noise in 2016 Chevy Malibu? Upload audio file for AI pattern detection on drive belts and tensioners.",
        "h1_title": "2016 Chevrolet Malibu Squealing Noise? Upload Your Sound",
        "common_issue_summary": "drive belt tension loss, AC clutch chatter, or alternator decoupler failure",
        "vehicle_specific_diagnosis": "2016 Malibu drive belt noise often manifests when accelerating hard, pointing to reduced spring pressure in the automatic belt tensioner."
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
    },
    {
        "slug": "2016-nissan-rogue-squealing-noise",
        "year": "2016",
        "make": "Nissan",
        "model": "Rogue",
        "page_title": "2016 Nissan Rogue AC Squeal & Belt Noise — AI Check | Carithm",
        "meta_description": "2016 Nissan Rogue squealing when AC engages? Diagnose AC compressor clutch wear and serpentine belt issues with AI sound mapping.",
        "h1_title": "2016 Nissan Rogue Squealing Noise? Analyze Sound With AI",
        "common_issue_summary": "AC compressor magnetic clutch wear, belt slippage, or idler pulley friction",
        "vehicle_specific_diagnosis": "In 2016 Rogue models, squealing when starting climate control usually stems from magnetic clutch slip on the AC compressor pulley."
    },
    {
        "slug": "2014-nissan-sentra-squealing-noise",
        "year": "2014",
        "make": "Nissan",
        "model": "Sentra",
        "page_title": "2014 Nissan Sentra Steering Belt Squeal — AI Sound Check | Carithm",
        "meta_description": "Squealing noise when turning steering wheel or starting 2014 Nissan Sentra? Upload sound clip to test belt and pulley integrity.",
        "h1_title": "2014 Nissan Sentra Squealing Noise? AI Fault Diagnosis",
        "common_issue_summary": "serpentine belt slippage, alternator pulley drag, or brake wear squeal",
        "vehicle_specific_diagnosis": "2014 Sentra serpentine belts deteriorate quickly under high heat, leading to loud squeaking when turning into tight parking spaces."
    },
    {
        "slug": "2015-jeep-grand-cherokee-squealing-noise",
        "year": "2015",
        "make": "Jeep",
        "model": "Grand Cherokee",
        "page_title": "2015 Jeep Grand Cherokee Squealing Engine — AI Diagnosis | Carithm",
        "meta_description": "2015 Jeep Grand Cherokee squealing under hood? Upload audio to detect water pump bearing squeal and serpentine belt tensioner faults.",
        "h1_title": "2015 Jeep Grand Cherokee Squealing? Check Engine Noise",
        "common_issue_summary": "3.6L Pentastar water pump failure, idler pulley wear, or belt misalignment",
        "vehicle_specific_diagnosis": "The 3.6L V6 in 2015 Grand Cherokees is well known for water pump bearing wear, which starts as a squeak and rapidly turns into a high pitch squeal."
    },
    {
        "slug": "2016-jeep-wrangler-squealing-noise",
        "year": "2016",
        "make": "Jeep",
        "model": "Wrangler",
        "page_title": "2016 Jeep Wrangler Belt & Brake Squeal — AI Sound Check | Carithm",
        "meta_description": "2016 Jeep Wrangler high-pitched squeal while driving? Upload sound clip to analyze serpentine belt vs brake pad wear noise.",
        "h1_title": "2016 Jeep Wrangler Squealing Noise? Upload Audio",
        "common_issue_summary": "serpentine belt contamination, idler pulley noise, or brake pad wear indicator",
        "vehicle_specific_diagnosis": "Off-road dust and mud in 2016 Wranglers frequently glaze the serpentine belt and idler pulleys, causing loud squealing during acceleration."
    },
    {
        "slug": "2015-hyundai-elantra-squealing-noise",
        "year": "2015",
        "make": "Hyundai",
        "model": "Elantra",
        "page_title": "2015 Hyundai Elantra Acceleration Squeal — AI Diagnosis | Carithm",
        "meta_description": "2015 Hyundai Elantra engine squeals when accelerating? Test audio for alternator belt loose tension and belt pulley alignment.",
        "h1_title": "2015 Hyundai Elantra Squealing Noise? AI Audio Check",
        "common_issue_summary": "loose manual belt tension, alternator pulley slipping, or water pump belt drag",
        "vehicle_specific_diagnosis": "Unlike hydraulic tensioner systems, 2015 Elantra drive belts require precise manual adjustment and often squeal when belt stretch occurs."
    },
    {
        "slug": "2016-hyundai-sonata-squealing-noise",
        "year": "2016",
        "make": "Hyundai",
        "model": "Sonata",
        "page_title": "2016 Hyundai Sonata Squealing Engine Noise — AI Check | Carithm",
        "meta_description": "2016 Hyundai Sonata squeal on morning start or AC startup? Upload sound recording for instant AI acoustic diagnostic feedback.",
        "h1_title": "2016 Hyundai Sonata Squealing Noise? Upload Sound",
        "common_issue_summary": "alternator belt slippage, AC clutch drag, or idler pulley failure",
        "vehicle_specific_diagnosis": "Morning chirp and squeal on 2016 Sonatas is usually tied to alternator pulley decoupler wear or reduced drive belt elasticity."
    },
    {
        "slug": "2015-kia-optima-squealing-noise",
        "year": "2015",
        "make": "Kia",
        "model": "Optima",
        "page_title": "2015 Kia Optima Tensioner Belt Squeal — AI Audio Check | Carithm",
        "meta_description": "Hearing high pitched squeal from 2015 Kia Optima engine? Analyze sound file to detect belt tensioner failure and alternator drag.",
        "h1_title": "2015 Kia Optima Squealing Noise? Instant AI Diagnosis",
        "common_issue_summary": "belt tensioner hydraulic leak/wear, drive belt slip, or AC compressor bearing",
        "vehicle_specific_diagnosis": "Hydraulic belt tensioners on 2015 Kia Optimas can leak damping fluid, resulting in rapid belt vibration and high-pitched squealing."
    },
    {
        "slug": "2016-kia-sorento-squealing-noise",
        "year": "2016",
        "make": "Kia",
        "model": "Sorento",
        "page_title": "2016 Kia Sorento AC Belt Squeal & Chirp — AI Diagnosis | Carithm",
        "meta_description": "2016 Kia Sorento engine squealing when AC turns on? Upload audio to diagnose accessory drive belt and pulley problems.",
        "h1_title": "2016 Kia Sorento Squealing Noise? Find the Cause",
        "common_issue_summary": "AC drive belt chirp, tensioner pulley play, or water pump bearing noise",
        "vehicle_specific_diagnosis": "2016 Sorento V6 and 2.4L models commonly exhibit belt squeal when AC load is engaged, usually fixed by replacing the main drive belt and tensioner assembly."
    },
    {
        "slug": "2015-subaru-outback-squealing-noise",
        "year": "2015",
        "make": "Subaru",
        "model": "Outback",
        "page_title": "2015 Subaru Outback Steering & Belt Squeal — AI Check | Carithm",
        "meta_description": "2015 Subaru Outback squeal at full steering lock or cold start? Upload audio for AI classification of power steering and belt slip.",
        "h1_title": "2015 Subaru Outback Squealing Noise? Upload Engine Sound",
        "common_issue_summary": "power steering belt slippage, alternator decoupler wear, or stretch belt slip",
        "vehicle_specific_diagnosis": "Squealing on full lock turns in 2015 Outbacks is caused by accessory belt slip over the alternator and power steering drive pulleys."
    },
    {
        "slug": "2016-subaru-forester-squealing-noise",
        "year": "2016",
        "make": "Subaru",
        "model": "Forester",
        "page_title": "2016 Subaru Forester AC Squeal — AI Sound Check | Carithm",
        "meta_description": "2016 Subaru Forester squealing on hot days when AC turns on? Upload engine audio to diagnose belt stretch and AC clutch slippage.",
        "h1_title": "2016 Subaru Forester Squealing Noise? AI Diagnosis",
        "common_issue_summary": "AC compressor clutch slippage, stretch fit belt failure, or idler pulley drag",
        "vehicle_specific_diagnosis": "2016 Foresters use stretch-fit belts for climate control systems; as they age, heavy AC compressor resistance leads to loud intermittent squealing."
    },
    {
        "slug": "2014-ram-1500-squealing-noise",
        "year": "2014",
        "make": "RAM",
        "model": "1500",
        "page_title": "2014 RAM 1500 5.7L Hemi Belt Squeal — AI Sound Check | Carithm",
        "meta_description": "2014 RAM 1500 engine squealing on acceleration or idle? Test engine recording for tensioner pulley wobble and belt wear.",
        "h1_title": "2014 RAM 1500 Squealing Noise? Upload Engine Audio",
        "common_issue_summary": "5.7L Hemi serpentine belt tensioner wobble, idler pulley wear, or water pump leak",
        "vehicle_specific_diagnosis": "The 2014 RAM 1500 Hemi automatic belt tensioner pivot can wear down over time, causing belt misalignment and high-rpm belt squeal."
    },
    {
        "slug": "2015-gmc-sierra-1500-squealing-noise",
        "year": "2015",
        "make": "GMC",
        "model": "Sierra 1500",
        "page_title": "2015 GMC Sierra 1500 Squealing Engine — AI Diagnosis | Carithm",
        "meta_description": "Squealing or chirping noise from 2015 GMC Sierra 1500 engine? Upload sound clip to test idler pulleys and serpentine belt glaze.",
        "h1_title": "2015 GMC Sierra 1500 Squealing Noise? AI Diagnosis",
        "common_issue_summary": "idler pulley bearing failure, drive belt glazing, or alternator pulley drag",
        "vehicle_specific_diagnosis": "Like its Silverado sibling, 2015 Sierra 1500 models frequently generate sharp belt squeals due to dry idler bearings or belt glaze."
    },
    {
        "slug": "2016-mazda-cx5-squealing-noise",
        "year": "2016",
        "make": "Mazda",
        "model": "CX-5",
        "page_title": "2016 Mazda CX-5 Hydraulic Tensioner Squeal — AI Check | Carithm",
        "meta_description": "2016 Mazda CX-5 squealing on cold start or acceleration? Upload sound file to check for hydraulic belt tensioner fluid leaks.",
        "h1_title": "2016 Mazda CX-5 Squealing Noise? Upload Sound Clip",
        "common_issue_summary": "leaking hydraulic belt tensioner, water pump belt slip, or alternator decoupler noise",
        "vehicle_specific_diagnosis": "A known issue on 2016 SkyActiv Mazda CX-5 engines is hydraulic tensioner leakage, causing belt slop and loud acceleration squeal."
    },
    {
        "slug": "2015-bmw-328i-squealing-noise",
        "year": "2015",
        "make": "BMW",
        "model": "328i",
        "page_title": "2015 BMW 328i N20 Engine Belt Squeal — AI Diagnosis | Carithm",
        "meta_description": "2015 BMW 328i squealing from engine bay? Upload audio to detect oil filter housing gasket belt oil contamination vs belt tensioner wear.",
        "h1_title": "2015 BMW 328i Squealing Noise? AI Sound Analysis",
        "common_issue_summary": "OFHG oil leak onto drive belt, belt tensioner failure, or mechanical squeal",
        "vehicle_specific_diagnosis": "Crucial on 2015 BMW 328i (N20): Oil filter housing gasket leaks oil onto the belt, causing it to slip/squeal and risk getting shredded into the front main seal."
    },
    {
        "slug": "2014-volkswagen-jetta-squealing-noise",
        "year": "2014",
        "make": "Volkswagen",
        "model": "Jetta",
        "page_title": "2014 VW Jetta Accessory Belt Squeal — AI Diagnosis | Carithm",
        "meta_description": "2014 Volkswagen Jetta squealing noise when starting or driving? Check audio clip for alternator clutch pulley and belt tensioner faults.",
        "h1_title": "2014 Volkswagen Jetta Squealing Noise? Upload Engine Sound",
        "common_issue_summary": "alternator freewheel pulley failure, serpentine belt wear, or AC compressor clutch",
        "vehicle_specific_diagnosis": "2014 Jettas often develop an engine squeal due to failure of the alternator freewheel clutch pulley, putting excessive flutter on the belt."
    },
    {
        "slug": "2015-mercedes-c300-squealing-noise",
        "year": "2015",
        "make": "Mercedes-Benz",
        "model": "C300",
        "page_title": "2015 Mercedes-Benz C300 Squealing Noise — AI Sound Check | Carithm",
        "meta_description": "2015 Mercedes C300 high pitched belt squeal or chirp? Upload engine audio file for AI pattern recognition on belt pulleys.",
        "h1_title": "2015 Mercedes-Benz C300 Squealing Noise? AI Diagnosis",
        "common_issue_summary": "belt tensioner wear, guide pulley bearing failure, or alternator clutch noise",
        "vehicle_specific_diagnosis": "2015 C300 2.0L Turbo engines frequently show belt tensioner and guide pulley bearing play, creating a high-frequency chirp and squeal."
    }
]

with open(template_path, "r", encoding="utf-8") as f:
    raw_template = f.read()

for v in vehicles:
    content = raw_template
    content = content.replace("{{ page_title }}", v["page_title"])
    content = content.replace("{{ meta_description }}", v["meta_description"])
    content = content.replace("{{ slug }}", v["slug"])
    content = content.replace("{{ h1_title }}", v["h1_title"])
    content = content.replace("{{ year }}", v["year"])
    content = content.replace("{{ make }}", v["make"])
    content = content.replace("{{ make.upper() }}", v["make"].upper())
    content = content.replace("{{ model }}", v["model"])
    content = content.replace("{{ model.upper() }}", v["model"].upper())
    content = content.replace("{{ common_issue_summary }}", v["common_issue_summary"])
    content = content.replace("{{ vehicle_specific_diagnosis }}", v["vehicle_specific_diagnosis"])

    out_file = os.path.join(script_dir, f"{v['slug']}.html")
    with open(out_file, "w", encoding="utf-8") as out:
        out.write(content)
    print(f"Generated: {out_file}")

print("Successfully generated all 30 vehicle pages!")
