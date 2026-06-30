// generate-sitemap.js

const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";

// folders to scan
const ROOT_DIR = path.join(__dirname, "..");

const IGNORE = ["node_modules", ".git", ".vercel", "cars"];

let urls = [];

/**
 * Recursively scan directory for HTML files
 */
function scanDir(dir) {
  const files = fs.readdirSync(dir);

  for (const file of files) {
    const fullPath = path.join(dir, file);

    if (IGNORE.some((i) => fullPath.includes(i))) continue;

    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      scanDir(fullPath);
    } else if (file.endsWith(".html")) {
      const relative = fullPath.replace(ROOT_DIR, "").replace(/\\/g, "/");
      urls.push(relative);
    }
  }
}

/**
 * Convert file path → URL
 */
function toUrl(filePath) {
  return BASE_URL + filePath;
}

/**
 * Build sitemap XML
 */
function buildSitemap(urls) {
  const today = new Date().toISOString().split("T")[0];

  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

${urls
  .map((url) => {
    let priority = "0.6";

    if (url.includes("/toyota/") || url.includes("/bmw/") || url.includes("/mercedes/")) {
      priority = "0.9";
    }

    if (url === "/index.html") {
      priority = "1.0";
    }

    return `
  <url>
    <loc>${toUrl(url)}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>${priority}</priority>
  </url>`;
  })
  .join("\n")}

</urlset>`;
}

/**
 * Run generator
 */
function generateSitemap() {
  console.log("🗺 Generating sitemap...");

  scanDir(ROOT_DIR);

  const sitemap = buildSitemap(urls);

  const outputPath = path.join(ROOT_DIR, "sitemap.xml");

  fs.writeFileSync(outputPath, sitemap);

  console.log(`✅ Sitemap generated with ${urls.length} URLs`);
}

generateSitemap();
