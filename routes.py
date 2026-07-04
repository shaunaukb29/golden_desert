from pathlib import Path

root = Path(".")
routes = set()

for f in root.rglob("*.html"):
    if "node_modules" in f.parts or ".git" in f.parts:
        continue

    rel = f.relative_to(root).as_posix()

    if rel.endswith("index.html"):
        route = "/" + str(Path(rel).parent)
        if route == "/.":
            route = "/"
    else:
        route = "/" + rel[:-5]

    routes.add(route)

print("Total routes:", len(routes))

for r in sorted(routes):
    print(r)
