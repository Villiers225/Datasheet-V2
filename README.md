# Armies & Technology — Data Sheet (Static Site)

A static HTML/CSS site designed to mirror the 4-box PDF structure with verbatim narrative on the left and data exhibits on the right.

## Use on GitHub Pages

1. Create a new GitHub repository (public or private with Pages enabled).
2. Upload the contents of `defence_datasheet_site/` to the repo root:
   - `index.html`
   - `assets/style.css`
   - `assets/app.js`
3. In **Settings → Pages**, choose "Deploy from a branch" and set the branch to `main` (or `master`) and the root to `/ (root)`.
4. Wait for Pages to deploy; the site will be available at `https://<user>.github.io/<repo>/`.

## Editing the narrative

- Open `index.html` and, inside each box, replace the placeholder list under **"Verbatim points from the PDF"** with the exact text from `4_box_house_style.pdf` (copy/paste verbatim).
- Do not change the **Evidence & Exhibits** unless you are updating data or links.

## Adding links

- In the **Evidence Index & References**, replace placeholder entries (`[Moneyball]`, `[IISS]`, etc.) with live URLs.

## Print / PDF export

- Use your browser’s **Print → Save as PDF**. The stylesheet includes print-friendly rules.
