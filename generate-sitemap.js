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

function buildXml(carUrls) {
  return carUrls
    .map(({ url, filePath }) => {
      const lastmod = getLastMod(filePath);
      return `
  <url>
    <loc>${BASE_URL}${url}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>`;
    })
    .join("\n");
}

function generateSitemap() {
  console.log("🗺 Generating sitemap...");

  const today = new Date().toISOString().split("T")[0];
  const carUrls = getCarUrls();
  const dynamicXml = buildXml(carUrls);

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
    <priority>0.7</priority>
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
  <!-- CAR PAGES -->
${dynamicXml}
</urlset>`;

  fs.writeFileSync(OUTPUT_PATH, finalXml, "utf-8");
  console.log(`✅ Sitemap generated with ${carUrls.length} car pages`);
}

generateSitemap();
