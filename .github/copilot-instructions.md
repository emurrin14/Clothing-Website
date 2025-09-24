# Copilot Instructions for Clothing Website

## Project Overview
This is a static website for a clothing brand, organized as follows:
- `index/`: Contains main HTML pages and the shared CSS stylesheet.
- `Pictures/`: Contains all image assets used throughout the site.

## Key Files & Structure
- `index/Index.html`: Main landing page.
- `index/sppantspage.html`: Product or category page for "SP Pants".
- `index/websitestylesheet.css`: Global stylesheet for all pages.
- `Pictures/`: All referenced images (e.g., `risk.jpg`, `sp.jpg`, `title.jpg`).

## Development Patterns
- All HTML files reference the shared CSS in `index/websitestylesheet.css`.
- Images are referenced with relative paths from HTML (e.g., `../Pictures/sp.jpg`).
- No build system, frameworks, or package managers are present; this is a pure HTML/CSS/JS (if added) project.
- Add new pages to the `index/` directory and update navigation links in all relevant HTML files.

## Conventions
- Keep all CSS in `websitestylesheet.css` unless a strong reason exists to inline or add per-page styles.
- Use semantic HTML5 elements where possible.
- Image filenames are descriptive and match their use in the UI.
- Maintain consistent navigation and layout across all pages.

## Developer Workflow
- Edit HTML/CSS directly; no build or test commands are required.
- Preview changes by opening HTML files in a browser.
- Add new images to `Pictures/` and reference them with correct relative paths.

## Examples
- To add a new product page:
  1. Create `index/newproduct.html`.
  2. Add a link to it in `Index.html` and other relevant pages.
  3. Add product images to `Pictures/` and reference them in the new HTML file.

## Integration Points
- No external dependencies or APIs are currently integrated.
- If adding JavaScript, place scripts in `index/` and link them from HTML files.

---
For questions about structure or conventions, review `Index.html` and `websitestylesheet.css` for examples.
