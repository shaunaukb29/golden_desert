// cars/generate-pages.js

const fs = require("fs");
const path = require("path");
const Handlebars = require("handlebars");

// Load data
const cars = require("./cars.json");

// Load template
const templatePath = path.join(__dirname, "template.html");
const templateSource = fs.readFileSync(templatePath, "utf-8");

// Compile template once (important for performance)
const compile = Handlebars.compile(templateSource);

/**
 * Create SEO-friendly slug if not provided
 */
function createSlug(car) {
  const make = car.make.toLowerCase().replace(/\s+/g, "-");
  const model = car.model.toLowerCase().replace(/\s+/g, "-");

  const location = (car.location || "uae").toLowerCase().replace(/\s+/g, "-");
  const type = (car.type || "repair-cost").toLowerCase().replace(/\s+/g, "-");

  return `${type}-${location}`;
}

/**
 * Main generator
 */
function generatePages() {
  console.log("🚀 Starting page generation...\n");

  cars.forEach((car, index) => {
    try {
      // Build HTML from template
      const html = compile(car);

      const slug = car.slug || createSlug(car);

      // Output folder structure:
      // /car/toyota/camry/
      const outputDir = path.join(
        __dirname,
        "..",
        "car",
        car.make.toLowerCase().replace(/\s+/g, "-"),
        car.model.toLowerCase().replace(/\s+/g, "-")
      );

      fs.mkdirSync(outputDir, { recursive: true });

      const outputPath = path.join(outputDir, `${slug}.html`);

      fs.writeFileSync(outputPath, html, "utf-8");

      console.log(`✅ [${index + 1}/${cars.length}] Generated: ${outputPath}`);
    } catch (err) {
      console.error(`❌ Error generating ${car.make} ${car.model}:`, err.message);
    }
  });

  console.log("\n🎉 All pages generated successfully!");
}

generatePages();
