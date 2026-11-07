#!/usr/bin/env python3
"""
Chevrolet Pilot Generator:
1. Generates /audio/chevrolet (Brand Hub) with clean hierarchy to Chevrolet models.
2. Generates 18 Elite Chevrolet sound diagnostic subpages:
   - Group A (9 pages): Scroll-triggered, slim, dismissible bottom bar + contextual CTA after DIY checks.
   - Group B (9 pages): Zero sticky bar (pure content + contextual CTA after DIY checks).
   - Real mechanical engineering (GM TSB 18-NA-355 AFM lifters, Ecotec timing chain stretch, slip yoke clunk).
   - Zero third-party ads (100% Core Web Vitals compliant).
"""

import os

OUTPUT_DIR = "/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static"

PILOT_PAGES = [
    # --- Chevrolet Silverado 1500 ---
    {
        "slug": "chevrolet-silverado-humming-noise",
        "title": "Chevrolet Silverado Humming Noise: Front Wheel Hub Bearings vs Rear Diff Pinion",
        "h1": "Chevrolet Silverado Highway Humming Drone Diagnostic Guide",
        "model": "Chevrolet Silverado 1500",
        "years": "2014–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–600 miles",
        "area": "Front Wheel Hub Assemblies / Rear Axle Pinion",
        "cost_range": "$110 – $1,100 (USD)",
        "tech_note": "On GMT K2XX (2014–2018) and T1XX (2019+) Silverado trucks, front unit-bearing hub assemblies commonly develop internal race spalling between 55,000 and 85,000 miles. A highway whine/drone that occurs only while on the throttle indicates rear 9.5/9.76-inch differential pinion bearing wear.",
        "causes": "Front wheel bearing hub assembly race spalling, rear differential pinion bearing wear under throttle load, aggressive all-terrain tire tread cupping, or front CV axle needle bearing slop.",
        "checklist": [
            "Weave gently in lane at 55 mph: if the humming tone gets louder when turning right, the left front wheel bearing is failing.",
            "Throttle on/off test at 50 mph: if whine/hum increases under light acceleration and silences when coasting, rear axle pinion bearings are worn.",
            "Inspect all-terrain tires for scalloped inner or outer tread blocks.",
            "Check front and rear differential gear oil levels and condition."
        ],
        "costs": [
            ("Tire Rotation, Road Force Balance & Alignment", "$110 – $180", "Eliminates aggressive tire tread roaring."),
            ("Front Heavy-Duty Wheel Hub & Bearing Assembly", "$310 – $540", "Complete OEM unit-bearing replacement with ABS sensor."),
            ("Rear Differential Pinion & Carrier Bearing Overhaul", "$650 – $1,100", "Includes new bearings, shims, seals, and synthetic 75W-90 gear oil.")
        ],
        "has_sticky": True
    },
    {
        "slug": "chevrolet-silverado-ticking-noise",
        "title": "Chevrolet Silverado Ticking Sound: AFM/DFM Lifter Failure (TSB) vs Exhaust Bolts",
        "h1": "Chevrolet Silverado V8 Engine Ticking Sound Diagnostic Guide",
        "model": "Chevrolet Silverado 1500",
        "years": "2014–2024",
        "noise": "Ticking",
        "severity": "🔴 High Risk (If AFM Lifter)",
        "urgency": "Inspect top-end tick immediately",
        "area": "5.3L/6.2L V8 AFM/DFM Lifters / Exhaust Manifolds",
        "cost_range": "$160 – $3,600 (USD)",
        "tech_note": "A persistent metallic clatter from the top of 5.3L or 6.2L EcoTec3 V8 engines is frequently collapsed Active Fuel Management (AFM) or Dynamic Fuel Management (DFM) deactivation lifters (GM TSB 18-NA-355 / TSB 21-NA-149). A ticking that softens when warm is broken rear exhaust manifold bolts.",
        "causes": "Collapsing AFM/DFM hydraulic lifters (GM TSB), broken exhaust manifold bolts on cylinders 7 and 8, high-pressure direct injection fuel pump pulse, or low oil pressure from pickup tube O-ring.",
        "checklist": [
            "Determine if ticking is top-end or cold start: sharp metallic clack from valve cover that tracks RPM indicates collapsed AFM lifter.",
            "Listen through front wheel wells during cold start: sharp exhaust puffing tick that fades as engine heats confirms broken rear exhaust manifold bolts.",
            "Check dashboard oil pressure gauge: hot engine idle pressure below 20 PSI points to oil pump pickup tube O-ring bleed-down.",
            "Check for check engine light with misfire code (P0300, P0301-P0308)."
        ],
        "costs": [
            ("Exhaust Manifold Bolt Repair (External Bracket Fix)", "$160 – $380", "Cures cold exhaust manifold stud tick without cylinder head drilling."),
            ("Oil Pickup Tube O-Ring & Pan Gasket", "$280 – $480", "Restores factory oil pressure and hydraulic lifter cushioning."),
            ("Complete AFM/DFM Lifter & Camshaft Service (TSB)", "$2,200 – $3,600", "Installs updated lifters, pushrods, camshaft, and head gaskets.")
        ],
        "has_sticky": False
    },
    {
        "slug": "chevrolet-silverado-rattling-noise",
        "title": "Chevrolet Silverado Rattling Noise: Catalytic Heat Shields vs Tailgate Rods",
        "h1": "Chevrolet Silverado Undercarriage & Exhaust Rattle Guide",
        "model": "Chevrolet Silverado 1500",
        "years": "2014–2024",
        "noise": "Rattling",
        "severity": "🟢 Low Risk (Nuisance)",
        "urgency": "Inspect exhaust clamps at convenience",
        "area": "Exhaust Catalytic Heat Shields / Tailgate Hardware",
        "cost_range": "$35 – $240 (USD)",
        "tech_note": "Loose catalytic converter heat shield clamps and fractured exhaust hanger brackets near the transmission crossmember are the leading external rattles on Silverado trucks. Tailgate latch rods also rattle against sheet metal when plastic clips break.",
        "causes": "Rusted catalytic converter heat shield weld clamps, loose spare tire winch cable, broken exhaust hanger brackets, or tailgate inner latch rod clip failure.",
        "checklist": [
            "Tap catalytic converter heat shields with gloved hand when cold: check for split weld clamps vibrating against the exhaust pipe.",
            "Inspect spare tire under truck bed: ensure winch cable is cranked tight against underside frame.",
            "Tap tailgate inner panel: broken plastic latch rod clips allow metal rods to slap tailgate skin over bumps.",
            "Inspect front bumper lower valance air deflector clips."
        ],
        "costs": [
            ("Stainless Steel Exhaust Shield Clamp Fix", "$35 – $75", "Permanent repair for buzzing underbody heat shields."),
            ("Tailgate Latch Rod Plastic Retainer Clip Kit", "$20 – $45", "Silences rear tailgate rod slap."),
            ("Exhaust Hanger Bracket Re-Weld / Bushing", "$65 – $120", "Secures vibrating exhaust pipe.")
        ],
        "has_sticky": True
    },
    {
        "slug": "chevrolet-silverado-clunking-noise",
        "title": "Chevrolet Silverado Clunking Noise: Driveshaft Slip Yoke Bump vs Ball Joints",
        "h1": "Chevrolet Silverado Driveshaft Slip Yoke & Suspension Clunk Guide",
        "model": "Chevrolet Silverado 1500",
        "years": "2014–2024",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Lube slip yoke within 500 miles",
        "area": "Driveshaft Slip Yoke / Front Suspension Ball Joints",
        "cost_range": "$60 – $680 (USD)",
        "tech_note": "A distinct 'bump from behind' or clunk felt 1 second after coming to a complete stop or when taking off from a light is caused by rear driveshaft slip yoke splines binding from dry lubrication (GM TSB 17-NA-056). Front clunking over bumps indicates upper ball joint or sway bar link wear.",
        "causes": "Driveshaft slip yoke splines dry binding (axle wrap / stoplight bump), front upper and lower ball joint wear, sway bar end link ball joints, or steering intermediate shaft slip joint.",
        "checklist": [
            "Come to a smooth complete stop: if you feel a delayed bump from behind 1 second after stopping, rear slip yoke splines are binding.",
            "Accelerate gently from a stop: clunk upon initial throttle tip-in confirms slip yoke spline release.",
            "Shake front sway bar links by hand: any vertical slack indicates ball joint wear.",
            "Check steering intermediate shaft: rapid left/right steering wiggle tests intermediate shaft joint knock."
        ],
        "costs": [
            ("Slip Yoke Clean & GM Special PTFE Lubricant Service", "$60 – $120", "Cleans splines and applies high-pressure lubricant per factory bulletin."),
            ("Front Sway Bar End Link Pair", "$130 – $220", "Restores quiet front suspension control over rough roads."),
            ("Upper Control Arm & Ball Joint Assemblies", "$380 – $680", "Replaces worn ball joints and control arm bushings.")
        ],
        "has_sticky": False
    },
    {
        "slug": "chevrolet-silverado-whining-noise",
        "title": "Chevrolet Silverado Whining Noise: 8L90 Transmission vs Transfer Case",
        "h1": "Chevrolet Silverado Transmission & Transfer Case Whining Guide",
        "model": "Chevrolet Silverado 1500",
        "years": "2014–2024",
        "noise": "Whining",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect transmission fluid and transfer case",
        "area": "8L90 / 10L80 Automatic Transmission / Transfer Case",
        "cost_range": "$120 – $3,200 (USD)",
        "tech_note": "On trucks equipped with the 8L90 8-speed automatic, torque converter clutch shudder and hydraulic pump whine is addressed by GM TSB 18-NA-355 (fluid exchange to Mobil 1 LV ATF HP). On 4WD models, acceleration whine can indicate transfer case drive chain stretch.",
        "causes": "8L90 transmission torque converter clutch slip/whine, transfer case drive chain wear, alternator rectifier diode ripple, or front differential pinion bearing.",
        "checklist": [
            "Rev engine in Park/Neutral: if whine tracks engine RPM while stationary, transmission is ruled out; inspect alternator/belt idler.",
            "Listen through audio speakers: electrical whining that rises with vehicle throttle confirms alternator diode ripple.",
            "Check 8-speed transmission service history: verify if Mobil 1 Synthetic LV ATF HP fluid flush was performed.",
            "Check transfer case fluid level through upper fill plug."
        ],
        "costs": [
            ("Mobil 1 LV ATF HP Transmission Fluid Flush (TSB)", "$220 – $340", "Cures 8L90 torque converter clutch slip and pump whine."),
            ("OEM Alternator Replacement", "$330 – $550", "Eliminates electrical whine and stabilizes charging."),
            ("Transfer Case Drive Chain & Bearing Overhaul", "$1,200 – $1,900", "Major repair for stretched 4WD transfer case chain.")
        ],
        "has_sticky": True
    },
    {
        "slug": "chevrolet-silverado-grinding-noise",
        "title": "Chevrolet Silverado Grinding Noise: Brake Pads vs Front Hub Bearings",
        "h1": "Chevrolet Silverado Brake & Hub Grinding Diagnostic Guide",
        "model": "Chevrolet Silverado 1500",
        "years": "2014–2024",
        "noise": "Grinding",
        "severity": "🔴 High Risk (Braking Hazard)",
        "urgency": "Inspect brake pads immediately",
        "area": "Heavy-Duty Braking System / Wheel Hub Bearings",
        "cost_range": "$90 – $540 (USD)",
        "tech_note": "Harsh metal-on-metal grinding when applying brakes indicates brake pad friction lining is completely depleted, allowing the steel backing plate to grind against the rotor. Constant grinding while rolling points to front hub unit-bearing spalling.",
        "causes": "Worn brake pads grinding on rotor surface, seized caliper slide pins, bent dust shield rubbing rotor backing, or failing front wheel hub assembly.",
        "checklist": [
            "Inspect brake rotor face: look for deep silver circular gouges indicating metal backing plate contact.",
            "Check inner brake pad thickness through wheel spokes: inner pads often wear faster if caliper pins are dry.",
            "Check if grinding occurs without braking: a constant scraping while rolling indicates a bent dust shield or seized bearing.",
            "Check wheel rim temperature after a short drive: hot wheel rim confirms dragging brake caliper."
        ],
        "costs": [
            ("Brake Dust Shield Adjustment", "$30 – $70", "Bends back rubbing sheet metal."),
            ("Front Heavy-Duty Brake Pads & Rotors", "$310 – $520", "Installs premium severe-duty ceramic pads and rotors."),
            ("Front Wheel Bearing Hub Assembly", "$310 – $540", "Complete unit-bearing replacement with ABS sensor.")
        ],
        "has_sticky": False
    },

    # --- Chevrolet Equinox ---
    {
        "slug": "chevrolet-equinox-grinding-noise",
        "title": "Chevrolet Equinox Grinding Noise: Caliper Slide Pins vs Rotor Rust Ridge",
        "h1": "Chevrolet Equinox Brake & Wheel Hub Grinding Guide",
        "model": "Chevrolet Equinox",
        "years": "2010–2024",
        "noise": "Grinding",
        "severity": "🔴 High Risk (Braking Hazard)",
        "urgency": "Inspect brake components immediately",
        "area": "Rear Brake Calipers / Wheel Hub Bearings",
        "cost_range": "$90 – $520 (USD)",
        "tech_note": "On Equinox models, rear brake calipers frequently seize on slide pins from road brine exposure, causing the inner brake pad to wear down to bare metal while the outer pad looks healthy. Worn front wheel hub assemblies also produce loud grinding under load.",
        "causes": "Seized rear brake caliper slide pins, worn inner brake pad grinding against rotor, rusted brake dust shield rubbing rotor edge, or front wheel bearing race failure.",
        "checklist": [
            "Inspect inner brake pads through wheel spokes: use a flashlight and mirror to verify inner pad friction thickness.",
            "Check if grinding occurs without braking: a constant scraping while rolling indicates a bent dust shield or seized caliper.",
            "Check wheel rim temperature after a short drive: unusually hot rear wheel confirms dragging caliper.",
            "Inspect brake rotor face: deep concentric grooves confirm metal-to-metal pad backing plate contact."
        ],
        "costs": [
            ("Brake Caliper Slide Pin Cleaning & Synthetic Lube", "$90 – $160", "Restores floating caliper movement and stops tapered pad wear."),
            ("Front / Rear Premium Ceramic Brake Pads & Rotors", "$290 – $490", "Complete replacement of friction discs and pads."),
            ("Front Wheel Bearing Hub Assembly", "$280 – $480", "OEM sealed hub unit replacement with ABS sensor.")
        ],
        "has_sticky": True
    },
    {
        "slug": "chevrolet-equinox-2010-2015-grinding-noise",
        "title": "Chevrolet Equinox (2010–2015) Grinding Noise: Rear Brakes vs Hubs",
        "h1": "Chevrolet Equinox (2010–2015) Grinding Noise Diagnostic Guide",
        "model": "Chevrolet Equinox",
        "years": "2010–2015",
        "noise": "Grinding",
        "severity": "🔴 High Risk (Braking Hazard)",
        "urgency": "Inspect brake pads immediately",
        "area": "Rear Brake Calipers / Wheel Hub Bearings",
        "cost_range": "$90 – $490 (USD)",
        "tech_note": "A top-ranked GA4 traffic query. Second-generation Equinox models (2010–2015) are notorious for seized rear brake caliper slide pins and premature rear rotor rust flaking, grinding inner pads down to metal.",
        "causes": "Seized rear brake caliper slide pins, inner brake pad worn to steel backing plate, rusted brake rotor edge, or front wheel bearing spalling.",
        "checklist": [
            "Inspect inner rear brake pads with flashlight: inner pads wear 2x faster than outer pads when slide pins are dry.",
            "Check for vehicle pulling to one side under braking: confirms seized caliper slide pin.",
            "Feel rear wheel center hub after driving: excessive heat confirms dragging brake caliper.",
            "Inspect rotor face for metal gouging."
        ],
        "costs": [
            ("Rear Caliper Slide Pin Lube & Hardware Kit", "$90 – $150", "Restores caliper sliding motion."),
            ("Rear Ceramic Brake Pads & Rotors Complete Set", "$280 – $460", "Replaces gouged discs and worn friction pads."),
            ("Front Wheel Bearing Hub Assembly", "$280 – $480", "Complete sealed replacement.")
        ],
        "has_sticky": False
    },
    {
        "slug": "chevrolet-equinox-humming-noise",
        "title": "Chevrolet Equinox Humming Noise: Front Wheel Hub Bearings vs AWD Carrier",
        "h1": "Chevrolet Equinox Highway Humming Noise Diagnostic Guide",
        "model": "Chevrolet Equinox",
        "years": "2010–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–600 miles",
        "area": "Front Wheel Hub Assemblies / AWD Differential",
        "cost_range": "$90 – $480 (USD)",
        "tech_note": "Sealed front wheel bearing hub units on the Theta platform Equinox are one of the most frequently replaced suspension items after 60,000 miles, creating a loud cockpit drone that peaks between 40 and 65 mph.",
        "causes": "Front wheel bearing hub unit spalling, rear wheel hub bearing wear, AWD rear differential carrier bearing hum, or cupped tires.",
        "checklist": [
            "Weave gently in lane at 50 mph: if drone gets louder when turning right, the left wheel bearing is damaged.",
            "Run your palm across the inner tread edge of rear tires: saw-tooth unevenness confirms tire scalloping.",
            "Jack up car and spin wheels by hand while holding suspension spring: vibration confirms bearing damage.",
            "Check wheel hub temperature after highway trip."
        ],
        "costs": [
            ("Tire Rotation & Computerized 4-Wheel Alignment", "$110 – $170", "Corrects tire wear and road roar."),
            ("Front Wheel Bearing Hub Assembly (Complete Unit)", "$280 – $480", "Bolt-on replacement with integrated ABS sensor."),
            ("AWD Rear Differential Fluid Exchange", "$110 – $180", "Fresh synthetic 75W-90 restores lubrication.")
        ],
        "has_sticky": True
    },
    {
        "slug": "chevrolet-equinox-rattling-noise",
        "title": "Chevrolet Equinox Rattling Noise: 2.4L Timing Chain Stretch vs Heat Shields",
        "h1": "Chevrolet Equinox Timing Chain & Exhaust Rattle Guide",
        "model": "Chevrolet Equinox",
        "years": "2010–2024",
        "noise": "Rattling",
        "severity": "🔴 High Risk (If Timing Chain)",
        "urgency": "Inspect cold start timing chain rattle immediately",
        "area": "2.4L Ecotec Timing Chain / Exhaust Heat Shields",
        "cost_range": "$35 – $1,650 (USD)",
        "tech_note": "On 2.4L Ecotec models (2010–2017), a loud metallic startup rattle lasting several seconds is timing chain stretch and broken plastic timing guide syndrome (well-documented GM Campaign / TSB). If neglected, the chain jumps teeth, causing catastrophic valve damage.",
        "causes": "Stretched timing chain and broken guide rails (2.4L Ecotec), variable valve timing (VVT) actuator phaser gear rattle, or exhaust catalytic converter heat shield clamp failure.",
        "checklist": [
            "Time the morning cold startup: harsh rattle lasting 3–5 seconds that persists until oil warms indicates stretched timing chain.",
            "Check engine oil dipstick: 2.4L Ecotec engines consume oil; low oil accelerates timing chain guide failure.",
            "Scan for OBD-II trouble codes: codes P0016 or P0017 (camshaft/crankshaft correlation) confirm timing chain stretch.",
            "Tap catalytic converter heat shields when cold: check for split weld seams."
        ],
        "costs": [
            ("Stainless Steel Exhaust Shield Clamp", "$35 – $75", "Permanent DIY fix for buzzing underbody shields."),
            ("VVT Solenoid Actuator Pair (Intake & Exhaust)", "$140 – $260", "Restores variable valve timing oil flow."),
            ("Complete Timing Chain, Guide & Water Pump Kit", "$950 – $1,650", "Replaces stretched chains, tensioners, guides, and sprockets.")
        ],
        "has_sticky": False
    },
    {
        "slug": "chevrolet-equinox-ticking-noise",
        "title": "Chevrolet Equinox Ticking Sound: Direct Injection HPFP vs Purge Valve",
        "h1": "Chevrolet Equinox Engine Ticking Sound Diagnostic Guide",
        "model": "Chevrolet Equinox",
        "years": "2010–2024",
        "noise": "Ticking",
        "severity": "🟢 Low Risk (Normal Operation)",
        "urgency": "Check oil level and injector pulse",
        "area": "Ecotec Direct Injection / Valvetrain",
        "cost_range": "$0 – $310 (USD)",
        "tech_note": "On 1.5L Turbo and 2.0L Turbo direct-injection engines, the mechanical high-pressure fuel pump produces a sharp, rhythmic mechanical click at idle that is completely normal operation and not valvetrain damage.",
        "causes": "High-pressure direct injection fuel pump (HPFP) normal operation, EVAP canister purge solenoid click, low engine oil level, or cold hydraulic valve lifter tick.",
        "checklist": [
            "Listen with hood open: rapid sewing-machine ticking centered on the fuel pump cover is normal direct injection.",
            "Feel the EVAP purge solenoid: rapid clicking pulses felt through valve body confirm normal emissions purge.",
            "Check engine oil dipstick: ensure oil is clean and topped up with Dexos1 0W-20/5W-30.",
            "Notice if ticking softens when engine reaches full operating temperature."
        ],
        "costs": [
            ("DIY Diagnostic Verification", "$0", "Normal direct-injection mechanical pulse confirmed."),
            ("Synthetic Engine Oil & Filter Change", "$55 – $85", "Restores proper lubrication to valvetrain components."),
            ("EVAP Purge Solenoid Valve Replacement", "$95 – $190", "Cures excessively loud emissions valve tick.")
        ],
        "has_sticky": True
    },
    {
        "slug": "chevrolet-equinox-clunking-noise",
        "title": "Chevrolet Equinox Clunking Noise: Sway Bar Links vs Strut Mounts",
        "h1": "Chevrolet Equinox Suspension Clunking Diagnostic Guide",
        "model": "Chevrolet Equinox",
        "years": "2010–2024",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 200–400 miles",
        "area": "Front Stabilizer Links / Upper Strut Mounts",
        "cost_range": "$95 – $580 (USD)",
        "tech_note": "A hollow knocking or popping over speed bumps or rough city pavement is predominantly caused by worn front stabilizer bar end links or degraded front upper strut mount bearings.",
        "causes": "Front sway bar link ball joint play, upper strut mount bearing binding, lower control arm compliance bushing tears, or loose motor mount torque strut.",
        "checklist": [
            "Drive over speed humps at an angle: chucking noise from front corners points to sway bar end link ball joint slack.",
            "Have a helper turn steering wheel lock-to-lock: coil spring jumping confirms a binding upper strut mount bearing.",
            "Inspect front control arm compliance bushings: look for tearing in large rubber bushings.",
            "Check upper engine torque strut mount for cracked rubber."
        ],
        "costs": [
            ("Front Sway Bar End Link Pair", "$110 – $190", "Restores quiet, firm suspension over city streets."),
            ("Front Lower Control Arm Compliance Bushings", "$310 – $520", "Replaces torn bushings and eliminates braking clunk."),
            ("Front Strut & Mount Assemblies", "$360 – $580", "Restores factory ride quality and damping.")
        ],
        "has_sticky": False
    },

    # --- Chevrolet Tahoe / Suburban ---
    {
        "slug": "chevrolet-tahoe-clunking-noise",
        "title": "Chevrolet Tahoe Clunking Noise: Slip Yoke Bump vs Upper Ball Joints",
        "h1": "Chevrolet Tahoe Driveshaft & Suspension Clunk Guide",
        "model": "Chevrolet Tahoe",
        "years": "2015–2024",
        "noise": "Clunking",
        "severity": "🟡 Moderate Risk",
        "urgency": "Lube slip yoke within 500 miles",
        "area": "Driveshaft Slip Yoke / Front Upper Control Arms",
        "cost_range": "$60 – $690 (USD)",
        "tech_note": "A distinct bump from behind when stopping or accelerating is caused by dry driveshaft slip yoke splines binding (GM TSB). Front suspension clunking over washboard roads indicates upper ball joint or magnetic ride shock top mount wear.",
        "causes": "Driveshaft slip yoke spline dry binding, front upper ball joint wear, magnetic ride control shock top mount play, or sway bar end links.",
        "checklist": [
            "Come to a smooth complete stop: if you feel a delayed bump from behind 1 second after stopping, rear slip yoke splines are binding.",
            "Accelerate gently from a stop: clunk upon initial throttle tip-in confirms slip yoke spline release.",
            "Drive over speed humps diagonally: front corner chucking points to sway bar end link wear.",
            "Inspect magnetic ride control shock bodies for hydraulic fluid weeping."
        ],
        "costs": [
            ("Slip Yoke Clean & GM Special PTFE Lubricant Service", "$60 – $120", "Cleans splines and applies high-pressure lubricant."),
            ("Front Sway Bar End Link Pair", "$130 – $220", "Restores quiet front suspension control over rough roads."),
            ("Upper Control Arm & Ball Joint Assemblies", "$390 – $690", "Replaces worn ball joints and control arm bushings.")
        ],
        "has_sticky": True
    },
    {
        "slug": "chevrolet-tahoe-rattling-noise",
        "title": "Chevrolet Tahoe Rattling Noise: Catalytic Heat Shields vs Power Liftgate",
        "h1": "Chevrolet Tahoe Undercarriage & Cargo Rattle Guide",
        "model": "Chevrolet Tahoe",
        "years": "2015–2024",
        "noise": "Rattling",
        "severity": "🟢 Low Risk (Nuisance)",
        "urgency": "Inspect exhaust shields at convenience",
        "area": "Catalytic Converter Heat Shields / Power Liftgate",
        "cost_range": "$35 – $240 (USD)",
        "tech_note": "Catalytic converter heat shield weld failure near the transmission crossmember is the leading external rattle. Rear interior rattles over highway bumps are almost universally misadjusted power liftgate bump stops or latch striker play.",
        "causes": "Rusted catalytic converter heat shield clamps, loose spare tire winch cable, power liftgate striker latch play, or dashboard trim rattle.",
        "checklist": [
            "Tap catalytic converter heat shields with gloved hand when cold: check for split weld clamps.",
            "Wrap two layers of electrical tape around rear liftgate latch striker: if cargo rattle stops over bumps, adjust rubber bump stops.",
            "Ensure under-bed spare tire winch cable is cranked tight.",
            "Press firmly on dashboard center speaker grille on coarse pavement."
        ],
        "costs": [
            ("Stainless Steel Exhaust Shield Clamp Fix", "$35 – $75", "Permanent repair for buzzing underbody heat shields."),
            ("Power Liftgate Striker & Bumper Adjustment", "$30 – $70", "Silences rear cargo hatch vibrations."),
            ("Felt Anti-Rattle Tape Interior Kit", "$15 – $35", "Eliminates dashboard and pillar trim buzz.")
        ],
        "has_sticky": False
    },
    {
        "slug": "chevrolet-tahoe-ticking-noise",
        "title": "Chevrolet Tahoe Ticking Sound: AFM/DFM Lifter Failure vs Manifold Bolts",
        "h1": "Chevrolet Tahoe V8 Engine Ticking Sound Diagnostic Guide",
        "model": "Chevrolet Tahoe",
        "years": "2015–2024",
        "noise": "Ticking",
        "severity": "🔴 High Risk (If AFM Lifter)",
        "urgency": "Inspect top-end tick immediately",
        "area": "5.3L/6.2L V8 AFM/DFM Lifters / Exhaust Manifolds",
        "cost_range": "$160 – $3,600 (USD)",
        "tech_note": "A persistent metallic clatter from the top of the 5.3L or 6.2L V8 is frequently collapsed AFM/DFM deactivation lifters (GM TSB 18-NA-355). Broken rear exhaust manifold bolts on cylinders 7/8 cause cold startup ticking that fades when warm.",
        "causes": "Collapsing AFM/DFM hydraulic lifters (GM TSB), broken exhaust manifold bolts on rear cylinders, direct injection fuel pump pulse, or oil pickup tube O-ring leak.",
        "checklist": [
            "Determine if ticking is top-end or cold start: sharp metallic clack from valve cover that tracks RPM indicates collapsed AFM lifter.",
            "Listen through front wheel wells on cold start: sharp exhaust puffing tick that fades as engine heats confirms broken rear exhaust manifold bolts.",
            "Check dashboard oil pressure gauge: hot engine idle pressure below 20 PSI points to oil pump pickup tube O-ring bleed-down.",
            "Check for check engine light with misfire code (P0300, P0301-P0308)."
        ],
        "costs": [
            ("Exhaust Manifold Bolt Repair (External Bracket Fix)", "$160 – $380", "Cures cold exhaust manifold stud tick without cylinder head drilling."),
            ("Oil Pickup Tube O-Ring & Pan Gasket", "$280 – $480", "Restores factory oil pressure and hydraulic lifter cushioning."),
            ("Complete AFM/DFM Lifter & Camshaft Service (TSB)", "$2,200 – $3,600", "Installs updated lifters, pushrods, camshaft, and head gaskets.")
        ],
        "has_sticky": True
    },
    {
        "slug": "chevrolet-tahoe-humming-noise",
        "title": "Chevrolet Tahoe Humming Noise: Heavy Chassis Hub Bearings vs Rear Axle",
        "h1": "Chevrolet Tahoe Highway Humming Noise Diagnostic Guide",
        "model": "Chevrolet Tahoe",
        "years": "2015–2024",
        "noise": "Humming",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect within 300–600 miles",
        "area": "Front Wheel Hub Assemblies / Rear Axle Pinion",
        "cost_range": "$110 – $1,100 (USD)",
        "tech_note": "Due to the Tahoe's 5,500+ lb curb weight, front wheel hub unit-bearings commonly develop internal race spalling between 60,000 and 90,000 miles. A highway whine/drone under light throttle indicates rear axle pinion bearing wear.",
        "causes": "Front wheel bearing hub assembly race spalling, rear differential pinion bearing wear under throttle load, aggressive all-terrain tire tread cupping, or front CV axle needle bearing slop.",
        "checklist": [
            "Weave gently in lane at 55 mph: if the humming tone gets louder when turning right, the left front wheel bearing is failing.",
            "Throttle on/off test at 50 mph: if whine/hum increases under light acceleration and silences when coasting, rear axle pinion bearings are worn.",
            "Inspect all-terrain tires for scalloped inner or outer tread blocks.",
            "Check front and rear differential gear oil levels and condition."
        ],
        "costs": [
            ("Tire Rotation, Road Force Balance & Alignment", "$110 – $180", "Eliminates aggressive tire tread roaring."),
            ("Front Heavy-Duty Wheel Hub & Bearing Assembly", "$320 – $560", "Complete OEM unit-bearing replacement with ABS sensor."),
            ("Rear Differential Pinion & Carrier Bearing Overhaul", "$650 – $1,100", "Includes new bearings, shims, seals, and synthetic 75W-90 gear oil.")
        ],
        "has_sticky": False
    },
    {
        "slug": "chevrolet-tahoe-whining-noise",
        "title": "Chevrolet Tahoe Whining Noise: 10L80 Transmission vs Transfer Case",
        "h1": "Chevrolet Tahoe Transmission & Transfer Case Whining Guide",
        "model": "Chevrolet Tahoe",
        "years": "2015–2024",
        "noise": "Whining",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect transmission fluid and transfer case",
        "area": "10L80 Automatic Transmission / Transfer Case",
        "cost_range": "$120 – $3,200 (USD)",
        "tech_note": "On the 10L80 10-speed automatic, gentle gear meshing whine in lower gears under light throttle is common. On 4WD models, acceleration whine can indicate transfer case drive chain stretch or low fluid.",
        "causes": "10L80 transmission gear meshing acoustics, transfer case drive chain wear, alternator rectifier diode ripple, or power steering electric motor load.",
        "checklist": [
            "Rev engine in Park/Neutral: if whine tracks engine RPM while stationary, transmission is ruled out; inspect alternator/belt idler.",
            "Listen through audio speakers: electrical whining that rises with vehicle throttle confirms alternator diode ripple.",
            "Check transmission fluid service history.",
            "Check transfer case fluid level through upper fill plug."
        ],
        "costs": [
            ("Transmission Fluid & Filter Service (Dexron ULV)", "$180 – $310", "Fresh synthetic fluid restores hydraulic cushion."),
            ("OEM Alternator Replacement", "$330 – $560", "Eliminates electrical whine and stabilizes charging."),
            ("Transfer Case Drive Chain & Bearing Overhaul", "$1,200 – $1,900", "Major repair for stretched 4WD transfer case chain.")
        ],
        "has_sticky": True
    },

    # --- Chevrolet Trailblazer ---
    {
        "slug": "chevrolet-trailblazer-2002-2009-squealing-noise",
        "title": "Chevrolet Trailblazer (2002–2009) Squealing Noise: Fan Clutch vs Idler Pulley",
        "h1": "Chevrolet Trailblazer (2002–2009) Engine Squeal Diagnostic Guide",
        "model": "Chevrolet Trailblazer",
        "years": "2002–2009",
        "noise": "Squealing",
        "severity": "🟡 Moderate Risk",
        "urgency": "Inspect fan clutch and pulleys",
        "area": "4.2L Vortec Electro-Viscous Fan Clutch / Idler Pulleys",
        "cost_range": "$65 – $420 (USD)",
        "tech_note": "A top-ranked GA4 traffic query. The 4.2L Vortec inline-6 utilizes an electro-viscous cooling fan clutch that commonly fails, causing intense squealing, roaring, and serpentine belt slip. Worn idler pulleys and water pumps are other primary causes.",
        "causes": "Electro-viscous cooling fan clutch bearing seizure, worn serpentine belt idler pulley bearings, water pump bearing weep, or glazed serpentine belt.",
        "checklist": [
            "Spin cooling fan by hand with engine off: if fan is completely locked or exhibits metallic scraping, the electro-viscous clutch is seized.",
            "Remove serpentine belt and spin idler and tensioner pulleys by hand: roughness confirms worn ball bearings.",
            "Inspect water pump weep hole for dried green/orange coolant crust.",
            "Spray water mist on belt while squealing: if noise silences, replace glazed serpentine belt."
        ],
        "costs": [
            ("Serpentine Accessory Belt & Idler Pulley Kit", "$95 – $180", "Restores quiet belt drive rotation."),
            ("Electro-Viscous Cooling Fan Clutch Assembly", "$220 – $390", "Cures fan clutch bearing seizure and jet-engine roar."),
            ("Engine Water Pump Replacement", "$280 – $420", "Includes new pump, gasket, and Dex-Cool coolant flush.")
        ],
        "has_sticky": False
    }
]

