<div align="center">

# Soumya Debnath

### Founding AI Product Engineer &middot; Forward-Deployed Software Engineer
**Building Autonomous Agent Infrastructure, Enterprise AI Systems & Production Mobile Apps**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-soumya--debnath-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/soumya-debnath-83a68a237/)
[![GitHub](https://img.shields.io/badge/GitHub-itsoumya--d-181717?style=for-the-badge&logo=github)](https://github.com/itsoumya-d)
[![Email](https://img.shields.io/badge/Email-soumyadebnath1619%40gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:soumyadebnath1619@gmail.com)

Kolkata, India &middot; Open to Relocation & Remote (Global) &middot; 5+ Years Production Delivery & Systems Architecture

</div>

---

## 📱 Shipped Consumer Products (Live on App Store & Google Play)

### CTrackAI — AI Calorie & Nutrition Tracker
**Flutter · Dart · Gemini Vision · Firebase · In-App Purchases**  
[App Store](https://apps.apple.com/in/app/ctrackai-free-calorie-tracker/id6758379785) · [Google Play](https://play.google.com/store/apps/details?id=com.ctrackaiai.nutrition) · [📖 Engineering Case Study](./case-studies/ctrackai-engineering.md)

* **Solo-built and shipped end-to-end:** Architecture, multimodal AI pipeline, 11-language localization, App Store/Play release operations, and unit economics.
* **Beyond database hits:** Low-latency Gemini vision pipeline recognizes real-world uncurated meals (dal, jollof rice, pho, regional mixed dishes).
* **Feature suite:** Barcode scanning, voice logging, 20+ micronutrient analytics, Apple Health / Health Connect sync, fasting timers, hydration tracking, and streak mechanics.
* **Economics & Reliability:** Local perceptual image hash (pHash) cache cuts recurring API costs by 42% (<240ms cached lookup); holds a **4.9/5 rating** on the App Store.

### Preeo — Privacy-First Cycle & Health Companion
**Cross-Platform Mobile · On-Device SQLite Encryption · Biometric Auth · Scoped Cloud Sync**  
[App Store](https://apps.apple.com/in/app/preeo-cycle-period-tracker/id6760804568) · [Google Play](https://play.google.com/store/apps/details?id=com.preeo.health.companion) · [📖 Architecture & Data Flow Case Study](./case-studies/preeo-architecture.md)

* **Cryptographic local storage:** Core health logs encrypted on-device (AES-256 GCM SQLite) with FaceID/TouchID protection. No account required for core tracking.
* **Explicit data boundaries:** Optional Firebase backup and cloud AI insights require explicit per-feature opt-in; users retain total data deletion and local export control.
* **Condition-specific journeys:** 9 distinct clinical journeys (cycles, PCOS, fertility, pregnancy, perimenopause, endometriosis, PMDD, birth control, adolescent health) with 100+ clinical symptom inputs.
* **Clinical export:** Secure doctor-share PDF generation and Apple HealthKit / Android Health Connect integration.

---

## 🤖 Flagship Agent Infrastructure & Applied AI Systems

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                             AGENT INFRASTRUCTURE STACK                                   │
├───────────────────────────────┬───────────────────────────────┬──────────────────────────┤
│ AutoPilot FDE 2.0             │ Motion MCP                    │ HEROS                    │
│ Autonomous Business Process   │ Codebase-Aware Motion Engine  │ Agent-Native Action      │
│ Discovery & LangGraph Agents  │ 64 MCP Tools · 230+ Tests     │ Safety & Contracts       │
├───────────────────────────────┼───────────────────────────────┼──────────────────────────┤
│ CertiFlow AI                  │ HostShift                     │ Mobile Design System     │
│ Autonomous GRC & Trust        │ Cross-Platform Generative UI  │ Whole-Codebase Scanner   │
│ Continuous Audit Automation   │ Open Benchmark (230+ Tests)   │ Multi-Framework Codex    │
└───────────────────────────────┴───────────────────────────────┴──────────────────────────┘
```

### 1. [AutoPilot FDE 2.0](https://github.com/itsoumya-d/autopilot-fde) — Autonomous Forward-Deployed Engineering Agent
*Python 3.12 · FastAPI · Next.js 15 · LangGraph · Shannon Entropy · Dual-Transport MCP*

* **Workflow-Mining Pipeline:** Ingests unstructured Slack, WhatsApp, email, and call transcripts, extracts organizational activities via Bayesian parsing, and constructs directed process graphs.
* **Graph Entropy Scoring:** Formulates an Automation Potential Score (APS) using transition entropy to pinpoint operational bottlenecks, then runs 1,000-event pre-deployment Monte Carlo simulations.
* **Self-Deploying State Machines:** Automatically compiles typed LangGraph state machines with Human-in-the-Loop review gates.
* **Dual MCP Support:** Ships stdio and Streamable-HTTP (`POST /mcp`) transports compatible with Claude Code, Cursor, and Codex CLI. Evaluated across 158 multi-turn interaction runs across 8 enterprise departments.

### 2. [Motion MCP](https://github.com/itsoumya-d/motion-mcp) — Codebase-Aware Motion Engine for Coding Agents
*TypeScript 5.7 · Model Context Protocol · SceneDoc Format · Kimodo.cpp Diffusion*

* **64 MCP Tools & 230+ Tests:** Plugs into Cursor, Claude Code, or Codex CLI to turn existing codebases into animated, living products without rewrites or proprietary runtimes.
* **Framework-Native Diff Staging:** Scans routes and component trees, models interactive state machines, compiles open SceneDoc specifications, and generates native code for React, React Native, Flutter, Unity, and Three.js/R3F.
* **3D Diffusion Bridge:** Features natural-language text-to-3D skeletal animation diffusion across 22 SMPL-X standard joints with retargeting for Mixamo and Unity Mecanim.

### 3. [HEROS](https://github.com/itsoumya-d/HEROS) — Agent-Native Infrastructure & Safety Primitives
*Zero-lang Primitives · Node.js / ESM SDK · MCP-Native Contracts · OWASP Agentic Top 10*

* **Contract-First Agent Execution:** Deterministic JSON-only outputs, stable machine-readable error codes, schema validation, idempotent writes, and auditable receipts so agents never hallucinate text execution branches.
* **Core Primitives:**
  * `@heros/agentic`: Installable SDK surface for explicit, authenticated, auditable agent website actions.
  * `forge`: Agent-safe database migration risk gate scoring schema modifications before execution.
  * `ledger`: Accounting receipt primitive with idempotency keys to prevent duplicate actions.

### 4. [CertiFlow AI](https://github.com/itsoumya-d/certiflow-ai) — Autonomous GRC & Agent Telemetry Simulator *(Prototype)*
*Next.js 14 · TypeScript · Gemini Computer Use · Server-Sent Events (SSE) · RBAC*

* **Autonomous Audit Automation (Prototype):** Demonstrates autonomous agents continuously inspecting compliance controls across AWS, GitHub, and Okta via Gemini Computer Use workflows.
* **Zero-Cloud Demo Architecture:** Runs on simulated AWS telemetry and in-memory audit logs for zero-dependency local evaluation and immediate reviewer verification.
* **Live SSE Dashboards:** Real-time compliance score ring with zero-polling updates, automated evidence parsing, and scoped Admin/User/Auditor access controls.

### 5. [HostShift](https://github.com/itsoumya-d/hostshift) — Cross-Platform Generative UI Portability Benchmark
*Python 3.11 · AGPL-3.0 · 230 Passing Tests (84% Coverage) · Open Benchmark Suite*

* **Empirical UI Portability Benchmark:** Evaluates whether LLM-generated UI code preserves visual and functional semantics across 5 targets: Web (Chromium), iOS (SwiftUI), Android (Jetpack Compose), Flutter (Dart), and Terminal (Textual).
* **Rigorous Validation Gates:** Combines AST-level syntax conformance checkers with isolated render oracles. Measured across 100 test tasks using tree-edit distance and bootstrap statistics.

### 6. [Mobile-Native Design System](https://github.com/itsoumya-d/mobile-native-design-system) — Codebase-Aware Codex Plugin
*Python · Flutter · React Native · SwiftUI · Jetpack Compose*

* Whole-codebase analyzer reconstructing routes, screen state, and design tokens. Enforces 7 progressively disclosed skills and a 30-rule evidence registry for guarded, one-screen-at-a-time native implementation.
* **Mobile Queue Reliability Research:** [FieldLens Concurrency & Queue Durability Case Study](./case-studies/fieldlens-offline-engine.md) (remediating concurrent read-modify-write lost updates and retry persistence).

---

## 🧪 Browser-Native Infrastructure Suite (10 Edge Prototypes)
*TypeScript · Go · WebRTC · WASM · WebGPU · WebCrypto · CRDTs*

An experimental research suite exploring client-side P2P systems and distributed edge execution:
* **Fuzz-Tested CRDT Convergence:** State convergence verified across **1,000+ randomized fuzz seeds with zero unhandled state divergences**.
* **Documented Network Boundaries:** Explicitly documented NAT/TURN relay requirements, local computational quotas, and cryptographic fallback semantics.
* **Projects:** [AllRTC](https://github.com/itsoumya-d/allrtc) · [GhostSearch](https://github.com/itsoumya-d/ghostsearch) · [PeerVault](https://github.com/itsoumya-d/peervault) · [SyncForge](https://github.com/itsoumya-d/syncforge) · [PulseNet](https://github.com/itsoumya-d/pulsenet) · [MeshAuth](https://github.com/itsoumya-d/meshauth) · [EdgeInfer](https://github.com/itsoumya-d/edgeinfer) · [SwarmCompute](https://github.com/itsoumya-d/swarmcompute) · [SyncPlay](https://github.com/itsoumya-d/syncplay) · [ZeroQ](https://github.com/itsoumya-d/zeroq)

---

## 🏆 Featured Tools & Hackathon Prototypes

* **[VulnHunter](https://github.com/itsoumya-d/vulnhunter):** High-speed AST & regex security scanner analyzing up to 40 source files in parallel; outputs CWE-tagged reports with automated line-level remediation patches.
* **[CyberMentor](https://github.com/itsoumya-d/cybermentor):** Interactive FastAPI security tutor featuring Socratic Claude-assisted hints and vulnerability walkthroughs.

---

## 🛠️ Technical Arsenal

| Category | Core Stack & Tooling |
|:--|:--|
| **Applied AI & Agents** | LangGraph, Model Context Protocol (MCP), Gemini 1.5, Claude 3.5, OpenAI Vision, Tool Calling, Structured Outputs, Process Mining, Monte Carlo Simulation |
| **Full-Stack & Real-Time** | TypeScript, Next.js 15, React, Python (FastAPI), Node.js, REST APIs, Server-Sent Events (SSE), WebSockets, PostgreSQL, Supabase, Redis |
| **Mobile Engineering** | Flutter, Dart, React Native, Expo, HealthKit, Health Connect, Biometric Authentication, SQLite Encryption, App Store Connect, Play Console |
| **DevOps & Security** | Docker, GitHub Actions CI/CD, OWASP Agentic Top 10, Threat Modeling, SOC 2 / ISO 27001 Controls, Linux, Git |

---

## 📬 Connect

* **Email:** [soumyadebnath1619@gmail.com](mailto:soumyadebnath1619@gmail.com)
* **LinkedIn:** [linkedin.com/in/soumya-debnath-83a68a237](https://www.linkedin.com/in/soumya-debnath-83a68a237/)
* **GitHub:** [github.com/itsoumya-d](https://github.com/itsoumya-d)
