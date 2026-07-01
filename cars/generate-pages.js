const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";
const ROOT_DIR = process.cwd();

// ignore noise folders/files
const IGNORE_DIRS = new Set(["node_modules", ".git", ".vercel"]);
const IGNORE_FILES = new Set([".DS_Store"]);

// store clean URLs only
const urlSet = new Set();

/**
 * STATIC PAGES (SEO core index)
 */
const STATIC_URLS = [
  "/",
  "/blog/",
  "/predictive/",
  "/research/",
  "/about/"
];

/**
 * Normalize URL (VERY IMPORTANT for SEO dedupe)
 */
function normalizeUrl(url) {
  return url
    .replace(/\\/g, "/")
    .replace(/\/+/g, "/")
    .replace(/\/index\.html$/, "/")
    .replace(/\.html$/, "");
}

/**
 * Scan structured car pages
 * /toyota/camry/service.html
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

        const rawUrl = `/${brand}/${model}/${file}`;
        const url = normalizeUrl(rawUrl);

        urlSet.add(url);
      }
    }
  }
}

/**
 * Scan misc HTML pages safely
 */
function scanMisc(dir) {
  let files;

  try {
    files = fs.readdirSync(dir);
  } catch (e) {
    return;
  }

  for (const file of files) {
    if (IGNORE_FILES.has(file)) continue;
    if (file.startsWith(".")) continue;

    const full = path.join(dir, file);

    let stat;
    try {
      stat = fs.statSync(full);
    } catch (e) {
      continue;
    }

    if (stat.isDirectory()) {
      if (IGNORE_DIRS.has(file)) continue;
      scanMisc(full);
    } else if (file.endsWith(".html")) {
      const relative = normalizeUrl(
        full.replace(ROOT_DIR, "").replace(/\\/g, "/")
      );

      urlSet.add(relative);
    }
  }
}

/**
 * Build XML entries
 */
function buildXml() {
  const today = new Date().toISOString().split("T")[0];

  return Array.from(urlSet)
    .map((url) => {
      let priority = "0.6";

      if (url === "/" || url === "/index") {
        priority = "1.0";
      } else if (
        url.includes("/toyota/") ||
        url.includes("/bmw/") ||
        url.includes("/mercedes/")
      ) {
        priority = "0.9";
      } else if (url.includes("/blog/")) {
        priority = "0.8";
      }

      return `
  <url>
    <loc>${BASE_URL}${url}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>${priority}</priority>
  </url>`;
    })
    .join("\n");
}

/**
 * MAIN
 */
function generateSitemap() {
  console.log("🗺 Generating sitemap...");

  STATIC_URLS.forEach((u) => urlSet.add(normalizeUrl(u)));

  scanCars();
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
