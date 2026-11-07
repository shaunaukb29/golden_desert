#!/usr/bin/env python3
"""
Mazda Pilot Generator:
1. Generates /audio/mazda (Brand Hub) with clean hierarchy to Mazda models.
2. Generates 16 Elite Mazda sound diagnostic subpages (CX-5 heavy focus):
   - Group A (8 pages): Scroll-triggered, slim, dismissible bottom bar + contextual CTA after DIY checks.
   - Group B (8 pages): Zero sticky bar (pure content + contextual CTA after DIY checks).
   - Real mechanical engineering (Mazda TSB 01-036/17 HLA rattle, hydraulic tensioner leak, EPB slide pin seizure).
   - Zero third-party ads (100% Core Web Vitals compliant).
"""

import os

OUTPUT_DIR = "/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static"

PILOT_PAGES = [
    # --- Mazda CX-5 (Top GA4 Dwell Time Winner: 323s avg engagement) ---
    {
        "slug": "mazda-cx-5-rattling-noise",
        "title": "Mazda CX-5 Rattling Noise: Hydraulic Lash Adjusters vs Belt Tensioner",
        "h1": "Mazda CX-5 Cold Start & Belt Tensioner Rattle Guide",
        "model": "Mazda CX-5",
        "years": "2013–2024",
        "noise": "Rattling",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect hydraulic belt tensioner",
        "area": "Hydraulic Lash Adjusters / Belt Tensioner Dampener",
        "cost_range": "$35 – $1,100 (USD)",
        "tech_note": "A harsh 2–4 second metallic valvetrain clatter on morning cold starts on the 2.5L Skyactiv-G is hydraulic lash adjuster (HLA) bleed-down (Mazda TSB 01-036/17). A continuous rattling buzz under throttle is frequently the hydraulic serpentine belt tensioner dampener leaking oil and chattering.",
        "causes": "Hydraulic lash adjuster (HLA) bleed-down on cold start, leaking hydraulic automatic belt tensioner dampener, rusted catalytic converter heat shield clamps, or loose rear cargo privacy cover.",
        "checklist": [
            "Time the morning rattle: if the harsh clatter lasts strictly 2–4 seconds immediately upon startup and silences completely, HLA bleed-down is confirmed.",
            "Inspect the serpentine belt tensioner below the alternator: wet hydraulic oil residue running down the tensioner dampener arm confirms internal spring failure.",
            "Tap catalytic converter heat shields when cold: listen for broken sheet metal clamps vibrating against the exhaust pipe.",
            "Remove rear retractable cargo shade: test drive over rough roads to rule out interior trunk cover rattle."
        ],
        "costs": [
            ("Stainless Steel Exhaust Shield Clamp Fix", "$35 – $75", "Permanent repair for buzzing undercarriage shields."),
            ("OEM Serpentine Belt & Hydraulic Tensioner Assembly", "$240 – $390", "Cures continuous tensioner arm chatter and belt chirp."),
            ("Hydraulic Lash Adjuster (HLA) Replacement (TSB)", "$650 – $1,100", "Replaces internal valvetrain lifter buckets.")
        ],
        "has_sticky": True
    },
    {
        "slug": "mazda-cx-5-ticking-noise",
        "title": "Mazda CX-5 Ticking Sound: Skyactiv Direct Injection vs Rocker Arms",
        "h1": "Mazda CX-5 Engine Ticking Sound Diagnostic Guide",
        "model": "Mazda CX-5",
        "years": "2013–2024",
        "noise": "Ticking",
        "severity": "🟢 Low Risk (Normal Acoustic Profile)",
        "urgency": "Check oil level and injector pulse",
        "area": "Skyactiv-G Direct Injection / Rocker Arms",
        "cost_range": "$0 – $320 (USD)",
        "tech_note": "Mazda Skyactiv-G engines utilize direct high-pressure fuel injection operating up to 2,900 PSI with roller-finger rocker arm valvetrain. A rapid, sewing-machine mechanical click at idle is completely normal operation and not engine damage.",
        "causes": "High-pressure direct injection fuel pump (HPFP) normal operation, EVAP canister purge solenoid valve pulsing, low engine oil level, or cold HLA valvetrain clearance.",
        "checklist": [
            "Open hood while idling: rapid rhythmic clicking centered directly over the fuel pump on the cylinder head is normal direct injection.",
            "Touch the EVAP purge solenoid valve near intake: rapid clicking felt in sync with sound confirms normal emissions valve operation.",
            "Check engine oil dipstick: low oil reduces hydraulic lifter cushioning and amplifies valvetrain tick; verify Castrol/Mazda with moly 0W-20.",
            "Increase engine RPM to 2,200: direct-injection ticks speed up uniformly without harsh knocking."
        ],
        "costs": [
            ("DIY Diagnostic Verification", "$0", "Normal Skyactiv-G mechanical pulse confirmed."),
            ("Engine Oil & Filter Service (0W-20 Moly Synthetic)", "$65 – $95", "Restores optimal lubrication to valvetrain components."),
            ("EVAP Purge Control Solenoid Valve", "$110 – $210", "Replaces excessively noisy emissions purge valve.")
        ],
        "has_sticky": False
    },
    {
        "slug": "mazda-cx-5-humming-noise",
        "title": "Mazda CX-5 Humming Noise: Front Wheel Hub Bearings vs AWD Drone",
        "h1": "Mazda CX-5 Highway Humming Noise Diagnostic Guide",
        "model": "Mazda CX-5",
        "years": "2013–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–600 miles",
        "area": "Front Wheel Hub Assemblies / AWD Differential",
        "cost_range": "$110 – $520 (USD)",
        "tech_note": "A persistent low drone or hum between 45 and 65 mph on the CX-5 is commonly a failing front wheel hub unit-bearing, or cupped rear tires caused by the independent rear suspension geometry.",
        "causes": "Front wheel bearing hub unit spalling, rear wheel bearing wear, AWD rear differential bearing hum, or cupped rear tires.",
        "checklist": [
            "Weave gently in lane at 50 mph: if drone pitch gets louder when turning right, the left wheel bearing is damaged.",
            "Run your palm across the inner tread edge of rear tires: saw-tooth unevenness confirms tire scalloping.",
            "Jack up car and spin wheels by hand while holding suspension spring: vibration confirms bearing damage.",
            "Check wheel hub temperature after highway trip."
        ],
        "costs": [
            ("Tire Rotation & Computerized 4-Wheel Alignment", "$110 – $170", "Corrects rear camber wear and road roar."),
            ("Front Wheel Bearing Hub Assembly (Complete Unit)", "$290 – $490", "Bolt-on replacement with integrated ABS sensor."),
            ("AWD Rear Differential Fluid Exchange", "$110 – $180", "Fresh synthetic 75W-85 gear oil restores lubrication.")
        ],
        "has_sticky": True
    },
    {
        "slug": "mazda-cx-5-clunking-noise",
        "title": "Mazda CX-5 Clunking Noise: Control Arm Hydro-Bushings vs Sway Bar Links",
        "h1": "Mazda CX-5 Suspension Clunking Diagnostic Guide",
        "model": "Mazda CX-5",
        "years": "2013–2024",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 200–400 miles",
        "area": "Front Lower Control Arms & Stabilizer Links",
        "cost_range": "$110 – $720 (USD)",
        "tech_note": "A popping or hollow clunk when steering into driveways or driving over speed humps is primarily caused by torn rear hydro-compliance bushings on the front lower control arms or worn front stabilizer end link ball joints.",
        "causes": "Torn front lower control arm compliance hydro-bushings, front sway bar end link ball joint slack, steering intermediate shaft slip joint play, or upper strut mount bearing binding.",
        "checklist": [
            "Brake tap test at 10 mph: apply brakes sharply; a forward thud accompanied by a clunk confirms torn compliance bushings.",
            "Inspect front control arms from below: look for black hydraulic fluid staining on large rear vertical bushings.",
            "Drive over speed humps diagonally: chucking noise from front corners points to sway bar end link wear.",
            "Wiggle steering wheel rapidly with engine off: footwell knock points to intermediate shaft."
        ],
        "costs": [
            ("Front Sway Bar End Link Pair", "$120 – $210", "Restores quiet, firm suspension over city streets."),
            ("Front Lower Control Arm Assembly Pair", "$420 – $720", "Replaces complete arms with pre-pressed heavy-duty bushings."),
            ("Front Struts & Upper Mount Assemblies", "$390 – $650", "Restores factory ride quality and damping.")
        ],
        "has_sticky": False
    },
    {
        "slug": "mazda-cx-5-squealing-noise",
        "title": "Mazda CX-5 Squealing Noise: Belt Tensioner Slip vs Brake Wear Tabs",
        "h1": "Mazda CX-5 Engine & Brake Squeal Diagnostic Guide",
        "model": "Mazda CX-5",
        "years": "2013–2024",
        "noise": "Squealing",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 150–300 miles",
        "area": "Serpentine Accessory Belt / Brake Wear Tabs",
        "cost_range": "$75 – $390 (USD)",
        "tech_note": "A loud squeal on cold morning starts or under AC load is typically caused by serpentine belt glazing or hydraulic tensioner spring relaxation. Squealing while braking indicates ceramic pad wear indicator contact.",
        "causes": "Serpentine belt glazing, leaking hydraulic automatic belt tensioner, AC compressor clutch bearing slip, or brake pad acoustic wear tabs.",
        "checklist": [
            "Spray water mist on ribbed side of belt while squealing: if noise quiets instantly, belt glazing or tensioner misalignment is confirmed.",
            "Inspect hydraulic tensioner dampener for oily grime.",
            "Apply brakes gently at 25 mph: if squeal only occurs during braking, replace worn brake pads.",
            "Check brake pad thickness through wheel spokes."
        ],
        "costs": [
            ("Serpentine Accessory Drive Belt", "$80 – $140", "Restores quiet accessory pulley drive."),
            ("Automatic Belt Tensioner Assembly", "$220 – $380", "Maintains calibrated belt tension."),
            ("Front Brake Pads & Hardware Kit", "$190 – $340", "Silences brake acoustic wear indicator tabs.")
        ],
        "has_sticky": True
    },
    {
        "slug": "mazda-cx-5-whining-noise",
        "title": "Mazda CX-5 Whining Noise: Skyactiv-Drive 6-Speed vs Alternator",
        "h1": "Mazda CX-5 Transmission & Alternator Whining Guide",
        "model": "Mazda CX-5",
        "years": "2013–2024",
        "noise": "Whining",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect transmission fluid and alternator",
        "area": "Skyactiv-Drive 6-Speed / Alternator",
        "cost_range": "$120 – $2,800 (USD)",
        "tech_note": "On the Skyactiv-Drive 6-speed automatic (FW6A-EL), gentle planetary gear meshing whine in 1st/2nd gear under light throttle is common. Electrical whine that tracks engine RPM is alternator rectifier diode ripple.",
        "causes": "Skyactiv-Drive 6-speed gear meshing acoustics, alternator rectifier diode ripple, normal 2.5T turbo spool, or electric power steering motor load.",
        "checklist": [
            "Rev engine in Park/Neutral: if whine tracks engine RPM while stationary, transmission is ruled out; inspect alternator/belt idler.",
            "Listen through audio speakers: electrical whining that rises with vehicle throttle confirms alternator diode ripple.",
            "Drive at 15–20 mph: does whine occur only in 1st/2nd gear and quiet down upon 3rd gear upshift? (Normal transmission acoustic profile).",
            "Check transmission fluid maintenance history."
        ],
        "costs": [
            ("Serpentine Belt & Tensioner Pulley", "$140 – $260", "Restores quiet belt drive rotation."),
            ("OEM Alternator Replacement", "$330 – $540", "Eliminates electrical whine and stabilizes charging."),
            ("Mazda ATF-FZ Fluid Exchange", "$160 – $260", "Fresh synthetic fluid restores hydraulic cushion.")
        ],
        "has_sticky": False
    },
    {
        "slug": "mazda-cx-5-grinding-noise",
        "title": "Mazda CX-5 Grinding Noise: EPB Caliper Slide Pins vs Rotor Rust",
        "h1": "Mazda CX-5 Brake Grinding Diagnostic Guide",
        "model": "Mazda CX-5",
        "years": "2013–2024",
        "noise": "Grinding",
        "severity": "🔴 High Risk (Braking Hazard)",
        "urgency": "Inspect brake pads immediately",
        "area": "Electronic Parking Brake / Brake Rotors",
        "cost_range": "$90 – $520 (USD)",
        "tech_note": "On CX-5s equipped with Electronic Parking Brake (EPB), rear caliper slide pins frequently seize from road salt, causing the inner pad to wear to bare metal while the outer pad looks healthy.",
        "causes": "Worn inner brake pads grinding against brake rotor, rusted brake dust shield rubbing against rotor backing edge, or dry caliper slider pins.",
        "checklist": [
            "Inspect inner brake pads through wheel spokes: use a flashlight and mirror to verify inner pad friction lining thickness.",
            "Check if grinding occurs without braking: a constant scraping/grinding while rolling indicates a bent dust shield or seized caliper.",
            "Check wheel rim temperature after a short drive: an unusually hot rear wheel indicates a dragging parking brake caliper.",
            "Inspect brake rotor face: deep concentric gouges indicate metal-to-metal pad backing plate contact."
        ],
        "costs": [
            ("Brake Dust Shield Adjustment", "$30 – $70", "Bends back rubbing sheet metal."),
            ("Caliper Slide Pin Service & Synthetic Lube", "$90 – $160", "Restores floating caliper movement."),
            ("Rear Brake Pads & Rotors Complete Set", "$310 – $520", "Installs premium ceramic pads and balanced discs.")
        ],
        "has_sticky": True
    },
    {
        "slug": "mazda-cx-5-clicking-noise",
        "title": "Mazda CX-5 Clicking Noise: HVAC Blend Door vs Front CV Axles",
        "h1": "Mazda CX-5 Dashboard & CV Axle Clicking Guide",
        "model": "Mazda CX-5",
        "years": "2013–2024",
        "noise": "Clicking",
        "severity": "🟢 Low to Moderate Risk",
        "urgency": "Inspect HVAC and CV boots",
        "area": "HVAC Blend Door Actuator / Front CV Axles",
        "cost_range": "$60 – $540 (USD)",
        "tech_note": "A rapid clicking or tapping behind the dashboard when starting the vehicle or adjusting temperature is stripped plastic gears inside the HVAC blend door actuator. Clicking while turning under power is a failing CV axle joint.",
        "causes": "HVAC blend door actuator motor stripped plastic gears, front CV axle joint wear, torn CV boots, or loose wheel center cap.",
        "checklist": [
            "Adjust climate control temperature: if clicking starts or changes when toggling from cold to hot, the blend door actuator is stripped.",
            "Perform tight slow circles in a parking lot: rhythmic clicking from front wheels while turning under power confirms CV axle failure.",
            "Inspect CV axle rubber boots: grease splattered inside the front wheel barrel confirms a torn boot.",
            "Verify clicking occurs with vehicle stationary vs in motion."
        ],
        "costs": [
            ("HVAC Blend Door Actuator Motor", "$110 – $240", "Common repair behind the glovebox."),
            ("Front CV Axle Assembly Replacement", "$320 – $540", "Complete new axle shaft with pre-packed greased joints."),
            ("Wheel Lug Torque Check", "$0", "Ensures lug nuts are tightened to factory spec.")
        ],
        "has_sticky": False
    },

    # --- Mazda 3 ---
    {
        "slug": "mazda-3-humming-noise",
        "title": "Mazda 3 Humming Noise: Front Wheel Hub Bearings vs Rear Tire Cupping",
        "h1": "Mazda 3 Highway Humming Noise Diagnostic Guide",
        "model": "Mazda 3",
        "years": "2014–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–600 miles",
        "area": "Front Wheel Hub Assemblies / Rear Tires",
        "cost_range": "$90 – $480 (USD)",
        "tech_note": "A continuous low drone or hum above 45 mph is commonly a failing front wheel hub unit-bearing or cupped rear tires on the torsion beam / multi-link rear suspension.",
        "causes": "Front wheel bearing hub unit spalling, rear wheel hub unit wear, inner tire tread feathering from camber, or uneven tire wear.",
        "checklist": [
            "Weave gently in lane at 50 mph: if drone gets louder when turning right, the left wheel bearing is failing.",
            "Run your palm across the inner tread edge of rear tires: saw-tooth unevenness confirms tire scalloping.",
            "Jack up car and spin wheels by hand while holding suspension spring: vibration confirms bearing damage.",
            "Check wheel hub temperature after highway trip."
        ],
        "costs": [
            ("Tire Rotation & Computerized Alignment", "$110 – $170", "Corrects tire wear and road roar."),
            ("Front Wheel Bearing Hub Assembly", "$280 – $480", "OEM sealed hub unit replacement with ABS sensor."),
            ("Rear Wheel Hub Bearing Unit", "$240 – $410", "Bolt-on replacement with integrated ABS sensor.")
        ],
        "has_sticky": True
    },
    {
        "slug": "mazda-3-rattling-noise",
        "title": "Mazda 3 Rattling Noise: Dashboard Trim Buzz vs Exhaust Heat Shield",
        "h1": "Mazda 3 Cabin & Undercarriage Rattle Guide",
        "model": "Mazda 3",
        "years": "2014–2024",
        "noise": "Rattling",
        "severity": "🟢 Low Risk (Nuisance)",
        "urgency": "Inspect at convenience",
        "area": "Dashboard Trim / Exhaust Heat Shields",
        "cost_range": "$25 – $240 (USD)",
        "tech_note": "A thin metallic buzz around 2,000 RPM is typically a cracked catalytic converter heat shield clamp. Interior rattling over rough roads is often the center dashboard speaker grille or A-pillar trim clips.",
        "causes": "Catalytic converter heat shield clamp corrosion, dashboard center speaker grille vibration, loose undertray clips, or sunglasses holder rattle.",
        "checklist": [
            "Tap catalytic converter heat shield when cold: broken weld clamps will rattle distinctly against the pipe.",
            "Press firmly on dashboard center speaker grille: if cabin buzzing stops on coarse pavement, apply felt tape.",
            "Inspect underside plastic undertray: missing nylon fasteners allow shield to flap at speed.",
            "Empty overhead sunglasses console: verify rattle is not personal items."
        ],
        "costs": [
            ("Stainless Steel Exhaust Shield Clamp", "$25 – $65", "Permanent DIY or shop clamp securing loose shield."),
            ("Felt Anti-Rattle Tape Interior Kit", "$15 – $35", "Eliminates dashboard and pillar trim buzz."),
            ("Undertray Push-Pin Clip Kit", "$20 – $40", "Secures sagging plastic splash covers.")
        ],
        "has_sticky": False
    },
    {
        "slug": "mazda-3-ticking-noise",
        "title": "Mazda 3 Ticking Sound: Skyactiv Direct Injection vs Purge Valve",
        "h1": "Mazda 3 Engine Ticking Sound Diagnostic Guide",
        "model": "Mazda 3",
        "years": "2014–2024",
        "noise": "Ticking",
        "severity": "🟢 Low Risk (Normal Operation)",
        "urgency": "Check oil level and injector pulse",
        "area": "Skyactiv Direct Injection / Valvetrain",
        "cost_range": "$0 – $310 (USD)",
        "tech_note": "The Skyactiv-G 2.0L and 2.5L direct-injection engines operate high-pressure fuel pumps up to 2,900 PSI. A sharp, rapid rhythmic mechanical click at idle is completely normal operation.",
        "causes": "High-pressure direct injection fuel pump (HPFP) normal operation, EVAP canister purge valve clicking, low engine oil level, or cold hydraulic valve lash clearance.",
        "checklist": [
            "Listen with hood open: rapid sewing-machine ticking centered on the fuel pump cover is normal direct injection.",
            "Feel the EVAP purge solenoid: rapid clicking pulses felt through valve body confirm normal emissions purge.",
            "Check engine oil dipstick: ensure oil is clean and topped up with 0W-20.",
            "Notice if ticking softens when engine reaches full operating temperature."
        ],
        "costs": [
            ("DIY Diagnostic Verification", "$0", "Normal Skyactiv mechanical pulse confirmed."),
            ("Synthetic Engine Oil & Filter Change (0W-20)", "$55 – $85", "Restores proper lubrication to valvetrain components."),
            ("EVAP Purge Solenoid Valve Replacement", "$95 – $190", "Cures excessively loud emissions valve tick.")
        ],
        "has_sticky": True
    },
    {
        "slug": "mazda-3-clunking-noise",
        "title": "Mazda 3 Clunking Noise: Sway Bar Links vs Rear Torsion Bushings",
        "h1": "Mazda 3 Suspension Clunking Diagnostic Guide",
        "model": "Mazda 3",
        "years": "2014–2024",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 200–400 miles",
        "area": "Front Stabilizer Links / Rear Axle Bushings",
        "cost_range": "$95 – $560 (USD)",
        "tech_note": "A hollow knocking over speed bumps or rough city pavement is predominantly caused by worn front sway bar end links or degraded rear torsion beam axle pivot bushings.",
        "causes": "Front sway bar link ball joint play, torn control arm compliance bushings, rear axle pivot bushing fatigue, or upper strut mount wear.",
        "checklist": [
            "Drive over speed humps at an angle: chucking noise from front corners points to sway bar end link ball joint slack.",
            "Inspect front control arm compliance bushings: look for tearing in large rubber bushings.",
            "Grab front sway bar links: any play or clicking indicates ball joint failure.",
            "Check upper engine torque strut mount for cracked rubber."
        ],
        "costs": [
            ("Front Sway Bar End Link Pair", "$110 – $190", "Restores quiet, firm suspension over city streets."),
            ("Front Lower Control Arm Compliance Bushings", "$310 – $520", "Replaces torn bushings and eliminates braking clunk."),
            ("Front Strut & Mount Assemblies", "$360 – $560", "Restores factory ride quality and damping.")
        ],
        "has_sticky": False
    },

    # --- Mazda 6 ---
    {
        "slug": "mazda-6-humming-noise",
        "title": "Mazda 6 Humming Noise: Front Wheel Hub Bearings vs Tire Feathering",
        "h1": "Mazda 6 Highway Humming Noise Diagnostic Guide",
        "model": "Mazda 6",
        "years": "2014–2021",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–600 miles",
        "area": "Front Wheel Hub Assemblies / Tires",
        "cost_range": "$110 – $510 (USD)",
        "tech_note": "A persistent low drone between 45 and 70 mph on the GJ/GL Mazda 6 chassis is commonly a failing front wheel hub unit-bearing, or cupped inner rear tire tread caused by rear camber geometry.",
        "causes": "Front wheel bearing unit spalling, rear hub bearing wear, inner tire feathering from rear camber, or transmission gear whine.",
        "checklist": [
            "Weave gently in lane at 55 mph: if drone gets louder when turning right, the left wheel bearing is damaged.",
            "Run hand along the inside edge of rear tires: saw-tooth unevenness confirms tire scalloping.",
            "Spin raised front wheels by hand while holding coil spring: vibration confirms bearing damage.",
            "Check wheel hub temperature after highway trip."
        ],
        "costs": [
            ("Tire Rotation & 4-Wheel Computerized Alignment", "$110 – $180", "Corrects rear camber wear and stops road roar."),
            ("Front Wheel Bearing Hub Assembly", "$290 – $490", "OEM sealed hub unit replacement with ABS sensor."),
            ("Rear Wheel Hub Bearing Unit", "$250 – $420", "Bolt-on replacement with integrated ABS sensor.")
        ],
        "has_sticky": True
    },
    {
        "slug": "mazda-6-rattling-noise",
        "title": "Mazda 6 Rattling Noise: Hydraulic Belt Tensioner vs Exhaust Shields",
        "h1": "Mazda 6 Engine & Exhaust Rattle Diagnostic Guide",
        "model": "Mazda 6",
        "years": "2014–2021",
        "noise": "Rattling",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect hydraulic belt tensioner",
        "area": "Hydraulic Belt Tensioner / Exhaust Shields",
        "cost_range": "$35 – $390 (USD)",
        "tech_note": "A continuous metallic rattle under light acceleration is frequently caused by the hydraulic automatic serpentine belt tensioner leaking dampener oil and chattering against its stop.",
        "causes": "Leaking hydraulic serpentine belt tensioner dampener, catalytic converter heat shield clamp corrosion, or cold-start HLA valvetrain bleed-down.",
        "checklist": [
            "Inspect belt tensioner beneath alternator: wet hydraulic oil residue running down the tensioner dampener arm confirms failure.",
            "Tap catalytic converter heat shields when cold: loose shields will rattle distinctly against the pipe.",
            "Cold start timing check: if rattle lasts 2–3 seconds upon startup and disappears, HLA bleed-down is responsible.",
            "Inspect serpentine belt for glazing or rib cracking."
        ],
        "costs": [
            ("Stainless Steel Exhaust Shield Clamp", "$35 – $75", "Permanent DIY fix for buzzing underbody shields."),
            ("OEM Serpentine Belt & Hydraulic Tensioner Assembly", "$240 – $390", "Cures continuous tensioner chatter and belt chirp."),
            ("Oil & Filter Change (0W-20 Castrol/Mazda Moly)", "$65 – $95", "Ensures rapid hydraulic tensioner pressurization.")
        ],
        "has_sticky": False
    },

    # --- Mazda CX-9 ---
    {
        "slug": "mazda-cx-9-humming-noise",
        "title": "Mazda CX-9 Humming Noise: Heavy Chassis Hub Bearings vs AWD Carrier",
        "h1": "Mazda CX-9 Highway Humming Drone Diagnostic Guide",
        "model": "Mazda CX-9",
        "years": "2016–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–600 miles",
        "area": "Front Wheel Hub Assemblies / AWD Transfer Case",
        "cost_range": "$120 – $560 (USD)",
        "tech_note": "Due to the CX-9's 4,400 lb curb weight, front wheel hub unit-bearings commonly develop internal race spalling after 65,000 miles, producing an intense cabin drone that peaks between 45 and 70 mph.",
        "causes": "Front wheel bearing unit spalling, rear hub bearing wear, AWD transfer case or differential bearing hum, or cupped tires.",
        "checklist": [
            "Weave gently in lane at 55 mph: if the humming tone gets louder when turning right, the left wheel bearing is failing.",
            "Jack up front wheels and spin by hand while gripping coil spring: roughness or vibration in spring confirms bearing damage.",
            "Feel wheel hub temperatures after a 30-minute highway run: failing bearing runs significantly hotter than opposite side.",
            "Inspect all four tires for uneven inner shoulder scalloping."
        ],
        "costs": [
            ("Tire Rotation, Road Force Balance & Alignment", "$110 – $180", "Eliminates uneven tire wear drone."),
            ("Front Wheel Bearing Hub Assembly (OEM Unit)", "$310 – $520", "Bolt-on replacement with integrated ABS sensor."),
            ("AWD Transfer Case & Rear Diff Fluid Exchange", "$130 – $210", "Fresh synthetic fluid restores driveline lubrication.")
        ],
        "has_sticky": True
    },
    {
        "slug": "mazda-cx-9-clunking-noise",
        "title": "Mazda CX-9 Clunking Noise: Compliance Bushings vs Strut Mounts",
        "h1": "Mazda CX-9 Suspension Clunking Diagnostic Guide",
        "model": "Mazda CX-9",
        "years": "2016–2024",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 200–400 miles",
        "area": "Front Control Arms & Upper Strut Mounts",
        "cost_range": "$120 – $850 (USD)",
        "tech_note": "A heavy clunk over speed bumps or when braking firmly is caused by fluid-filled compliance bushings tearing on the front lower control arms, or upper strut bearing binding during low-speed steering maneuvers.",
        "causes": "Torn front lower control arm compliance hydro-bushings, front sway bar end link ball joint wear, upper strut mount bearing binding, or rear power liftgate striker play.",
        "checklist": [
            "Brake tap test at 10 mph: apply brakes sharply; a forward thud accompanied by a clunk confirms torn compliance bushings.",
            "Inspect front control arms from below: look for black hydraulic fluid staining on large rear vertical bushings.",
            "Drive over speed humps diagonally: chucking noise from front corners points to sway bar end link wear.",
            "Wrap electrical tape around rear liftgate striker: if cargo rattle stops over bumps, adjust rubber bump stops."
        ],
        "costs": [
            ("Front Sway Bar End Link Pair", "$130 – $220", "Stops low-speed suspension chatter over bumps."),
            ("Front Lower Control Arm Compliance Bushings", "$380 – $640", "Replaces torn hydro-bushings and restores braking firmness."),
            ("Front Struts & Upper Mount Assemblies", "$450 – $780", "Eliminates steering pops and restores ride quality.")
        ],
        "has_sticky": False
    }
]

