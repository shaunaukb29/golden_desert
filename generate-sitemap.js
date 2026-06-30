const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";
const OUTPUT_FILE = path.join(__dirname, "sitemap_v4.xml");

function walkDir(dir, urlPath = "") {
  let urls = [];

  const files = fs.readdirSync(dir);

  files.forEach(file => {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      urls = urls.concat(walkDir(fullPath, urlPath + "/" + file));
    } else if (file.endsWith(".html")) {
      urls.push(urlPath + "/" + file);
    }
  });

  return urls;
}

const pages = walkDir(path.join(__dirname, "car"));

const xml =
`<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages.map(p => `
  <url>
    <loc>${BASE_URL}${p}</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
`).join("")}
</urlset>`;

fs.writeFileSync(OUTPUT_FILE, xml);

console.log("✅ Sitemap generated:", OUTPUT_FILE);
