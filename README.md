<div align="center">

# Soumya Debnath

### Software Engineer — Mobile, Full-Stack & Applied AI

**I ship and operate real products.** Two consumer apps live on the App Store, built solo end to end — product, architecture, AI pipeline, localisation, monetisation and release operations.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-soumya--debnath-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/soumya-debnath-83a68a237/)
[![Email](https://img.shields.io/badge/Email-soumyadebnath1619%40gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:soumyadebnath1619@gmail.com)

Kolkata, India · Open to relocation and remote · MCA 2026

</div>

---

## 📱 Live in the App Store

### CTrackAI — AI Calorie & Nutrition Tracker
**Flutter · Dart · Gemini · Firebase**
[App Store](https://apps.apple.com/in/app/ctrackai-free-calorie-tracker/id6758379785) · [Google Play](https://play.google.com/store/apps/details?id=com.ctrackaiai.nutrition)

Shipped March 2026 and maintained since — currently v1.3, **localised into 11 languages**, rated **4.9/5** (small review base, 9 ratings).

Most nutrition apps are built around a food database, which means roughly three billion people eat food the app cannot recognise. CTrackAI takes the visual route instead: point the camera at dal, jollof rice, pho or mole and get calories and macros back from a Gemini vision pipeline. Barcode scanning, voice and manual entry, 20+ nutrient analytics, Apple Health, fasting and hydration tracking, streaks.

I built and run all of it — the AI pipeline, the localisation, the rewarded-ad and subscription economics that make the API costs work, and every store release.

### Preeo — Cycle & Health Companion
**Cross-platform mobile · on-device AI · encrypted health data**
[App Store](https://apps.apple.com/in/app/preeo-cycle-period-tracker/id6760804568) · [Google Play](https://play.google.com/store/apps/details?id=com.preeo.health.companion)

Launched July 2026. **No account required, health data encrypted on-device.** Nine condition-specific journeys — typical cycles, PCOS, fertility, pregnancy, perimenopause, endometriosis, PMDD, birth control, teens — instead of one generic flow. 100+ symptom inputs, BBT charting, HealthKit and Health Connect, biometric protection, time-limited doctor sharing.

---

## 🏆 Recognition

- **Best Cybersecurity Tool — Quantum Sprint 2026** for [VulnHunter](https://github.com/itsoumya-d/vulnhunter): paste a GitHub repo URL, get an OWASP Top 10 report in under 30 seconds. Analyses up to 40 files in parallel batches, returns CWE-tagged findings with line-level patches and a weighted 0–100 risk score.
- **Finalist — NextDev Hackathon 2026** for [CyberMentor](https://github.com/itsoumya-d/cybermentor): 15 OWASP exploit challenges with Claude-based Socratic review of attempted fixes.

---

## 🔧 Selected engineering work

**[CertiFlow AI](https://github.com/itsoumya-d/certiflow-ai)** — agentic GRC platform. *Next.js · TypeScript · Gemini · SSE · RBAC*
Autonomous compliance checks against AWS S3 encryption, AWS IAM MFA, GitHub branch protection and Okta MFA, with live SSE dashboards, evidence analysis and Admin/User/Auditor scopes. My most substantial single codebase.

**[Motion MCP](https://github.com/itsoumya-d/motion-mcp)** — codebase-aware motion generation. *TypeScript · Model Context Protocol*
A 22-tool MCP server that scans an existing app, models Rive-like state machines, ranks high-value interactions, and stages framework-native animation diffs — applying changes only after approval.

**[HEROS](https://github.com/itsoumya-d/HEROS)** — agent-safe infrastructure toolkit. *Node.js · MCP*
JSON-only contracts, stable error codes, schema validation, approval challenges, idempotent writes, audit receipts, file-locking and atomic-write hardening, plus an OWASP Agentic Top 10 threat model.

**[Mobile-Native Design System](https://github.com/itsoumya-d/mobile-native-design-system)** — *Python · Flutter · React Native · SwiftUI · Compose*
A plugin that reconstructs routes, state, data boundaries and design language before proposing changes. Seven focused skills, a 30-rule evidence registry, guarded one-screen-at-a-time implementation across four native frameworks.

---

## 🧪 Browser-native infrastructure — 10 prototypes, independently audited

*TypeScript · Go · WebRTC · WASM · WebGPU · WebCrypto · CRDTs · AGPL-3.0*

Ten SDK prototypes exploring what becomes possible when you remove the server: peer-to-peer encrypted file transfer, CRDT sync, swarm video relay, on-device analytics, distributed WASM tasks, passkeys, browser inference.

**I commissioned an independent external audit of all ten and published what it found — including my own mistakes.** It surfaced a concurrency bug losing 90% of writes, remotely triggerable prototype pollution, silent file corruption, and documentation claims my code did not support. I fixed them and shipped the fixes.

What held up afterwards: CRDT convergence verified across **1000+ randomised fuzz seeds with zero divergences**, and genuine AV1 encoding through WebCodecs.

These are **prototypes, not production libraries** — no external users. I list them because the audit-and-repair cycle is the part I would want a team to judge me on.

[AllRTC](https://github.com/itsoumya-d/allrtc) · [GhostSearch](https://github.com/itsoumya-d/ghostsearch) · [PeerVault](https://github.com/itsoumya-d/peervault) · [SyncForge](https://github.com/itsoumya-d/syncforge) · [PulseNet](https://github.com/itsoumya-d/pulsenet) · [MeshAuth](https://github.com/itsoumya-d/meshauth) · [EdgeInfer](https://github.com/itsoumya-d/edgeinfer) · [SwarmCompute](https://github.com/itsoumya-d/swarmcompute) · [SyncPlay](https://github.com/itsoumya-d/syncplay) · [ZeroQ](https://github.com/itsoumya-d/zeroq)

---

## 🛠️ Stack

| | |
|:--|:--|
| **Mobile** | Flutter, Dart, React Native, Expo, Riverpod, HealthKit / Health Connect, App Store Connect, Play Console |
| **Frontend** | TypeScript, React, Next.js, Tailwind |
| **Backend** | Go, Python (FastAPI), Node.js, PostgreSQL, Supabase, Firebase, Edge Functions, Docker |
| **Applied AI** | Gemini, Claude, OpenAI Vision, MCP servers, tool calling, structured outputs, evaluation |
| **Browser systems** | WebRTC DataChannels, WebAssembly, WebGPU, WebCrypto, CRDTs, IndexedDB, WebAuthn, ONNX Runtime Web |
| **Security** | OWASP Top 10, threat modelling, SOC 2 / ISO 27001 control automation |

---

## 🧭 Positioning: why this portfolio looks the way it does

The 2026 hiring market is reorganising around exactly the problems these repos attack:

- Forward-Deployed Engineer postings on Indeed grew **729% in one year** (643 → 5,330, April 2025 → April 2026); OpenAI, Meta, Anthropic and Google Cloud all built dedicated FDE teams ([skai.io](https://skai.io/blog/why-forward-deployed-engineering-is-enterprise-ais-newest-fastest-growing-role)).
- Agentic-AI job postings grew **~280% year-over-year**, and ~64% of enterprises deployed AI agents *before* feeling organisationally ready — i.e., before governance existed for them ([F5 Hiring / Stanford AI Index data](https://f5hiringsolutions.com/blog/agentic-ai-job-postings-2026)).
- The two fastest-growing enterprise titles are Forward-Deployed Engineer and Agent Manager — roles about shipping *and operating* agent systems inside real constraints, not training models ([ekas.io analysis](https://ekas.io/blog/enterprise-ai-hiring-split)).

That is the shape of this portfolio: two shipped consumer apps (operating real products solo), an agent-governance platform (CertiFlow), agent-safety infrastructure (HEROS, mapped to OWASP Agentic Top 10), an MCP server for UI motion (Motion MCP), and ten audited browser-infrastructure prototypes. Building the infrastructure agents need — and proving it survives an audit — is the skill those roles test for.

---

## 📬 Contact

**[soumyadebnath1619@gmail.com](mailto:soumyadebnath1619@gmail.com)** · **[LinkedIn](https://www.linkedin.com/in/soumya-debnath-83a68a237/)**

Open to software engineering roles — mobile, full-stack, or applied AI. Kolkata-based, open to relocation or remote. Completing an MCA in 2026.