print(f"Loaded {len(PILOT_PAGES)} Mazda pilot specifications.")

def render_subpage(page):
    costs_html = ""
    for item, cost, desc in page["costs"]:
        costs_html += f"""
      <div style="display: flex; justify-content: space-between; align-items: baseline; padding: 12px 0; border-bottom: 1px solid var(--border); flex-wrap: wrap; gap: 8px;">
        <div>
          <strong style="color: #fff; font-size: 0.95rem;">{item}</strong>
          <p style="margin: 3px 0 0; font-size: 0.85rem; color: var(--muted);">{desc}</p>
        </div>
        <span style="font-weight: 700; color: #22c55e; font-size: 0.95rem; white-space: nowrap;">{cost}</span>
      </div>"""

    checklist_html = ""
    for step in page["checklist"]:
        checklist_html += f"""
        <li style="padding: 10px 0; border-bottom: 1px solid var(--border); display: flex; align-items: flex-start; gap: 10px;">
          <span style="color: var(--teal); font-weight: 700;">&#10003;</span>
          <span style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.5;">{step}</span>
        </li>"""

    cta_ref = "sticky_mazda" if page["has_sticky"] else "inline_mazda"
    contextual_cta = f"""
    <!-- Contextual In-Content Diagnostic CTA (Placed where intent is highest) -->
    <section class="contextual-cta-card" style="margin: 32px 0; background: linear-gradient(135deg, rgba(14,27,42,0.95) 0%, rgba(9,19,30,0.98) 100%); border: 1.5px solid rgba(56,189,248,0.35); border-radius: 12px; padding: 24px; position: relative; overflow: hidden;">
      <div style="display: inline-flex; align-items: center; gap: 6px; background: rgba(56,189,248,0.12); border: 1px solid rgba(56,189,248,0.25); padding: 3px 10px; border-radius: 16px; font-size: 0.75rem; font-weight: 600; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 12px;">
        <span>Acoustic Frequency Verification</span>
      </div>
      <h3 style="margin: 0 0 8px 0; font-size: 1.25rem; color: #ffffff; font-weight: 700;">Can't isolate the sound with your eyes alone?</h3>
      <p style="margin: 0 0 16px 0; color: #94a3b8; font-size: 0.9rem; line-height: 1.55;">
        Acoustic symptoms can closely mimic each other. If you have an audio recording or can capture 5 seconds under the hood, Carithm's free browser tool analyzes frequency peaks to identify ranked possibilities.
      </p>
      <a href="https://carithm.vercel.app/audio?ref={cta_ref}" style="display: inline-flex; align-items: center; justify-content: center; gap: 8px; background: #0284c7; color: #ffffff; text-decoration: none; padding: 12px 22px; border-radius: 8px; font-weight: 600; font-size: 0.92rem; transition: background 0.2s ease;">
        <span>Analyze Your Sound in Browser (Free)</span>
        <span style="font-size: 1.1rem;">&rarr;</span>
      </a>
      <span style="display: block; margin-top: 8px; font-size: 0.78rem; color: #64748b;">No download, login, or personal info required. Runs instantly on mobile or desktop.</span>
    </section>"""

    sticky_bar_html = ""
    if page["has_sticky"]:
        sticky_bar_html = """
<!-- Slim, Dismissible, Scroll-Triggered Mobile Action Bar (Group A) -->
<div id="pilotStickyBar" style="display: none; position: fixed; bottom: 0; left: 0; right: 0; background: rgba(11, 17, 26, 0.96); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-top: 1px solid rgba(56,189,248,0.3); padding: 10px 16px; z-index: 9999; box-shadow: 0 -4px 16px rgba(0,0,0,0.4); max-width: 100vw; box-sizing: border-box;">
  <div style="max-width: 820px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; gap: 10px;">
    <div style="display: flex; flex-direction: column; min-width: 0;">
      <span style="font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.04em; color: #38bdf8; font-weight: 700;">Acoustic Check</span>
      <span style="font-size: 0.82rem; color: #f1f5f9; font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Verify audio pattern</span>
    </div>
    <div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">
      <a href="https://carithm.vercel.app/audio?ref=sticky_mazda" style="background: #0284c7; color: #ffffff; font-size: 0.8rem; font-weight: 600; padding: 7px 14px; border-radius: 6px; text-decoration: none; white-space: nowrap;">
        Analyze Sound &rarr;
      </a>
      <button onclick="dismissPilotBar()" aria-label="Dismiss banner" style="background: transparent; border: 0; color: #94a3b8; font-size: 1.2rem; cursor: pointer; padding: 4px 6px; line-height: 1;">&times;</button>
    </div>
  </div>
</div>
<script>
  function dismissPilotBar() {
    try { sessionStorage.setItem('pilot_bar_dismissed', '1'); } catch(e){}
    var el = document.getElementById('pilotStickyBar');
    if (el) el.style.display = 'none';
  }
  (function() {
    try {
      if (sessionStorage.getItem('pilot_bar_dismissed') === '1') return;
    } catch(e){}
    var showed = false;
    window.addEventListener('scroll', function() {
      if (showed) return;
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;
      var totalH = document.documentElement.scrollHeight - window.innerHeight;
      if (totalH > 0 && (scrollY / totalH) > 0.45) {
        showed = true;
        var el = document.getElementById('pilotStickyBar');
        if (el) el.style.display = 'block';
      }
    }, { passive: true });
  })();
</script>
"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page['title']}</title>
  <meta name="description" content="Diagnose {page['model']} ({page['years']}) {page['noise'].lower()} sound. Review confirmed factory root causes, DIY inspection checklist, repair cost ranges, and acoustic analysis.">
  <link rel="canonical" href="https://carithm.vercel.app/audio/{page['slug']}">
  <meta name="robots" content="index, follow">

  <!-- Schema Graph: TechArticle & BreadcrumbList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "TechArticle",
        "headline": "{page['h1']}",
        "description": "Diagnostic and troubleshooting guide for {page['model']} ({page['years']}) {page['noise'].lower()} noise.",
        "url": "https://carithm.vercel.app/audio/{page['slug']}",
        "datePublished": "2026-11-07",
        "dateModified": "2026-11-07",
        "author": {{
          "@type": "Organization",
          "name": "Carithm Automotive Research",
          "url": "https://carithm.vercel.app"
        }},
        "publisher": {{
          "@type": "Organization",
          "name": "Carithm",
          "url": "https://carithm.vercel.app"
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://carithm.vercel.app"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "Acoustic Diagnostics",
            "item": "https://carithm.vercel.app/audio"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "Mazda Noise Hub",
            "item": "https://carithm.vercel.app/audio/mazda"
          }},
          {{
            "@type": "ListItem",
            "position": 4,
            "name": "{page['model']} {page['noise']}",
            "item": "https://carithm.vercel.app/audio/{page['slug']}"
          }}
        ]
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --bg: #090a0f;
      --surface: #10131a;
      --surface2: #161b24;
      --border: rgba(255,255,255,0.08);
      --text: #f8fafc;
      --muted: #94a3b8;
      --muted2: #64748b;
      --accent: #38bdf8;
      --teal: #2dd4bf;
      --r: 10px;
    }}
    * {{ box-sizing: border-box; }}
    html {{
      overflow-x: hidden;
      max-width: 100%;
      width: 100%;
      touch-action: pan-y;
      background: var(--bg);
    }}
    body {{
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      margin: 0;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      max-width: 100%;
      width: 100%;
    }}
    header {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .brand {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #fff;
      text-decoration: none;
      letter-spacing: -0.02em;
    }}
    .brand span {{ color: var(--accent); }}
    nav a {{
      color: var(--muted);
      text-decoration: none;
      font-size: 0.88rem;
      margin-left: 16px;
    }}
    nav a:hover {{ color: #fff; }}
    main {{
      max-width: 820px;
      margin: 0 auto;
      padding: 32px 18px 48px;
    }}
    .breadcrumb {{
      font-size: 0.82rem;
      color: var(--muted2);
      margin-bottom: 20px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 6px;
    }}
    .breadcrumb a {{ color: var(--muted); text-decoration: none; }}
    .breadcrumb a:hover {{ color: #fff; }}
    .badge-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
      margin-bottom: 14px;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 0.75rem;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 20px;
      letter-spacing: 0.03em;
      text-transform: uppercase;
    }}
    .badge-accent {{ background: rgba(56,189,248,0.12); color: var(--accent); border: 1px solid rgba(56,189,248,0.25); }}
    .badge-severity {{ background: rgba(245,158,11,0.12); color: #fbbf24; border: 1px solid rgba(245,158,11,0.25); }}
    h1 {{
      font-size: clamp(1.8rem, 4vw, 2.4rem);
      font-weight: 800;
      line-height: 1.2;
      margin: 0 0 16px;
      color: #ffffff;
      letter-spacing: -0.02em;
    }}
    .card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--r);
      padding: 24px;
      margin-bottom: 24px;
    }}
    h2 {{
      font-size: 1.3rem;
      font-weight: 700;
      color: #fff;
      margin: 0 0 14px;
      letter-spacing: -0.01em;
    }}
    footer {{
      border-top: 1px solid var(--border);
      padding: 32px 20px;
      text-align: center;
      font-size: 0.85rem;
      color: var(--muted2);
      background: var(--surface);
    }}
    footer a {{ color: var(--muted); text-decoration: none; }}
    footer a:hover {{ color: #fff; }}
    .disclaimer-box {{
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(255,255,255,0.06);
      border-radius: 8px;
      padding: 14px 18px;
      font-size: 0.8rem;
      color: var(--muted2);
      line-height: 1.5;
      margin-top: 24px;
    }}
  </style>
</head>
<body>

<header>
  <a href="https://carithm.vercel.app/" class="brand">Carithm<span>AI</span></a>
  <nav>
    <a href="https://carithm.vercel.app/audio">Audio Diagnoser</a>
    <a href="https://carithm.vercel.app/audio/mazda" style="color: #fff;">Mazda Hub</a>
    <a href="https://carithm.vercel.app/audio/toyota">Toyota Hub</a>
    <a href="https://carithm.vercel.app/audio/honda">Honda Hub</a>
    <a href="https://carithm.vercel.app/audio/ford">Ford Hub</a>
    <a href="https://carithm.vercel.app/about">About</a>
  </nav>
</header>

<main>
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="https://carithm.vercel.app/">Home</a>
    <span>&rsaquo;</span>
    <a href="https://carithm.vercel.app/audio">Acoustic Diagnostics</a>
    <span>&rsaquo;</span>
    <a href="https://carithm.vercel.app/audio/mazda">Mazda</a>
    <span>&rsaquo;</span>
    <span style="color: #fff;">{page['model']} {page['noise']}</span>
  </nav>

  <div class="badge-bar">
    <span class="badge badge-accent">{page['model']} ({page['years']})</span>
    <span class="badge badge-severity">{page['severity']}</span>
    <span class="badge" style="background: rgba(45,212,191,0.12); color: var(--teal); border: 1px solid rgba(45,212,191,0.25);">{page['area']}</span>
  </div>

  <h1>{page['h1']}</h1>

  <p style="font-size: 1.05rem; color: #cbd5e1; margin-bottom: 24px; line-height: 1.6;">
    If your <strong>{page['model']} ({page['years']})</strong> is producing an abnormal <strong>{page['noise'].lower()} sound</strong>, this diagnostic overview outlines verified mechanical causes, DIY inspection steps, estimated repair costs, and acoustic verification options.
  </p>

  <!-- Technical Briefing Card -->
  <section class="card">
    <h2>Verified Mechanical Context &amp; Root Causes</h2>
    <div style="background: var(--surface2); border-left: 3px solid var(--accent); padding: 14px 16px; border-radius: 0 8px 8px 0; margin-bottom: 18px;">
      <strong style="color: #fff; font-size: 0.92rem;">Factory Technical Note:</strong>
      <p style="margin: 4px 0 0; color: var(--muted); font-size: 0.88rem; line-height: 1.55;">{page['tech_note']}</p>
    </div>
    <p style="color: #cbd5e1; font-size: 0.93rem; margin: 0 0 12px 0;"><strong>Primary Causes Identified:</strong> {page['causes']}</p>
  </section>

  <!-- Driveway Inspection Steps -->
  <section class="card">
    <h2>DIY Driveway Diagnostic Checklist</h2>
    <p style="color: var(--muted); font-size: 0.88rem; margin: 0 0 14px;">Follow these non-invasive steps before booking a shop inspection:</p>
    <ul style="list-style: none; padding: 0; margin: 0;">
      {checklist_html}
    </ul>
  </section>

  {contextual_cta}

  <!-- Estimated Repair Cost Card -->
  <section class="card">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
      <h2 style="margin: 0;">Typical Repair Costs (USD)</h2>
      <span style="font-size: 0.82rem; color: var(--teal); background: rgba(45,212,191,0.1); padding: 4px 10px; border-radius: 6px; font-weight: 600;">Est. Range: {page['cost_range']}</span>
    </div>
    <p style="color: var(--muted); font-size: 0.86rem; margin: 0 0 14px;">Independent shop averages across parts &amp; labor:</p>
    {costs_html}
  </section>

  <!-- Related Mazda Acoustic Guides -->
  <section class="card" style="margin-bottom: 16px;">
    <h2>More Mazda Diagnostic Guides</h2>
    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;">
      <a href="https://carithm.vercel.app/audio/mazda-cx-5-rattling-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">CX-5 Rattling</a>
      <a href="https://carithm.vercel.app/audio/mazda-cx-5-ticking-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">CX-5 Ticking</a>
      <a href="https://carithm.vercel.app/audio/mazda-cx-5-humming-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">CX-5 Humming</a>
      <a href="https://carithm.vercel.app/audio/mazda-cx-5-clunking-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">CX-5 Clunking</a>
      <a href="https://carithm.vercel.app/audio/mazda-3-humming-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Mazda 3 Humming</a>
      <a href="https://carithm.vercel.app/audio/mazda-6-humming-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Mazda 6 Humming</a>
      <a href="https://carithm.vercel.app/audio/mazda" style="background: rgba(56,189,248,0.15); border: 1px solid rgba(56,189,248,0.3); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--accent); text-decoration: none; font-weight: 600;">View All Mazda Models &rarr;</a>
    </div>
  </section>

  <div class="disclaimer-box">
    <strong>Technical Disclaimer:</strong> Acoustic diagnostics provide preliminary pattern matching and should be verified with an ASE-certified technician or factory scan tool. Never drive a vehicle exhibiting severe braking degradation or sudden oil pressure loss.
  </div>
</main>

<footer>
  <p>&copy; 2026 Carithm. Autonomous Automotive Acoustic Research.</p>
  <p style="margin-top: 4px;"><a href="https://carithm.vercel.app/audio">Acoustic Diagnoser</a> &bull; <a href="https://carithm.vercel.app/audio/mazda">Mazda Directory</a> &bull; <a href="https://carithm.vercel.app/audio/toyota">Toyota Directory</a> &bull; <a href="https://carithm.vercel.app/audio/honda">Honda Directory</a> &bull; <a href="https://carithm.vercel.app/audio/ford">Ford Directory</a> &bull; <a href="https://carithm.vercel.app/about">About Carithm</a></p>
</footer>

{sticky_bar_html}

</body>
</html>"""


