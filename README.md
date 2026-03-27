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

## 🛰️ Air-Gapped Deployment Guide (Pop!_OS Server)

Follow these steps when deploying in a highly restricted network without internet access.

### Phase 1: Preparation (Machine with Internet)
1. **Download NVIDIA Quadro Drivers:**
   - Go to NVIDIA's website and download the `.run` file for your specific Quadro card (Linux 64-bit).
2. **Download Docker and NVIDIA Toolkit Packages:**
   - Download the `.deb` files for `docker.io`, `docker-compose`, and `nvidia-container-toolkit`.
3. **Export Sapo AI Engine (llama.cpp CUDA):**
   - Pull the image: `docker pull ghcr.io/ggerganov/llama.cpp:server-cuda`
   - Save to disk: `docker save ghcr.io/ggerganov/llama.cpp:server-cuda > llama_cuda.tar`
4. **Copy all assets to a USB Drive:**
   - Your Sapo AI repository.
   - The `.run` driver.
   - The `.deb` bundles.
   - The `llama_cuda.tar` image.
   - Your `.gguf` model files.

### Phase 2: Server Installation (Offline)
1. **Install NVIDIA Drivers:**
   - `sudo systemctl stop gdm3` (Stops the UI).
   - `sudo sh ./NVIDIA-Linux-x86_64-XXX.XX.run`
   - Follow prompts, then `sudo reboot`.
2. **Install Docker & Toolkit:**
   - `sudo dpkg -i *.deb` (from your deb folder).
   - `sudo nvidia-ctk runtime configure --runtime=docker`
   - `sudo systemctl restart docker`
3. **Import Engine Image:**
   - `docker load -i llama_cuda.tar`

### Phase 3: Launch
1. **Start Infrastructure:** `cd infra && docker-compose up -d`
2. **Start Inference Engine:**
   - Instead of local python script, use the pre-loaded Docker image:
   ```bash
   docker run -d --name sapo-engine --gpus all -p 8080:8080 -v /path/to/models:/models ghcr.io/ggerganov/llama.cpp:server-cuda -m /models/Llama-3.1-8B-Instruct-Q5_K_M.gguf --port 8080 --host 0.0.0.0 --n-gpu-layers 99
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