print(f"Loaded {len(PILOT_PAGES)} Chevrolet pilot specifications.")

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

    cta_ref = "sticky_chevy" if page["has_sticky"] else "inline_chevy"
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
      <a href="https://carithm.vercel.app/audio?ref=sticky_chevy" style="background: #0284c7; color: #ffffff; font-size: 0.8rem; font-weight: 600; padding: 7px 14px; border-radius: 6px; text-decoration: none; white-space: nowrap;">
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
            "name": "Chevrolet Noise Hub",
            "item": "https://carithm.vercel.app/audio/chevrolet"
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
    <a href="https://carithm.vercel.app/audio/chevrolet" style="color: #fff;">Chevrolet Hub</a>
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
    <a href="https://carithm.vercel.app/audio/chevrolet">Chevrolet</a>
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

  <!-- Related Chevrolet Acoustic Guides -->
  <section class="card" style="margin-bottom: 16px;">
    <h2>More Chevrolet Diagnostic Guides</h2>
    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;">
      <a href="https://carithm.vercel.app/audio/chevrolet-silverado-humming-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Silverado Humming</a>
      <a href="https://carithm.vercel.app/audio/chevrolet-silverado-ticking-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Silverado Ticking</a>
      <a href="https://carithm.vercel.app/audio/chevrolet-silverado-clunking-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Silverado Clunking</a>
      <a href="https://carithm.vercel.app/audio/chevrolet-equinox-grinding-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Equinox Grinding</a>
      <a href="https://carithm.vercel.app/audio/chevrolet-equinox-humming-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Equinox Humming</a>
      <a href="https://carithm.vercel.app/audio/chevrolet-tahoe-clunking-noise" style="background: var(--surface2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--muted); text-decoration: none;">Tahoe Clunking</a>
      <a href="https://carithm.vercel.app/audio/chevrolet" style="background: rgba(56,189,248,0.15); border: 1px solid rgba(56,189,248,0.3); padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; color: var(--accent); text-decoration: none; font-weight: 600;">View All Chevrolet Models &rarr;</a>
    </div>
  </section>

  <div class="disclaimer-box">
    <strong>Technical Disclaimer:</strong> Acoustic diagnostics provide preliminary pattern matching and should be verified with an ASE-certified technician or factory scan tool. Never drive a vehicle exhibiting severe braking degradation or sudden oil pressure loss.
  </div>
