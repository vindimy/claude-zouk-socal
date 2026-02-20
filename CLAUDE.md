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

**Sub-tabs or grouped sections by region:** Los Angeles | Orange County | San Diego

Display teacher cards in a responsive CSS grid (3 cols desktop, 2 tablet, 1 mobile). Each card has:
- Circular photo (use placeholder images from `https://i.pravatar.cc/150?u=[name]` as stand-ins with a note that real photos should be swapped in)
- Teacher name (bold)
- Region tag badge (e.g., "Los Angeles")
- Short 2–3 sentence bio
- Social/web links as icon buttons (Instagram, Facebook, website)

Populate with these placeholder teachers (clearly comment that real bios/photos should be filled in):

**Los Angeles:**
- Dmitriy (nyamaste) — Zouk instructor and community organizer known for his musicality and flow-focused teaching style. Instagram: `@nyamaste`
- Ly — Energetic teacher with a background in multiple partner dances. Instagram: `@broc.co.ly`

**Orange County:**
- [Placeholder OC Teacher 1] — Add real teacher name and bio here.
- [Placeholder OC Teacher 2] — Add real teacher name and bio here.

**San Diego:**
- [Placeholder SD Teacher 1] — Add real teacher name and bio here.
- [Placeholder SD Teacher 2] — Add real teacher name and bio here.

Use `<!-- TODO: Replace placeholder teachers with real data -->` comments throughout.

---

### 6. Organizers & DJs Section

**Heading:** "Organizers & DJs"

A horizontal scroll or responsive grid of organizer profile cards (slightly smaller than teacher cards). Each card shows:
- Avatar/photo (placeholder)
- Name
- Role badge (Organizer / DJ / Both)
- Short one-liner
- Social link

Populate with:
- **Dmitriy (nyamaste)** — Organizer & DJ · *"Bringing the Zouk vibes to SoCal since day one."* · Instagram: `@nyamaste`
- **Ly (broc.co.ly)** — Organizer · *"Growing the San Diego Zouk scene with love."* · Instagram: `@broc.co.ly`
- Additional placeholder cards with `<!-- TODO: Add more organizers -->` comment

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

---

## Deliverable

A single, complete `index.html` file, plus image and graphic assets, that can be uploaded directly to `www.zoukcal.com` and work immediately. Include inline comments marking where real content (photos, bios, teacher names) should be filled in by the site owner.