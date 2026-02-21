# Claude Code Prompt: ZoukCal California — Website Redesign

## Project Overview

Build a complete, production-ready **single-page HTML/CSS/JavaScript website** for **Zouk Calendar California** (`www.zoukcal.com`). This site serves the Southern California Brazilian Zouk dance community — it is the central hub for classes, workshops, socials, teachers, and organizers across Los Angeles, Orange County, and San Diego.

---

## Design Direction

Create a **warm, sensual, rhythmic** aesthetic that evokes the mood of Brazilian Zouk dance — fluid motion, intimacy, connection. Think:
- Deep jewel tones: rich indigo/midnight navy as base, warm gold/amber accents, soft rose/blush highlights
- Flowing, organic typography — pair a beautiful serif display font (e.g., Playfair Display or Cormorant Garamond from Google Fonts) with a clean modern body font (e.g., DM Sans or Outfit)
- Subtle wave/flow motifs in backgrounds and dividers to echo Zouk's wavelike movement
- Smooth scroll-triggered fade-in animations and gentle parallax
- Mobile-first, fully responsive layout
- Dark, moody hero with a full-width cinematic feel
- Section dividers using flowing SVG wave shapes

---

## Technical Requirements

- **Single HTML file** (`index.html`) with embedded `<style>` and `<script>` tags — no external files required except Google Fonts CDN
- SEO-optimized: proper `<meta>` tags (title, description, OG tags, canonical URL, keywords), semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<footer>`, `<nav>`, `<article>`)
- Fast-loading: no heavy frameworks, pure vanilla JS, lazy-loaded images
- Accessible: ARIA labels, proper heading hierarchy, color contrast
- Smooth scroll navigation with a sticky top navbar that collapses on mobile (hamburger menu)
- Google Analytics-ready placeholder (`<!-- GA TAG HERE -->`)

---

## Page Structure & Sections

### 1. Navigation (sticky top bar)
- Logo: "ZoukCal" in display font with a subtle wave underline
- Nav links: `Classes & Events`, `Teachers`, `Organizers`, `Join Us`
- Mobile hamburger menu
- CTA button: "Join WhatsApp Community" → `https://chat.whatsapp.com/HgPl6fK4h4zIjdHox06gbp?mode=gi_t`

---

### 2. Hero Section
- Full-viewport height hero
- Background: a deep indigo-to-black gradient with a subtle animated particle/wave overlay (CSS-only or lightweight canvas)
- Headline: **"Find Your Flow in Southern California"**
- Subheadline: *"Brazilian Zouk classes, workshops & socials across Los Angeles, Orange County, and San Diego"*
- Two CTA buttons:
  - "Explore Events" (scrolls to calendar section)
  - "Join the Community" (links to WhatsApp)
- Animated down-scroll indicator

---

### 3. About / What is Zouk? (brief section)
- Short 2–3 sentence intro to Brazilian Zouk as a dance
- Warm, welcoming tone — "Whether you're brand new or a seasoned dancer, SoCal's Zouk community is here for you"
- Three icon feature blocks: 🎵 Music · 💃 Connection · 🌊 Flow

---

### 4. Classes, Workshops & Events (Calendar Section)

**Heading:** "Classes, Workshops & Events"

Create a **tabbed interface** with two tabs:
- **Tab 1: Los Angeles / Orange County**
- **Tab 2: San Diego**

Each tab contains an embedded Google Calendar iframe. Use the embed format:

**LA/OC Calendar embed URL:**
```
https://calendar.google.com/calendar/embed?src=ZTE0dXBzMjducDJjM21xZjU5YW5wYTdmMmNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&ctz=America%2FLos_Angeles&mode=AGENDA&showTitle=0&showNav=1&showPrint=0&showTabs=0&showCalendars=0&bgcolor=%230d0d1a&color=%23c9a84c
```

**San Diego Calendar embed URL:**
```
https://calendar.google.com/calendar/embed?src=ZnVsZTNuY2ZldW04ZzhwaGYxM2p0MnVhYzRAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&ctz=America%2FLos_Angeles&mode=AGENDA&showTitle=0&showNav=1&showPrint=0&showTabs=0&showCalendars=0&bgcolor=%230d0d1a&color=%23c9a84c
```

Each iframe should be:
- Width: 100%, Height: 600px
- `frameborder="0"` `scrolling="no"`
- Surrounded by a styled card container
- Note below calendar: "Times shown in Pacific Time"

Also display a note: *"Want your event listed? Submit to our community calendar via the WhatsApp group."*

---

### 5. Teachers Section

**Heading:** "Meet the Teachers"

**Authoritative data source:** `teachers.list`

**Grouped by region** with tab switcher: Los Angeles | Orange County | San Diego

Display teacher cards in a responsive CSS grid (3 cols desktop, 2 tablet, 1 mobile). Each card has:
- Circular profile photo from `images/<slug>.jpg` (downloaded from Instagram)
- Teacher name (bold)
- Region tag badge (e.g., "Los Angeles")
- Short bio
- Social/web links as icon buttons (Instagram, website globe icon)

**Region mapping for new entries (city → region tab):**
- West LA, Burbank, Downtown LA, Torrance → **Los Angeles**
- Buena Park, Costa Mesa → **Orange County**
- San Diego → **San Diego**

**Current teachers (from `teachers.list`):**

*Los Angeles:* Aneska Franca (@aneskafranca, aneskadance.com), Adam J Craig (@adamjcraig), Stephanie Tong (@stonganie), Myla Ostroshenko (@mylaosa), Nathalia Carbajal (@nathy.carbajal), Viktor Tiz (@dj_viktorr_tiz)

