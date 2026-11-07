#!/usr/bin/env python3
"""
Toyota Pilot Generator:
1. Generates /audio/toyota (Brand Hub) with clean hierarchy to Toyota models.
2. Generates 32 Elite Toyota sound diagnostic subpages:
   - Group A (16 pages): Scroll-triggered, slim, dismissible bottom bar + contextual CTA after DIY checks.
   - Group B (16 pages): Zero sticky bar (pure content + contextual CTA after DIY checks).
   - Responsible E-E-A-T claims (grounded mechanical TSBs, DIY tests, cost tables).
   - Contextual CTA placed right after DIY checklist ("Can't tell which one it is?").
   - Zero AdSense on subpages (100% Core Web Vitals compliant).
"""

import os
import re

OUTPUT_DIR = "/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static"

# 32 Pilot Toyota Specifications
PILOT_PAGES = [
    # --- Toyota RAV4 ---
    {
        "slug": "toyota-rav4-whining-noise",
        "title": "Toyota RAV4 Whining Noise: Transmission vs Hybrid MG2 & DIY Checks",
        "h1": "Toyota RAV4 Whining Noise Diagnostic Guide",
        "model": "Toyota RAV4",
        "years": "2013–2024",
        "noise": "Whining",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 200–500 miles",
        "area": "Transmission & Transfer Case / Hybrid MG2",
        "cost_range": "$90 – $2,800 (USD)",
        "tech_note": "On gas AWD models, high-pitched whining under light throttle often originates from transfer case pinion bearings or intermediate shaft carrier bearings. On RAV4 Hybrid / Prime models, a distinct electronic whine during deceleration is normal regenerative braking from Motor-Generator 2 (MG2).",
        "causes": "Transfer case bearing wear or low fluid, 8-speed automatic (UB80F) planetary gear whine, failing alternator decoupler pulley, or normal hybrid inverter/regenerative braking whine.",
        "checklist": [
            "Check sound behavior in Neutral: rev engine gently to 2,000 RPM in Park/Neutral; if whine disappears, the noise is drivetrain/transmission-load dependent.",
            "On Hybrid models, monitor dashboard 'CHG' needle: if high-pitch electric whine corresponds exactly with green charging gauge on deceleration, it is normal MG2 regen.",
            "Inspect transfer case and rear differential oil levels: look for dark or metallic-sheened fluid.",
            "Remove serpentine belt momentarily on cold engine: if whine ceases, inspect alternator clutch pulley and belt idler."
        ],
        "costs": [
            ("Transfer Case & Diff Fluid Service", "$110 – $190", "Fresh synthetic 75W-85 gear oil restores lubrication."),
            ("Alternator Decoupler Pulley Assembly", "$190 – $340", "Eliminates high-pitch engine-speed whine."),
            ("AWD Transfer Case / Transmission Overhaul", "$1,800 – $2,800", "Major repair if internal pinion or planetary bearings are spalled.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-rav4-humming-noise",
        "title": "Toyota RAV4 Humming Noise: Rear Differential TSB vs Wheel Bearing",
        "h1": "Toyota RAV4 Highway Humming Noise Diagnostic Guide",
        "model": "Toyota RAV4",
        "years": "2013–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–600 miles",
        "area": "Rear Differential Coupler / Wheel Hubs",
        "cost_range": "$120 – $1,400 (USD)",
        "tech_note": "A prominent low drone or hum between 40 and 65 mph on AWD RAV4s is frequently caused by the rear differential electromagnetic coupler bearing (covered by Toyota TSB-0080-13 and warranty extension). Distinguish this from hub bearing drone.",
        "causes": "Electromagnetic coupler bearing pitting (TSB-0080-13), front or rear wheel bearing assembly wear, or scalloped rear tire tread from improper alignment.",
        "checklist": [
            "Perform gentle lane sways at 50 mph: if the humming tone changes pitch or disappears when turning in one direction, suspect a wheel hub bearing.",
            "If the humming tone remains perfectly steady regardless of steering angle between 45–60 mph, suspect the rear differential coupler bearing.",
            "Run your palm across rear tire treads: jagged, feathered tread blocks ('scalloping') cause a loud tire roar that mimics bearing failure.",
            "Feel rear differential housing temperature after a 30-minute highway run: excessive heat confirms coupler bearing friction."
        ],
        "costs": [
            ("Tire Rotation & 4-Wheel Alignment", "$110 – $180", "Corrects rear toe and eliminates tire tread roaring."),
            ("Rear Wheel Bearing Hub Assembly", "$290 – $510", "Includes integrated ABS wheel speed sensor."),
            ("Rear Differential Coupler Replacement (TSB Kit)", "$850 – $1,400", "Replaces defective electromagnetic coupler unit.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-rav4-clunking-noise",
        "title": "Toyota RAV4 Clunking Noise: Control Arm Bushings vs Steering Shaft",
        "h1": "Toyota RAV4 Clunking & Popping Diagnostic Guide",
        "model": "Toyota RAV4",
        "years": "2013–2024",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 200–400 miles",
        "area": "Suspension Lower Control Arms & Steering",
        "cost_range": "$90 – $750 (USD)",
        "tech_note": "A dull pop or hollow clunk when turning into driveways, driving over speed humps, or braking to a stop is commonly caused by torn rear hydro-bushings on the front lower control arms or slip joint play in the steering intermediate shaft (TSB-0018-18).",
        "causes": "Torn front lower control arm rear bushings, worn front stabilizer bar end links, steering intermediate shaft slip joint play, or upper strut mount bearing binding.",
        "checklist": [
            "Inspect front lower control arms from underneath: look for black hydraulic fluid stains or deep rubber tearing on the large vertical rear bushings.",
            "Grip front stabilizer bar links by hand: check for vertical play in the ball-socket joints.",
            "Stationary steering test: with engine off, rapidly wiggle steering wheel 2 inches left and right; a metallic knock at your feet indicates the intermediate shaft.",
            "Drive over speed humps at an angle: clunking on diagonal suspension articulation points directly to sway bar links."
        ],
        "costs": [
            ("Front Sway Bar End Link Pair", "$120 – $210", "Eliminates low-speed chatter over rough roads."),
            ("Steering Intermediate Shaft Lubrication / Replacement", "$220 – $480", "Cures clunking felt through steering column."),
            ("Front Lower Control Arm Assembly Pair", "$460 – $750", "Replaces complete arms with pre-pressed heavy-duty bushings.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-rav4-rattling-noise",
        "title": "Toyota RAV4 Rattling Noise: 2.5L Cold Start VVT-i Gear vs Heat Shields",
        "h1": "Toyota RAV4 Cold Start & Undercarriage Rattle Guide",
        "model": "Toyota RAV4",
        "years": "2013–2024",
        "noise": "Rattling",
        "severity": "🟡 Moderate Risk",
        "urgency": "Check oil and cold start duration",
        "area": "VVT-i Cam Gear / Exhaust Heat Shields",
        "cost_range": "$40 – $1,800 (USD)",
        "tech_note": "A brief, harsh 1–3 second metallic rattle on cold morning start-ups on 2.5L engines (2AR-FE) is a documented intake camshaft VVT-i gear lock-pin failure (Toyota TSB-0041-13). A continuous rattle under acceleration is typically a loose exhaust shield clamp.",
        "causes": "Intake camshaft variable valve timing (VVT-i) gear lock-pin backlash (TSB-0041-13), rusted exhaust catalytic converter heat shield clamps, or loose rear hatch door latch striker.",
        "checklist": [
            "Cold start timing: if the harsh rattle lasts strictly 1–2 seconds upon starting cold and completely silences once oil pressure builds, the VVT gear lock pin is worn.",
            "Tap underbody exhaust shields when cold: a thin metallic buzz at 1,800–2,200 RPM is almost always a split heat shield clamp near the exhaust flex pipe.",
            "Check engine oil viscosity: verify 0W-16 or 0W-20 factory oil; incorrect thick oil delays hydraulic tensioner pressurization.",
            "Wrap electrical tape around rear hatch striker bar: if interior rattling over bumps ceases, adjust the hatch rubber bump stops."
        ],
        "costs": [
            ("Stainless Steel Exhaust Shield Clamp Fix", "$30 – $80", "Simple permanent fix for buzzing underbody heat shields."),
            ("Rear Liftgate Latch & Bumper Service", "$40 – $90", "Stops rear interior tailgate rattle."),
            ("VVT-i Camshaft Gear & Timing Kit", "$1,200 – $1,800", "Installs updated cam gear assembly per factory bulletin.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-rav4-ticking-noise",
        "title": "Toyota RAV4 Ticking Sound: D-4S Direct Injection vs Purge Valve",
        "h1": "Toyota RAV4 Engine Ticking Sound Diagnostic Guide",
        "model": "Toyota RAV4",
        "years": "2013–2024",
        "noise": "Ticking",
        "severity": "🟢 Low Risk (Normal Operation)",
        "urgency": "Inspect frequency and oil level",
        "area": "Fuel System (Direct Injection) / EVAP",
        "cost_range": "$0 – $380 (USD)",
        "tech_note": "Toyota 2.5L Dynamic Force engines utilize D-4S dual-injection (combining port and high-pressure direct fuel injectors). Direct injection pulses operate at up to 2,900 PSI, generating a noticeable mechanical click that is completely normal.",
        "causes": "High-Pressure Direct Injection Fuel Pump (HPFP) normal operation, EVAP canister purge control solenoid valve pulse, low engine oil level, or exhaust manifold gasket leak.",
        "checklist": [
            "Locate sound with engine idling: sound centered directly on top of the silver aluminum fuel pump on the valve cover is normal high-pressure injection.",
            "Touch the EVAP purge solenoid near intake manifold: rapid rhythmic clicking felt through your fingertip confirms normal emissions valve operation.",
            "Pull engine oil dipstick: confirm oil level is at full mark and viscosity is clean.",
            "Listen during cold start under load: a sharp puffing tick that speeds up with engine RPM under acceleration indicates an exhaust gasket leak."
        ],
        "costs": [
            ("Acoustic Verification / System Check", "$0", "Normal mechanical operation confirmed."),
            ("EVAP Canister Purge Solenoid Valve", "$110 – $220", "Replaces excessively loud or sticking purge valve."),
            ("Exhaust Manifold Flange Gasket", "$180 – $380", "Repairs cold-engine exhaust leak tick.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-rav4-grinding-noise",
        "title": "Toyota RAV4 Grinding Noise: Electronic Parking Brake vs Wheel Rotor Rust",
        "h1": "Toyota RAV4 Brake & Drivetrain Grinding Guide",
        "model": "Toyota RAV4",
        "years": "2013–2024",
        "noise": "Grinding",
        "severity": "🔴 High Risk (Braking Safety)",
        "urgency": "Inspect brake components immediately",
        "area": "Rear Electronic Parking Brakes / Wheel Hubs",
        "cost_range": "$80 – $580 (USD)",
        "tech_note": "On modern RAV4s with Electronic Parking Brake (EPB), rear caliper slide pins frequently seize due to road salt, causing the inner pad to wear to bare metal while the outer pad looks healthy.",
        "causes": "Worn inner brake pads grinding against brake rotor, rusted brake dust shield rubbing against rotor backing edge, or dry caliper slider pins.",
        "checklist": [
            "Inspect inner brake pads through wheel spokes: use a flashlight and mirror to verify inner pad friction lining thickness.",
            "Check if grinding occurs without braking: a constant scraping/grinding while rolling indicates a bent dust shield or seized caliper.",
            "Check wheel rim temperature after a short drive: an unusually hot rear wheel indicates a dragging parking brake caliper.",
            "Inspect brake rotor face: deep concentric gouges indicate metal-to-metal pad backing plate contact."
        ],
        "costs": [
            ("Brake Backing Plate Adjustment & Cleaning", "$40 – $90", "Frees bent dust shields touching rotor edge."),
            ("Rear Brake Caliper Slider Pin Cleaning & Lube", "$90 – $160", "Restores floating caliper movement."),
            ("Premium Ceramic Brake Pads & Rotors (Axle Pair)", "$320 – $540", "Full replacement of friction discs and pads.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-rav4-squealing-noise",
        "title": "Toyota RAV4 Squealing Noise: Serpentine Belt vs Water Pump Bearing",
        "h1": "Toyota RAV4 Engine Squeal & Chirp Diagnostic Guide",
        "model": "Toyota RAV4",
        "years": "2013–2024",
        "noise": "Squealing",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 100–300 miles",
        "area": "Serpentine Accessory Belt / Water Pump",
        "cost_range": "$70 – $550 (USD)",
        "tech_note": "A high-pitched squeal upon cold engine start or when engaging air conditioning is typically caused by serpentine belt glazing, a weakened automatic tensioner, or early water pump bearing weep.",
        "causes": "Glazed serpentine drive belt, worn automatic belt tensioner pulley, water pump bearing failure, or brake pad wear acoustic squealer clips.",
        "checklist": [
            "Spray water mist on ribbed side of belt while squealing: if noise quiets instantly, belt glazing or pulley misalignment is confirmed.",
            "Inspect belt tensioner alignment marks: if indicator arrow is past the allowable wear notch, tensioner spring has relaxed.",
            "Check bottom of water pump with flashlight: dried pink crusty coolant residue confirms water pump bearing seal failure.",
            "Test braking: if squeal only occurs while gently applying brakes, the ceramic brake pad wear indicators are alerting."
        ],
        "costs": [
            ("Serpentine Accessory Drive Belt", "$80 – $140", "Restores quiet accessory pulley drive."),
            ("Automatic Belt Tensioner Assembly", "$190 – $320", "Maintains proper factory belt tension."),
            ("Engine Water Pump Replacement", "$360 – $550", "Includes new pump, gasket, and fresh Toyota Super Long Life Coolant.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-rav4-5th-gen-2019-2024-whining-noise",
        "title": "Toyota RAV4 (2019–2024) Whining Noise: 8-Speed Direct Shift vs Hybrid eCVT",
        "h1": "Toyota RAV4 5th Gen (2019–2024) Whining Diagnostic Guide",
        "model": "Toyota RAV4 5th Gen",
        "years": "2019–2024",
        "noise": "Whining",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect transmission & fluid level",
        "area": "Direct Shift 8-Speed (UB80F) / Hybrid eCVT",
        "cost_range": "$120 – $2,800 (USD)",
        "tech_note": "Fifth-generation RAV4s (2019+) feature the Direct Shift 8-speed automatic (UB80F) on gas models, which has documented gear whine characteristics in 1st/2nd gear under light throttle. Hybrid models feature high-pitch electric motor acoustics.",
        "causes": "UB80F 8-speed transmission 1st/2nd gear meshing whine, low AWD transfer unit fluid, normal MG2 hybrid regenerative braking acoustic pitch, or electric power steering motor whine.",
        "checklist": [
            "Track whine speed: does the whine peak around 15–20 mph and shift down in pitch when shifting to 3rd gear? (Points to UB80F 1st/2nd gear meshing).",
            "On Hybrid models: does the high-pitch tone occur strictly when releasing the accelerator and coasting to a stop? (Normal regenerative braking).",
            "Inspect transfer case fill plug: ensure gear lubricant is clean and filled to bottom of fill hole.",
            "Turn steering wheel lock-to-lock in driveway: high-pitch electric whine at full lock is normal EPS motor load."
        ],
        "costs": [
            ("Transfer Case & Rear Differential Fluid Service", "$120 – $210", "Synthetic gear oil replacement per factory maintenance schedule."),
            ("Transmission ECU Software Update (TSB)", "$0 – $160", "Calibrates shift pressure mapping and reduces torque converter slip."),
            ("Transmission Assembly Replacement", "$2,400 – $3,600", "Necessary if internal planetary ring gear exhibits excessive backlash.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-rav4-5th-gen-2019-2024-humming-noise",
        "title": "Toyota RAV4 (2019–2024) Humming Noise: Dynamic Torque Vectoring vs Hubs",
        "h1": "Toyota RAV4 5th Gen (2019–2024) Humming Noise Guide",
        "model": "Toyota RAV4 5th Gen",
        "years": "2019–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300 miles",
        "area": "AWD Rear Disconnect / Wheel Bearings",
        "cost_range": "$110 – $980 (USD)",
        "tech_note": "AWD Adventure, Limited, and TRD trims feature Dynamic Torque Vectoring with rear driveline disconnect. A subtle rhythmic hum between 35 and 50 mph can indicate rear dog-clutch actuator friction or early wheel hub bearing fatigue.",
        "causes": "Dynamic torque vectoring rear disconnect clutch friction, front wheel hub assembly spalling, or factory tire inner shoulder wear.",
        "checklist": [
            "Toggle Drive Mode to 'MUD & SAND' or 'ROCK & DIRT': this forces AWD engagement; if hum disappears or alters pitch, rear disconnect is involved.",
            "Perform gentle lane shifts at 45 mph: increasing drone when loading the outside wheel points directly to a wheel hub bearing.",
            "Inspect factory all-season tires for scalloped inner tread blocks.",
            "Check rear differential fluid level and color."
        ],
        "costs": [
            ("Four-Wheel Computerized Alignment", "$110 – $180", "Prevents recurring tire feathering and road hum."),
            ("Front Wheel Bearing Hub Unit", "$310 – $540", "OEM sealed hub assembly replacement."),
            ("Rear Driveline Disconnect Actuator Service", "$420 – $850", "Calibrates or replaces electromagnetic dog clutch actuator.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-rav4-5th-gen-2019-2024-rattling-noise",
        "title": "Toyota RAV4 (2019–2024) Rattling Noise: Roof Rail Clips vs A-Pillar Buzz",
        "h1": "Toyota RAV4 5th Gen Cabin & Undercarriage Rattle Guide",
        "model": "Toyota RAV4 5th Gen",
        "years": "2019–2024",
        "noise": "Rattling",
        "severity": "🟢 Low Risk (Cabin Trim / TSB)",
        "urgency": "Inspect roof rail clip TSB",
        "area": "Exterior Roof Rails / Interior Trim",
        "cost_range": "$25 – $380 (USD)",
        "tech_note": "A documented factory issue on 2019–2021 RAV4 models involves deteriorating roof rail clip seals (Toyota Customer Support Program 22TE05), which can cause both cabin water intrusion and persistent high-speed wind rattles.",
        "causes": "Loose roof rail retaining clips (TSB / 22TE05), vibrating front A-pillar interior trim speaker cover, loose undercarriage engine splash shield clips, or rear cargo privacy cover vibration.",
        "checklist": [
            "Press firmly on exterior roof rail trim: if rails wiggle or lift, clip retainers are broken or missing orange gasket seals.",
            "Drive on coarse asphalt at 45 mph: press fingers against front windshield A-pillar speaker grilles; if buzz stops, install felt tape.",
            "Remove rear retractable cargo cover: test drive over bumps to rule out rear hatch shade spring rattle.",
            "Inspect underside plastic splash shield pins: missing push-pins allow plastic to slap against subframe."
        ],
        "costs": [
            ("Anti-Rattle Felt Tape DIY Trim Fix", "$15 – $35", "Eliminates A-pillar and center console vibrations."),
            ("Undertray Plastic Push-Pin Replacement Kit", "$20 – $45", "Secures loose underbody splash trays."),
            ("Roof Rail Retainer Clip Kit & Gasket Service (TSB)", "$160 – $380", "Installs updated orange waterproof clip retainers.")
        ],
        "has_sticky": False
    },

    # --- Toyota Camry ---
    {
        "slug": "toyota-camry-whining-noise",
        "title": "Toyota Camry Whining Noise: 8-Speed Direct Shift vs Alternator Diode",
        "h1": "Toyota Camry Whining Sound Diagnostic Guide",
        "model": "Toyota Camry",
        "years": "2012–2024",
        "noise": "Whining",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 200–500 miles",
        "area": "Transmission (UB80E) / Alternator",
        "cost_range": "$120 – $2,900 (USD)",
        "tech_note": "A high-pitched whine that tracks engine RPM is most commonly a failing alternator rectifier diode or idler pulley bearing. If the whine tracks vehicle speed in 1st/2nd gear, it is gear meshing in the UB80E 8-speed automatic.",
        "causes": "Alternator rectifier diode ripple, automatic transmission gear meshing, low transmission fluid level, or worn serpentine belt idler pulley.",
        "checklist": [
            "Rev engine in Park: if whine pitch directly rises and falls with RPM while stationary, the issue is on the engine accessory belt (alternator or idler).",
            "Listen through radio speakers: electrical whine that increases with accelerator pedal indicates alternator diode voltage ripple.",
            "Drive at 15–25 mph in 2nd gear: if whine is audible only in lower gears under load and silences on highway cruise, transmission gear acoustic profile is responsible.",
            "Check transmission fluid pan for weeping or low fluid level."
        ],
        "costs": [
            ("Serpentine Belt Idler & Tensioner Pulley", "$140 – $260", "Restores smooth rotating bearing operation."),
            ("OEM Alternator Replacement", "$340 – $560", "Eliminates electrical whine and restores clean DC charging."),
            ("Transmission Fluid Exchange & Filter", "$180 – $310", "Fresh Toyota WS fluid cures hydraulic pump cavitation.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-camry-humming-noise",
        "title": "Toyota Camry Humming Noise: Front Wheel Hub Bearings vs Tire Feathering",
        "h1": "Toyota Camry Highway Humming Noise Diagnostic Guide",
        "model": "Toyota Camry",
        "years": "2012–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–500 miles",
        "area": "Front Wheel Hub Assemblies / Tires",
        "cost_range": "$110 – $520 (USD)",
        "tech_note": "A persistent low-frequency drone or hum between 45 and 75 mph that resembles driving over a rumble strip is predominantly a failing front wheel hub unit-bearing.",
        "causes": "Front wheel bearing internal race pitting, rear hub assembly wear, or cupped inner tire tread from worn rear strut dampers.",
        "checklist": [
            "Weave gently inside your lane at 55 mph: if turning left makes the humming louder, the right wheel bearing is damaged (and vice-versa).",
            "Jack up front corner and spin wheel by hand while holding suspension spring: vibration felt through the coil spring confirms bearing spalling.",
            "Inspect front and rear tire treads for uneven scalloped wear.",
            "Check CV axle boots for tears or grease loss."
        ],
        "costs": [
            ("Tire Rotation & Balance", "$40 – $80", "Rules out wheel balance and tire tread cupping."),
            ("Four-Wheel Computerized Alignment", "$110 – $180", "Restores true tracking and stops tire feathering."),
            ("Front Wheel Bearing & Hub Assembly", "$280 – $490", "Complete sealed OEM hub unit with ABS sensor.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-camry-rattling-noise",
        "title": "Toyota Camry Rattling Noise: 2.5L Cold Start Cam Gear TSB vs Heat Shields",
        "h1": "Toyota Camry Cold Start & Exhaust Rattle Diagnostic Guide",
        "model": "Toyota Camry",
        "years": "2012–2024",
        "noise": "Rattling",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect oil level and cold start rattle",
        "area": "VVT-i Cam Phaser / Exhaust Flange",
        "cost_range": "$40 – $1,850 (USD)",
        "tech_note": "A 1–2 second harsh rattle on cold starts on 2.5L (2AR-FE / A25A) engines is the variable valve timing (VVT-i) gear locking pin releasing late (Toyota TSB-0041-13). A metallic buzz at 2,000 RPM is an exhaust donut gasket or shield clamp.",
        "causes": "Intake camshaft VVT-i phaser gear pin wear, exhaust manifold heat shield weld crack, intermediate exhaust pipe donut gasket degradation, or loose engine cowl clips.",
        "checklist": [
            "Monitor cold morning startup: if rattle occurs for 1–2 seconds immediately as engine catches and then disappears completely, VVT-i cam phaser pin has play.",
            "Tap catalytic converter heat shields with gloved fist when exhaust is cold: metallic buzzing confirms broken weld.",
            "Inspect intermediate exhaust flex joint: rusted flange bolts cause donut gasket vibration under acceleration.",
            "Verify engine oil viscosity: always use Toyota genuine 0W-16 or 0W-20."
        ],
        "costs": [
            ("Exhaust Flange Donut Gasket & Spring Bolts", "$90 – $180", "Cures acceleration exhaust buzz."),
            ("Stainless Heat Shield Clamps", "$35 – $75", "Secures loose undercarriage shields."),
            ("VVT-i Camshaft Gear & Timing Kit (TSB)", "$1,250 – $1,850", "Installs updated cam phaser and timing chain set.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-camry-ticking-noise",
        "title": "Toyota Camry Ticking Sound: D-4S Direct Injection vs EVAP Purge Solenoid",
        "h1": "Toyota Camry Engine Ticking Sound Diagnostic Guide",
        "model": "Toyota Camry",
        "years": "2012–2024",
        "noise": "Ticking",
        "severity": "🟢 Low Risk (Normal Acoustic Profile)",
        "urgency": "Check oil level and injector pulse",
        "area": "High-Pressure Direct Injection / Valvetrain",
        "cost_range": "$0 – $360 (USD)",
        "tech_note": "Toyota D-4S direct-injection engines (2.5L 4-cylinder and 3.5L V6) utilize a mechanical camshaft-driven high pressure fuel pump. A rhythmic, sharp ticking sound at idle is normal high-pressure injection operation.",
        "causes": "Direct injection high-pressure pump (HPFP) normal operation, EVAP canister purge control valve clicking, low engine oil level, or worn hydraulic valve lifters.",
        "checklist": [
            "Open hood while idling: if ticking is loudest near the rear passenger side of cylinder head, it is the mechanical HPFP.",
            "Place hand on EVAP purge valve mounted near intake: if ticking pulses in sync with valve vibration, operation is normal.",
            "Check engine oil dipstick: low oil reduces hydraulic lifter cushioning and increases valvetrain tick.",
            "Increase engine RPM to 2,500: direct-injection ticks increase in rate but maintain uniform sound without harsh clatter."
        ],
        "costs": [
            ("Acoustic Verification / DIY Diagnostic Check", "$0", "Normal D-4S mechanical pulse verified."),
            ("Engine Oil & Filter Service (0W-16/0W-20)", "$65 – $95", "Restores optimal hydraulic lifter lubrication."),
            ("EVAP Purge Solenoid Replacement", "$110 – $220", "Replaces excessively loud or failing emissions purge valve.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-camry-clunking-noise",
        "title": "Toyota Camry Clunking Noise: Front Strut Mounts vs Sway Bar Links",
        "h1": "Toyota Camry Front Suspension Clunking Diagnostic Guide",
        "model": "Toyota Camry",
        "years": "2012–2024",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 200–400 miles",
        "area": "Front Struts & Stabilizer Bar Links",
        "cost_range": "$110 – $680 (USD)",
        "tech_note": "A popping or hollow clunk when steering at low speeds or driving over small driveway bumps is most frequently caused by worn front upper strut bearing plates or loose stabilizer end link ball joints.",
        "causes": "Worn upper strut mount bearings, front sway bar end links, steering intermediate shaft play, or lower control arm bushing tears.",
        "checklist": [
            "Have a helper turn steering wheel while holding front coil spring: a spring that 'jumps' or vibrates with a pop indicates a binding strut bearing.",
            "Drive over driveway curb cutouts: sharp metallic knocking from wheel corners indicates sway bar end link ball joint slack.",
            "Check steering intermediate shaft: wiggle wheel rapidly left/right with engine off to test slip joint knock.",
            "Inspect control arm rear hydro-bushings for cracking or fluid seepage."
        ],
        "costs": [
            ("Front Sway Bar End Link Pair", "$120 – $220", "Restores quiet, tight suspension over road bumps."),
            ("Front Upper Strut Mounts & Bearings", "$310 – $520", "Eliminates steering pops and binding."),
            ("Steering Intermediate Shaft Assembly", "$240 – $460", "Stops steering column footwell clunking.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-camry-grinding-noise",
        "title": "Toyota Camry Grinding Noise: Brake Pad Backing vs Caliper Slide Pins",
        "h1": "Toyota Camry Brake Grinding Diagnostic Guide",
        "model": "Toyota Camry",
        "years": "2012–2024",
        "noise": "Grinding",
        "severity": "🔴 High Risk (Braking Hazard)",
        "urgency": "Inspect brake friction immediately",
        "area": "Braking System / Caliper Hardware",
        "cost_range": "$90 – $510 (USD)",
        "tech_note": "A harsh metal-on-metal grinding when braking indicates brake pad friction material is completely depleted, allowing the steel backing plate to contact the cast iron rotor.",
        "causes": "Worn brake pads grinding on rotor surface, seized caliper slide pins causing tapered pad wear, or a bent dust shield contacting rotor edge.",
        "checklist": [
            "Inspect brake rotor face: look for deep silver circular grooves indicating metal backing plate contact.",
            "Check inner brake pad thickness: inner pads often wear twice as fast as outer pads if caliper slide pins are dry.",
            "Test braking behavior: does vehicle pull to one side under braking? (Indicates a seized caliper slide pin).",
            "Inspect brake dust shield clearance: ensure at least 5mm clearance all around rotor perimeter."
        ],
        "costs": [
            ("Brake Dust Shield Adjustment", "$30 – $70", "Bends back rubbing sheet metal."),
            ("Caliper Slide Pin Service & Synthetic Lube", "$90 – $150", "Restores even caliper sliding motion."),
            ("Front Brake Pads & Rotors Complete Kit", "$290 – $490", "Installs premium ceramic pads and balanced discs.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-camry-squealing-noise",
        "title": "Toyota Camry Squealing Noise: Serpentine Belt Slip vs AC Compressor Clutch",
        "h1": "Toyota Camry Engine Belt Squeal Diagnostic Guide",
        "model": "Toyota Camry",
        "years": "2012–2024",
        "noise": "Squealing",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 150–300 miles",
        "area": "Serpentine Belt / AC Compressor",
        "cost_range": "$75 – $480 (USD)",
        "tech_note": "A loud squeal that occurs upon cold startup or when switching on the defrost / air conditioning is caused by serpentine belt slippage over the alternator or AC compressor pulley.",
        "causes": "Glazed or oily serpentine belt, automatic belt tensioner spring fatigue, AC compressor clutch bearing slip, or brake pad acoustic wear tabs.",
        "checklist": [
            "Turn on AC and headlights: if squeal begins or gets louder with heavy electrical and AC load, belt slippage is verified.",
            "Check serpentine belt ribs with engine off: look for micro-cracking, shiny glazed rubber, or oil contamination from front crank seal.",
            "Inspect tensioner wear indicator: ensure pointer is within acceptable range.",
            "Apply brakes gently at 20 mph: if squeal only occurs during braking, replace worn brake pads."
        ],
        "costs": [
            ("Serpentine Accessory Drive Belt", "$75 – $130", "Replaces glazed or stretched EPDM belt."),
            ("Automatic Belt Tensioner Assembly", "$180 – $310", "Maintains calibrated belt tension."),
            ("Brake Pad Replacement (Axle Pair)", "$190 – $340", "Silences brake acoustic wear indicator tabs.")
        ],
        "has_sticky": True
    },

    # --- Toyota Corolla ---
    {
        "slug": "toyota-corolla-humming-noise",
        "title": "Toyota Corolla Humming Noise: Rear Wheel Bearing Hub vs Tire Cupping",
        "h1": "Toyota Corolla Highway Humming Noise Diagnostic Guide",
        "model": "Toyota Corolla",
        "years": "2014–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–600 miles",
        "area": "Rear Wheel Hub Bearings / Tires",
        "cost_range": "$90 – $450 (USD)",
        "tech_note": "Rear wheel bearing hub unit assemblies on E170 and E210 Corolla chassis are one of the most frequently replaced suspension wear items after 70,000 miles, producing a loud cockpit drone above 40 mph.",
        "causes": "Sealed rear wheel bearing hub unit spalling, front wheel bearing wear, or cupped rear tires due to torsion beam suspension geometry.",
        "checklist": [
            "Weave gently in lane at 50 mph: if drone gets louder when turning right, the left wheel bearing is damaged.",
            "Spin rear wheels by hand with car safely raised: listen for roughness or rumbling from the center hub bearing.",
            "Inspect rear tire tread blocks: run hand across inner tread edge to feel for high-and-low saw-tooth cupping.",
            "Verify hub temperature after highway trip: a failing bearing will be hot to the touch compared to opposite side."
        ],
        "costs": [
            ("Rear Wheel Bearing Hub Assembly (Complete Unit)", "$240 – $420", "Bolt-on replacement with integrated ABS sensor."),
            ("Tire Rotation, Wheel Balance & Alignment", "$110 – $170", "Corrects tire wear noise and extends tire life."),
            ("Front Wheel Bearing Press Service", "$280 – $460", "Includes machine pressing and hub install.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-corolla-whining-noise",
        "title": "Toyota Corolla Whining Noise: Super CVT-i Transmission vs Alternator",
        "h1": "Toyota Corolla CVT & Engine Whining Diagnostic Guide",
        "model": "Toyota Corolla",
        "years": "2014–2024",
        "noise": "Whining",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect CVT fluid and alternator",
        "area": "Super CVT-i Transmission / Alternator",
        "cost_range": "$120 – $3,200 (USD)",
        "tech_note": "On modern Corollas equipped with the Super CVT-i (or Direct-Shift CVT with physical 1st launch gear), high-pitch whining on acceleration can indicate fluid degradation or belt/pulley wear.",
        "causes": "CVT transmission fluid breakdown, CVT hydraulic pump cavitation, failing alternator rectifier diode, or worn idler pulley bearings.",
        "checklist": [
            "Rev engine in Neutral: if whine rises with RPM in Park/Neutral, the noise is from the alternator or belt pulley, not the transmission.",
            "Accelerate smoothly from 0 to 45 mph: metallic whine that changes tone smoothly without distinct shift points points to the CVT transmission.",
            "Check transmission service history: Toyota CVT-FE fluid should be exchanged every 60,000 miles to prevent hydraulic valve whine.",
            "Listen near alternator with mechanic's stethoscope to isolate bearing whine."
        ],
        "costs": [
            ("Genuine Toyota CVT-FE Fluid Exchange", "$180 – $280", "Restores proper CVT hydraulic pressure and quiet operation."),
            ("OEM Alternator Replacement", "$310 – $520", "Replaces whining charging system diode assembly."),
            ("CVT Transmission Assembly Replacement", "$2,800 – $4,200", "Major repair if internal steel drive belt or conical pulleys are scored.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-corolla-rattling-noise",
        "title": "Toyota Corolla Rattling Noise: Exhaust Heat Shields vs Undertray",
        "h1": "Toyota Corolla Undercarriage & Exhaust Rattle Guide",
        "model": "Toyota Corolla",
        "years": "2014–2024",
        "noise": "Rattling",
        "severity": "🟢 Low Risk (Nuisance)",
        "urgency": "Inspect exhaust clamps at convenience",
        "area": "Exhaust Manifold Heat Shield / Undertray",
        "cost_range": "$25 – $240 (USD)",
        "tech_note": "The thin aluminum heat shield bolted above the exhaust manifold and catalytic converter frequently fractures at the bolt mounting eyelets, creating an annoying metallic buzz around 1,800–2,200 RPM.",
        "causes": "Fractured exhaust manifold heat shield mounts, catalytic converter pipe shield corrosion, loose plastic engine splash undertray fasteners, or glovebox rattle.",
        "checklist": [
            "Rev engine gently to 2,000 RPM in driveway: if a metallic buzz resonates at specific RPMs, inspect exhaust heat shields.",
            "Tap catalytic converter heat shield when cold: loose shields will rattle distinctly against the pipe.",
            "Inspect underside plastic undertray: missing nylon fasteners allow plastic panel to flap at speed.",
            "Empty glovebox and center console: verify rattle is not personal items vibrating in plastic trays."
        ],
        "costs": [
            ("Stainless Steel Worm-Gear Shield Clamp Fix", "$25 – $65", "Permanent DIY or shop clamp securing loose shield."),
            ("OEM Splash Shield Fastener Clip Kit", "$20 – $40", "Secures sagging plastic engine covers."),
            ("Exhaust Flange Donut Gasket & Spring Kit", "$110 – $190", "Silences vibrating mid-pipe exhaust joint.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-corolla-ticking-noise",
        "title": "Toyota Corolla Ticking Sound: Valvetrain Lash vs High-Pressure Injectors",
        "h1": "Toyota Corolla Engine Ticking Sound Diagnostic Guide",
        "model": "Toyota Corolla",
        "years": "2014–2024",
        "noise": "Ticking",
        "severity": "🟢 Low Risk (Normal Operation)",
        "urgency": "Check oil level and injector cycle",
        "area": "Valvetrain (2ZR-FE) / Direct Injection (M20A)",
        "cost_range": "$0 – $320 (USD)",
        "tech_note": "On 1.8L (2ZR-FE) models, mild valvetrain ticking can occur if oil level is low. On 2.0L Dynamic Force (M20A-FKS) engines, D-4S direct-injection fuel pumps emit a rapid, uniform mechanical click that is completely normal.",
        "causes": "High-pressure direct fuel injector pulse (normal), EVAP canister purge valve clicking, low engine oil level, or cold hydraulic valve lash adjuster tick.",
        "checklist": [
            "Check oil dipstick: ensure oil is at the full mark with proper 0W-16/0W-20 viscosity.",
            "Listen with hood open: rapid sewing-machine-like clicking centered over the cylinder head is normal injector operation.",
            "Feel the EVAP purge solenoid: rapid clicking pulses felt through valve body confirm normal vapor purge.",
            "Notice if ticking quiets when engine warms: cold oil takes a few minutes to fully pump hydraulic lash adjusters."
        ],
        "costs": [
            ("DIY Inspection & Acoustic Verification", "$0", "Normal mechanical operation confirmed."),
            ("Synthetic Engine Oil & OEM Filter Change", "$55 – $85", "Ensures correct lubrication for hydraulic lifters."),
            ("EVAP Purge Solenoid Valve Replacement", "$95 – $190", "Cures excessively loud emissions valve tick.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-corolla-clunking-noise",
        "title": "Toyota Corolla Clunking Noise: Sway Bar End Links vs Torsion Bushings",
        "h1": "Toyota Corolla Suspension Clunking Diagnostic Guide",
        "model": "Toyota Corolla",
        "years": "2014–2024",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 200–400 miles",
        "area": "Front Stabilizer Links / Rear Torsion Beam",
        "cost_range": "$95 – $540 (USD)",
        "tech_note": "A hollow knocking or chucking noise over broken pavement or speed humps is primarily caused by worn front sway bar end links or degraded rear torsion beam axle pivot bushings.",
        "causes": "Front sway bar link ball joint play, front strut upper bearing wear, worn rear torsion beam axle bushings, or loose motor mount torque strut.",
        "checklist": [
            "Drive over speed humps at an angle: chucking noise from front wheel corners indicates worn stabilizer links.",
            "Grab front sway bar links with vehicle on ground: any play or clicking indicates ball joint failure.",
            "Inspect rear torsion beam bushings: dry rot or rubber separation produces rear suspension thumping over dips.",
            "Check upper engine torque strut mount ('dogbone mount') for cracked rubber."
        ],
        "costs": [
            ("Front Sway Bar End Link Pair", "$110 – $190", "Restores quiet, firm suspension over city streets."),
            ("Upper Engine Torque Strut Mount", "$120 – $220", "Stops engine rocking and shifting thumps."),
            ("Front Strut & Mount Assemblies (Pair)", "$360 – $540", "Restores factory ride quality and eliminates strut clunk.")
        ],
        "has_sticky": True
    },

    # --- Toyota Highlander ---
    {
        "slug": "toyota-highlander-rattling-noise",
        "title": "Toyota Highlander Rattling Noise: 3.5L Timing Chain vs Liftgate Latch",
        "h1": "Toyota Highlander Rattling Noise Diagnostic Guide",
        "model": "Toyota Highlander",
        "years": "2014–2024",
        "noise": "Rattling",
        "severity": "🟡 Moderate Risk",
        "urgency": "Check cold start and rear hatch",
        "area": "Timing Chain (2GR-FE/FKS) / Power Liftgate",
        "cost_range": "$40 – $2,200 (USD)",
        "tech_note": "On 3.5L V6 models, brief startup rattle can occur from timing chain hydraulic tensioner bleed-down. Interior rear rattles over highway bumps are almost universally misadjusted power liftgate bump stops or latch strikers.",
        "causes": "Timing chain hydraulic tensioner bleed-down, loose exhaust intermediate pipe heat shield, power liftgate latch striker play, or panoramic sunroof seal rattle.",
        "checklist": [
            "Cold start timing check: if rattle lasts 1–3 seconds only on cold morning starts and silences, monitor timing tensioner.",
            "Adjust rear liftgate rubber bump stops: turn rubber stops counter-clockwise 1/2 turn to preload tailgate latch against weatherstrip.",
            "Inspect underside exhaust shields when cold: tap catalytic converter brackets for cracked welds.",
            "Clean and lubricate panoramic sunroof seals with Krytox fluorinated grease."
        ],
        "costs": [
            ("Liftgate Bump Stop & Striker Adjustment", "$0 – $50", "Instant fix for rear cabin cargo rattle."),
            ("Exhaust Heat Shield Clamp Kit", "$35 – $80", "Silences underbody buzzing under throttle."),
            ("Timing Chain Tensioner & Guide Service", "$1,400 – $2,200", "Major repair for high-mileage V6 valvetrain rattle.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-highlander-humming-noise",
        "title": "Toyota Highlander Humming Noise: Center Driveshaft Support vs Hubs",
        "h1": "Toyota Highlander Highway Humming Drone Diagnostic Guide",
        "model": "Toyota Highlander",
        "years": "2014–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–600 miles",
        "area": "Driveshaft Center Carrier Bearing / Wheel Hubs",
        "cost_range": "$120 – $750 (USD)",
        "tech_note": "A mid-vehicle humming or low drone between 45 and 65 mph on AWD Highlanders frequently originates from the driveshaft center support carrier bearing rubber mount tearing or bearing race spalling.",
        "causes": "Two-piece propeller shaft center support bearing failure, front/rear wheel bearing unit fatigue, rear differential coupler wear, or scalloped all-terrain tires.",
        "checklist": [
            "Locate drone sound in vehicle: a hum centered directly beneath the middle row seats points to the driveshaft center carrier bearing.",
            "Weave gently inside your lane at 50 mph: if tone changes pitch under lateral load, suspect a wheel hub bearing.",
            "Inspect center driveshaft carrier bearing: grab driveshaft and shake; excessive radial play or torn rubber surround confirms failure.",
            "Feel wheel hubs for abnormal heat build-up after highway cruise."
        ],
        "costs": [
            ("Tire Rotation & 4-Wheel Computerized Alignment", "$110 – $180", "Eliminates uneven tire tread roaring."),
            ("Front / Rear Wheel Hub Assembly", "$310 – $520", "OEM sealed hub unit replacement."),
            ("Driveshaft Center Support Bearing Assembly", "$380 – $680", "Eliminates mid-driveline vibration and drone.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-highlander-whining-noise",
        "title": "Toyota Highlander Whining Noise: UA80 8-Speed Automatic vs Steering",
        "h1": "Toyota Highlander Transmission & Steering Whine Guide",
        "model": "Toyota Highlander",
        "years": "2014–2024",
        "noise": "Whining",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect transmission fluid level",
        "area": "UA80 8-Speed Automatic / Electric Power Steering",
        "cost_range": "$140 – $3,100 (USD)",
        "tech_note": "Highlanders equipped with the Direct Shift 8-speed automatic (UA80) can exhibit gear meshing whine in 1st/2nd gear under gentle acceleration. Power steering electric motor whine is normal at full steering lock.",
        "causes": "UA80 8-speed automatic planetary gear meshing, low transmission fluid level, electric power steering rack load, or failing alternator diode.",
        "checklist": [
            "Test gear dependency: if whine occurs only in 1st/2nd gear and drops in pitch upon upshift, transmission gear acoustic profile is responsible.",
            "Stationary full-lock turn: electric steering whine is normal only at maximum steering angle in parking lots.",
            "Rev engine in Neutral: electrical whining that rises with RPM points to alternator diode ripple or idler pulley.",
            "Inspect transmission pan for fluid seepage."
        ],
        "costs": [
            ("Alternator Decoupler Pulley / Belt Service", "$140 – $280", "Eliminates engine accessory whine."),
            ("Transmission Fluid Level Check & Drain/Fill", "$160 – $280", "Fresh Toyota WS fluid cures hydraulic aeration."),
            ("Transmission Assembly Overhaul", "$2,600 – $3,800", "Necessary if internal planetary gear bearings fail.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-highlander-clunking-noise",
        "title": "Toyota Highlander Clunking Noise: Control Arm Hydro-Bushings vs Struts",
        "h1": "Toyota Highlander Suspension Clunking Diagnostic Guide",
        "model": "Toyota Highlander",
        "years": "2014–2024",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 200–400 miles",
        "area": "Front Control Arms & Upper Strut Mounts",
        "cost_range": "$120 – $880 (USD)",
        "tech_note": "Due to the Highlander's curb weight, the front lower control arm rear hydraulic compliance bushings are prone to fluid leakage and tearing, producing a distinct clunk when tapping the brakes or hitting dips.",
        "causes": "Torn front lower control arm hydro-bushings, worn front stabilizer end links, upper strut mount bearing binding, or steering intermediate shaft slip joint.",
        "checklist": [
            "Brake tap test at 10 mph: apply brakes sharply; a forward lurch accompanied by a dull clunk indicates torn control arm rear hydro-bushings.",
            "Visual inspection: look for black hydraulic fluid leaked around the rear vertical control arm bushings.",
            "Drive over speed humps diagonally: chucking noise from front corners points to sway bar end link wear.",
            "Check steering intermediate shaft slip joint for footwell knock."
        ],
        "costs": [
            ("Front Sway Bar End Link Pair", "$130 – $220", "Stops low-speed rattling over potholes."),
            ("Front Lower Control Arm Assembly Pair", "$490 – $880", "Replaces complete arms with pre-pressed heavy-duty bushings."),
            ("Upper Strut Mounts & Front Struts", "$420 – $750", "Eliminates steering popping and restores smooth damping.")
        ],
        "has_sticky": True
    },

    # --- Toyota Tacoma ---
    {
        "slug": "toyota-tacoma-humming-noise",
        "title": "Toyota Tacoma Humming Noise: Front Differential Needle Bearing vs ECGS Bushing",
        "h1": "Toyota Tacoma Front Differential Humming (ECGS Fix) Guide",
        "model": "Toyota Tacoma",
        "years": "2016–2023",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect front diff needle bearing",
        "area": "Front Differential Needle Bearing / Hubs",
        "cost_range": "$110 – $650 (USD)",
        "tech_note": "The famous Tacoma front driver-side differential needle bearing vibration/hum between 30 and 55 mph occurs on 3rd Gen Tacomas (especially lifted trucks). Shifting into 4WD loads the cv axle and silences the noise instantly (solved by ECGS solid bronze bushing).",
        "causes": "Front differential driver-side needle bearing slop (cured by ECGS solid bronze bushing), front wheel hub unit-bearing wear, or aggressive all-terrain tire hum.",
        "checklist": [
            "The 4WD Test: when the hum/vibration occurs at 40 mph, safely switch from 2WD to 4WD (4H) in a straight line; if the hum instantly disappears, the front differential needle bearing is confirmed.",
            "Inspect driver-side front CV axle stub where it enters differential: excessive radial up-down play confirms needle bearing wear.",
            "Inspect all-terrain tires for scalloped inner or outer tread blocks.",
            "Check front differential gear oil level and condition."
        ],
        "costs": [
            ("Front Differential Fluid Service (75W-85 Synthetic)", "$90 – $160", "Fresh lubricant service."),
            ("ECGS Solid Bronze Bushing & Seal Upgrade", "$280 – $520", "Permanent aftermarket fix replacing failure-prone needle bearing."),
            ("Front Wheel Bearing Hub Assembly", "$310 – $540", "Complete unit-bearing replacement.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-tacoma-rattling-noise",
        "title": "Toyota Tacoma Rattling Noise: Skid Plate Bolts vs Direct Injection Cleaning",
        "h1": "Toyota Tacoma Skid Plate & Engine Rattle Guide",
        "model": "Toyota Tacoma",
        "years": "2016–2023",
        "noise": "Rattling",
        "severity": "🟢 Low Risk (Inspection Required)",
        "urgency": "Inspect skid plate hardware",
        "area": "Engine Skid Plates / Direct Injection",
        "cost_range": "$15 – $280 (USD)",
        "tech_note": "After oil changes, technicians frequently omit rubber isolating washers or strip the rear bolts on the steel engine skid plate, causing severe metallic buzzing under acceleration or over washboard roads.",
        "causes": "Loose front skid plate mounting bolts or missing rubber isolators, 3.5L V6 direct-injection self-cleaning mode rattle, or catalytic converter heat shield weld failure.",
        "checklist": [
            "Tap front steel skid plate with a rubber mallet: a loud buzz or hollow vibration confirms loose mounting bolts.",
            "Inspect skid plate bolt holes: check for stripped crossmember threads or missing rubber isolating grommets.",
            "Notice sound during hot idle: 3.5L 2GR-FKS engine runs an automated direct-injector cleaning mode that sounds like a mechanical rattle for 10 minutes (normal).",
            "Inspect catalytic converter heat shields near transmission crossmember."
        ],
        "costs": [
            ("Skid Plate Hardware & Rubber Isolator Kit", "$15 – $45", "Fast DIY fix securing skid plate."),
            ("Stainless Steel Heat Shield Clamp Kit", "$35 – $75", "Secures loose exhaust heat shields."),
            ("Exhaust Crossover Pipe Gasket Replacement", "$120 – $220", "Stops exhaust vibration rattle.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-tacoma-ticking-noise",
        "title": "Toyota Tacoma Ticking Sound: The 'Taco Tick' vs Manifold Studs",
        "h1": "Toyota Tacoma 'Taco Tick' Sound Diagnostic Guide",
        "model": "Toyota Tacoma",
        "years": "2016–2023",
        "noise": "Ticking",
        "severity": "🟢 Low Risk (Normal Tacoma Characteristic)",
        "urgency": "Verify Taco Tick vs exhaust leak",
        "area": "D-4S Dual Injection / Exhaust Manifolds",
        "cost_range": "$0 – $650 (USD)",
        "tech_note": "The legendary 'Taco Tick' on the 3.5L V6 (2GR-FKS) is caused by the engine alternating between port injection and direct high-pressure injection, including an automated self-cleaning cycle that produces a distinct, loud mechanical click.",
        "causes": "D-4S direct-injection cleaning cycle ('Taco Tick' - completely normal), EVAP canister purge valve pulsing against firewall, or broken exhaust manifold stud.",
        "checklist": [
            "Determine if ticking comes and goes: if engine idles quietly for 15 minutes, then starts a loud rhythmic tick for 10 minutes, that is the automated D-4S injector cleaning cycle.",
            "Touch the EVAP purge solenoid on driver inner fender: rapid clicking felt in sync with sound confirms normal emissions valve operation.",
            "Listen during cold morning startup under throttle: a ticking that sounds like an air puff and accelerates with RPM indicates an exhaust manifold stud leak.",
            "Check engine oil dipstick to verify proper lubrication."
        ],
        "costs": [
            ("Acoustic Diagnostic Verification", "$0", "Normal 'Taco Tick' mechanical cycle confirmed."),
            ("EVAP Purge Valve Replacement", "$110 – $220", "Replaces loud or clicking purge solenoid."),
            ("Exhaust Manifold Gasket & Stud Repair", "$450 – $750", "Repairs exhaust manifold flange leak if detected.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-tacoma-clunking-noise",
        "title": "Toyota Tacoma Clunking Noise: Driveshaft Slip Yoke Bump vs Leaf Springs",
        "h1": "Toyota Tacoma Driveshaft Slip Yoke Clunk Guide",
        "model": "Toyota Tacoma",
        "years": "2016–2023",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Grease slip yoke within 500 miles",
        "area": "Driveshaft Slip Yoke / Rear Leaf Springs",
        "cost_range": "$40 – $520 (USD)",
        "tech_note": "A distinct 'bump from behind' or clunk felt when coming to a complete stop or taking off from a red light is caused by the rear driveshaft slip yoke splines binding from dry lubrication.",
        "causes": "Driveshaft slip yoke splines dry binding (axle wrap / slip yoke bump), rear leaf spring friction pad wear, or front sway bar end link slack.",
        "checklist": [
            "Come to a smooth complete stop: if you feel a delayed bump from behind 1 second after stopping, rear slip yoke splines are binding.",
            "Accelerate gently from a stop: a clunk upon pedal tip-in confirms slip yoke spline release.",
            "Inspect rear leaf spring friction pads: worn nylon pads between leaf spring leaves cause clicking/clunking over uneven road beds.",
            "Inspect front sway bar end links and ball joints."
        ],
        "costs": [
            ("Slip Yoke Clean & PTFE Grease Service", "$50 – $110", "Cleans splines and applies high-pressure PTFE lubricant."),
            ("Leaf Spring Anti-Friction Pad Kit", "$40 – $95", "Eliminates leaf spring slap and creaks."),
            ("Heavy-Duty U-Joint & Carrier Bearing Service", "$280 – $480", "Replaces worn universal joints and driveshaft center support.")
        ],
        "has_sticky": True
    },

    # --- Toyota 4Runner ---
    {
        "slug": "toyota-4runner-clunking-noise",
        "title": "Toyota 4Runner Clunking Noise: Propeller Shaft Slip Yoke vs KDSS Bushings",
        "h1": "Toyota 4Runner Driveline Clunk & KDSS Diagnostic Guide",
        "model": "Toyota 4Runner",
        "years": "2014–2024",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Lube driveshaft grease zerks",
        "area": "Driveshaft Slip Yoke / KDSS Stabilizer",
        "cost_range": "$30 – $580 (USD)",
        "tech_note": "A bump from behind when stopping or taking off is caused by dry driveshaft slip yoke splines. On Trail/TRD Off-Road models with KDSS, clunking over washboard terrain can indicate accumulator valve noise or worn stabilizer bushings.",
        "causes": "Dry propeller shaft slip yoke splines (requires moly-grease via zerk fittings), KDSS sway bar bushing wear, front sway bar links, or upper control arm ball joints.",
        "checklist": [
            "Grease zerk check: 4Runners have grease zerks on the driveshaft spider joints and slip yoke; when was it last lubricated with moly-lithium grease?",
            "Notice if clunk occurs 1 second after coming to a full stop: confirms slip yoke spline binding.",
            "On KDSS-equipped models: check KDSS hydraulic cylinder boots for leaks or cracked rubber bushings.",
            "Drive over washboard gravel: front corner clatter indicates sway bar end link ball joint slack."
        ],
        "costs": [
            ("Driveshaft Spider & Slip Yoke Lube Service", "$40 – $85", "Greases all driveshaft fittings with genuine moly grease."),
            ("Front Sway Bar End Link Pair", "$120 – $210", "Restores tight front stabilizer control."),
            ("KDSS Stabilizer Bushing Replacement", "$240 – $480", "Silences hydraulic sway bar articulation.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-4runner-humming-noise",
        "title": "Toyota 4Runner Humming Noise: Front Unit-Bearings vs Mud Terrain Tires",
        "h1": "Toyota 4Runner Highway Humming Noise Diagnostic Guide",
        "model": "Toyota 4Runner",
        "years": "2014–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–600 miles",
        "area": "Front Wheel Hub Assemblies / All-Terrain Tires",
        "cost_range": "$90 – $560 (USD)",
        "tech_note": "A heavy roar or hum at 45–65 mph is most commonly either aggressive all-terrain/mud-terrain tire cupping or a worn front wheel unit-bearing hub assembly.",
        "causes": "Front wheel bearing hub assembly wear, tire tread scalloping from lack of 5-tire rotation, or transfer case output bearing wear.",
        "checklist": [
            "Perform gentle lane changes at 50 mph: if drone pitch increases when loading one side of the vehicle, a wheel bearing is failing.",
            "Check tire tread wear: run palm across tread; uneven, jagged lug edges generate an identical roar to a bad bearing.",
            "Check transfer case and front/rear differential fluid levels.",
            "Spin front wheels while holding coil spring: roughness confirms wheel bearing race pitting."
        ],
        "costs": [
            ("Tire Rotation & High-Speed Road Force Balance", "$60 – $110", "Rules out tire cupping and tread roar."),
            ("Front Wheel Hub & Bearing Assembly", "$320 – $540", "Complete pre-pressed hub unit replacement."),
            ("Transfer Case & Differential Fluid Service", "$140 – $240", "Fresh synthetic 75W-90 restores quiet gear meshing.")
        ],
        "has_sticky": True
    },
    {
        "slug": "toyota-4runner-rattling-noise",
        "title": "Toyota 4Runner Rattling Noise: Front Skid Plate vs Rear Window Regulator",
        "h1": "Toyota 4Runner Skid Plate & Cargo Rattle Guide",
        "model": "Toyota 4Runner",
        "years": "2014–2024",
        "noise": "Rattling",
        "severity": "🟢 Low Risk (Nuisance)",
        "urgency": "Inspect skid plate bolts",
        "area": "Steel Skid Plates / Tailgate Glass",
        "cost_range": "$20 – $220 (USD)",
        "tech_note": "The factory or TRD steel front skid plate frequently vibrates against the radiator crossmember brackets if bolts are improperly torqued. Inside the cabin, the roll-down rear window glass regulator can develop rattle over washboard trails.",
        "causes": "Loose front skid plate mounting bolts or missing shims, rear roll-down tailgate window regulator play, catalytic converter heat shield clamp failure, or loose roof rack crossbars.",
        "checklist": [
            "Kick or hit front skid plate with shoe sole: metallic buzz confirms loose skid plate bolts.",
            "Roll rear tailgate window down 1 inch: if interior rattle over bumps disappears, window regulator guide clips need adjustment.",
            "Tap underbody exhaust shields: check crossover exhaust pipe heat shield clamps.",
            "Tighten roof rack thumb screws: loose crossbars rattle loudly against roof rails."
        ],
        "costs": [
            ("Skid Plate Hardware & Rubber Shim Kit", "$20 – $50", "Permanent fix for front skid plate buzz."),
            ("Tailgate Window Regulator Guide Adjustment", "$80 – $160", "Silences rear hatch glass rattle over bumps."),
            ("Stainless Exhaust Heat Shield Clamps", "$35 – $75", "Secures rattling crossover exhaust shields.")
        ],
        "has_sticky": False
    },
    {
        "slug": "toyota-4runner-ticking-noise",
        "title": "Toyota 4Runner Ticking Sound: 1GR-FE Valve Train vs EVAP Purge Solenoid",
        "h1": "Toyota 4Runner 4.0L V6 Engine Ticking Guide",
        "model": "Toyota 4Runner",
        "years": "2014–2024",
        "noise": "Ticking",
        "severity": "🟢 Low Risk (Normal 1GR-FE Sound)",
        "urgency": "Verify EVAP purge vs exhaust leak",
        "area": "4.0L 1GR-FE Valvetrain / EVAP Solenoid",
        "cost_range": "$0 – $750 (USD)",
        "tech_note": "The legendary 4.0L 1GR-FE V6 engine is known for its mechanical valvetrain tick. In addition, the EVAP purge solenoid on the driver's side fender pulses loudly at idle, which is completely normal.",
        "causes": "EVAP canister purge valve pulsing (normal), 1GR-FE mechanical valvetrain lifter clearance, low oil level, or cracked exhaust manifold weld.",
        "checklist": [
            "Locate EVAP purge valve on driver-side inner fender: place finger on valve; rhythmic clicking felt through plastic body confirms normal emissions purge.",
            "Listen under hood: uniform valvetrain tick from 1GR-FE dual VVT-i is characteristic of this engine family.",
            "Check for exhaust manifold tick: listen through front wheel wells during cold engine startup under load; a sharp puffing tick that fades as engine heats indicates manifold crack.",
            "Check engine oil dipstick to verify 0W-20/5W-20 oil level."
        ],
        "costs": [
            ("DIY Diagnostic Verification", "$0", "Normal 1GR-FE mechanical acoustics confirmed."),
            ("EVAP Purge Solenoid Replacement", "$95 – $190", "Cures excessively loud emissions valve tick."),
            ("Exhaust Manifold Assembly Replacement", "$550 – $950", "Repairs cracked exhaust manifold if air leak is detected.")
        ],
        "has_sticky": True
    }
]

print(f"Loaded {len(PILOT_PAGES)} Toyota pilot specifications.")

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

    cta_ref = "sticky_toyota" if page["has_sticky"] else "inline_toyota"
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
      <a href="https://carithm.vercel.app/audio?ref=sticky_toyota" style="background: #0284c7; color: #ffffff; font-size: 0.8rem; font-weight: 600; padding: 7px 14px; border-radius: 6px; text-decoration: none; white-space: nowrap;">
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
            "name": "Toyota Noise Hub",
            "item": "https://carithm.vercel.app/audio/toyota"
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
    <a href="https://carithm.vercel.app/audio/toyota" style="color: #fff;">Toyota Hub</a>
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
    <a href="https://carithm.vercel.app/audio/toyota">Toyota</a>
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

  <!-- Related Toyota Acoustic Guides -->
  <section class="card" style="margin-bottom: 16px;">
    <h2>More Toyota Diagnostic Guides</h2>
    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;">
      <a href="https://carithm.vercel.app/audio/toyota-rav4-whining-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">RAV4 Whining</a>
      <a href="https://carithm.vercel.app/audio/toyota-rav4-humming-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">RAV4 Humming</a>
      <a href="https://carithm.vercel.app/audio/toyota-rav4-clunking-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">RAV4 Clunking</a>
      <a href="https://carithm.vercel.app/audio/toyota-camry-whining-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Camry Whining</a>
      <a href="https://carithm.vercel.app/audio/toyota-camry-humming-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Camry Humming</a>
      <a href="https://carithm.vercel.app/audio/toyota-corolla-humming-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Corolla Humming</a>
      <a href="https://carithm.vercel.app/audio/toyota-tacoma-humming-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Tacoma Humming</a>
      <a href="https://carithm.vercel.app/audio/toyota" style="background: rgba(56,189,248,0.15); border: 1px solid rgba(56,189,248,0.3); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--accent); text-decoration: none; font-weight: 600;">View All Toyota Models &rarr;</a>
    </div>
  </section>

  <div class="disclaimer-box">
    <strong>Technical Disclaimer:</strong> Acoustic diagnostics provide preliminary pattern matching and should be verified with an ASE-certified technician or factory scan tool. Never drive a vehicle exhibiting severe braking degradation or sudden oil pressure loss.
  </div>
</main>

<footer>
  <p>&copy; 2026 Carithm. Autonomous Automotive Acoustic Research.</p>
  <p style="margin-top: 4px;"><a href="https://carithm.vercel.app/audio">Acoustic Diagnoser</a> &bull; <a href="https://carithm.vercel.app/audio/toyota">Toyota Directory</a> &bull; <a href="https://carithm.vercel.app/audio/ford">Ford Directory</a> &bull; <a href="https://carithm.vercel.app/about">About Carithm</a></p>
</footer>

{sticky_bar_html}

</body>
</html>"""


# Template for Brand Hub /audio/toyota
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
  <title>Toyota Noise Diagnostic Hub: Common Sounds, TSBs &amp; Repair Costs | Carithm</title>
  <meta name="description" content="Explore documented acoustic diagnostic guides for Toyota RAV4, Camry, Corolla, Highlander, Tacoma, and 4Runner. Verified root causes, factory TSBs, and repair estimates.">
  <link rel="canonical" href="https://carithm.vercel.app/audio/toyota">
  <meta name="robots" content="index, follow">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "headline": "Toyota Automotive Acoustic Diagnostic Hub",
    "description": "Comprehensive directory of documented mechanical sound diagnostics for Toyota vehicles.",
    "url": "https://carithm.vercel.app/audio/toyota",
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
    <a href="https://carithm.vercel.app/audio/toyota" style="color: #fff;">Toyota Hub</a>
    <a href="https://carithm.vercel.app/audio/ford">Ford Hub</a>
    <a href="https://carithm.vercel.app/about">About</a>
  </nav>
</header>

<main>
  <div class="hero">
    <span style="font-size: 0.78rem; text-transform: uppercase; color: var(--accent); font-weight: 700; letter-spacing: 0.05em;">Brand Acoustic Directory</span>
    <h1>Toyota Vehicle Noise Diagnostic Hub</h1>
    <p style="color: var(--muted); font-size: 1.05rem; max-width: 720px; margin: 0 0 20px;">
      Documented diagnostic guides for common acoustic failure modes across Toyota passenger cars, crossovers, and trucks. Verified factory TSB references, driveway checks, and estimated repair costs.
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
  <p style="margin-top: 4px;"><a href="https://carithm.vercel.app/audio" style="color: var(--muted);">Acoustic Diagnoser</a> &bull; <a href="https://carithm.vercel.app/audio/toyota" style="color: var(--muted);">Toyota Directory</a> &bull; <a href="https://carithm.vercel.app/audio/ford" style="color: var(--muted);">Ford Directory</a> &bull; <a href="https://carithm.vercel.app/about" style="color: var(--muted);">About Carithm</a></p>
</footer>

</body>
</html>"""


# Main Execution
print("Writing 32 Toyota pilot pages to:", OUTPUT_DIR)
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

print(f"Generated {len(PILOT_PAGES)} Toyota subpages (Group A Sticky: {sticky_count}, Group B Clean: {clean_count}).")

# Generate Toyota Brand Hub
hub_path = os.path.join(OUTPUT_DIR, "toyota.html")
with open(hub_path, "w", encoding="utf-8") as f:
    f.write(render_brand_hub())
print("Generated Toyota Brand Hub at /audio/toyota -> toyota.html")

# Create Dedicated Priority Pilot Sitemap
sitemap_urls = ['  <url>\n    <loc>https://carithm.vercel.app/audio/toyota</loc>\n    <lastmod>2026-11-07</lastmod>\n  </url>']
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

sitemap_path = "/Users/shaunaukbasu/Desktop/golden_desert/sitemap_pilot_toyota.xml"
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print(f"Created dedicated pilot sitemap at: {sitemap_path} with {len(sitemap_urls)} URLs.")