def render_brand_hub():
    models_dict = {}
    for p in PILOT_PAGES:
        m = p["model"]
        if m not in models_dict:
            models_dict[m] = []
        models_dict[m].append(p)

    model_sections = ""
    for model_name, pages in models_dict.items():
        links_html = ""
        for p in pages:
            links_html += f"""
        <a href="https://carithm.vercel.app/audio/{p['slug']}" style="background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; padding: 14px 16px; text-decoration: none; display: flex; flex-direction: column; justify-content: space-between; transition: border-color 0.2s;">
          <div>
            <span style="font-size: 0.72rem; text-transform: uppercase; color: var(--accent); font-weight: 700; letter-spacing: 0.04em;">{p['noise']} Noise</span>
            <h4 style="margin: 6px 0 0; color: #fff; font-size: 0.95rem; font-weight: 600;">{p['model']} {p['noise']}</h4>
          </div>
          <span style="margin-top: 10px; font-size: 0.78rem; color: #22c55e; font-weight: 500;">Est: {p['cost_range']}</span>
        </a>"""

        model_sections += f"""
      <section style="margin-bottom: 32px;">
        <h3 style="font-size: 1.25rem; color: #fff; border-bottom: 1px solid var(--border); padding-bottom: 8px; margin-bottom: 14px;">{model_name}</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 12px;">
          {links_html}
        </div>
      </section>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mazda Noise Diagnostic Hub: Common Sounds, TSBs &amp; Repair Costs | Carithm</title>
  <meta name="description" content="Explore documented acoustic diagnostic guides for Mazda CX-5, Mazda 3, Mazda 6, and Mazda CX-9. Verified root causes, factory TSB references, and repair cost estimates.">
  <link rel="canonical" href="https://carithm.vercel.app/audio/mazda">
  <meta name="robots" content="index, follow">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "headline": "Mazda Automotive Acoustic Diagnostic Hub",
    "description": "Comprehensive directory of documented mechanical sound diagnostics for Mazda vehicles.",
    "url": "https://carithm.vercel.app/audio/mazda",
    "publisher": {{
      "@type": "Organization",
      "name": "Carithm",
      "url": "https://carithm.vercel.app"
    }}
  }}
  </script>

  <style>
    :root {{
      --bg: #090a0f;
      --surface: #10131a;
      --surface2: #161b24;
      --border: rgba(255,255,255,0.08);
      --text: #f8fafc;
      --muted: #94a3b8;
      --muted2: #64748b;
      --accent: #38bdf8;
      --teal: #2dd4bf;
    }}
    * {{ box-sizing: border-box; }}
    html {{
      overflow-x: hidden;
      max-width: 100%;
      width: 100%;
      touch-action: pan-y;
      background: var(--bg);
    }}
    body {{
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      margin: 0;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      max-width: 100%;
      width: 100%;
    }}
    header {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .brand {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #fff;
      text-decoration: none;
      letter-spacing: -0.02em;
    }}
    .brand span {{ color: var(--accent); }}
    nav a {{
      color: var(--muted);
      text-decoration: none;
      font-size: 0.88rem;
      margin-left: 16px;
    }}
    main {{
      max-width: 960px;
      margin: 0 auto;
      padding: 36px 18px 48px;
    }}
    .hero {{
      margin-bottom: 36px;
    }}
    h1 {{
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 800;
      margin: 0 0 12px;
      letter-spacing: -0.02em;
    }}
    footer {{
      border-top: 1px solid var(--border);
      padding: 32px 20px;
      text-align: center;
      font-size: 0.85rem;
      color: var(--muted2);
      background: var(--surface);
    }}
  </style>
</head>
<body>

<header>
  <a href="https://carithm.vercel.app/" class="brand">Carithm<span>AI</span></a>
  <nav>
    <a href="https://carithm.vercel.app/audio">Audio Diagnoser</a>
    <a href="https://carithm.vercel.app/audio/mazda" style="color: #fff;">Mazda Hub</a>
    <a href="https://carithm.vercel.app/audio/toyota">Toyota Hub</a>
    <a href="https://carithm.vercel.app/audio/honda">Honda Hub</a>
    <a href="https://carithm.vercel.app/audio/ford">Ford Hub</a>
    <a href="https://carithm.vercel.app/about">About</a>
  </nav>
</header>

<main>
  <div class="hero">
    <span style="font-size: 0.78rem; text-transform: uppercase; color: var(--accent); font-weight: 700; letter-spacing: 0.05em;">Brand Acoustic Directory</span>
    <h1>Mazda Vehicle Noise Diagnostic Hub</h1>
    <p style="color: var(--muted); font-size: 1.05rem; max-width: 720px; margin: 0 0 20px;">
      Documented diagnostic guides for common acoustic failure modes across Mazda crossovers and sedans. Verified factory TSB references, driveway checks, and estimated repair costs.
    </p>
    <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(56,189,248,0.1); border: 1px solid rgba(56,189,248,0.25); padding: 8px 16px; border-radius: 8px; font-size: 0.88rem; color: #cbd5e1;">
      <span>Need live acoustic analysis?</span>
      <a href="https://carithm.vercel.app/audio" style="color: var(--accent); font-weight: 600; text-decoration: none;">Open Free AI Sound Diagnoser &rarr;</a>
    </div>
  </div>

  {model_sections}
</main>

<footer>
  <p>&copy; 2026 Carithm. Autonomous Automotive Acoustic Research.</p>
  <p style="margin-top: 4px;"><a href="https://carithm.vercel.app/audio">Acoustic Diagnoser</a> &bull; <a href="https://carithm.vercel.app/audio/mazda">Mazda Directory</a> &bull; <a href="https://carithm.vercel.app/audio/toyota">Toyota Directory</a> &bull; <a href="https://carithm.vercel.app/audio/honda">Honda Directory</a> &bull; <a href="https://carithm.vercel.app/audio/ford">Ford Directory</a> &bull; <a href="https://carithm.vercel.app/about">About Carithm</a></p>
</footer>

</body>
</html>"""


