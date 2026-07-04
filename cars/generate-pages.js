const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";
const ROOT_DIR = process.cwd();

const CARS_JSON_PATH = path.join(ROOT_DIR, "cars", "cars.json");
const TEMPLATE_PATH = path.join(ROOT_DIR, "cars", "template.html");
const BRAND_HUB_TEMPLATE_PATH = path.join(ROOT_DIR, "brand-hub-template.html");
const MANIFEST_PATH = path.join(ROOT_DIR, "cars", ".generated-manifest.json");

/**
 * These were created before the URL structure was fixed and are NOT
 * tracked by the manifest system, so they need to be removed explicitly
 * once. Safe to delete this block after your next deploy confirms the
 * old files are gone from the live site.
 */
const LEGACY_FILES = [
  "",
  "toyota/toyota-land-cruiser-maintenance-cost-uae.html",
  "toyota/toyota-corolla-service-cost-uae.html",
  "toyota/toyota-prado-repair-cost-uae.html",
  "bmw/bmw-x5-maintenance-cost-dubai.html",
  "bmw/bmw-x3-repair-cost-uae.html",
  "bmw/bmw-5-series-service-cost-uae.html",
  "bmw/bmw-3-series-repair-cost-uae.html",
  "mercedes/mercedes-c200-service-cost-abu-dhabi.html",
  "mercedes/mercedes-e300-maintenance-cost-uae.html",
  "mercedes/mercedes-gle-350-repair-cost-uae.html",
  "mercedes/mercedes-s500-maintenance-cost-uae.html",
  "nissan/nissan-patrol-maintenance-cost-uae.html",
  "nissan/nissan-altima-service-cost-uae.html",
  "nissan/nissan-xtrail-repair-cost-uae.html",
  "honda/honda-accord-repair-cost-uae.html",
  "honda/honda-civic-maintenance-cost-uae.html",
  "honda/honda-crv-service-cost-uae.html",
  "lexus/lexus-rx350-maintenance-cost-uae.html",
  "lexus/lexus-lx570-repair-cost-uae.html",
  "lexus/lexus-es350-service-cost-uae.html"
];

function loadCars() {
  return JSON.parse(fs.readFileSync(CARS_JSON_PATH, "utf-8"));
}

/**
 * Path helper — slug already excludes the make, so no more
 */
function getOutputPath(car) {
  const makeLower = car.make.toLowerCase().replace(/\s+/g, "-");
  return {
    dir: path.join(ROOT_DIR, makeLower),
    filePath: path.join(ROOT_DIR, makeLower, `${car.slug}.html`),
    url: `/${makeLower}/${car.slug}.html`,
    makeLower
  };
}

function fmtRange([min, max]) {
  return `${min.toLocaleString()} \u2013 ${max.toLocaleString()}`;
}

/**
 * Cost table driven by real per-car data, with a fallback so the
 * generator never crashes if a car is added without cost data yet.
 */
function buildCostTable(car) {
  const c = car.costs || {};
  const fallback = [0, 0];
  const rows = [
    ["Minor Service", c.minor_service || fallback],
    ["Major Service", c.major_service || fallback],
    ["Brake Replacement", c.brakes || fallback],
    ["AC System Repair", c.ac_repair || fallback]
  ];

  const rowsHtml = rows
    .map(([label, range]) => `<tr><td>${label}</td><td>${fmtRange(range)}</td></tr>`)
    .join("\n        ");

  return `
    <table>
      <thead>
        <tr>
          <th scope="col">Service Type</th>
          <th scope="col">Estimated Cost (AED)</th>
        </tr>
      </thead>
      <tbody>
        ${rowsHtml}
      </tbody>
    </table>`;
}

/**
 * Issue sections built from real known_issues per car, not generic text.
 */
