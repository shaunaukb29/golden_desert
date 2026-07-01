const fs = require("fs");
const path = require("path");
const https = require("https");

const BASE_URL = "https://carithm.vercel.app";
const ROOT_DIR = process.cwd();

const CARS_JSON_PATH = path.join(ROOT_DIR, "cars", "cars.json");
const TEMPLATE_PATH = path.join(ROOT_DIR, "cars", "template.html");
const BRAND_TEMPLATE_PATH = path.join(ROOT_DIR, "brand-hub-template.html");
const HOMEPAGE_PATH = path.join(ROOT_DIR, "index.html");

const AUTO_LINKS_START = "<!-- AUTO_CAR_LINKS_START -->";
const AUTO_LINKS_END = "<!-- AUTO_CAR_LINKS_END -->";

// IndexNow config
// Generate a key at https://www.bing.com/indexnow — it's just a random hex string.
// Host it at https://carithm.vercel.app/{INDEXNOW_KEY}.txt containing only the key itself.
const INDEXNOW_KEY = process.env.INDEXNOW_KEY || "REPLACE_WITH_YOUR_INDEXNOW_KEY";
const INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow";

/**
 * Load and parse cars.json
 */
function loadCars() {
  const raw = fs.readFileSync(CARS_JSON_PATH, "utf-8");
  return JSON.parse(raw);
}

/**
 * Build the file path + URL for a given car.
 * Uses the car's own slug as the filename: /{make}/{slug}.html
 */
function getOutputPath(car) {
  const makeLower = car.make.toLowerCase().replace(/\s+/g, "-");
  const dir = path.join(ROOT_DIR, makeLower);
  const filePath = path.join(dir, `${car.slug}.html`);
  const url = `/${makeLower}/${car.slug}.html`;
  return { dir, filePath, url, makeLower };
}

/**
 * Build the related-links <li> markup for other models of the same make,
 * excluding the current car itself.
 */
function buildRelatedLinks(car, allCars) {
  const siblings = allCars.filter(
    (c) => c.make === car.make && c.slug !== car.slug
  );

  if (siblings.length === 0) return { html: "", hasRelated: false };

  const html = siblings
    .map((c) => {
      const { url } = getOutputPath(c);
      return `      <li><a href="${url}">${c.make} ${c.model} Repair Cost</a></li>`;
    })
    .join("\n");

  return { html, hasRelated: true };
}

/**
 * Resolve the {{#IF_RELATED_LINKS}}...{{/IF_RELATED_LINKS}} block.
 * Strips the block entirely if there are no related links, otherwise
 * keeps the inner content and removes just the markers.
 */
