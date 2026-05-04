# 🐳 The SGLang Docker-Agent Pattern

This repository is a canonical template for building fast, local, GPU-accelerated AI agents. It utilizes a disaggregated architecture, separating the heavy tensor computations from the lightweight agentic control flow.

## 🏗️ Infrastructure Stack

This project is built on the cutting edge of local AI infrastructure:

1. **NVIDIA Container Toolkit:** Bridges a bare GPU (RTX 4060) into the Docker runtime, allowing isolated containers to execute native CUDA kernels.
2. **SGLang (LMSYS):** The state-of-the-art inference backend designed specifically for complex language model programs. 
    * *Why SGLang?* Based on the paper *"SGLang: Efficient Execution of Structured Language Model Programs"*, SGLang introduces **RadixAttention**. Unlike standard engines that discard KV caches, SGLang uses a Radix Tree to automatically detect shared prefixes in prompts. Because AI agents reuse heavy system prompts constantly, this achieves near zero-overhead prefilling and up to 6x faster throughput.
    * It also utilizes **Compressed Finite State Machines (FSM)** for lightning-fast, guaranteed structured JSON generation for agent tool-calling.

---

## 📂 Project Structure

```text
docker-agent/
├── docker-compose.yml     # The architecture orchestrator
├── Dockerfile             # The lightweight agent environment
├── pyproject.toml         # uv dependencies
└── agent.py               # Python agent logic