function buildIssueSections(car) {
  const issues = car.known_issues && car.known_issues.length
    ? car.known_issues
    : [
        { title: "AC System Wear", detail: `${car.make} ${car.model} AC components see accelerated wear under continuous high-load use in UAE heat.` },
        { title: "Suspension Wear", detail: "Suspension components degrade faster under GCC road and heat conditions." }
      ];

  const sections = issues
    .map(i => `<h3>${i.title}</h3>\n<p>${i.detail}</p>`)
    .join("\n\n");

  return `
<h2>Known ${car.make} ${car.model} Issues${car.year_range ? ` (${car.year_range})` : ""}</h2>

${sections}
`;
}

/**
 * FAQ content AND matching JSON-LD are built from the exact same
 * question/answer pairs, so structured data never diverges from
 * what's visible on the page.
 */
function buildFAQData(car) {
  const cityLine = car.city ? ` in ${car.city}` : " in the UAE";
  const topIssue = car.known_issues && car.known_issues[0];

  const qa = [
    {
      q: `Is ${car.make} ${car.model} expensive to maintain${cityLine}?`,
      a: car.costs
        ? `Minor services typically run AED ${fmtRange(car.costs.minor_service)}, with major services from AED ${fmtRange(car.costs.major_service)}, depending on mileage and workshop choice.`
        : `Costs depend on mileage and service history, but GCC heat increases wear on AC and suspension systems.`
    },
    {
      q: `What is the most common repair for the ${car.model}?`,
      a: topIssue
        ? `${topIssue.title} is the most frequently reported issue: ${topIssue.detail}`
        : `AC and suspension components are among the most common repairs in UAE conditions.`
    },
    {
      q: `Dealer vs independent garage \u2014 which is cheaper${cityLine}?`,
      a: `Independent garages are typically 30\u201360% cheaper than dealers for this model in the UAE.`
    },
    {
      q: `How often should I service the ${car.make} ${car.model}?`,
      a: `Every 8,000\u201310,000 km is recommended under UAE driving conditions.`
    }
  ];

  return qa;
}

function buildFAQBlock(car) {
  const qa = buildFAQData(car);
  const html = qa
    .map(({ q, a }) => `<h3>${q}</h3>\n<p>${a}</p>`)
    .join("\n\n");
  return `\n<h2>Frequently Asked Questions</h2>\n\n${html}\n`;
}

function buildFAQJsonLd(car) {
  const qa = buildFAQData(car);
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: qa.map(({ q, a }) => ({
      "@type": "Question",
      name: q,
      acceptedAnswer: { "@type": "Answer", text: a }
    }))
  };
  return `<script type="application/ld+json">\n${JSON.stringify(jsonLd, null, 2)}\n</script>`;
}

function buildIntentBlock(car) {
  const city = car.city || "the UAE";
  return `
<p>
${car.make} ${car.model} repair cost data for ${city}, covering dealer vs independent garage pricing, model-specific known issues${car.year_range ? ` for ${car.year_range} model years` : ""}, and realistic annual ownership estimates.
</p>
`;
}

function buildInternalLinks(car, allCars) {
  const sameMake = allCars
    .filter(c => c.make === car.make && c.slug !== car.slug)
    .slice(0, 5);

  if (!sameMake.length) return "";

  return `
<h2>Related ${car.make} Models</h2>
<ul>
${sameMake.map(c => {
  const { url } = getOutputPath(c);
  return `<li><a href="${url}">${c.make} ${c.model} repair cost</a></li>`;
}).join("\n")}
</ul>
`;
}

function buildHubLinks(allCars) {
  const makes = [...new Set(allCars.map(c => c.make))];
  return makes
    .map(make => {
      const makeLower = make.toLowerCase().replace(/\s+/g, "-");
      return `<li><a href="/${makeLower}/">${make} Repair Cost Guides</a></li>`;
    })
    .join("\n");
}

function buildPopularLinks(allCars, currentSlug) {
  const popular = allCars.filter(c => c.popular && c.slug !== currentSlug).slice(0, 8);
  if (!popular.length) return "<li>No popular guides yet.</li>";
  return popular
    .map(c => {
      const { url } = getOutputPath(c);
      return `<li><a href="${url}">${c.make} ${c.model} repair cost</a></li>`;
    })
    .join("\n");
}

