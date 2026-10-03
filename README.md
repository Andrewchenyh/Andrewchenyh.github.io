# Andrew Chen — AI & Software Engineering

A lightweight, single-page portfolio for 2027 new-grad AI/ML, applied AI, and software engineering opportunities.

**Production URL:** https://andrewchenyh.github.io/

## Run locally

From the repository root:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173/. Stop the server with Ctrl+C. There is no install or build step.

Optional local checks:

```sh
python3 scripts/check_site.py
node --check script.js
```

The Python check uses only the standard library. Node is optional and only needed for the JavaScript syntax check; neither runtime is needed in production.

## Deploy to GitHub Pages

This is the account site repository, `Andrewchenyh/Andrewchenyh.github.io`, so it serves at the domain root. The existing repository has GitHub Pages enabled. No custom domain, client-side router, build system, or backend is required.

1. Commit the site changes and push them to `main`.
2. In GitHub **Settings → Pages → Build and deployment**, use **Deploy from a branch**, **main**, **/ (root)**. The remote Pages source settings require authenticated access, so they could not be inspected during the redesign; confirm these settings if deployment does not run automatically.
3. Wait for GitHub's Pages deployment to finish. Open the production URL and hard-refresh.
4. Verify both `/#work` and `files/Andrew_Chen_Resume.pdf` on the deployed site.

`.nojekyll` tells Pages to publish static files directly. All local assets use relative paths, and navigation uses real fragment links, so refreshes do not need a routing fallback. No new Actions workflow was introduced; GitHub manages the branch-based Pages deployment. The redesign has not been pushed or deployed by the agent.

## Files and editing

| File | Purpose |
| --- | --- |
| `index.html` | Copy, semantic sections, project disclosures, architecture diagrams, SEO/social metadata |
| `style.css` | Responsive visual system, focus styles, reduced-motion behavior |
| `script.js` | Mobile navigation, focus management, active-section indication |
| `files/Andrew_Chen_Resume.pdf` | Resume served by all view/download links |
| `assets/jd-logo.png` | Official Jingdong wordmark from JD.com’s corporate blog |
| `assets/finsight-chat.webp` | Real FinSight screenshot, optimized from its public repository |
| `assets/favicon.svg` | Editable monogram; PNG fallback and Apple touch icon sit alongside it |
| `assets/social-card.svg` | Editable share-card source; `social-card.png` is the 1200×630 image used by metadata |
| `robots.txt`, `sitemap.xml`, `.nojekyll` | Crawling and static GitHub Pages support |
| `scripts/check_site.py` | Dependency-free local link/asset/content structure checks |

To update the resume, replace `files/Andrew_Chen_Resume.pdf` with the new PDF using the same filename. All three resume links will use it. The PDF currently in this repository is a byte-for-byte copy of the updated resume supplied on October 3, 2026 (PDF creation date: October 1, 2026).

Edit SVG artwork directly. If the social card or favicon changes, export its PNG derivatives at the sizes used above. No graphics tooling is needed to serve the existing files.

The legacy stock imagery and all old styling were removed. The new diagrams are HTML/CSS, and the images are the real FinSight screenshot and JD.com’s official logo. System fonts avoid external font requests. There are no frontend dependencies, analytics, cookies, or third-party runtime scripts.

## Content decisions and sources

- The supplied updated resume is authoritative for dates and titles, as confirmed by Andrew: AI Research Fellow **Mar–Jul 2026**; Research Assistant **Sep 2025–Jun 2026**; **Student Analyst**, Technology Transfer Office; **Business Analyst Intern**, PAGO, **Jul–Sep 2025**. Graduation is **June 2027**.
- Copilot's **100%** and **5.0/5** results are explicitly limited to its **10-query golden benchmark**. Deterministic correctness checks and LLM judging are described separately.
- FinSight's **0.71 → 0.87 Fact Recall@5** and **40% → 70% Full Coverage@5** compare dense retrieval with hybrid retrieval plus reranking on the **10-question Microsoft 2023 filing benchmark**. The updated resume and public README agree on these results. No cross-company generalization is claimed.
- The FinSight evaluation notes reflect the newer source-grounded benchmark, rather than presenting the older heuristic evaluation as current. Its screenshot comes from `Andrewchenyh/finsight/assets/screenshots/chat_answer.png` and is labeled as a screenshot, not a live demo.
- The JD.com internship ends **October 2026**, per Andrew’s later instruction; the resume PDF was intentionally not changed. The company context is supported by [JD.com’s official company profile](https://ir.jd.com/about-JD). The authentic logo is the [official corporate-blog wordmark](https://jdcorporateblog.com/wp-content/uploads/2024/01/42741705567864_.png), saved locally without modification.
- JD.com copy describes public/resume-safe responsibilities and approximate aggregate metrics. The website body omits internal operational volumes, account-level information, incident details, experiment specifics, and proprietary formulas. The user-supplied resume PDF is preserved unchanged.
- The archival research optimization is phrased as downloads reduced **to 34.6%**, not **by 34.6%**, based on the original brief. PAGO results use “contributed to” and “approximately.”
- The existing email and LinkedIn URL were preserved and match the updated resume. All project repository URLs were verified publicly. Neither flagship repository advertises a live hosted demo, so no demo link was invented.
- No new resume, employment claims, awards, project screenshots, or metrics were fabricated. No additional user-supplied assets are required.

## Verification

See `VERIFICATION.md` for the final browser, accessibility, responsive, and link checks. To review future edits, run the static check above, then check the rendered site on desktop and mobile, use keyboard navigation, open both project disclosures, and test both resume viewing and downloading.
