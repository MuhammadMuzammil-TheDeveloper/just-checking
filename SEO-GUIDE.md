# GitHub SEO checklist — Muhammad Muzammil

Be realistic: a profile README is indexed, but ranking comes mostly from **profile settings, repo metadata and backlinks**. Ranking #1 for your own name is realistic in weeks; "MERN developer Karachi" needs the portfolio site plus backlinks. Nobody can guarantee a rank.

## 1. Profile settings (github.com/settings/profile)
- **Name:** `Muhammad Muzammil` (use this exact spelling everywhere: LinkedIn, portfolio, resume)
- **Bio (≤160 chars):** `Full-Stack Web Developer (MERN) · BSCS @ KIET Karachi · React, Node.js, Supabase, WordPress · Open to freelance & internships`
- **Location:** `Karachi, Pakistan` · **Website:** your portfolio URL · **Company:** `@NexSoft Solutions` text is fine
- Repo must be public and named exactly `MuhammadMuzammil-TheDeveloper`

## 2. Pin 6 repos and fix each one
- Description with keywords, e.g. `Supabase-powered sticky notes SaaS — vanilla JavaScript`
- Set the **Website** field to the live demo; add **Topics**, e.g. `javascript react nodejs expressjs mongodb supabase mern-stack rest-api tailwindcss portfolio karachi pakistan`
- Each repo README: one-line summary, screenshot, tech list, live link, setup steps

## 3. Portfolio site (this is where most ranking comes from)
- Put `portfolio-seo-head.html` into your `<head>` (title, description, canonical, Open Graph, JSON-LD `Person` schema linking GitHub + LinkedIn)
- Add `sitemap.xml` + `robots.txt`, verify in **Google Search Console**, submit the sitemap
- Add your portfolio URL to GitHub, LinkedIn and every demo footer ("Built by Muhammad Muzammil")

## 4. Backlinks and consistency
- Link GitHub ↔ LinkedIn ↔ portfolio ↔ demos (Netlify/Vercel) both ways
- Publish 2–3 short articles (dev.to / Hashnode) about projects, linking to the repos
- Keep contributing regularly; the heatmap and stats update automatically via the Action
