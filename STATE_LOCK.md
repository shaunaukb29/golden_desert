# REPOSITORY GOLDEN STATE LOCK & ACTIVE RECOVERY SPECIFICATION

- **Locked Git Commit**: `7ac7934f4` (Tagged locally as `locked-nov-4-golden-state`)
- **Base Baseline Reference**: Commit `1b110c288` (Monday Nov 2 22:02 / Peak Nov 4 112+ AED Performance)
- **Status**: LOCKED AND FROZEN. Under NO circumstances touch the ad code, Auto Ads script, or core DOM structure of the money pages without explicit directive.

---

## 1. Locked Code & Ad Architecture (Do NOT Modify)

1. **Money Hubs (`index.html` & `audio/.../app.html`)**:
   - Clean, unmodified Auto Ads script in `<head>`:
     `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5227538935323998" crossorigin="anonymous"></script>`
   - NO manual `<ins class="adsbygoogle">` ad blocks beneath the Streamlit embed.
   - NO `google-anno-skip` tags.
   - Zero font reflow shifts (`display=optional`).
   - Clean Streamlit embed wrapper (`.streamlit-embed-wrap`).

2. **Robots.txt Crawler Boundary**:
   - `User-agent: Mediapartners-Google` strictly ALLOWED only on:
     - `/$`
     - `/audio$`, `/audio/$`
     - `/app$`, `/app/$`
     - `/vision$`, `/vision/$`
     - `/cost-calculator$`, `/cost-calculator/$`
   - `Mediapartners-Google` DISALLOWED on `/audio/*`, `/bmw/*`, `/toyota/*`, `/mercedes/*`, etc.
   - `User-agent: *` completely open (`Allow: /`) so Googlebot indexes all 12,700+ subpages.

3. **Subpages (12,700+ programmatic vehicle pages)**:
   - 0 AdSense tags (Zero impression dilution / Zero Smart Pricing penalties).
   - "Blueprint: Page -> Record" funnel active with high-contrast direct links to `/audio`.
