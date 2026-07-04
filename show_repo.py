from pathlib import Path

root = Path(".")

print("\n📦 PROJECT FILE TREE\n")

for path in sorted(root.rglob("*")):
    if ".git" in str(path) or "node_modules" in str(path):
        continue

    if path.is_file():
        print("📄", path)
    else:
        print("📁", path)
