const fs = require("fs");
const path = require("path");

const BASE_URL = "https://carithm.vercel.app";

const ROOT = process.cwd();
const SITEMAP_PATH = path.join(ROOT, "sitemap_v4.xml");

// IMPORTANT: adjust this path if your cars.json is elsewhere
const CARS_PATH = path.join(ROOT, "cars", "cars.json");

/**
 * Collect all car URLs from JSON (Vercel-safe, no filesystem scanning)
 */
function getCarUrls() {
  if (!fs.existsSync(CARS_PATH)) {
    console.error("❌ cars.json not found at:", CARS_PATH);
    return [];
  }

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

/**
 * Convert URLs → sitemap XML blocks
 */
function buildXml(urls) {
  const today = new Date().toISOString().split("T")[0];

  return urls
    .map((u) => {
      const priority =
        u.includes("/toyota/") ||
        u.includes("/bmw/") ||
        u.includes("/mercedes/")
          ? "0.9"
          : "0.8";

      return `
  <url>
    <loc>${BASE_URL}${u}</loc>
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

  if (!fs.existsSync(SITEMAP_PATH)) {
    console.error("❌ sitemap_v4.xml not found");
    process.exit(1);
  }

  const staticXml = fs.readFileSync(SITEMAP_PATH, "utf-8");

  const carUrls = getCarUrls();
  const dynamicXml = buildXml(carUrls);

  if (carUrls.length === 0) {
    console.warn("⚠️ No car pages found — check cars.json path/data");
  }

  const finalXml = staticXml.replace(
    "</urlset>",
    `${dynamicXml}\n</urlset>`
  );

  fs.writeFileSync(SITEMAP_PATH, finalXml, "utf-8");

  console.log(`✅ Sitemap updated with ${carUrls.length} car pages`);
}

generateSitemap();