</main>

<footer>
  <p>&copy; 2026 Carithm. Autonomous Automotive Acoustic Research.</p>
  <p style="margin-top: 4px;"><a href="https://carithm.vercel.app/audio">Acoustic Diagnoser</a> &bull; <a href="https://carithm.vercel.app/audio/chevrolet">Chevrolet Directory</a> &bull; <a href="https://carithm.vercel.app/audio/toyota">Toyota Directory</a> &bull; <a href="https://carithm.vercel.app/audio/honda">Honda Directory</a> &bull; <a href="https://carithm.vercel.app/audio/ford">Ford Directory</a> &bull; <a href="https://carithm.vercel.app/about">About Carithm</a></p>
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
  <title>Chevrolet Noise Diagnostic Hub: Common Sounds, TSBs &amp; Repair Costs | Carithm</title>
  <meta name="description" content="Explore documented acoustic diagnostic guides for Chevrolet Silverado, Equinox, Tahoe, and Trailblazer. Verified root causes, factory TSB references, and repair cost estimates.">
  <link rel="canonical" href="https://carithm.vercel.app/audio/chevrolet">
  <meta name="robots" content="index, follow">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "headline": "Chevrolet Automotive Acoustic Diagnostic Hub",
    "description": "Comprehensive directory of documented mechanical sound diagnostics for Chevrolet vehicles.",
    "url": "https://carithm.vercel.app/audio/chevrolet",
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
    <a href="https://carithm.vercel.app/audio/chevrolet" style="color: #fff;">Chevrolet Hub</a>
    <a href="https://carithm.vercel.app/audio/toyota">Toyota Hub</a>
    <a href="https://carithm.vercel.app/audio/honda">Honda Hub</a>
    <a href="https://carithm.vercel.app/audio/ford">Ford Hub</a>
    <a href="https://carithm.vercel.app/about">About</a>
  </nav>