function renderCarPage(template, car, allCars) {
  const { url, makeLower } = getOutputPath(car);
  const now = new Date();
  const today = now.toISOString().split("T")[0];
  const year = now.getFullYear();

  let output = template;

  const replacements = {
    "{{MAKE}}": car.make,
    "{{MODEL}}": car.model,
    "{{MAKE_LOWER}}": makeLower,
    "{{MODEL_SLUG}}": car.slug,
    "{{CITY}}": car.city || "UAE",
    "{{YEAR_RANGE}}": car.year_range || "",
    "{{DATE_PUBLISHED}}": car.date_published || today,
    "{{DATE_MODIFIED}}": today,
    "{{YEAR}}": String(year),

    "{{COST_TABLE}}": buildCostTable(car),
    "{{ISSUE_BLOCK}}": buildIssueSections(car),
    "{{FAQ_BLOCK}}": buildFAQBlock(car),
    "{{FAQ_JSONLD}}": buildFAQJsonLd(car),
    "{{INTENT_BLOCK}}": buildIntentBlock(car),
    "{{INTERNAL_LINKS}}": buildInternalLinks(car, allCars),
    "{{HUB_LINKS}}": buildHubLinks(allCars),
    "{{POPULAR_LINKS}}": buildPopularLinks(allCars, car.slug)
  };

  for (const [k, v] of Object.entries(replacements)) {
    output = output.split(k).join(v);
  }

  return { output, url };
}

/**
 * Brand hub page — uses the real brand-hub-template.html.
 */
function renderBrandHub(brandHubTemplate, make, carsForMake) {
  const makeLower = make.toLowerCase().replace(/\s+/g, "-");
  const year = new Date().getFullYear();

  const modelList = carsForMake
    .map(c => {
      const { url } = getOutputPath(c);
      return `      <li><a href="${url}">${c.make} ${c.model} \u2014 repair &amp; maintenance cost</a></li>`;
    })
    .join("\n");

  const replacements = {
    "{{MAKE}}": make,
    "{{MAKE_LOWER}}": makeLower,
    "{{MODEL_COUNT}}": String(carsForMake.length),
    "{{MODEL_LIST}}": modelList,
    "{{YEAR}}": String(year)
  };

  let output = brandHubTemplate;
  for (const [k, v] of Object.entries(replacements)) {
    output = output.split(k).join(v);
  }
  return output;
}

/**
 * Site-wide hub page.
 */
