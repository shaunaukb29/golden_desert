const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";
const ROOT_DIR = process.cwd();

const CARS_JSON_PATH = path.join(ROOT_DIR, "cars", "cars.json");
const TEMPLATE_PATH = path.join(ROOT_DIR, "cars", "template.html");

function loadCars() {
  return JSON.parse(fs.readFileSync(CARS_JSON_PATH, "utf-8"));
}

/**
 * Path helper — slug already excludes the make, so no more
 * /toyota/toyota-camry-repair-cost.html stutter.
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
 * Falls back to generic categories only if a car has no data yet, so
 * pages never break, but incentivizes filling in real data.
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

/**
 * SEO intent paragraph, now city-aware instead of generic "UAE".
 */
function buildIntentBlock(car) {
  const city = car.city || "the UAE";
  return `
<p>
${car.make} ${car.model} repair cost data for ${city}, covering dealer vs independent garage pricing, model-specific known issues${car.year_range ? ` for ${car.year_range} model years` : ""}, and realistic annual ownership estimates.
</p>
`;
}

/**
 * Related models — same make, different model.
 */
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

/**
 * Hub links — one per brand, pointing at that brand's hub/index page.
 */
function buildHubLinks(allCars) {
  const makes = [...new Set(allCars.map(c => c.make))];
  return makes
    .map(make => {
      const makeLower = make.toLowerCase().replace(/\s+/g, "-");
      return `<li><a href="/${makeLower}/">${make} Repair Cost Guides</a></li>`;
    })
    .join("\n");
}

/**
 * Popular links — cars explicitly flagged "popular": true in cars.json,
 * so this is editorially controlled rather than arbitrary.
 */
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

/**
 * Render page
 */
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
 * Brand hub page — lists every model page for that make.
 * Fixes the previously-dead /toyota/, /bmw/ links in the footer.
 */
function renderBrandHub(make, carsForMake) {
  const rows = carsForMake
    .map(c => {
      const { url } = getOutputPath(c);
      return `<li><a href="${url}">${c.make} ${c.model} \u2014 repair &amp; maintenance cost</a></li>`;
    })
    .join("\n");

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>${make} Repair Cost Guides UAE (2026) | Carithm</title>
<meta name="description" content="All ${make} repair and maintenance cost guides for the UAE \u2014 dealer vs independent pricing, common issues, and ownership estimates.">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="canonical" href="${BASE_URL}/${make.toLowerCase().replace(/\s+/g, "-")}/">
<style>
body{font-family:system-ui,sans-serif;background:#0b0f14;color:#fff;margin:0;padding:40px;line-height:1.7}
.container{max-width:850px;margin:auto}
a{color:#4ade80}
ul{padding-left:18px}
</style>
</head>
<body>
<main class="container">
<p><a href="/repair-costs/">\u2190 Browse all car repair guides</a></p>
<h1>${make} Repair &amp; Maintenance Cost Guides (UAE)</h1>
<ul>
${rows}
</ul>
</main>
</body>
</html>`;
}

/**
 * Site-wide hub page — fixes the previously-dead /repair-costs/ link
 * that every generated page already links to.
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

function generatePages() {
  console.log("\ud83d\ude97 Generating pages with real per-car data");

  const cars = loadCars();
  const template = fs.readFileSync(TEMPLATE_PATH, "utf-8");

  const allUrls = [];
  let count = 0;

  for (const car of cars) {
    const { dir, filePath } = getOutputPath(car);
    const { output, url } = renderCarPage(template, car, cars);

    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(filePath, output);

    allUrls.push(url);
    console.log(`\u2714 ${url}`);
    count++;
  }

  // Brand hub pages
  const makes = [...new Set(cars.map(c => c.make))];
  for (const make of makes) {
    const makeLower = make.toLowerCase().replace(/\s+/g, "-");
    const dir = path.join(ROOT_DIR, makeLower);
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, "index.html"), renderBrandHub(make, cars.filter(c => c.make === make)));
    allUrls.push(`/${makeLower}/`);
    console.log(`\u2714 /${makeLower}/ (brand hub)`);
  }

  // Site-wide hub page
  const hubDir = path.join(ROOT_DIR, "repair-costs");
  fs.mkdirSync(hubDir, { recursive: true });
  fs.writeFileSync(path.join(hubDir, "index.html"), renderSiteHub(cars));
  allUrls.push("/repair-costs/");
  console.log("\u2714 /repair-costs/ (site hub)");

  console.log(`\n\u2705 Generated ${count} car pages, ${makes.length} brand hubs, 1 site hub`);
  console.log("\u2139\ufe0f  Run `npm run build` (or `node generate-sitemap.js`) next to regenerate sitemap_v4.xml");
}

generatePages();
