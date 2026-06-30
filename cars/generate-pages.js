const fs = require("fs");
const path = require("path");

const cars = require("./cars.json");

// read template
const template = fs.readFileSync("template.html", "utf8");

// output folder
const outputDir = path.join(__dirname, "output");

if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}

function replaceTemplate(data) {
  return template
    .replace(/{{MAKE}}/g, data.make)
    .replace(/{{MODEL}}/g, data.model)
    .replace(/{{CITY}}/g, data.city)
    .replace(/{{COUNTRY}}/g, data.country);
}

cars.forEach((car) => {
  const html = replaceTemplate(car);

  const filePath = path.join(outputDir, car.slug + ".html");

  fs.writeFileSync(filePath, html);

  console.log("Generated:", filePath);
});

console.log("DONE: All pages generated.");