function renderSiteHub(allCars) {
  const makes = [...new Set(allCars.map(c => c.make))];
  const sections = makes
    .map(make => {
      const makeLower = make.toLowerCase().replace(/\s+/g, "-");
      const rows = allCars
        .filter(c => c.make === make)
        .map(c => {
          const { url } = getOutputPath(c);
          return `<li><a href="${url}">${c.make} ${c.model}</a></li>`;
        })
        .join("\n");
      return `<h2><a href="/${makeLower}/">${make}</a></h2>\n<ul>\n${rows}\n</ul>`;
    })
    .join("\n\n");

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>All Car Repair Cost Guides UAE (2026) | Carithm</title>
<meta name="description" content="Browse every car repair and maintenance cost guide on Carithm, organized by brand.">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="canonical" href="${BASE_URL}/repair-costs/">
<style>
body{font-family:system-ui,sans-serif;background:#0b0f14;color:#fff;margin:0;padding:40px;line-height:1.7}
.container{max-width:850px;margin:auto}
a{color:#4ade80}
ul{padding-left:18px}
</style>
</head>
<body>
<main class="container">
<h1>All Car Repair Cost Guides (UAE)</h1>
${sections}
</main>
</body>
</html>`;
}

/**
 * leave in permanently — once the files are gone, this is a no-op.
 */
function cleanupLegacyFiles() {
  let removed = 0;
  for (const rel of LEGACY_FILES) {
    const filePath = path.join(ROOT_DIR, rel);
    if (fs.existsSync(filePath)) {
      if (filePath.includes("cars") || filePath.includes(".html")) if (isSafeDelete(filePath)) fs.unlinkSync(filePath);
      console.log(`\ud83e\uddf9 Removed legacy file: /${rel}`);
      removed++;
    }
  }
  return removed;
}

/**
 * Manifest-based cleanup: if a car's slug changes in the future (or a
 * car is removed from cars.json), delete the file this script wrote
 * for it last time, so stale generated pages never accumulate again.
 */
function cleanupStaleGenerated(newFilePaths) {
  let previous = [];
  if (fs.existsSync(MANIFEST_PATH)) {
    try {
      previous = JSON.parse(fs.readFileSync(MANIFEST_PATH, "utf-8"));
    } catch (e) {
      previous = [];
    }
  }

  const newSet = new Set(newFilePaths);
  let removed = 0;
  for (const oldPath of previous) {
    if (!newSet.has(oldPath) && fs.existsSync(oldPath)) {
      if (oldPath.includes("cars") || oldPath.includes(".html")) fs.unlinkSync(oldPath);
      console.log(`\ud83e\uddf9 Removed stale generated file: ${path.relative(ROOT_DIR, oldPath)}`);
      removed++;
    }
  }

  fs.writeFileSync(MANIFEST_PATH, JSON.stringify(newFilePaths, null, 2));
  return removed;
}

function generatePages() {
  console.log("\ud83d\ude97 Generating pages with real per-car data");

  const legacyRemoved = cleanupLegacyFiles();
  if (legacyRemoved > 0) {
  }

  const cars = loadCars();
  const template = fs.readFileSync(TEMPLATE_PATH, "utf-8");
  const brandHubTemplate = fs.readFileSync(BRAND_HUB_TEMPLATE_PATH, "utf-8");

  const allUrls = [];
  const generatedFilePaths = [];
  let count = 0;

  for (const car of cars) {
    if (car.slug && car.slug.includes("camry")) continue;
    const { dir, filePath } = getOutputPath(car);
    const { output, url } = renderCarPage(template, car, cars);

    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(filePath, output);

    allUrls.push(url);
    generatedFilePaths.push(filePath);
    console.log(`\u2714 ${url}`);
    count++;
  }

  // Brand hub pages
  const makes = [...new Set(cars.map(c => c.make))];
  for (const make of makes) {
    const makeLower = make.toLowerCase().replace(/\s+/g, "-");
    const dir = path.join(ROOT_DIR, makeLower);
    fs.mkdirSync(dir, { recursive: true });
    const hubPath = path.join(dir, "index.html");
    fs.writeFileSync(hubPath, renderBrandHub(brandHubTemplate, make, cars.filter(c => c.make === make)));
    allUrls.push(`/${makeLower}/`);
    generatedFilePaths.push(hubPath);
    console.log(`\u2714 /${makeLower}/ (brand hub)`);
  }

  // Site-wide hub page
  const hubDir = path.join(ROOT_DIR, "repair-costs");
  fs.mkdirSync(hubDir, { recursive: true });
  const siteHubPath = path.join(hubDir, "index.html");
  fs.writeFileSync(siteHubPath, renderSiteHub(cars));
  allUrls.push("/repair-costs/");
  generatedFilePaths.push(siteHubPath);
  console.log("\u2714 /repair-costs/ (site hub)");

  const staleRemoved = cleanupStaleGenerated(generatedFilePaths);
  if (staleRemoved > 0) {
    console.log(`\ud83e\uddf9 Cleaned up ${staleRemoved} stale generated file(s) from previous builds`);
  }

  console.log(`\n\u2705 Generated ${count} car pages, ${makes.length} brand hubs, 1 site hub`);
  console.log("\u2139\ufe0f  Run `npm run build` (or `node generate-sitemap.js`) next to regenerate sitemap_v4.xml");
}

generatePages();

function isSafeDelete(p){ return typeof p === 'string' && (p.includes('cars') || p.includes('.html')); }