function resolveConditionalBlock(template, hasRelated) {
  const blockRegex = /{{#IF_RELATED_LINKS}}([\s\S]*?){{\/IF_RELATED_LINKS}}/;

  if (hasRelated) {
    return template.replace(blockRegex, (_, inner) => inner);
  }
  return template.replace(blockRegex, "");
}

/**
 * Fill all placeholders in the template for a single car.
 */
function renderCarPage(template, car, allCars) {
  const { url, makeLower } = getOutputPath(car);
  const modelSlug = car.slug.replace(new RegExp(`^${makeLower}-`), "");
  const today = new Date().toISOString().split("T")[0];
  const year = new Date().getFullYear();

  const { html: relatedLinksHtml, hasRelated } = buildRelatedLinks(car, allCars);

  let output = resolveConditionalBlock(template, hasRelated);

  const replacements = {
    "{{MAKE}}": car.make,
    "{{MODEL}}": car.model,
    "{{MAKE_LOWER}}": makeLower,
    "{{MODEL_SLUG}}": car.slug,
    "{{OG_IMAGE}}": car.og_image || `${BASE_URL}/og-image.png`,
    "{{DATE_PUBLISHED}}": car.date_published || today,
    "{{DATE_MODIFIED}}": today,
    "{{YEAR}}": String(year),
    "{{RELATED_LINKS}}": relatedLinksHtml,
  };

  for (const [placeholder, value] of Object.entries(replacements)) {
    output = output.split(placeholder).join(value);
  }

  return { output, url };
}

/**
 * Group cars by make.
 */
function groupByMake(cars) {
  const groups = new Map();
  for (const car of cars) {
    if (!groups.has(car.make)) groups.set(car.make, []);
    groups.get(car.make).push(car);
  }
  return groups;
}

/**
 * Generate one hub page per brand (e.g. /toyota/index.html) listing
 * every model page for that brand. Fixes the nav/hero links on the
 * homepage that point at /toyota, /bmw, /mercedes.
 */
function generateBrandHubs(cars) {
  if (!fs.existsSync(BRAND_TEMPLATE_PATH)) {
    console.warn("⚠️  brand-hub-template.html not found — skipping brand hub generation.");
    return [];
  }

  const brandTemplate = fs.readFileSync(BRAND_TEMPLATE_PATH, "utf-8");
  const grouped = groupByMake(cars);
  const generatedUrls = [];

  for (const [make, models] of grouped.entries()) {
    const makeLower = make.toLowerCase().replace(/\s+/g, "-");
    const dir = path.join(ROOT_DIR, makeLower);
    const filePath = path.join(dir, "index.html");
    const url = `/${makeLower}/`;

    const listHtml = models
      .map((c) => {
        const { url: carUrl } = getOutputPath(c);
        return `      <li><a href="${carUrl}">${c.make} ${c.model} Repair Cost</a></li>`;
      })
      .join("\n");

    let output = brandTemplate
      .split("{{MAKE}}").join(make)
      .split("{{MAKE_LOWER}}").join(makeLower)
      .split("{{MODEL_COUNT}}").join(String(models.length))
      .split("{{MODEL_LIST}}").join(listHtml)
      .split("{{YEAR}}").join(String(new Date().getFullYear()));

    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(filePath, output, "utf-8");
    generatedUrls.push(url);

    console.log(`  ✅ ${url} (${models.length} models)`);
  }

  return generatedUrls;
}

/**
 * Keep the homepage footer's model links in sync with cars.json.
 * Replaces everything between AUTO_CAR_LINKS_START/END markers.
 * If the homepage or markers are missing, this is skipped safely —
 * it never touches the file outside of those markers.
 */
function syncHomepageFooterLinks(cars) {
  if (!fs.existsSync(HOMEPAGE_PATH)) {
    console.warn("⚠️  index.html not found — skipping footer link sync.");
    return;
  }

  const html = fs.readFileSync(HOMEPAGE_PATH, "utf-8");
  const startIdx = html.indexOf(AUTO_LINKS_START);
  const endIdx = html.indexOf(AUTO_LINKS_END);

  if (startIdx === -1 || endIdx === -1 || endIdx < startIdx) {
    console.warn("⚠️  AUTO_CAR_LINKS markers not found in index.html — skipping footer link sync.");
    return;
  }

  const linksHtml = cars
    .map((car) => {
      const { url } = getOutputPath(car);
      return `    <li>\n      <a href="${url}">\n        ${car.make} ${car.model} Repair Cost\n      </a>\n    </li>`;
    })
    .join("\n\n");

  const before = html.slice(0, startIdx + AUTO_LINKS_START.length);
  const after = html.slice(endIdx);

  const updated = `${before}\n${linksHtml}\n    ${after}`;
  fs.writeFileSync(HOMEPAGE_PATH, updated, "utf-8");

  console.log(`  ✅ Homepage footer synced with ${cars.length} car links`);
}

/**
 * Ping IndexNow with the list of URLs that were generated/updated this run.
 */
function pingIndexNow(urls) {
  return new Promise((resolve) => {
    if (!urls.length) return resolve();

    if (!INDEXNOW_KEY || INDEXNOW_KEY === "REPLACE_WITH_YOUR_INDEXNOW_KEY") {
      console.warn("⚠️  INDEXNOW_KEY not set — skipping IndexNow ping.");
      return resolve();
    }

    const payload = JSON.stringify({
      host: "carithm.vercel.app",
      key: INDEXNOW_KEY,
      keyLocation: `${BASE_URL}/${INDEXNOW_KEY}.txt`,
      urlList: urls.map((u) => `${BASE_URL}${u}`),
    });

    const req = https.request(
      INDEXNOW_ENDPOINT,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          "Content-Length": Buffer.byteLength(payload),
        },
      },
      (res) => {
        console.log(`📡 IndexNow ping status: ${res.statusCode}`);
        res.on("data", () => {});
        res.on("end", resolve);
      }
    );

    req.on("error", (err) => {
      console.error("⚠️  IndexNow ping failed:", err.message);
      resolve();
    });

    req.write(payload);
    req.end();
  });
}

/**
 * MAIN
 */
async function generatePages() {
  console.log("🚗 Generating car pages...");

  const cars = loadCars();
  const template = fs.readFileSync(TEMPLATE_PATH, "utf-8");

  const generatedUrls = [];

  for (const car of cars) {
    const { dir, filePath } = getOutputPath(car);
    const { output, url } = renderCarPage(template, car, cars);

    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(filePath, output, "utf-8");
    generatedUrls.push(url);

    console.log(`  ✅ ${url}`);
  }

  console.log(`✅ Generated ${generatedUrls.length} car pages`);

  console.log("🏷️  Generating brand hub pages...");
  const brandUrls = generateBrandHubs(cars);
  console.log(`✅ Generated ${brandUrls.length} brand hub pages`);

  console.log("🔗 Syncing homepage footer links...");
  syncHomepageFooterLinks(cars);

  await pingIndexNow([...generatedUrls, ...brandUrls]);
}

generatePages().catch((err) => {
  console.error("❌ Page generation failed:", err);
  process.exit(1);
});
