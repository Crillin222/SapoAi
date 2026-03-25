# Sapo AI - Private & Agentic AI Infrastructure

Sapo AI is a high-performance, private, and offline-first AI ecosystem designed for restricted corporate environments. It serves as a unified **AI Gateway**, providing an OpenAI-compatible API for internal teams while ensuring absolute data sovereignty.

## 🚀 Key Features

- **Unified AI Gateway:** A single endpoint for multiple local LLM backends (llama.cpp, vLLM, Ollama).
- **Enterprise Governance:** API Key management and token tracking powered by LiteLLM and Redis.
- **Agentic Ready:** Optimized for coding agents (Aider, Continue, OpenCode) with specialized models for Chat and Code.
- **Offline First:** Designed for air-gapped networks with support for manual model transfers and offline dependency management.
- **Hardware Agnostic:** Flexible inference supporting GPU (vLLM/Pop!_OS) or high-performance CPU/Hybrid modes (llama.cpp).

## 🏗️ Architecture

The system consists of three main layers:
1. **Inference Engine:** High-fidelity backends (llama.cpp/vLLM) running quantized GGUF/EXL2 models.
2. **Gateway (The Brain):** LiteLLM Proxy acting as a router, authenticator, and parameter translator.
3. **Consumption Layer:** Integration with VS Code (Continue), CLI tools (Aider), and WebUIs.

## 🛠️ Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.10+
- Local LLM engine (e.g., llama.cpp server running on port 8080)

### Setup
1. **Launch the Gateway:**
   ```bash
   cd infra
   docker compose up -d
   ```

2. **Verify Connectivity:**
   ```bash
   python app/main.py check
   ```

3. **Connect your Tools:**
   Point any OpenAI-compatible tool to `http://<your-server-ip>:4000/v1` using your `MASTER_KEY`.

## 📁 Project Structure

- `app/`: Custom CLI and diagnostic tools.
- `infra/`: Gateway configuration and Docker orchestration.
- `models/`: Model registration files (Modelfiles).
- `scripts/`: Offline setup and automation scripts.
- `RESEARCH.md`: Technical benchmarks and architectural decisions.

## 🧠 Model Strategy
- **sapo-chat:** Focused on reasoning and general assistance (e.g., Llama 3.1 8B/70B).
- **sapo-code:** Optimized for deterministic code generation (e.g., Qwen 2.5 Coder 7B/32B).

---
*Developed for high-security laboratory environments.*
