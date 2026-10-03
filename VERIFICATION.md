# Verification — October 3, 2026

The redesign was served locally at `http://127.0.0.1:4173/` using Python's static HTTP server. Browser checks used Playwright with Chromium. These initial checks concern the local implementation; production checks from the follow-up are recorded below.

## Functional and responsive checks

- Widths checked: **320, 375, 390, 680, 768, 1024, and 1440 pixels**. No horizontal overflow or offscreen content.
- Visually reviewed desktop, tablet, mobile, project cards, expanded FinSight screenshot/details, experience, about/education, and contact.
- Section anchor targets, native project disclosures, mobile menu open/close, Escape behavior, and focus restoration verified.
- The keyboard skip link moves focus to main content. The Experience navigation link activates correctly and leaves its heading visible below the sticky header.
- Mobile section selection closes the menu and transfers focus to the destination. Hash navigation still works after a reload.
- Resume download returned `Andrew_Chen_Resume.pdf`; the PDF endpoint returned HTTP 200 and `application/pdf`.
- The published resume asset is byte-for-byte identical to the updated PDF supplied by the user. Its single page was rendered and visually inspected.
- The real FinSight screenshot returned HTTP 200, decoded successfully, and displayed correctly inside its disclosure.
- No JavaScript console errors, uncaught page errors, or failed local asset requests.
- Navigation and project disclosures remain usable with JavaScript disabled.
- `prefers-reduced-motion: reduce` disables smooth scrolling and transitions.

## Accessibility

Axe-core 4.10.3 checked WCAG 2 A/AA, WCAG 2.1 A/AA, and best-practice rules:

- Mobile: **0 violations**, 41 passing checks.
- Desktop with project details expanded: **0 violations**, 42 passing checks.

The contrast issues found in the first run were corrected before the final pass. Manual checks covered heading structure, descriptive links, visible focus, native keyboard disclosures, mobile menu focus handling, image alternatives, and reduced motion. Automated checks do not replace a full assistive-technology audit.

## Links and deployment

- GitHub profile and all six linked project repositories: **HTTP 200**.
- Email and LinkedIn match the original site and updated resume. LinkedIn returned its automated-access-blocking HTTP 999, so live profile contents could not be verified automatically.
- Static check: **26 links and 7 linked assets**, no broken local paths, duplicate IDs, or missing anchor targets. Metadata, resume PDF signature, sitemap XML, and `.nojekyll` also passed.
- `node --check script.js` and `git diff --check` passed.
- No build, package installation, backend, or client-side routing is required. Relative assets and fragment navigation work on GitHub Pages at the account-domain root.
- GitHub reports Pages enabled for the existing repository. Its private Pages source configuration was unavailable through the unauthenticated API; the expected `main` / root deployment settings are documented in `README.md`.

## Performance footprint

- HTML: approximately **26 KB** uncompressed.
- CSS: approximately **37 KB** uncompressed.
- JavaScript: approximately **2.7 KB** uncompressed, loaded with `defer`.
- One optimized **90 KB WebP** content image, with explicit dimensions and lazy loading.
- A fresh initial page load requested only local CSS, JavaScript, and the favicon; the disclosure screenshot stayed deferred.
- System fonts, no runtime libraries, no third-party scripts, and no generated app bundle.
- The share-card PNG is metadata only and is not loaded as visible page content.

## JD.com follow-up

Added the official JD.com/Jingdong corporate-blog logo and a concise company-context sentence, and changed the website internship dates to July–October 2026. Checked the updated card at 1440, 768, 390, and 320 pixels: no horizontal overflow, missing image, JavaScript errors, or scoped axe accessibility violations. Visually reviewed the desktop and mobile card. The resume PDF was not changed during this follow-up (SHA-256: `b39d5619f75a0ea6f720f1bd534f8567a7fd5dc7eb03eb5170ad415cd045fbef`).

## Public-site cache follow-up

The public HTML, stylesheet, and JavaScript matched the local files, and the Pages deployment succeeded. The public site rendered correctly in a fresh browser. The files had been published through separate commits, and Pages returned `Cache-Control: max-age=600`; these findings point to a stale/mixed asset cache as the likely cause of the reported broken view.

CSS and JavaScript references now include SHA-256-derived versions, bypassing the legacy unversioned cache entries. `scripts/version_assets.py` refreshes those versions, and `scripts/check_site.py` fails if either is stale. Deployment instructions now require related files to be published together. The resume PDF remains unchanged.
