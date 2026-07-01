const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";
const ROOT = process.cwd();
const OUTPUT_PATH = path.join(ROOT, "sitemap_v4.xml");
const CARS_PATH = path.join(ROOT, "cars", "cars.json");

/**
 * Build car page URLs, matching the flat pattern used by cars/generate-pages.js:
 * /{make}/{slug}.html
 * Only includes a URL if the file actually exists on disk, to avoid
 * submitting broken links to Google/Bing.
 */
function getCarUrls() {
  if (!fs.existsSync(CARS_PATH)) return [];

  const cars = JSON.parse(fs.readFileSync(CARS_PATH, "utf-8"));
  const urls = [];

  for (const car of cars) {
    if (!car.slug) {
      console.warn(`⚠️  Skipping car with no slug: ${car.make} ${car.model}`);
      continue;
    }

    const make = car.make.toLowerCase().replace(/\s+/g, "-");
    const relativePath = `/${make}/${car.slug}.html`;
    const diskPath = path.join(ROOT, make, `${car.slug}.html`);

    if (!fs.existsSync(diskPath)) {
      console.warn(`⚠️  Skipping missing file (not yet generated?): ${relativePath}`);
      continue;
    }

    urls.push({ url: relativePath, filePath: diskPath });
  }

  return urls;
}

function getLastMod(filePath) {
  try {
    return fs.statSync(filePath).mtime.toISOString().split("T")[0];
  } catch (e) {
    return new Date().toISOString().split("T")[0];
  }
}

/**
 * Scan a flat content folder (blog/, research/) for .html files.
 * Excludes index.html from individual listing since it's added separately
 * as the folder's hub URL.
 */
function scanContentFolder(folderName, options = {}) {
  const folderPath = path.join(ROOT, folderName);
  if (!fs.existsSync(folderPath)) return [];

  const urls = [];
  const entries = fs.readdirSync(folderPath);

  for (const entry of entries) {
    if (!entry.endsWith(".html")) continue;
    if (entry === "index.html") continue; // hub page added separately
    const filePath = path.join(folderPath, entry);
    if (!fs.statSync(filePath).isFile()) continue;
    urls.push({ url: `/${folderName}/${entry}`, filePath, priority: options.priority || "0.7" });
  }

  return urls;
}

/**
 * Brand hub URLs (/{make}/), derived from cars.json makes.
 * Only included if the hub file actually exists on disk.
 */
function getBrandHubUrls() {
  if (!fs.existsSync(CARS_PATH)) return [];

  const cars = JSON.parse(fs.readFileSync(CARS_PATH, "utf-8"));
  const makes = [...new Set(cars.map((c) => c.make.toLowerCase().replace(/\s+/g, "-")))];
  const urls = [];

  for (const make of makes) {
    const filePath = path.join(ROOT, make, "index.html");
    if (!fs.existsSync(filePath)) {
      console.warn(`⚠️  Skipping missing brand hub: /${make}/`);
      continue;
    }
    urls.push({ url: `/${make}/`, filePath, priority: "0.8" });
  }

  return urls;
}

function buildXml(urls) {
  return urls
    .map(({ url, filePath, priority }) => {
      const lastmod = getLastMod(filePath);
      return `
  <url>
    <loc>${BASE_URL}${url}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>${priority || "0.7"}</priority>
  </url>`;
    })
    .join("\n");
}

function generateSitemap() {
  console.log("🗺 Generating sitemap...");

  const today = new Date().toISOString().split("T")[0];

  const carUrls = getCarUrls().map((u) => ({ ...u, priority: "0.9" }));
  const brandUrls = getBrandHubUrls();
  const blogUrls = scanContentFolder("blog", { priority: "0.8" });
  const researchUrls = scanContentFolder("research", { priority: "0.7" });

  const allDynamicXml = buildXml([...brandUrls, ...carUrls, ...blogUrls, ...researchUrls]);

  const finalXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- STATIC PAGES -->
  <url>
    <loc>${BASE_URL}/</loc>
    <lastmod>${today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>${BASE_URL}/blog/</loc>
    <lastmod>${today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>${BASE_URL}/predictive/</loc>
    <lastmod>${today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>${BASE_URL}/about/</loc>
    <lastmod>${today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>${BASE_URL}/research/</loc>
    <lastmod>${today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <!-- LOCATION HUB PAGES -->
  <url>
    <loc>${BASE_URL}/dubai/car-repairs/</loc>
    <lastmod>${today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>${BASE_URL}/abu-dhabi/car-repairs/</loc>
    <lastmod>${today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>${BASE_URL}/sharjah/car-repairs/</loc>
    <lastmod>${today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <!-- BRAND HUBS, CAR PAGES, BLOG POSTS, RESEARCH PAGES (auto-discovered) -->
${allDynamicXml}
</urlset>`;

  fs.writeFileSync(OUTPUT_PATH, finalXml, "utf-8");
  console.log(
    `✅ Sitemap generated: ${brandUrls.length} brand hubs, ${carUrls.length} car pages, ${blogUrls.length} blog posts, ${researchUrls.length} research pages`
  );
}

generateSitemap();
