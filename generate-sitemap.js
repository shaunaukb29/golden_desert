const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";

const ROOT = process.cwd();

// your static sitemap file
const SITEMAP_PATH = path.join(ROOT, "sitemap_v4.xml");

const CAR_DIRS = ["toyota", "bmw", "mercedes"];

/**
 * Scan only generated car pages safely
 */
function getCarUrls() {
  let urls = [];

  for (const brand of CAR_DIRS) {
    const brandPath = path.join(ROOT, brand);

    if (!fs.existsSync(brandPath)) continue;

    const models = fs.readdirSync(brandPath);

    for (const model of models) {
      const modelPath = path.join(brandPath, model);

      if (!fs.existsSync(modelPath)) continue;

      const files = fs.readdirSync(modelPath);

      for (const file of files) {
        if (file.endsWith(".html")) {
          urls.push(`/${brand}/${model}/${file}`);
        }
      }
    }
  }

  return urls;
}

/**
 * Convert URLs into sitemap XML blocks
 */
function buildXml(urls) {
  const today = new Date().toISOString().split("T")[0];

  return urls.map((u) => {
    let priority = "0.8";

    if (u.includes("/toyota/") || u.includes("/bmw/") || u.includes("/mercedes/")) {
      priority = "0.9";
    }

    return `
  <url>
    <loc>${BASE_URL}${u}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>${priority}</priority>
  </url>`;
  }).join("\n");
}

/**
 * MAIN
 */
function generateSitemap() {
  console.log("🗺 Updating sitemap_v4.xml...");

  if (!fs.existsSync(SITEMAP_PATH)) {
    console.error("❌ sitemap_v4.xml not found");
    process.exit(1);
  }

  const staticXml = fs.readFileSync(SITEMAP_PATH, "utf-8");

  const carUrls = getCarUrls();
  const dynamicXml = buildXml(carUrls);

  // insert BEFORE closing tag
  const finalXml = staticXml.replace(
    "</urlset>",
    `${dynamicXml}\n</urlset>`
  );

  fs.writeFileSync(SITEMAP_PATH, finalXml, "utf-8");

  console.log(`✅ Sitemap updated with ${carUrls.length} car pages`);
}

generateSitemap();
