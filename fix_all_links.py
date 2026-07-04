from pathlib import Path

root = Path(".")

replacements = {
    # AI page fixes → point to real existing research pages
    "/research/how-to-tell-if-a-mechanic-is-overcharging-you": "/research/repair-estimate-guide",
    "/research/oem-vs-aftermarket-parts": "/research/repair",
    "/research/brake-repair-cost-guide": "/research/brakes",
    "/research/check-engine-light-guide": "/problems/check-engine-light",
    "/research/car-maintenance-checklist": "/research/servicing",
    "/research/pre-purchase-inspection-guide": "/research/inspection",
    "/research/repair-estimate-guide": "/research/cost",
    "/research/understanding-labor-costs": "/research/cost",
    "/research/dealership-vs-independent-mechanic": "/research/repair",

    # predictive fixes
    "/toyota/toyota-corolla-service-cost-uae.html": "/toyota/corolla-service-cost.html",
    "/toyota/toyota-camry-repair-cost-uae.html": "/toyota/camry-repair-cost.html",

    "/toyota/toyota-land-cruiser-maintenance-cost-uae.html": "/toyota/land-cruiser-maintenance-cost.html",
    "/mercedes/mercedes-c200-service-cost-abu-dhabi.html": "/mercedes/c200-service-cost.html",

    # mercedes mismatch
    "/mercedes/mercedes-e300-maintenance-cost-uae.html": "/mercedes/e300-maintenance-cost.html",

    # about fix
    "/how-carithm-engineers-fleet-health": "/about"
}

fixed = 0

for file in root.rglob("*.html"):
    text = file.read_text(errors="ignore")

    new_text = text
    for old, new in replacements.items():
        if old in new_text:
            new_text = new_text.replace(old, new)

    if new_text != text:
        file.write_text(new_text)
        print("fixed:", file)
        fixed += 1

print("\nTOTAL FILES FIXED:", fixed)
