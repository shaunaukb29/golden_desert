from pathlib import Path

root = Path(".")

OLD = "/maintenance-guide/"
NEW = "/research/servicing.html"   # <-- safe replacement page you already have

fixed = 0

for file in root.rglob("*.html"):
    text = file.read_text(errors="ignore")

    if OLD in text:
        text = text.replace(OLD, NEW)
        file.write_text(text)
        print("fixed:", file)

        fixed += 1

print("\nTOTAL FILES FIXED:", fixed)
