const API_BASE = "http://127.0.0.1:8000";

// ---------- DOM ----------
const quoteTextEl = document.getElementById("quoteText");
const analyzeBtn = document.getElementById("analyzeBtn");

const vehicleSection = document.getElementById("vehicleSection");
const makeSelect = document.getElementById("make");
const modelSelect = document.getElementById("model");
const yearInput = document.getElementById("year");
const mileageInput = document.getElementById("mileage");
const drivetrainSelect = document.getElementById("drivetrain");
const drivingSelect = document.getElementById("driving");

const servicesSection = document.getElementById("servicesSection");
const servicesList = document.getElementById("servicesList");

const historySection = document.getElementById("historySection");
const historyForm = document.getElementById("historyForm");
const generateReportBtn = document.getElementById("generateReportBtn");

const reportSection = document.getElementById("reportSection");
const reportOutput = document.getElementById("reportOutput");

const statusEl = document.getElementById("status");

// ---------- State ----------
let analyzedServices = [];
let historyAnswers = {};
let availableMakes = [];
let availableModels = [];

// ---------- Helpers ----------
function setStatus(msg, isError = false) {
  if (!statusEl) return;
  statusEl.textContent = msg || "";
  statusEl.style.color = isError ? "#b00020" : "#333";
}

function escapeHtml(str) {
  return String(str ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function renderMarkdown(md) {
  if (!md) return "";
  let html = escapeHtml(md);

  // headers
  html = html.replace(/^### (.*)$/gm, "<h3>$1</h3>");
  html = html.replace(/^## (.*)$/gm, "<h2>$1</h2>");
  html = html.replace(/^# (.*)$/gm, "<h1>$1</h1>");

  // bold
  html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

  // bullet points
  html = html.replace(/^- (.*)$/gm, "<li>$1</li>");
  html = html.replace(/(<li>.*<\/li>)/gs, "<ul>$1</ul>");

  // line breaks
  html = html.replace(/\n/g, "<br>");

  return html;
}

function normalizeNumber(value) {
  if (value === null || value === undefined) return null;
  const cleaned = String(value).replace(/,/g, "").trim();
  if (!cleaned) return null;
  const num = Number(cleaned);
  return Number.isFinite(num) ? num : null;
}

function createOption(value, label) {
  const opt = document.createElement("option");
  opt.value = value;
  opt.textContent = label;
  return opt;
}

// ---------- API ----------
async function apiGet(path) {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) {
    const txt = await res.text();
    throw new Error(`GET ${path} failed (${res.status}) ${txt}`);
  }
  return res.json();
}

async function apiPost(path, body) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    const txt = await res.text();
    throw new Error(`POST ${path} failed (${res.status}) ${txt}`);
  }

  return res.json();
}

// ---------- Load make/model data ----------
async function loadMakes() {
  try {
    const data = await apiGet("/makes");
    availableMakes = Array.isArray(data) ? data : (data.makes || []);
    makeSelect.innerHTML = "";
    makeSelect.appendChild(createOption("", "Select make"));

    availableMakes.forEach((make) => {
      makeSelect.appendChild(createOption(make, make));
    });
  } catch (err) {
    console.error(err);
    setStatus(`Failed to load makes: ${err.message}`, true);
  }
}

async function loadModels(make) {
  modelSelect.innerHTML = "";
  modelSelect.appendChild(createOption("", "Select model"));

  if (!make) return;

  try {
    const data = await apiGet(`/models/${encodeURIComponent(make)}`);
    availableModels = Array.isArray(data) ? data : (data.models || []);

    availableModels.forEach((model) => {
      modelSelect.appendChild(createOption(model, model));
    });
  } catch (err) {
    console.error(err);
    setStatus(`Failed to load models: ${err.message}`, true);
  }
}

makeSelect?.addEventListener("change", async () => {
  await loadModels(makeSelect.value);
});

// ---------- Analyze quote ----------
async function analyzeQuote() {
  const quoteText = quoteTextEl?.value?.trim();
  if (!quoteText) {
    setStatus("Please paste the quote text first.", true);
    return;
  }

  setStatus("Analyzing quote...");
  reportSection.style.display = "none";
  historySection.style.display = "none";

  try {
    const data = await apiPost("/analyze-quote-text", {
      quote_text: quoteText,
    });

    analyzedServices = data.services || [];
    historyAnswers = {};

    renderServices(analyzedServices);
    renderHistoryQuestions(analyzedServices);

    servicesSection.style.display = "block";
    vehicleSection.style.display = "block";
    historySection.style.display = "block";

    setStatus("Quote analyzed.");
  } catch (err) {
    console.error(err);
    setStatus(err.message, true);
  }
}

// ---------- Render analyzed services ----------
function renderServices(services) {
  if (!servicesList) return;
  servicesList.innerHTML = "";

  if (!services?.length) {
    servicesList.innerHTML = "<p>No services found.</p>";
    return;
  }

  services.forEach((svc, idx) => {
    const row = document.createElement("div");
    row.className = "service-row";

    const display = svc.display || svc.raw || `Service ${idx + 1}`;
    const price = svc.price ?? 0;
    const matched = svc.part_key && svc.part_key !== "UNMATCHED";

    row.innerHTML = `
      <div><strong>${escapeHtml(display)}</strong></div>
      <div>Part key: ${escapeHtml(svc.part_key || "UNMATCHED")}</div>
      <div>Price: AED ${escapeHtml(price)}</div>
      <div>${matched ? "Matched" : "Unmatched"}</div>
    `;

    servicesList.appendChild(row);
  });
}

// ---------- Render history questions ----------
function renderHistoryQuestions(services) {
  if (!historyForm) return;
  historyForm.innerHTML = "";

  const historyServices = services.filter(
    (svc) => Array.isArray(svc.history_options) && svc.history_options.length > 0
  );

  if (!historyServices.length) {
    historyForm.innerHTML = "<p>No history questions needed for this quote.</p>";
    return;
  }

  historyServices.forEach((svc, idx) => {
    const wrapper = document.createElement("div");
    wrapper.className = "history-question";

    const label = document.createElement("label");
    label.textContent = `When was "${svc.display || svc.raw}" last done?`;

    const select = document.createElement("select");
    select.dataset.partKey = svc.part_key;
    select.dataset.index = String(idx);

    select.appendChild(createOption("", "Select one"));

    svc.history_options.forEach((opt) => {
      // supports either ["Label", "value"] or {label, value}
      let optionLabel = "";
      let optionValue = "";

      if (Array.isArray(opt)) {
        optionLabel = opt[0];
        optionValue = opt[1];
      } else if (opt && typeof opt === "object") {
        optionLabel = opt.label;
        optionValue = opt.value;
      }

      select.appendChild(createOption(optionValue, optionLabel));
    });

    select.addEventListener("change", () => {
      if (svc.part_key) {
        historyAnswers[svc.part_key] = select.value;
      }
    });

    wrapper.appendChild(label);
    wrapper.appendChild(select);
    historyForm.appendChild(wrapper);
  });
}

// ---------- Validate vehicle inputs ----------
function collectVehicleData() {
  const make = makeSelect?.value?.trim();
  const model = modelSelect?.value?.trim();
  const year = yearInput?.value?.trim();
  const mileage = normalizeNumber(mileageInput?.value);
  const drivetrain = drivetrainSelect?.value?.trim();
  const driving = drivingSelect?.value?.trim();

  const missing = [];
  if (!make) missing.push("make");
  if (!model) missing.push("model");
  if (!year) missing.push("year");
  if (mileage === null) missing.push("mileage");
  if (!drivetrain) missing.push("drivetrain");
  if (!driving) missing.push("driving");

  if (missing.length) {
    throw new Error(`Missing required fields: ${missing.join(", ")}`);
  }

  return {
    make,
    model,
    year,
    mileage,
    drivetrain,
    driving,
  };
}

// ---------- Generate report ----------
async function submitHistoryAndGenerateReport() {
  try {
    setStatus("Preparing report...");

    const vehicle = collectVehicleData();

    // Ensure all history-answer services have an answer if you want strict validation.
    // If not, you can remove this block.
    const servicesRequiringHistory = analyzedServices.filter(
      (svc) => Array.isArray(svc.history_options) && svc.history_options.length > 0
    );

    for (const svc of servicesRequiringHistory) {
      if (!historyAnswers[svc.part_key]) {
        throw new Error(`Please answer the history question for "${svc.display || svc.raw}".`);
      }
    }

    const payload = {
      services: analyzedServices,
      history_answers: historyAnswers,

      // IMPORTANT: these names must match backend schema exactly
      make: vehicle.make,
      model: vehicle.model,
      year: vehicle.year,
      mileage: vehicle.mileage,
      driving: vehicle.driving,
      drivetrain: vehicle.drivetrain,
      consent_to_log: false
    };

    console.log("POST /generate-report payload:", payload);

    const result = await apiPost("/generate-report", payload);

    reportOutput.innerHTML = renderMarkdown(result.report || "No report returned.");
    reportSection.style.display = "block";
    setStatus("Report generated.");
  } catch (err) {
    console.error(err);
    setStatus(err.message, true);
  }
}

// ---------- Events ----------
analyzeBtn?.addEventListener("click", analyzeQuote);
generateReportBtn?.addEventListener("click", submitHistoryAndGenerateReport);

// ---------- Init ----------
loadMakes();
