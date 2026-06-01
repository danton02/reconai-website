# ReconAI Website — Claude Code Reference

## Project Overview

This is the marketing website for **ReconAI**, a reconditioning cost estimator for automotive dealerships. It is a product of **Dealer Ops Consulting**.

ReconAI connects to a dealership's DMS (dealer management system), imports completed repair orders, and uses that data to give buyers a data-backed reconditioning cost estimate at the point of acquisition — before a vehicle is purchased.

The website is designed to attract dealer principals, used car managers, and dealer group executives to request a demo.

---

## File Structure

The entire site is a **single self-contained HTML file**:

ReconAI\_Production\_Site.html   ← The entire website. All CSS, JS, and content is inline.

There is no build process, no npm, no framework. Edit the HTML file directly. To deploy, drag the updated HTML file to Netlify (see Deployment section).

**Important:** The Socket mascot image is embedded as a base64 string inside the HTML. It is long (\~50KB of characters). Never delete or truncate it. When editing near it, search for `data:image/jpeg;base64,` and leave that entire string untouched.

---

## Pages

The site uses a JavaScript page-switching system — there is no server routing. All seven pages live in the single HTML file as `<div id="page-X">` blocks. JavaScript shows/hides them.

| Page ID | Nav Label | `div` ID |
| :---- | :---- | :---- |
| home | Home | `page-home` |
| hiw | How It Works | `page-hiw` |
| features | Features | `page-features` |
| integrations | Integrations | `page-integrations` |
| pricing | Pricing | `page-pricing` |
| about | About | `page-about` |
| contact | Contact / Request a Demo | `page-contact` |

**To navigate between pages in JavaScript:** `showPage('pricing')` — always use the page IDs from the table above.

**To add a new page:**

1. Add a `<div id="page-newpage" class="page">` block with the content inside  
2. Add a nav link: `<a onclick="showPage('newpage')" id="nav-newpage">Label</a>`  
3. Add a mobile nav link in the `<div id="mobileMenu">` panel  
4. Add a footer link if appropriate

---

## Design System

### Colors (CSS Variables)

All colors are defined as CSS variables in `:root` at the top of the `<style>` block. **Always use variables, never hardcode hex values in new CSS.**

\--blue:       \#1B4FD8   /\* Primary brand blue — buttons, links, accents \*/

\--blue-dark:  \#0F2F8C   /\* Darker blue — hover states, button text \*/

\--blue-light: \#EEF3FF   /\* Very light blue — badges, callout backgrounds \*/

\--blue-mid:   \#2563EB   /\* Mid blue — used in gradients \*/

\--navy:       \#0A1628   /\* Deep navy — hero backgrounds, footer, dark sections \*/

\--text:       \#0F172A   /\* Near-black — all body text \*/

\--muted:      \#64748B   /\* Gray — captions, labels, secondary text \*/

\--light:      \#F8FAFC   /\* Off-white — alternating section backgrounds \*/

\--border:     \#E2E8F0   /\* Light gray — all borders and dividers \*/

\--white:      \#ffffff

\--green:      \#16A34A   /\* Success, positive indicators, low cost \*/

\--amber:      \#D97706   /\* Warning, high cost indicators \*/

**To change the brand blue across the entire site:** update `--blue: #1B4FD8` in `:root` and it propagates everywhere automatically.

### Typography

Loaded from Google Fonts (requires internet connection to render correctly):

- **Headings:** `Outfit` — weights 700, 800, 900  
- **Body:** `Plus Jakarta Sans` — weights 400, 500, 600

/\* Heading example \*/

font-family: 'Outfit', sans-serif;

font-weight: 800;

/\* Body example \*/

font-family: 'Plus Jakarta Sans', sans-serif;

font-weight: 400;

### Spacing

Sections use consistent padding. Do not change these values unless redesigning a full section:

- Hero and CTA band sections: `padding: 7rem 2rem` (desktop), `4rem 1.25rem` (mobile)  
- Standard content sections: `padding: 5rem 2rem` (class `.section`)  
- Max content width: `max-width: 1180px` with `margin: 0 auto` on `.section-inner`

### Common Utility Classes

.section          — Standard white content section with 5rem top/bottom padding

