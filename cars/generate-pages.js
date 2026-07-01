const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";
const ROOT_DIR = process.cwd();

// ignore noise folders/files
// NOTE: brand folders (toyota/bmw/mercedes) are handled explicitly by
// scanCars(), so they're excluded here to avoid scanning them twice.
const IGNORE_DIRS = new Set([
  "node_modules",
  ".git",
  ".vercel",
  "toyota",
  "bmw",
  "mercedes",
]);
const IGNORE_FILES = new Set([".DS_Store"]);

// store clean URLs, keyed by url -> lastmod date
const urlMap = new Map();

/**
 * STATIC PAGES (SEO core index)
 */
const STATIC_URLS = ["/", "/blog/", "/predictive/", "/research/", "/about/"];

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
 * Get a lastmod date string (YYYY-MM-DD) from a file's mtime.
 * Falls back to today if the file can't be stat'd.
 */
function getLastMod(filePath) {
  try {
    return fs.statSync(filePath).mtime.toISOString().split("T")[0];
  } catch (e) {
    return new Date().toISOString().split("T")[0];
  }
}

function addUrl(url, filePath) {
  const normalized = normalizeUrl(url);
  urlMap.set(normalized, getLastMod(filePath));
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
      if (!fs.existsSync(modelPath) || !fs.statSync(modelPath).isDirectory()) continue;

      const files = fs.readdirSync(modelPath);
      for (const file of files) {
        if (!file.endsWith(".html")) continue;
        const rawUrl = `/${brand}/${model}/${file}`;
        addUrl(rawUrl, path.join(modelPath, file));
      }
    }
  }
}

/**
 * Scan misc HTML pages safely (skips brand folders, already handled above)
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
      const relative = full.replace(ROOT_DIR, "").replace(/\\/g, "/");
      addUrl(relative, full);
    }
  }
}

/**
 * Build XML entries
 */
function buildXml() {
  const today = new Date().toISOString().split("T")[0];

  return Array.from(urlMap.entries())
    .map(([url, lastmod]) => {
      let priority = "0.6";
      if (url === "/") {
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
    <lastmod>${lastmod || today}</lastmod>
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

  const today = new Date().toISOString().split("T")[0];
  STATIC_URLS.forEach((u) => urlMap.set(normalizeUrl(u), today));

  scanCars();
  scanMisc(ROOT_DIR);

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${buildXml()}
</urlset>`;

  const outputPath = path.join(ROOT_DIR, "sitemap_v4.xml");
  fs.writeFileSync(outputPath, xml, "utf-8");

  console.log(`✅ Sitemap generated with ${urlMap.size} URLs`);
}

generateSitemap();
