const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";
const ROOT_DIR = process.cwd();

// ignore noise folders
const IGNORE = new Set(["node_modules", ".git", ".vercel"]);

// store clean URLs only (dedupe)
const urlSet = new Set();

/**
 * STATIC PAGES (explicit control = SEO stability)
 */
const STATIC_URLS = [
  "/",
  "/blog/",
  "/predictive/",
  "/research/",
  "/about/"
];

/**
 * scan only relevant car structure:
 * /toyota/model/file.html
 * /bmw/model/file.html
 */
function scanCars() {
  const brands = ["toyota", "bmw", "mercedes"];

  for (const brand of brands) {
    const brandPath = path.join(ROOT_DIR, brand);

    if (!fs.existsSync(brandPath)) continue;

    const models = fs.readdirSync(brandPath);

    for (const model of models) {
      const modelPath = path.join(brandPath, model);

      if (!fs.existsSync(modelPath)) continue;

      const files = fs.readdirSync(modelPath);

      for (const file of files) {
        if (!file.endsWith(".html")) continue;

        const url = `/${brand}/${model}/${file}`;
        urlSet.add(url);
      }
    }
  }
}

/**
 * scan extra html files (blogs, static pages, etc.)
 */
function scanMisc(dir) {
  const files = fs.readdirSync(dir);

  for (const file of files) {
    const full = path.join(dir, file);

    if (IGNORE.has(file)) continue;

    const stat = fs.statSync(full);

    if (stat.isDirectory()) {
      scanMisc(full);
    } else if (file.endsWith(".html")) {
      const relative = full
        .replace(ROOT_DIR, "")
        .replace(/\\/g, "/");

      urlSet.add(relative);
    }
  }
}

/**
 * convert to XML
 */
function buildXml() {
  const today = new Date().toISOString().split("T")[0];

  const urls = Array.from(urlSet);

  return urls.map((url) => {
    let priority = "0.6";

    // homepage
    if (url === "/" || url === "/index.html") {
      priority = "1.0";
    }

    // brand + model pages
    else if (
      url.includes("/toyota/") ||
      url.includes("/bmw/") ||
      url.includes("/mercedes/")
    ) {
      priority = "0.9";
    }

    // blog/content pages
    else if (url.includes("/blog/")) {
      priority = "0.8";
    }

    return `
  <url>
    <loc>${BASE_URL}${url}</loc>
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
  console.log("🗺 Generating sitemap...");

  // add static pages first
  STATIC_URLS.forEach((u) => urlSet.add(u));

  // scan structured car pages
  scanCars();

  // scan everything else (blogs etc.)
  scanMisc(ROOT_DIR);

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

${buildXml()}

</urlset>`;

  const outputPath = path.join(ROOT_DIR, "sitemap_v4.xml");

  fs.writeFileSync(outputPath, xml, "utf-8");

  console.log(`✅ Sitemap generated with ${urlSet.size} URLs`);
}

generateSitemap();