.section-alt      — Same as .section but with \--light (\#F8FAFC) background

.section-inner    — Max-width 1180px centered container

.section-label    — Small uppercase blue label shown above section headings

.section-title    — H2 heading style

.section-sub      — Large muted subtitle paragraph

.text-center      — text-align: center

.btn-primary      — White filled button (used on dark backgrounds)

.btn-outline      — Transparent outlined button (used on dark backgrounds)

---

## Key Sections & How to Edit Them

### Hero (Homepage)

Located in `<div id="page-home">`, first section with class `.hero`.

- Background is a CSS gradient on the `.hero` element: `background: linear-gradient(135deg, var(--navy) 0%, #1B2E5E 60%, #1B4FD8 100%)`  
- The demo card (`.demo-card`) on the right side shows a sample VIN result with the Socket mascot  
- The Socket mascot in the demo card is the embedded base64 image — do not modify it

To change the hero headline, find:

\<h1\>Know Your Recon Cost \<span\>Before You Buy\</span\> the Car.\</h1\>

The `<span>` text renders in `#93C5FD` (light blue). Any text inside `<span>` in the H1 will get that color automatically via `color: #93C5FD` on `.hero h1 span`.

### Stats Band

The three-stat blue band below the hero. Edit the numbers and labels directly:

\<div class="stat-num"\>5,000+\</div\>

\<div class="stat-lbl"\>Repair Records Analyzed Per Dealer\</div\>

Replace with real statistics as they become available.

### Navigation Bar

The nav has two versions: desktop (`.nav-links`) and mobile (inside `#mobileMenu .mobile-panel`). **When adding or renaming a nav item, update both.** The desktop nav items use `id="nav-X"` attributes that match page IDs for the active state highlighting.

### Contact Form

Form fields have these IDs: `firstName`, `lastName`, `dealership`, `role`, `email`, `phone`, `dms`, `locations`, `message`, `submitBtn`.

The submit button calls `handleFormSubmit()` in JavaScript.

**To activate real email delivery**, find this line in the `<script>` block and replace `YOUR_FORM_ID` with the actual Formspree endpoint:

var FORMSPREE\_URL \= 'https://formspree.io/f/YOUR\_FORM\_ID';

Until this is set, the form simulates a successful submission (for demo purposes) but does not actually send email.

**To add a new field to the contact form:**

1. Add the HTML input/select inside `.contact-form` in `page-contact`  
2. Give it an `id` attribute  
3. If it should be required, add its ID to the `required` array in `handleFormSubmit()`  
4. Add it to the `data` object in `handleFormSubmit()` so it gets included in the Formspree submission

### Pricing Cards

Located in `page-pricing`. Two cards with class `.pricing-card`. The featured/premium card also has class `featured` which adds the blue border.

Current state: pricing shows "Contact for Pricing" buttons. When pricing is set, replace the `.pricing-name` line or add a price display above `.pricing-desc`. Example structure to add:

\<div class="pricing-price" style="font-family:'Outfit',sans-serif;font-size:2.5rem;font-weight:900;color:var(--navy);margin-bottom:0.25rem"\>

  $299\<span style="font-size:1rem;font-weight:400;color:var(--muted)"\>/mo per location\</span\>

\</div\>

### DMS Integration Cards

Located in `page-integrations`. Each platform is a `.dms-card` div. To add a new DMS platform, copy an existing `.dms-card` block and update the platform name, description, and the `.dms-logo-box` abbreviation text.

### Testimonial Band

Located near the bottom of `page-home`. Placeholder text currently reads "Used Car Manager, ReconAI Beta Dealer." Replace with real customer name and dealership when available:

\<div class="testimonial-quote"\>"\[REAL QUOTE HERE\]"\</div\>

\<div class="testimonial-author"\>— First Last, Title, Dealership Name\</div\>

---

## JavaScript Reference

All JavaScript is in a single `<script>` block at the bottom of the file, just before `</body>`.

### Functions

| Function | Purpose |
| :---- | :---- |
| `showPage(id)` | Switch the visible page. ID must match a `page-X` div ID. Updates nav active state and browser URL hash. |
| `openMobileNav()` | Opens the mobile slide-in menu |
| `closeMobileNav()` | Closes the mobile menu |
| `closeMobileMenu(e)` | Closes mobile menu when clicking the backdrop |
| `showToast(msg, duration)` | Shows a temporary notification bar at the bottom of the screen. Duration in ms, default 4000\. |
| `handleFormSubmit()` | Validates and submits the contact form via Formspree. Shows loading/success/error states on the button. |

### URL Hash Routing

Pages are accessible via URL hash: `yoursite.com/#pricing`, `yoursite.com/#contact`, etc. This is handled automatically by `showPage()` (writes to `history.pushState`) and a `popstate` listener for browser back/forward navigation.

---

## Brand & Business Context

**Company:** Dealer Ops Consulting **Product:** ReconAI **Mascot:** Socket — a cartoon socket wrench character holding a tablet. Embedded as base64 in the HTML. Do not remove or replace without a new image asset from the client.

**Target audience:** Dealer principals, general managers, used car managers, dealer group executives at franchised and independent automotive dealerships.

**Tone:** Confident, data-driven, automotive-insider. Not corporate. Not overly casual. Talks to people who work on dealer lots.

**Core value proposition:** ReconAI uses a dealership's own completed repair orders (pulled from their DMS) to estimate reconditioning costs at the point of vehicle acquisition — before the deal is done.

**Key DMS platforms to reference:** myKaarma (highest priority), CDK Global, Tekion, Reynolds & Reynolds, DealerSocket, xTime.

**First major dealer partner (beta):** Fletcher Jones (dealer group).

**Two plan tiers:**

- **Base** — My Dealership \+ My Auto Group search modes  
- **Premium** — adds National Database search mode (anonymized data from all ReconAI-connected dealers)

---

## What to Be Careful About

**The base64 Socket image** is \~49,000 characters of encoded data inside the HTML. It appears as `src="data:image/jpeg;base64,/9j/4AAQ..."` in two places (hero card and about page). Never truncate, modify, or delete this string. If you need to edit content near it, search for `data:image/jpeg;base64,` to locate it and work around it.

**Page routing depends on exact IDs.** If you rename a page div's ID, you must update: the div itself, the `showPage()` call in the nav link, the `id="nav-X"` on the nav anchor, and the mobile menu link. Missing any one of these breaks navigation.

**CSS specificity.** The media query overrides at the bottom of the `<style>` block use `!important` to enforce mobile layouts. If a new desktop style isn't applying on mobile, check whether a media query override exists before adding `!important` to the desktop rule.

**Google Fonts require internet.** The fonts are loaded from `fonts.googleapis.com`. When testing the file locally with no internet connection, the browser will fall back to system sans-serif. This is expected and will look slightly different — deploy to Netlify and view online for the real rendering.

**Single file \= single deployment.** There is no separate CSS or JS file to update. Everything is in the one HTML file. When you make a change, save the file and re-deploy to Netlify by dragging the updated file onto the Netlify dashboard.

---

## Deployment

**Platform:** Netlify (free tier) **Method:** Drag and drop `ReconAI_Production_Site.html` onto the Netlify dashboard at [app.netlify.com](https://app.netlify.com)

Each re-deploy takes about 10 seconds. Netlify keeps a deploy history so you can roll back if needed.

**Custom domain:** Managed in Netlify under Site Configuration → Domain Management. GoDaddy nameservers should point to Netlify's nameservers (configured in GoDaddy's DNS settings).

**To rename the file for cleaner Netlify URLs:** rename `ReconAI_Production_Site.html` to `index.html` before uploading. Netlify then serves it at the root URL (`yoursite.com/`) rather than `yoursite.com/ReconAI_Production_Site.html`.

---

## Common Edit Examples

**Change phone number in footer:** Search for the current phone number string and replace it. It appears once in the footer and once in the Contact page.

**Change primary brand blue:** Find `--blue: #1B4FD8` in `:root` and update the hex value. The new color cascades to all buttons, links, and accents automatically.

**Add a new testimonial:** Find `.testimonial-band` in `page-home`. Replace the quote text and author attribution. If adding multiple testimonials, add additional `.testimonial-inner` divs — they stack vertically in the dark band.

**Add a pricing number:** In `page-pricing`, inside each `.pricing-card`, add a price display div before `.pricing-desc`. See the Pricing Cards section above for the recommended HTML structure.

**Add a new feature card:** In `page-features`, find the `.feature-grid`. Copy an existing `.feature-card` div block and paste it as a new card. Update the emoji icon, heading, and description text. The grid automatically handles up to 6 cards in two rows of three on desktop.

**Update the Formspree endpoint:** Find `var FORMSPREE_URL = 'https://formspree.io/f/YOUR_FORM_ID';` in the `<script>` block. Replace `YOUR_FORM_ID` with the ID from your Formspree dashboard.

**Update company contact details:** Search for `hello@dealerops.com` and `(312) 555-0100` — these appear in the Contact page and the footer. Replace with real values.  
