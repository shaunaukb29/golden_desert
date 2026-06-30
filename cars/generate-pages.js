const fs = require("fs");
const path = require("path");
const Handlebars = require("handlebars");

const cars = require("./cars.json");
const template = fs.readFileSync("./template.html", "utf-8");

const compiled = Handlebars.compile(template);

cars.forEach(car => {
  const html = compiled(car);

  const outputDir = path.join(
    __dirname,
    "..",
    "car",
    car.make.toLowerCase(),
    car.model.toLowerCase()
  );

  fs.mkdirSync(outputDir, { recursive: true });

  const fileName = car.slug + ".html";

  fs.writeFileSync(
    path.join(outputDir, fileName),
    html
  );

  console.log("Generated:", car.make, car.model);
});
