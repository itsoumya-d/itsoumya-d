# Engineering Evidence Matrix

Public source, measured local evidence, and live static demos. "Boundary" states
what is **not** claimed. Last updated 2026-10-31.

**Portfolio hub:** https://huggingface.co/spaces/itssoumyad/portfolio  
**HF Collection:** https://huggingface.co/collections/itssoumyad/heros-ai-systems-portfolio-6ae5978d7b5be2d991c1934b

| Project | Source | Live demo | Tests | Headline evidence | Boundary |
|---|---|---|---|---|---|
| HEROS-RL | [GitHub](https://github.com/itsoumya-d/HEROS-RL) | [Space](https://huggingface.co/spaces/itssoumyad/heros-rl) · [Dataset](https://huggingface.co/datasets/itssoumyad/heros-migration-500) | 33 | Toy GRPO: G=1 no learning, G=4–32 solve; 500-case dataset | 1.5B GPU run pending |
| Reflexion-SWE | [GitHub](https://github.com/itsoumya-d/Reflexion-SWE) | [Space](https://huggingface.co/spaces/itssoumyad/reflexion-swe) | 40 | Toy ablation base 0.00 → full 1.00; 6 priors from 24 rollouts | HumanEval Rust/SWE-bench model runs pending |
| edgeinfer v2 | [GitHub](https://github.com/itsoumya-d/edgeinfer) | [Space](https://huggingface.co/spaces/itssoumyad/edgeinfer-v2) | 95 | 100k chunks p50 25.1 ms; Recall@10 0.725→1.000 | Synthetic, not MTEB/WebGPU |
| peervault | [GitHub](https://github.com/itsoumya-d/peervault) | [Space](https://huggingface.co/spaces/itssoumyad/peervault-pqc) | 75 | 100/100 ML-KEM KAT; handshake p50 0.836 ms; 1395 MB/s local encrypt | No live WebRTC network throughput |
| GraphRAG-CodeAudit | [GitHub](https://github.com/itsoumya-d/GraphRAG-CodeAudit) | [Space](https://huggingface.co/spaces/itssoumyad/graphrag-codeaudit) · [Dataset](https://huggingface.co/datasets/itssoumyad/graphrag-questions-100) | 15 | 7.58 vs 7.07; 64/100 wins | Synthetic repo + deterministic judge |
| Anthropic-PerfBench | [GitHub](https://github.com/itsoumya-d/Anthropic-PerfBench) | [Space](https://huggingface.co/spaces/itssoumyad/anthropic-perfbench) | pass | NEON 3.09× / 2.35× / 11.83× | OCI perf/WebGPU timings pending |
| Mobbin-UI-Compiler | [GitHub](https://github.com/itsoumya-d/Mobbin-UI-Compiler) | [Space](https://huggingface.co/spaces/itssoumyad/mobbin-ui-compiler) | 10 | 5 surfaces + boards | Fixture Mobbin; no browser audit |
| HEROS-Firewall | [GitHub](https://github.com/itsoumya-d/HEROS-Firewall) | [Space](https://huggingface.co/spaces/itssoumyad/heros-firewall) | 16 | 1000 adv/200 benign; FNR 0, FPR 0; p99 0.103 ms | Policy-layer only; no UI/OCI e2e |
| RouteLLM-Gateway | [GitHub](https://github.com/itsoumya-d/RouteLLM-Gateway) | [Space](https://huggingface.co/spaces/itssoumyad/routellm-gateway) | 12 | 98.38% retention; 69.40% cost reduction | Synthetic mocks; no MMLU/GSM8K |
| HEROS-Cloud-SaaS | [GitHub](https://github.com/itsoumya-d/HEROS-Cloud-SaaS) | [Space](https://huggingface.co/spaces/itssoumyad/heros-cloud-saas) | 6 | 70% → 100% completion; 4 PLLB rules | Simulation; no voice/UI/cloud/ARR |

## Selected arXiv references

- 2402.03300 — DeepSeekMath / GRPO
- 2501.12948 — DeepSeek-R1
- 2303.11366 — Reflexion
- 2510.08191 — Training-Free GRPO
- 2310.06770 — SWE-bench
- 2205.13147 — Matryoshka Representation Learning
- 2211.17192 — Speculative Decoding
- 2404.16130 — GraphRAG local-to-global
- 2307.08691 — FlashAttention-2
- 2406.18665 — RouteLLM
- 2305.05176 — FrugalGPT

## Honest boundaries

- No model weights were published; no GPU training run was executed.
- Hugging Face demos are static because Gradio/Docker Spaces require PRO.
- No customer, deployment, billing, or ARR claims.
- Local benchmark harnesses are reproducible; model-dependent results remain pending.