*Orange County:* Christina Montoya (@christinazouk, zoukoc.com), Brayden Schmidt (@braydenzouk, zoukoc.com), Sarah Miles (@sarahzouk, zoukoc.com), Marissa A Rivera (@marissa.a.rivera / @dancewithmares / @zoukvibes)

*San Diego:* Richele Marie (@richele_marie, solzouk.com), Walter Fernandes (@walterfernandes___), Larissa Secco (@larissasecco)

**Image slug convention:** lowercase name with hyphens (e.g., `aneska-franca.jpg`). Download using `download_photos.py` when adding new teachers.

---

### 6. Organizers Section

**Heading:** "Organizers"

**Authoritative data source:** `organizers.list`

**Grouped by region** (same LA / OC / SD mapping as Teachers section). A responsive grid of profile cards. Each card shows:
- Profile photo from `images/<slug>.jpg`
- Name
- Role badge: "Organizer"
- Location one-liner
- Social links (Instagram, website if available)

**Current organizers (from `organizers.list`):**
- Dmitriy Vi (@nyamaste) — West Los Angeles
- Ly Le (@broc.co.ly, @zoukasa.ocla) — Downtown Los Angeles
- Corina Post (@cococonnects) — Los Angeles

---

### 6b. DJs Section

**Heading:** "DJs"

**Authoritative data source:** `djs.list`

**Not grouped by region** — display all DJs in a single flat grid (same card style as Organizers). Each card shows:
- Profile photo from `images/<slug>.jpg`
- Name
- Role badge: "DJ"
- Location one-liner
- Social links (Instagram, website if available)

**Current DJs (from `djs.list`):**
- Matt Laney (@amastrus_music) — Los Angeles
- Orlan Mat (@djcal_z) — Los Angeles
- Dhruv Puri (@dhroovvy) — San Diego

---

### 7. Join Us Section

**Heading:** "Join the SoCal Zouk Community"

- Warm, inviting full-width section with a contrasting background (soft warm gradient)
- Welcome message:
  > *"Whether you're lacing up your dance shoes for the first time or you're a seasoned Zouk dancer, you belong here. Our community spans Los Angeles, Orange County, and San Diego — united by music, movement, and connection. Come dance with us!"*
- Large WhatsApp CTA button: **"Join Our WhatsApp Community"** → `https://chat.whatsapp.com/HgPl6fK4h4zIjdHox06gbp?mode=gi_t`
- WhatsApp icon (use SVG or emoji 💬)
- Secondary note: *"Free to join · All levels welcome · SoCal dancers only"*

---

### 8. Footer

- Logo + tagline: *"The heartbeat of Brazilian Zouk in Southern California"*
- Quick nav links
- Copyright: `© 2025 Zouk Calendar California`
- Disclaimer: *"Calendar events are community-submitted. Contact event organizers directly for details."*
- Link to submit events via WhatsApp

---

## SEO Meta Tags to Include

```html
<title>Zouk Calendar California | Brazilian Zouk Classes & Events in LA, OC & San Diego</title>
<meta name="description" content="Find Brazilian Zouk dance classes, workshops, and social events in Los Angeles, Orange County, and San Diego. SoCal's community calendar for Zouk dancers.">
<meta name="keywords" content="Brazilian Zouk, Zouk dance, Los Angeles Zouk, San Diego Zouk, Orange County Zouk, Zouk classes Southern California, Zouk socials SoCal, Zouk workshops LA">
<meta property="og:title" content="Zouk Calendar California">
<meta property="og:description" content="Brazilian Zouk classes, workshops & socials across Southern California">
<meta property="og:url" content="https://www.zoukcal.com">
<meta property="og:type" content="website">
<link rel="canonical" href="https://www.zoukcal.com">
```

---

## Implementation Notes for Claude Code

1. **Start by scaffolding** the full HTML structure with all sections as empty containers
2. **Build the CSS** using CSS custom properties (variables) for the color system and spacing scale
3. **Implement the navbar** with working hamburger toggle in JS
4. **Build the calendar tab switcher** — pure JS, no libraries needed
5. **Build the teacher and organizer cards** — use CSS Grid
6. **Add scroll animations** — use `IntersectionObserver` API for fade-in-on-scroll effects
7. **Test mobile responsiveness** at 375px, 768px, 1024px, 1440px breakpoints
8. **Validate HTML** is semantic and accessible before finalizing
9. Output the complete, ready-to-deploy `index.html` file

## Updating People (Teachers / Organizers / DJs)

When updating any of the three people sections, always read the corresponding `.list` file first:
- `teachers.list` → Teachers section (region-grouped tabs: LA / OC / SD)
- `organizers.list` → Organizers section (region-grouped)
- `djs.list` → DJs section (no grouping, single flat grid)

Each `.list` entry follows this format:
```
Full Name
https://www.instagram.com/handle/   ← one or more social/web URLs
Location: City Name
```

After adding new entries to `index.html`, download their Instagram profile photo using `download_photos.py` and save to `images/<slug>.jpg` (lowercase hyphenated name). Reference the image in the card's `<img src="images/<slug>.jpg">`.

## Deployment

Site deploys to [https://zoukcal-socal.surge.sh](https://zoukcal-socal.surge.sh) via:
```
surge . zoukcal-socal.surge.sh
```

---

## Deliverable

A single, complete `index.html` file, plus image and graphic assets, that can be uploaded directly to `www.zoukcal.com` and work immediately. Include inline comments marking where real content (photos, bios, teacher names) should be filled in by the site owner.