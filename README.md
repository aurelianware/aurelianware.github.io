# Aurelianware, Inc.

Company website for [aurelianware.com](https://aurelianware.com).

Aurelianware, Inc. is a pre-seed, single-product software company. This site says what it sells (Cloud Health Office, by subscription), who runs it, and how to reach it. Product evaluation lives on cloudhealthoffice.com.

| Path | Purpose |
| --- | --- |
| `/` | Home: product, proof, business model, team and stage |
| `/products/` | Cloud Health Office capabilities and evidence links |
| `/services/` | Retired. `noindex` redirect to `/company/#business-model` |
| `/services/cms-0057-f-api-validation/` | Retired. `noindex` redirect to cloudhealthoffice.com/docs/compliance |
| `/company/` | Business model, licensing, team and stage |
| `/trust/` | No borrowed badges. HIPAA and security contacts. |
| `/privacy/` | Marketing-site privacy notes |
| `/contact/` | Mailto. Nothing stored here. |

## Voice

Precise. Founder-written. Austere. Short sentences. No invented metrics, customers, or certifications. No dollar pricing.

This is a product company site. Do not add consulting-for-hire content (rates, staffing, fractional roles, custom development). Implementation and onboarding are described only as services that support a Cloud Health Office subscription. Every page footer says "Cloud Health Office is a product of Aurelianware, Inc."

## Deploy

`sitemap.xml` and each page's footer "Last updated" date are generated. On every push to `main` that touches HTML, `.github/workflows/site-meta.yml` runs `.github/scripts/update_site_meta.py` and commits the result. Don't edit the sitemap by hand. A new page is picked up automatically when it has a self-referencing canonical link and no `noindex`.

GitHub Pages from `main`. Custom domain: `aurelianware.com` (`CNAME`).

Clean URLs use directory `index.html` files so GitHub Pages serves `/products/` without a rewrite layer.

## Products

- [cloudhealthoffice.com](https://cloudhealthoffice.com) — BSL 1.1
- [clouddental.io](https://clouddental.io) — Apache 2.0
