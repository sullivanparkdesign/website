# Sullivan Park Design website

The website for [sullivanparkdesign.com](https://www.sullivanparkdesign.com): website design, branding and SEO in Vancouver, BC.

It's a plain static site (HTML, CSS and a small script), hosted on Cloudflare Pages. There's no WordPress, no database and nothing to update or patch.

## What's in this repo

| Folder | What it is |
| --- | --- |
| `site/` | **The live website.** Cloudflare Pages publishes this folder exactly as it is. |
| `design-source/` | The page designs exported from the Claude Design canvas (`*.dc.html`). |
| `build/` | The script that turns the designs into the website, plus the original images (`build/blobs/`) and the checks. |
| `templates-src/` | The three actor website demos (Editorial, Luminous, Feature). The build copies them to `/templates/`, kept out of search, and leaves out each demo's `HANDOFF.md`, which is also kept out of this repo. |

## Publishing on Cloudflare Pages

1. In Cloudflare, go to **Workers & Pages → Create → Pages → Connect to Git** and pick this repository.
2. Use these settings:
   - **Production branch:** `main`
   - **Framework preset:** None
   - **Build command:** leave empty
   - **Build output directory:** `site`
3. Save and deploy. Every push to `main` updates the site within a minute or so.

The `*.pages.dev` preview address is set to `noindex` (in `site/_headers`), so Google only indexes the real domain.

### Connecting the domain (at launch)

In the Pages project, open **Custom domains** and add `www.sullivanparkdesign.com` and `sullivanparkdesign.com`. Cloudflare shows the exact DNS records to add. Wait until launch day to switch the DNS away from Squarespace.

## Updating the site

Most changes happen on the Claude Design canvas first. Then:

1. Copy the updated `*.dc.html` files into `design-source/`.
2. Rebuild and check:

   ```sh
   cd build && npm install && cd ..   # first time only
   node build/build.mjs               # rebuilds site/
   node build/check.mjs               # layout, links and images at 5 screen widths
   node build/behave.mjs              # menu, dropdowns, FAQs, form and video
   ```

3. Commit and push. Cloudflare publishes `site/` automatically.

New canvas images need adding to `build/blobs/` (named by their canvas id) before rebuilding.

## Settings (`build/config.json`)

- `formEndpoint`: where the contact form sends messages (for example a Formspree form URL). While it's empty, the form checks the fields and then opens the visitor's email app with their message filled in, addressed to info@sullivanparkdesign.com.
- `imageNames`: friendly file names for images. Everything else is named from its alt text.

## Good to know

- **Placeholders are hidden.** Review and before/after sections that are still waiting on content stay on the canvas but are removed from the live site automatically.
- **Old addresses redirect.** `site/_redirects` sends old Squarespace paths (`/blog`, `/journal`, `/web-design` and so on) to the matching new pages.
- **Search basics are built in.** Each page gets its own title, description, canonical address, social preview image and structured data, and `sitemap.xml` and `robots.txt` are generated on every build.
