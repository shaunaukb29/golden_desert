const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";

const ROOT = process.cwd();
const OUTPUT_PATH = path.join(ROOT, "sitemap_v4.xml");

const CARS_PATH = path.join(ROOT, "cars", "cars.json");

function getCarUrls() {
  if (!fs.existsSync(CARS_PATH)) return [];

  const cars = JSON.parse(fs.readFileSync(CARS_PATH, "utf-8"));

  return cars.map((car) => {
    const make = car.make.toLowerCase().replace(/\s+/g, "-");
    const model = car.model.toLowerCase().replace(/\s+/g, "-");

    const slug =
      car.slug ||
      `${car.type || "repair-cost"}-${car.location || "uae"}`;

    return `/${make}/${model}/${slug}.html`;
  });
}

function buildXml(urls) {
  const today = new Date().toISOString().split("T")[0];

  return urls
    .map((u) => {
      return `
  <url>
    <loc>${BASE_URL}${u}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>`;
    })
    .join("\n");
}

function generateSitemap() {
  console.log("🗺 Generating sitemap...");

  const carUrls = getCarUrls();
  const dynamicXml = buildXml(carUrls);

  const finalXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

  <!-- STATIC PAGES -->
  <url>
    <loc>${BASE_URL}/</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>

  <url>
    <loc>${BASE_URL}/blog/</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>${BASE_URL}/predictive/</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>${BASE_URL}/about/</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>

  <url>
    <loc>${BASE_URL}/research/</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- CAR PAGES -->
${dynamicXml}

</urlset>`;

  fs.writeFileSync(OUTPUT_PATH, finalXml, "utf-8");

  console.log(`✅ Sitemap generated with ${carUrls.length} car pages`);
}

generateSitemap();
