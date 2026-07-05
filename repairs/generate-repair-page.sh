#!/bin/bash

CAR="$1"
FILE="$2"
BRAND="$3"

TITLE="${BRAND} Repair Quote Analysis (UAE) | Carithm Knowledge Base"
URL="https://carithm.vercel.app/repairs/${FILE}"
H1="${BRAND} Repair Quote Breakdown (UAE)"

cat > repairs/$FILE <<EOL
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

  <title>${TITLE}</title>

  <meta name="description" content="${BRAND} repair quote breakdown in UAE — how to read service invoices, estimate costs, and avoid overcharging.">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="canonical" href="${URL}">

  <meta property="og:title" content="${TITLE}">
  <meta property="og:description" content="${BRAND} repair cost breakdown UAE — dealer vs independent garage pricing insights.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="${URL}">

  <h1>${H1}</h1>

  <p>
    This guide explains how ${BRAND} repair quotes typically work in UAE workshops, including labor breakdowns, parts pricing, and common upselling patterns.
  </p>

  <h2>What is included in a typical ${BRAND} repair quote?</h2>
  <ul>
    <li>Labor charges (diagnostics + repair time)</li>
    <li>OEM or aftermarket parts</li>
    <li>Fluids and consumables</li>
    <li>Workshop service fees</li>
  </ul>

  <h2>How to avoid overpaying</h2>
  <p>Always compare dealer pricing with independent garages and verify whether parts are OEM or aftermarket.</p>

  <footer>
    <p>© 2026 Carithm — ${BRAND} repair guide UAE</p>
  </footer>

</body>
</html>
EOL

echo "Created: repairs/$FILE"