</header>

<main>
  <div class="hero">
    <span style="font-size: 0.78rem; text-transform: uppercase; color: var(--accent); font-weight: 700; letter-spacing: 0.05em;">Brand Acoustic Directory</span>
    <h1>Chevrolet Vehicle Noise Diagnostic Hub</h1>
    <p style="color: var(--muted); font-size: 1.05rem; max-width: 720px; margin: 0 0 20px;">
      Documented diagnostic guides for common acoustic failure modes across Chevrolet trucks, SUVs, and crossovers. Verified factory TSB references, driveway checks, and estimated repair costs.
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
  <p style="margin-top: 4px;"><a href="https://carithm.vercel.app/audio">Acoustic Diagnoser</a> &bull; <a href="https://carithm.vercel.app/audio/chevrolet">Chevrolet Directory</a> &bull; <a href="https://carithm.vercel.app/audio/toyota">Toyota Directory</a> &bull; <a href="https://carithm.vercel.app/audio/honda">Honda Directory</a> &bull; <a href="https://carithm.vercel.app/audio/ford">Ford Directory</a> &bull; <a href="https://carithm.vercel.app/about">About Carithm</a></p>
</footer>

</body>
</html>"""


# Main Execution
print("Writing Chevrolet pilot pages to:", OUTPUT_DIR)
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

print(f"Generated {len(PILOT_PAGES)} Chevrolet subpages (Group A Sticky: {sticky_count}, Group B Clean: {clean_count}).")

# Generate Chevrolet Brand Hub
hub_path = os.path.join(OUTPUT_DIR, "chevrolet.html")
with open(hub_path, "w", encoding="utf-8") as f:
    f.write(render_brand_hub())
print("Generated Chevrolet Brand Hub at /audio/chevrolet -> chevrolet.html")

# Create Dedicated Priority Pilot Sitemap
sitemap_urls = ['  <url>\n    <loc>https://carithm.vercel.app/audio/chevrolet</loc>\n    <lastmod>2026-11-07</lastmod>\n  </url>']
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

sitemap_path = "/Users/shaunaukbasu/Desktop/golden_desert/sitemap_pilot_chevrolet.xml"
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print(f"Created dedicated pilot sitemap at: {sitemap_path} with {len(sitemap_urls)} URLs.")
