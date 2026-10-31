<div align="center">

# Soumya Debnath

### Founding AI Product Engineer &middot; Senior AI Software Engineer &middot; Forward-Deployed Engineer
**Building Applied AI Systems, Document Intelligence, Developer Tools & Shipped Mobile Apps**

**LLM Features &middot; Document Extraction &middot; Retrieval &middot; Evals &middot; Python &middot; C#/.NET &middot; React/TypeScript**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-soumya--debnath-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/soumya-debnath-83a68a237/)
[![GitHub](https://img.shields.io/badge/GitHub-itsoumya--d-181717?style=for-the-badge&logo=github)](https://github.com/itsoumya-d)
[![Email](https://img.shields.io/badge/Email-soumyadebnath1619%40gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:soumyadebnath1619@gmail.com)

Kolkata, India &middot; Open to Relocation & Remote (Global) &middot; 5+ Years Professional Delivery &middot; Coding since 2017

</div>

---

## 📱 Shipped Consumer Products

### CTrackAI — AI Calorie & Nutrition Tracker
**Flutter · Dart · AI-Assisted Food Logging**

[App Store](https://apps.apple.com/in/app/ctrackai-free-calorie-tracker/id6758379785) · [Google Play](https://play.google.com/store/apps/details?id=com.ctrackaiai.nutrition) · [📖 Product & Engineering Overview](./case-studies/ctrackai-engineering.md)

* **Built and shipped:** A consumer nutrition app available on iOS and Android.
* **Published feature set:** Photo-based food logging, barcode scanning, macro tracking, meal planning, fasting and hydration tracking.
* **Evidence:** Store listings and release history are public. Performance, reliability and cost-reduction figures are omitted until a reproducible measurement report is available.

### Preeo — Cycle & Health Companion
**Cross-Platform Mobile · Cycle Tracking · Health Reports**

[App Store](https://apps.apple.com/in/app/preeo-cycle-period-tracker/id6760804568) · [Google Play](https://play.google.com/store/apps/details?id=com.preeo.health.companion) · [📖 Product & Data Boundary Overview](./case-studies/preeo-architecture.md)

* **Built and shipped:** A consumer cycle-tracking app available on iOS and Android.
* **Published feature set:** Cycle and symptom logging, BBT charts, health integrations and reports for sharing with a healthcare provider.
* **Scope:** An informational wellness product. Store descriptions establish the advertised features, not clinical validation or independently verified security guarantees.

---

## 🌐 Live Demos, Datasets & Portfolio Hub

- **[HEROS AI Systems Portfolio](https://huggingface.co/spaces/itssoumyad/portfolio)** — live index of all ten systems.
- **[HEROS-RL Migration Reward Lab](https://huggingface.co/spaces/itssoumyad/heros-rl)** — browser reward scorer.
- **[Reflexion-SWE Repair Loop](https://huggingface.co/spaces/itssoumyad/reflexion-swe)** — actor/evaluator/reflection trace.
- **[GraphRAG CodeAudit Explorer](https://huggingface.co/spaces/itssoumyad/graphrag-codeaudit)** — local/global query demo.
- **[edgeinfer-v2](https://huggingface.co/spaces/itssoumyad/edgeinfer-v2)** · **[peervault PQC](https://huggingface.co/spaces/itssoumyad/peervault-pqc)** · **[HEROS-Firewall](https://huggingface.co/spaces/itssoumyad/heros-firewall)** — retrieval/PQC/security evidence pages.
- **[PerfBench roofline](https://huggingface.co/spaces/itssoumyad/anthropic-perfbench)** · **[RouteLLM Pareto](https://huggingface.co/spaces/itssoumyad/routellm-gateway)** · **[Mobbin boards](https://huggingface.co/spaces/itssoumyad/mobbin-ui-compiler)** · **[HEROS Cloud PLLB](https://huggingface.co/spaces/itssoumyad/heros-cloud-saas)** — evidence dashboards.
- **[heros-migration-500](https://huggingface.co/datasets/itssoumyad/heros-migration-500)** — 500-case PostgreSQL migration dataset.
- **[graphrag-questions-100](https://huggingface.co/datasets/itssoumyad/graphrag-questions-100)** — 100 sensemaking questions.

Full test counts, headline metrics, and boundaries: **[EVIDENCE.md](./EVIDENCE.md)**. Collection: **[HEROS AI Systems Portfolio](https://huggingface.co/collections/itssoumyad/heros-ai-systems-portfolio-6ae5978d7b5be2d991c1934b)**. Release audit: **[AUDIT.md](./AUDIT.md)**.

These are free **static** Spaces. Hugging Face requires a PRO subscription for Gradio/Docker Spaces on `cpu-basic`, so no GPU/Gradio demo is claimed. Model-weight publication and ZeroGPU demos remain pending.

---

## 🔎 Selected Proof of Work

Public source and CI checked on **31 October 2026**. “Merged” means included in the repository, not deployed to users. Open PRs are labelled Open; green CI is not a deployment claim.

* **LLM platform · llm-control-plane:** Provider-agnostic LLM gateway and evaluation control plane with ordered failover, per-tenant rate limits, cost attribution, PII redaction, SHA-256 hash-chained audit log, versioned eval datasets, deterministic scorers, Prometheus metrics and a FastAPI adapter. **45 tests, 93% coverage**, green CI on Python 3.9/3.11/3.12. [Source](https://github.com/itsoumya-d/llm-control-plane) · [Architecture](https://github.com/itsoumya-d/llm-control-plane/blob/main/docs/ARCHITECTURE.md)
* **Rust/Python spatial systems · Shado / Factory Monitor:** 13-crate Rust 2024 workspace, 434 tests, 7/7 CI jobs, typed spatial contracts, REST/WebSocket APIs, TimescaleDB, and ERP/MES integrations (OPC UA, Modbus, ONVIF). [Source](https://github.com/itsoumya-d/factory-monitor)
* **Queue reliability · FieldLens:** Merged same-runtime serialization, persisted retries and shared create/update/delete dispatch. The [case study](./case-studies/fieldlens-offline-engine.md) links source, regression evidence and remaining delivery limits. Browser recording is a separate draft; a working web app is not yet demonstrated.
* **Reviewable developer tooling · Motion MCP:** A [runnable, credential-free patch walkthrough](https://github.com/itsoumya-d/motion-mcp/blob/9f1787443c959b39866225eecd40d1fe052675d2/examples/patch-review/README.md) demonstrates import inspection, text-anchor insertion, repeatability and guarded no-ops. [Merged PR #2](https://github.com/itsoumya-d/motion-mcp/pull/2) · [Node 22/24 CI](https://github.com/itsoumya-d/motion-mcp/actions/runs/37775446846). Hand-written fixtures; no live AI or semantic code-review claim.
* **Measurement integrity · HostShift:** [Merged PR #2](https://github.com/itsoumya-d/hostshift/pull/2) prevents conflicting artifact overwrites and requires the task's requested contact message. [Python 3.11–3.14 CI](https://github.com/itsoumya-d/hostshift/actions/runs/37782677973) passed at `deee566`. This validates harness behavior, not live-model or native-device benchmark results.
* **Cross-platform tooling · Mobile-Native Design System:** The [token-parity fixture](https://github.com/itsoumya-d/mobile-native-design-system/blob/7b2bb97ebc968e9e52b4dce85b1743f1df658d27/fixtures/token-parity/README.md) detects edited output even after its stored hash is refreshed. [Draft PR #4](https://github.com/itsoumya-d/mobile-native-design-system/pull/4) has passing [core](https://github.com/itsoumya-d/mobile-native-design-system/actions/runs/37786316900), [Android](https://github.com/itsoumya-d/mobile-native-design-system/actions/runs/37786316947) and [Apple](https://github.com/itsoumya-d/mobile-native-design-system/actions/runs/37786317099) checks at `7b2bb97`. Compiler/reference-app fixtures, not physical-device certification.
* **Full-stack maintenance · AutoPilot FDE:** Merged [API error-contract/CI repairs](https://github.com/itsoumya-d/autopilot-fde/pull/2) and a [Next.js dependency security patch](https://github.com/itsoumya-d/autopilot-fde/pull/3). [Backend Python matrix and frontend CI](https://github.com/itsoumya-d/autopilot-fde/actions/runs/37775763497) passed at `45cd4cd`. The workflow-discovery product remains a prototype; no live deployment or comprehensive security audit is claimed.
* **Document extraction evaluation · AutoPilot FDE:** Open [PR #13](https://github.com/itsoumya-d/autopilot-fde/pull/13) adds a provider-agnostic eval harness for schema validity, field accuracy, exact-match rate, p50/p95 latency, and cost per call. [Backend 3.12–3.14 + frontend CI](https://github.com/itsoumya-d/autopilot-fde/actions/runs/40786952085) passed at `bb3f324`. The default fixture proves the harness, not a live model.
* **Media feed ingestion · AutoPilot FDE:** Open [PR #14](https://github.com/itsoumya-d/autopilot-fde/pull/14) adds an RSS 2.0/Atom parser with deduplication, since filtering, and UTC normalization. [Backend 3.12–3.14, frontend and runtime CI](https://github.com/itsoumya-d/autopilot-fde/actions/runs/40793732144) passed at `586d3fd`; 15 tests and 100% module coverage.
* **Payments correctness · go-ledger:** Idempotent payment intents + double-entry ledger service in Go. Replay-safe `Idempotency-Key` handling, 409 conflicts on payload mismatch, capture-once semantics under concurrent requests, insufficient-funds guard, HTTP API and CI (`go test -race`, vet, build). [Source](https://github.com/itsoumya-d/go-ledger) · [Live page](https://itsoumya-d.github.io/go-ledger/)
* **Applied ML · ComplaintGraph:** Frozen DistilBERT embeddings + logistic regression on the public `app_reviews` dataset, **0.690 accuracy / 0.689 macro F1** on 2,880/720 reviews, TF-IDF/KMeans complaint themes with evidence quotes, a FastAPI surface, pytest coverage and a GitHub Actions smoke-training job. The [Intercom Conversations gap report](https://github.com/itsoumya-d/complaintgraph/blob/main/reports/intercom_gap_report.md) analyses 284 public reviews; it is an independent analysis, not an official company document. [Source](https://github.com/itsoumya-d/complaintgraph) · [Live page](https://itsoumya-d.github.io/complaintgraph/)
* **Production .NET integration · Fuel Integration Hub:** Open [PR #3](https://github.com/itsoumya-d/factory-monitor/pull/3) adds a .NET 10 / ASP.NET Core service with 31 tests, HMAC webhooks, idempotency, transactional outbox, reconciliation, and a signed smoke harness. [All 18 checks](https://github.com/itsoumya-d/factory-monitor/pull/3/checks) passed at `bf67c22`; not merged or deployed.

---

## 🤖 Agent Infrastructure & Applied AI Projects

These repositories cover developer tools, research and prototypes. Their linked documentation describes setup and project-specific limitations; they should not be read as evidence of customer deployments.

### 1. [AutoPilot FDE 2.0](https://github.com/itsoumya-d/autopilot-fde) — Workflow Discovery & Agent Prototype
*Python · FastAPI · Next.js · MCP*

* Explores communication ingestion, process graphs, automation scoring and workflow generation.
* Includes local evaluation and simulation tooling, structured invoice extraction with deterministic validation, and a provider-agnostic document-extraction eval harness ([PR #13](https://github.com/itsoumya-d/autopilot-fde/pull/13)). Enterprise deployment, customer adoption and multi-department production performance are not established by the portfolio.
* Agent-first delivery: Claude Code/Codex used with AGENTS.md, test-first prompts and review checkpoints; the eval harness measures schema validity, field accuracy, p50/p95 latency and cost per call.

### 2. [Motion MCP](https://github.com/itsoumya-d/motion-mcp) — Codebase-Aware Motion Tooling
*TypeScript · Model Context Protocol · SceneDoc*

* Scans application structure, represents motion in SceneDoc and stages generated changes for review.
* Explores framework-native motion generation and a skeletal-animation bridge. Test coverage and target-specific support are documented in the repository; support for a target does not imply every generated interaction has been runtime-validated.

### 3. [HEROS](https://github.com/itsoumya-d/HEROS) — Agent-Native Infrastructure & Safety Primitives
*Zero-lang Primitives · Node.js / ESM SDK · MCP-Native Contracts*

* Provides structured agent actions, schema validation, machine-readable errors and auditable receipts.
* Includes the `@heros/agentic` web SDK, `forge` migration-risk tooling and `ledger` accounting-receipt primitives. These controls reduce execution ambiguity; they are not a guarantee against all agent errors.
* **Cross-platform MCP bridge (`packages/mcp`):** one Node process exposes forge + ledger over stdio and Streamable HTTP (MCP 2025-11-25), with HMAC API-key auth, human approval nonces, per-tool rate limits, atomic state writes, and symlink-safe locks. **19 MCP tests** plus the full repo suite pass on macOS, Linux, and Windows CI.

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

### 7. [ComplaintGraph](https://github.com/itsoumya-d/complaintgraph) — Public-Review Complaint Mining
*Hugging Face Transformers · DistilBERT · TF-IDF/KMeans · FastAPI*

* Trains a frozen-encoder DistilBERT + logistic regression baseline on the public `app_reviews` dataset; **0.690 accuracy / 0.689 macro F1** on 2,880 train / 720 eval reviews.
* Clusters negative reviews into themes with top terms and evidence quotes, then generates a Markdown gap report with suggested experiments.
* Includes `/themes` and `/score` FastAPI endpoints, pytest coverage and CI smoke training.
* [Independent Intercom Conversations report](https://github.com/itsoumya-d/complaintgraph/blob/main/reports/intercom_gap_report.md) — 284 public reviews, five complaint themes; not an official company document.
* [Live portfolio page](https://itsoumya-d.github.io/complaintgraph/) — the report, themes and evidence in one place.

---

### 8. [HEROS-RL](https://github.com/itsoumya-d/HEROS-RL) — Critic-Free GRPO for Migration Safety
*Python · PyTorch · TRL / Unsloth · PostgreSQL · GRPO*

* Implements critic-free Group Relative Policy Optimization for rewriting hazardous PostgreSQL migrations as expand-and-contract plans, with a deterministic format reward, a SQL safety audit, and an optional forge risk gate.
* Ships a reproducible **500-case** migration dataset, Pass@1 / cons@64 evaluators, and TRL + Unsloth training scripts for `DeepSeek-R1-Distill-Qwen-1.5B`.
* **33 unit tests** pass; a 5-seed toy ablation shows `G=1` has zero advantage (no learning) while `G=4/8/16/32` solve the validation task. The 1.5B GPU runs are explicitly pending, not claimed.
* [Live reward lab](https://huggingface.co/spaces/itssoumyad/heros-rl) · [Dataset](https://huggingface.co/datasets/itssoumyad/heros-migration-500)

---

### 9. [Reflexion-SWE](https://github.com/itsoumya-d/Reflexion-SWE) — Verbal Reflexion & Training-Free GRPO
*Python · Actor/Evaluator/Self-Reflection · AST-filtered tests · sandboxed execution · verbal priors*

* Implements the three Reflexion models with a bounded episodic memory (Ω=3), generates up to six AST/syntax-filtered tests per issue, and executes them in an isolated Python/Rust sandbox (optional Docker network isolation).
* Adds training-free group-relative prior distillation: sample a group of trajectories, normalise rewards, and write successful/failed contrasts into a weighted natural-language prior bank — no model weights change.
* **40 unit tests** pass, including sandbox timeouts, Rust execution, Reflexion vs. no-reflection controls, and TF-GRPO prior guidance. The measured toy mechanism ablation is `base 0.00 / -TestGen 0.00 / -Reflection 0.00 / full 1.00 / +TF-GRPO 1.00`; HumanEval Rust and SWE-bench Lite model runs are explicitly pending, not claimed.
* [Live repair-loop demo](https://huggingface.co/spaces/itssoumyad/reflexion-swe)

---

### 10. [GraphRAG-CodeAudit](https://github.com/itsoumya-d/GraphRAG-CodeAudit) — Local-to-Global GraphRAG for Code Audits
*Python · AST extraction · weighted knowledge graph · Louvain/Leiden · local + global retrieval · deterministic judge*

* Extracts entities, typed edges, and security/privacy claims from a repository, builds a weighted knowledge graph, partitions it into hierarchical communities, and generates bottom-up community reports with risks, dependencies, and recommended actions.
* Implements local entity-neighbourhood search and global map-reduce community search, plus a flat hashed-embedding RAG baseline sharing the same text units.
* **15 tests** pass; 100 synthetic sensemaking questions scored by a deterministic rubric: GraphRAG **7.58** vs flat RAG **7.07**, winning **64/100** (empowerment 4.01 vs 2.28, directness 7.72 vs 7.40). This is a reproducible harness result, not the paper's LLM-judge replication; Oracle/HF 3D explorer and real Leiden are explicitly not deployed.
* [Live explorer](https://huggingface.co/spaces/itssoumyad/graphrag-codeaudit) · [Questions dataset](https://huggingface.co/datasets/itssoumyad/graphrag-questions-100)

---

### 11. [Anthropic-PerfBench](https://github.com/itsoumya-d/Anthropic-PerfBench) — AI-Resistant Kernel Optimization
*C · ARMv8.2-A NEON · WebGPU WGSL · roofline analysis*

* Three transformer kernels — fused RMSNorm+residual, fused in-place RoPE, and group-wise INT4 dequant+GEMV — each in three iterations: scalar baseline, unrolled/blocked, then NEON `float32x4_t`/WGSL vectorization.
* Correctness tests compare every iteration against the scalar reference. Measured Apple Silicon speedups: RMSNorm **3.09×**, RoPE **2.35×**, INT4 GEMV **11.83×** over scalar; copy bandwidth 66.31 GB/s; roofline CSV/SVG committed.
* WGSL sources and a WebGPU harness are included but were not executed; OCI Ampere `perf stat` is scripted, not claimed. Memory-roof caveats (cache-resident RoPE, instruction-bound GEMV) are documented.
* [Live roofline](https://huggingface.co/spaces/itssoumyad/anthropic-perfbench)

---

### 12. [HEROS-Firewall](https://github.com/itsoumya-d/HEROS-Firewall) — MCP Agentic Security Proxy
*Node.js · MCP stdio · OWASP ASI01–ASI10 · HMAC approvals · Merkle receipts · red team*

* Inline MCP proxy that evaluates every `tools/call` against deterministic ASI01–ASI10 policies, blocks tool misuse, scope abuse, exfiltration chains, memory poisoning, and resource exhaustion, and forwards allowed calls downstream.
* Destructive/high-cost calls require an HMAC-signed, expiring, single-use human approval bound to the exact tool+argument hash. Every decision emits a hash-chained receipt with a Merkle root and inclusion proof; idempotency returns cached responses.
* **16 tests** pass. Red team: **1,000 adversarial payloads, 200 benign**, FNR **0.0000**, FPR **0.0000**, p99 policy latency **0.103 ms**. The React/SSE dashboard and OCI k3s deployment are explicitly not built; Mobbin/cloud access was unavailable.
* [Live evidence page](https://huggingface.co/spaces/itssoumyad/heros-firewall)

---

### 13. [RouteLLM-Gateway](https://github.com/itsoumya-d/RouteLLM-Gateway) — Calibrated Cost-Latency-Quality Router
*Node.js · Bradley–Terry routing · semantic cache · OpenAI/Anthropic SSE · Pareto harness*

* Routes each prompt between a fast and a frontier model using a trained Bradley–Terry `σ(θᵀφ(q))` router, with a semantic cache (cosine ≥0.94 + numeric guard), JSON-schema fallback to the frontier model, and drift diagnostics.
* Exposes OpenAI-compatible `/v1/chat/completions` (streaming) and Anthropic-compatible `/v1/messages`, with routing/cost/cache metadata.
* **12 tests** pass. Synthetic 250-question harness: **98.38% accuracy retention** of always-frontier with **69.40% cost reduction** (threshold 0.74; router+cache 97.20% vs 98.80%). This is mock-provider evidence, not an MMLU-Pro/GSM8K run.
* [Live Pareto page](https://huggingface.co/spaces/itssoumyad/routellm-gateway)

---

### 14. [HEROS-Cloud-SaaS](https://github.com/itsoumya-d/HEROS-Cloud-SaaS) — PLLB Governance Studio
*Python · Policy Learning with a Language Bottleneck · workflow receipts · approval policy · API*

* Composes the HEROS workflow studio around a human-readable policy bottleneck: execute a batch, synthesise explicit risk rules from failures, require human approval, then run the next episode under those rules. No model weights are updated.
* Emits per-step SHA-256 receipts with a Merkle root for every workflow; exposes execution, policy, approval, pricing, and evaluation endpoints.
* **6 tests** pass. 50-workflow simulation: completion **70% → 100%** on held-out workflows after 4 approved PLLB rules (+30 points), 100% receipt coverage. Voice/audio, Mobbin UI, OCI/Oracle, billing, and the $200k ARR claim are explicitly not deployed.
* [Live evidence page](https://huggingface.co/spaces/itssoumyad/heros-cloud-saas)

---

### 15. [Mobbin-UI-Compiler](https://github.com/itsoumya-d/Mobbin-UI-Compiler) — Reference-Driven UI Compiler
*Node.js · Mobbin search_screens contract · React 19/TS/Tailwind source generation · accessibility invariants*

* Compiles PRD/surface intents into five production-shaped SaaS surfaces: KYC stepper, tiered paywall, keyboard-first dashboard, agentic chat with citation drill-through, and usage-billing ledger.
* Queries a Mobbin `search_screens`-style adapter, extracts layout tokens/microcopy, writes local reference boards, and emits React/TS/Tailwind component source with focus-visible, 44px targets, ARIA labels, and reduced-motion rules.
* **10 tests** pass; all five surfaces compile to components, tokens, and boards. The live Mobbin MCP was unavailable, so a clearly labelled fixture adapter is used; Playwright/axe/Lighthouse and hosting are explicitly not claimed.
* [Live reference boards](https://huggingface.co/spaces/itssoumyad/mobbin-ui-compiler)

---

### 16. [go-ledger](https://github.com/itsoumya-d/go-ledger) — Idempotent Payments & Double-Entry Ledger
*Go · HTTP · concurrency · ledger invariants*

* Idempotent `POST /v1/payment_intents`: the same key and payload returns the original intent; the same key with a different payload returns `409`.
* Capture writes a double-entry pair that sums to zero, and concurrent captures produce exactly one posting pair.
* Insufficient-funds capture leaves balances and postings untouched.
* `go test -race`, `go vet` and `go build` run in CI. A reference implementation, not a production payment system.
* [Live page](https://itsoumya-d.github.io/go-ledger/) — invariants, API and honest limits.

---

## 🧪 Browser-Native Infrastructure Suite (Edge Prototypes)
*TypeScript · Go · WebRTC · WASM · WebGPU · WebCrypto · CRDTs*

An experimental suite exploring client-side P2P systems and distributed edge execution:

* **Seeded testing:** [SyncForge's property and regression tests](https://github.com/itsoumya-d/syncforge/blob/b08435c22b35fffebb1afa99b3a697e92e481cde/tests/crdt-properties.test.mjs) exercise merge laws and replica delivery scenarios. This is bounded test coverage, not proof of convergence under every network or failure condition.
* **Post-quantum P2P transport:** [PeerVault](https://github.com/itsoumya-d/peervault) now runs a hybrid **ML-KEM-768 + P-256** handshake from a from-scratch Rust/wasm core, binds the full 21-byte frame header as AES-GCM AAD, and passes **100/100 NIST KAT vectors**, Node/OpenSSL interop, and **75 tests**. It also ships a versioned `MeshNode` for syncing edgeinfer vectors and Reflexion memories over encrypted DataChannel control messages (local AES-GCM throughput ~1.4 GB/s encrypt / ~1.0 GB/s decrypt).
* [Live evidence page](https://huggingface.co/spaces/itssoumyad/peervault-pqc)
* **Edge inference:** [EdgeInfer](https://github.com/itsoumya-d/edgeinfer) v2 is MIT-licensed with auto int64 ONNX casting, a two-stage Matryoshka RAG index (INT8 d=64 scan → FP32 d=768 re-rank, IndexedDB persistence), and gamma=5 speculative decoding with residual resampling and cache-aware truncation. **95 tests** pass. Synthetic 100k-chunk benchmark: p50 25.1 ms coarse+re-rank, Recall@10 0.725 → 1.000 across d=64→768; mock speculative acceptance 68.4% at 0.45 target calls/token. These are synthetic/mock results, not MTEB or WebGPU measurements.
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
| **Applied AI & Agents** | LangGraph, Model Context Protocol (MCP), Gemini, Claude, OpenAI, Tool Calling, Structured Outputs, Document Extraction, Retrieval, Evals, Hugging Face Transformers, DistilBERT, TF-IDF/KMeans |
| **Payments & Go** | Go, idempotency keys, double-entry ledgers, capture-once semantics, concurrency tests, HTTP APIs |
| **Full-Stack & Real-Time** | TypeScript, Next.js, React, Python (FastAPI), Node.js, REST APIs, Server-Sent Events, WebSockets, PostgreSQL, Supabase, Redis |
| **Mobile Engineering** | Flutter, Dart, React Native, Expo, HealthKit, Health Connect, App Store Connect, Play Console |
| **.NET & Enterprise Integration** | C#, .NET 10, ASP.NET Core Minimal APIs, EF Core 10, SQL Server/T-SQL, SQLite, REST APIs, webhooks, HMAC, idempotency, transactional outbox, xUnit |
| **Development & Delivery** | Docker, GitHub Actions CI/CD, Azure Container Apps, Bicep, Linux, Git, Testing, Threat Modeling |

---

## 📬 Connect

* **Email:** [soumyadebnath1619@gmail.com](mailto:soumyadebnath1619@gmail.com)
* **LinkedIn:** [linkedin.com/in/soumya-debnath-83a68a237](https://www.linkedin.com/in/soumya-debnath-83a68a237/)
* **GitHub:** [github.com/itsoumya-d](https://github.com/itsoumya-d)

### Verified credentials

* **Anthropic Building with the Claude API** — [verify](https://academy.claude.com/badges/f1de3ec2-3d44-48a9-a1fe-3d05f9f1122a) — credential `f1de3ec2-3d44-48a9-a1fe-3d05f9f1122a`
* **HackerRank SQL (Intermediate)** — [verify](https://www.hackerrank.com/certificates/c5a80e6adda0) — credential `c5a80e6adda0`
* **Anthropic Claude Code in Action** — [verify](https://academy.claude.com/badges/fd1a399f-5fe9-4635-977c-440cab5eb62c) — credential `fd1a399f-5fe9-4635-977c-440cab5eb62c`
* **Anthropic Model Context Protocol: Advanced Topics** — [verify](https://academy.claude.com/badges/2cc5045b-85c1-43cd-aeb8-e0ea7f3dac59) — credential `2cc5045b-85c1-43cd-aeb8-e0ea7f3dac59`
* **Anthropic Teaching AI Fluency** — [verify](https://academy.claude.com/badges/236d54cb-6398-4302-8726-f037c92a3e51) — credential `236d54cb-6398-4302-8726-f037c92a3e51`
