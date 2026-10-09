<div align="center">

# Soumya Debnath

### Founding AI Product Engineer &middot; Forward-Deployed Software Engineer
**Building Applied AI Systems, Developer Tools & Shipped Mobile Apps**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-soumya--debnath-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/soumya-debnath-83a68a237/)
[![GitHub](https://img.shields.io/badge/GitHub-itsoumya--d-181717?style=for-the-badge&logo=github)](https://github.com/itsoumya-d)
[![Email](https://img.shields.io/badge/Email-soumyadebnath1619%40gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:soumyadebnath1619@gmail.com)

Kolkata, India &middot; Open to Relocation & Remote (Global)

</div>

---

## Start Here

* **Shipped Flutter apps:** [CTrackAI](./case-studies/ctrackai-engineering.md) and [Preeo](./case-studies/preeo-architecture.md). The store links below lead to published iOS/Android products; their commercial source is not included here.
* **React/TypeScript frontend:** [Cognition (`aeo_geo`)](https://github.com/itsoumya-d/aeo_geo), the audit-dashboard project linked in my CVs. [Main CI](https://github.com/itsoumya-d/aeo_geo/actions/runs/34338373525) verifies typechecking, unit tests and build. The full audit flow needs backend/provider setup. A credential-free report-editor demo is proposed in [open PR #3](https://github.com/itsoumya-d/aeo_geo/pull/3); its browser workflow currently has a [keyboard-reorder failure](https://github.com/itsoumya-d/aeo_geo/actions/runs/37789771619), so it is not presented as verified main-branch functionality.
* **Local full-stack prototype:** [AutoPilot FDE quick start and walkthrough](https://github.com/itsoumya-d/autopilot-fde/blob/6f2986f96a604a74f0851e6bab4dda97edb59755/README.md#quick-start). Python 3.12+, Node 22 and local dependencies run a FastAPI/Next.js demo seeded with synthetic messages, without external accounts or model API keys. Live connectors and hosted deployment need separate validation.
* **Dependency-free engineering exercise:** [FieldLens queue tests](https://github.com/itsoumya-d/fieldlens__/blob/b035fc284c1c8c93f20839af1f27b4bf68317bf3/tests/README.md) run on Node 24 without provider credentials or app-package installation. The [case study](./case-studies/fieldlens-offline-engine.md) explains the concurrency decision and delivery limits.

## 📱 Shipped Consumer Products

### CTrackAI — AI Calorie & Nutrition Tracker
**Flutter · Dart · AI-Assisted Food Logging**

[App Store](https://apps.apple.com/in/app/ctrackai-free-calorie-tracker/id6758379785) · [Google Play](https://play.google.com/store/apps/details?id=com.ctrackaiai.nutrition) · [📖 Product & Engineering Overview](./case-studies/ctrackai-engineering.md)

* **Built and shipped:** A consumer nutrition app available on iOS and Android.
* **Published feature set:** Photo-based food logging, barcode scanning, macro tracking, meal planning, fasting and hydration tracking.
* **Evidence:** Store listings and release history are public. Performance, reliability and cost-reduction figures are omitted until a reproducible measurement report is available.

### Preeo — Cycle & Health Companion
**Flutter · Dart · Cycle Tracking · Health Reports**

[App Store](https://apps.apple.com/in/app/preeo-cycle-period-tracker/id6760804568) · [Google Play](https://play.google.com/store/apps/details?id=com.preeo.health.companion) · [📖 Product & Data Boundary Overview](./case-studies/preeo-architecture.md)

* **Built and shipped:** A consumer cycle-tracking app available on iOS and Android.
* **Published feature set:** Cycle and symptom logging, BBT charts, health integrations and reports for sharing with a healthcare provider.
* **Scope:** An informational wellness product. Store descriptions establish the advertised features, not clinical validation or independently verified security guarantees.

---

## 🔎 Selected Proof of Work

Public source and CI checked on **9 October 2026**. “Merged” means included in the repository, not deployed to users. CI links below cover the cited revisions.

* **Queue reliability · FieldLens:** Merged same-runtime serialization, persisted retries and shared create/update/delete dispatch. The [case study](./case-studies/fieldlens-offline-engine.md) links source, regression evidence and remaining delivery limits. Browser recording is now [merged in PR #9](https://github.com/itsoumya-d/fieldlens__/pull/9). Main has passing provider-free runtime/queue checks, but its EAS build fails without Expo authentication and the web biometric startup blocker remains.
* **Reviewable developer tooling · Motion MCP:** A [runnable, credential-free patch walkthrough](https://github.com/itsoumya-d/motion-mcp/blob/9f1787443c959b39866225eecd40d1fe052675d2/examples/patch-review/README.md) demonstrates import inspection, text-anchor insertion, repeatability and guarded no-ops. [Merged PR #2](https://github.com/itsoumya-d/motion-mcp/pull/2) · [Node 22/24 CI](https://github.com/itsoumya-d/motion-mcp/actions/runs/37775446846). Hand-written fixtures; no live AI or semantic code-review claim.
* **Measurement integrity · HostShift:** Merged [fail-closed criteria validation](https://github.com/itsoumya-d/hostshift/pull/5) and [unavailable/partial-calibration reporting](https://github.com/itsoumya-d/hostshift/pull/6). Combined-main [Python 3.11–3.14 CI](https://github.com/itsoumya-d/hostshift/actions/runs/37921645160) passed at `f8860a2`. The synthetic-demo short-budget correction remains [draft PR #7](https://github.com/itsoumya-d/hostshift/pull/7). These checks validate evaluation tooling, not live-model or native-device benchmark outcomes.
* **Cross-platform tooling · Mobile-Native Design System:** The [token-parity fixture](https://github.com/itsoumya-d/mobile-native-design-system/blob/7b2bb97ebc968e9e52b4dce85b1743f1df658d27/fixtures/token-parity/README.md) detects edited output even after its stored hash is refreshed. [Merged PR #4](https://github.com/itsoumya-d/mobile-native-design-system/pull/4) has passing [core](https://github.com/itsoumya-d/mobile-native-design-system/actions/runs/37786316900), [Android](https://github.com/itsoumya-d/mobile-native-design-system/actions/runs/37786316947) and [Apple](https://github.com/itsoumya-d/mobile-native-design-system/actions/runs/37786317099) checks at `7b2bb97`. Compiler/reference-app fixtures, not physical-device certification.
* **Full-stack maintenance · AutoPilot FDE:** Merged [API error-contract/CI repairs](https://github.com/itsoumya-d/autopilot-fde/pull/2) and a [Next.js dependency security patch](https://github.com/itsoumya-d/autopilot-fde/pull/3). [Current-main backend Python matrix and frontend CI](https://github.com/itsoumya-d/autopilot-fde/actions/runs/37883736388) passed at `6f2986f`. Generated-workflow follow-up [PR #5](https://github.com/itsoumya-d/autopilot-fde/pull/5) remains open. The workflow-discovery product remains a prototype; no live deployment or comprehensive security audit is claimed.

---

## 🤖 Agent Infrastructure & Applied AI Projects

These repositories cover developer tools, research and prototypes. Their linked documentation describes setup and project-specific limitations; they should not be read as evidence of customer deployments.

### 1. [AutoPilot FDE 2.0](https://github.com/itsoumya-d/autopilot-fde) — Workflow Discovery & Agent Prototype
*Python · FastAPI · Next.js · MCP*

* Explores communication ingestion, process graphs, automation scoring and workflow generation.
* Includes local evaluation and simulation tooling. Enterprise deployment, customer adoption and multi-department production performance are not established by the portfolio.

### 2. [Motion MCP](https://github.com/itsoumya-d/motion-mcp) — Codebase-Aware Motion Tooling
*TypeScript · Model Context Protocol · SceneDoc*

* Scans application structure, represents motion in SceneDoc and stages generated changes for review.
* Explores framework-native motion generation and a skeletal-animation bridge. Test coverage and target-specific support are documented in the repository; support for a target does not imply every generated interaction has been runtime-validated.

### 3. [HEROS](https://github.com/itsoumya-d/HEROS) — Agent-Native Infrastructure & Safety Primitives
*Zero-lang Primitives · Node.js / ESM SDK · MCP-Native Contracts*

* Provides structured agent actions, schema validation, machine-readable errors and auditable receipts.
* Includes the `@heros/agentic` web SDK, `forge` migration-risk tooling and `ledger` accounting-receipt primitives. These controls reduce execution ambiguity; they are not a guarantee against all agent errors.

### 4. [CertiFlow AI](https://github.com/itsoumya-d/certiflow-ai) — GRC & Agent Telemetry Simulator *(Prototype)*
*Next.js · TypeScript · Server-Sent Events*

* Demonstrates compliance-agent workflows and live telemetry dashboards.
* Uses simulated cloud telemetry and an in-memory audit store. It does not establish live compliance certification or enterprise audit outcomes.

### 5. [HostShift](https://github.com/itsoumya-d/hostshift) — Cross-Platform UI Portability Research
*Python · UI Specifications · Renderers · Evaluation Harness*

* Investigates whether generated interfaces preserve task behavior across Web, SwiftUI, Compose and Textual hosts.
* Separates offline/synthetic pipeline checks from device-backed experiments. See the repository's status section before interpreting benchmark results.

### 6. [Mobile-Native Design System](https://github.com/itsoumya-d/mobile-native-design-system) — Codebase-Aware Codex Plugin
*Python · Flutter · React Native · SwiftUI · Jetpack Compose*

* Organizes codebase analysis, screen planning, design tokens and reviewable native implementation workflows.
* **Mobile queue reliability:** [FieldLens Queue Repair & Validation](./case-studies/fieldlens-offline-engine.md), covering merged concurrent-write/retry fixes, deterministic regression tests and the remaining runtime boundaries.

---

## 🧪 Browser-Native Infrastructure Suite (Edge Prototypes)
*TypeScript · Go · WebRTC · WASM · WebGPU · WebCrypto · CRDTs*

An experimental suite exploring client-side P2P systems and distributed edge execution:

* **Seeded testing:** [SyncForge's property and regression tests](https://github.com/itsoumya-d/syncforge/blob/b08435c22b35fffebb1afa99b3a697e92e481cde/tests/crdt-properties.test.mjs) exercise merge laws and replica delivery scenarios. This is bounded test coverage, not proof of convergence under every network or failure condition.
* **Deployment constraints:** Browser capabilities, signaling, NAT/TURN relays and local resource limits need project-specific evaluation.
* **Projects:** [AllRTC](https://github.com/itsoumya-d/allrtc) · [GhostSearch](https://github.com/itsoumya-d/ghostsearch) · [PeerVault](https://github.com/itsoumya-d/peervault) · [SyncForge](https://github.com/itsoumya-d/syncforge) · [PulseNet](https://github.com/itsoumya-d/pulsenet) · [MeshAuth](https://github.com/itsoumya-d/meshauth) · [EdgeInfer](https://github.com/itsoumya-d/edgeinfer) · [SwarmCompute](https://github.com/itsoumya-d/swarmcompute) · [SyncPlay](https://github.com/itsoumya-d/syncplay) · [ZeroQ](https://github.com/itsoumya-d/zeroq)

---

## 🏆 Featured Tools & Hackathon Prototypes

* **[VulnHunter](https://github.com/itsoumya-d/vulnhunter):** A source-analysis security scanner prototype with vulnerability reports and suggested remediation.
* **[CyberMentor](https://github.com/itsoumya-d/cybermentor):** An interactive security-learning prototype with AI-assisted hints and vulnerability walkthroughs.

---

## 🛠️ Technical Stack

| Category | Stack & Tooling |
|:--|:--|
| **Applied AI & Agents** | LangGraph, Model Context Protocol (MCP), Gemini, Claude, OpenAI, Tool Calling, Structured Outputs |
| **Full-Stack & Real-Time** | TypeScript, Next.js, React, Python (FastAPI), Node.js, REST APIs, Server-Sent Events, WebSockets, PostgreSQL, Supabase, Redis |
| **Mobile Engineering** | Flutter, Dart, React Native, Expo, HealthKit, Health Connect, App Store Connect, Play Console |
| **Development & Delivery** | Docker, GitHub Actions, Linux, Git, Testing, Threat Modeling |

---

## 📬 Connect

* **Email:** [soumyadebnath1619@gmail.com](mailto:soumyadebnath1619@gmail.com)
* **LinkedIn:** [linkedin.com/in/soumya-debnath-83a68a237](https://www.linkedin.com/in/soumya-debnath-83a68a237/)
* **GitHub:** [github.com/itsoumya-d](https://github.com/itsoumya-d)
