# Aurelianware, Inc.

Company website for [aurelianware.com](https://aurelianware.com).

This is the parent: identity, product index, trust, and contact. Product evaluation lives on the product sites.

| Path | Purpose |
| --- | --- |
| `/` | Home |
| `/products/` | Cloud Health Office and Cloud Dental Office |
| `/services/` | Payer consulting: CMS-0057-F API validation, integration, cloud migration |
| `/services/cms-0057-f-api-validation/` | Inferno-based CMS-0057-F API validation offer |
| `/company/` | Legal entity and licensing |
| `/trust/` | No borrowed badges. HIPAA and security contacts. |
| `/privacy/` | Marketing-site privacy notes |
| `/contact/` | Mailto. Nothing stored here. |

## Voice

Precise. Founder-written. Austere. Short sentences. No invented metrics, customers, or certifications.

## Deploy

`sitemap.xml` and each page's footer "Last updated" date are generated. On every push to `main` that touches HTML, `.github/workflows/site-meta.yml` runs `.github/scripts/update_site_meta.py` and commits the result. Don't edit the sitemap by hand. A new page is picked up automatically when it has a self-referencing canonical link and no `noindex`.

GitHub Pages from `main`. Custom domain: `aurelianware.com` (`CNAME`).

Clean URLs use directory `index.html` files so GitHub Pages serves `/products/` without a rewrite layer.

## Products

- [cloudhealthoffice.com](https://cloudhealthoffice.com) — BSL 1.1
- [clouddental.io](https://clouddental.io) — Apache 2.0