# Main Execution
print("Writing Mazda pilot pages to:", OUTPUT_DIR)
sticky_count = 0
clean_count = 0

for p in PILOT_PAGES:
    filepath = os.path.join(OUTPUT_DIR, f"{p['slug']}.html")
    html_code = render_subpage(p)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_code)
    if p["has_sticky"]:
        sticky_count += 1
    else:
        clean_count += 1

print(f"Generated {len(PILOT_PAGES)} Mazda subpages (Group A Sticky: {sticky_count}, Group B Clean: {clean_count}).")

# Generate Mazda Brand Hub
hub_path = os.path.join(OUTPUT_DIR, "mazda.html")
with open(hub_path, "w", encoding="utf-8") as f:
    f.write(render_brand_hub())
print("Generated Mazda Brand Hub at /audio/mazda -> mazda.html")

# Create Dedicated Priority Pilot Sitemap
sitemap_urls = ['  <url>\n    <loc>https://carithm.vercel.app/audio/mazda</loc>\n    <lastmod>2026-11-07</lastmod>\n  </url>']
for p in PILOT_PAGES:
    sitemap_urls.append(f"""  <url>
    <loc>https://carithm.vercel.app/audio/{p['slug']}</loc>
    <lastmod>2026-11-07</lastmod>
  </url>""")

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>
"""

sitemap_path = "/Users/shaunaukbasu/Desktop/golden_desert/sitemap_pilot_mazda.xml"
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print(f"Created dedicated pilot sitemap at: {sitemap_path} with {len(sitemap_urls)} URLs.")
