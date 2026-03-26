# Sapo AI - Private & Agentic AI Infrastructure

Sapo AI is a high-performance, private, and offline-first AI ecosystem designed for restricted corporate environments. It serves as a unified **AI Gateway**, providing an OpenAI-compatible API for internal teams while ensuring absolute data sovereignty.

---

## 🚀 Key Features

- **Unified AI Gateway:** A single endpoint for multiple local LLM backends (llama.cpp, vLLM, Ollama).
- **Maestro Architecture:** A "Brain" (Llama 3.1) routes general inquiries and delegates complex tasks to specialized workers (Qwen 2.5 Coder).
- **Enterprise Governance:** API Key management and token tracking powered by LiteLLM and Redis.
- **Offline First:** Designed for air-gapped networks with support for manual model transfers and offline dependency management.
- **Optimized for CPU/GPU:** Adaptive inference supporting Full GPU Offloading or High-Performance CPU/Hybrid modes.

---

## 🏗️ Architecture

The system operates in three distinct layers:
1. **Inference Layer:** Multiple `llama-server` instances running quantized GGUF models.
2. **Gateway Layer:** LiteLLM Proxy acting as a router, authenticator, and request translator.
3. **Client Layer:** Industry-standard tools like VS Code (Continue), Aider, and Open WebUI.

---

## 🐧 Setup Guide: Pop!_OS (Production Server)

This guide assumes a dedicated server running **Pop!_OS** with an NVIDIA GPU (e.g., 6GB VRAM).

### 1. OS & Driver Preparation
Pop!_OS comes with NVIDIA drivers out of the box. Ensure they are up to date:
```bash
sudo apt update && sudo apt full-upgrade -y
```

### 2. Install Docker & NVIDIA Container Toolkit
```bash
# Install Docker
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER

# Install NVIDIA Toolkit for Docker
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
# (Follow official NVIDIA instructions to add the repo and install)
sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

### 3. Engine Setup (llama.cpp)
1. Download the latest Linux `llama.cpp` binaries to the `engines/` directory.
2. Ensure the binary is executable: `chmod +x engines/llama-server`.

### 4. Deploy Sapo AI
1. **Clone & Configuration:**
   - Clone this repository.
   - Place your `.gguf` models in the `models/` directory.
2. **Launch the Gateway:**
   ```bash
   cd infra
   docker-compose up -d
   ```
3. **Start the Engines:**
   ```bash
   python3 scripts/start_engines.py
   ```

---

## 💻 Client Configuration

### VS Code (Continue Extension)
Add the following to your `config.json`:
```json
{
  "models": [
    {
      "title": "Sapo Maestro",
      "model": "sapo-maestro",
      "apiBase": "http://<SERVER_IP>:4000/v1",
      "apiKey": "sk-sapo-123",
      "provider": "openai"
    },
    {
      "title": "Sapo Coder",
      "model": "sapo-code",
      "apiBase": "http://<SERVER_IP>:4000/v1",
      "apiKey": "sk-sapo-123",
      "provider": "openai"
    }
  ]
}
```

### Aider (CLI)
Run Aider pointing to the Sapo Gateway:
```bash
aider --openai-api-base http://<SERVER_IP>:4000/v1 --openai-api-key sk-sapo-123 --model sapo-code
```

---

## 📁 Project Structure

- `app/`: Custom CLI and diagnostic tools.
- `infra/`: Gateway configuration and Docker orchestration.
- `models/`: Model storage (.gguf).
- `engines/`: Inference engine binaries (llama-server).
- `scripts/`: Automation and setup scripts.
- `RESEARCH.md`: Technical benchmarks and architectural decisions.

---
*Developed for high-security laboratory environments. Ensure compliance with internal IT policies.*
