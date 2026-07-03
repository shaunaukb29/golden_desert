const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";
const ROOT_DIR = process.cwd();

const CARS_JSON_PATH = path.join(ROOT_DIR, "cars", "cars.json");
const TEMPLATE_PATH = path.join(ROOT_DIR, "cars", "template.html");

/**
 * Load cars
 */
function loadCars() {
  return JSON.parse(fs.readFileSync(CARS_JSON_PATH, "utf-8"));
}

/**
 * Path helper
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

/**
 * 🔥 ISSUE CLUSTERS (LEVEL 5.5 CORE)
 */
function buildIssueSections(car) {
  const model = car.model.toLowerCase();

  return `
<h2>Common ${car.make} ${car.model} Problems in UAE</h2>

<h3>❄️ AC System Issues</h3>
<p>In UAE heat, ${car.make} ${car.model} AC compressor wear is one of the most common repair costs due to continuous high-load usage.</p>

<h3>⚙️ Transmission / Gearbox</h3>
<p>Gearbox wear in ${car.model} models can increase repair costs significantly, especially in stop-and-go Dubai traffic conditions.</p>

<h3>🛞 Suspension Problems</h3>
<p>Suspension components degrade faster in GCC road conditions due to heat and road texture stress.</p>

<h3>🔌 Electrical Issues</h3>
<p>Sensor failures and electrical degradation can occur in older ${car.make} ${car.model} units due to heat exposure.</p>
`;
}

/**
 * 🔥 INTENT FAQ GENERATOR
 */
function buildFAQ(car) {
  return `
<h2>Frequently Asked Questions</h2>

<h3>Is ${car.make} ${car.model} expensive to maintain in UAE?</h3>
<p>It depends on mileage, but GCC heat significantly increases AC and suspension repair frequency.</p>

<h3>What is the most common repair for ${car.model}?</h3>
<p>AC compressor and suspension components are among the most common repairs in UAE conditions.</p>

<h3>Dealer vs garage — which is cheaper?</h3>
<p>Independent garages are typically 30–60% cheaper than dealers in UAE.</p>

<h3>How often should I service it?</h3>
<p>Every 8,000–10,000 km is recommended under UAE driving conditions.</p>
`;
}

/**
 * 🔥 SEO INTENT LAYER
 */
function buildIntentBlock(car) {
  return `
<p>
${car.make} ${car.model} repair cost UAE analysis includes dealer vs independent garage pricing, common issues in Dubai heat, and long-term maintenance breakdowns.
</p>
`;
}

/**
 * SMART INTERNAL LINKS (authority graph)
 */
function buildInternalLinks(car, allCars) {
  const sameMake = allCars
    .filter(c => c.make === car.make && c.slug !== car.slug)
    .slice(0, 5);

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
 * Render page
 */
function renderCarPage(template, car, allCars) {
  const { url, makeLower } = getOutputPath(car);
  const now = new Date();

  const today = now.toISOString().split("T")[0];
  const year = now.getFullYear();

  let output = template;

  const issueBlock = buildIssueSections(car);
  const faqBlock = buildFAQ(car);
  const intentBlock = buildIntentBlock(car);
  const internalLinks = buildInternalLinks(car, allCars);

  const replacements = {
    "{{MAKE}}": car.make,
    "{{MODEL}}": car.model,
    "{{MAKE_LOWER}}": makeLower,
    "{{MODEL_SLUG}}": car.slug,
    "{{DATE_PUBLISHED}}": car.date_published || today,
    "{{DATE_MODIFIED}}": today,
    "{{YEAR}}": String(year),

    "{{ISSUE_BLOCK}}": issueBlock,
    "{{FAQ_BLOCK}}": faqBlock,
    "{{INTENT_BLOCK}}": intentBlock,
    "{{INTERNAL_LINKS}}": internalLinks
  };

  for (const [k, v] of Object.entries(replacements)) {
    output = output.split(k).join(v);
  }

  return { output, url };
}

/**
 * MAIN
 */
function generatePages() {
  console.log("🚗 LEVEL 5.5 SEO AUTHORITY MODE");

  const cars = loadCars();
  const template = fs.readFileSync(TEMPLATE_PATH, "utf-8");

  let count = 0;

  for (const car of cars) {
    const { dir, filePath } = getOutputPath(car);
    const { output, url } = renderCarPage(template, car, cars);

    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(filePath, output);

    console.log(`✔ ${url}`);
    count++;
  }

  console.log(`\n✅ Generated ${count} authority pages`);
}

generatePages();
