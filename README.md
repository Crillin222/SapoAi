# Sapo AI - Private & Agentic AI Infrastructure

Sapo AI is a high-performance, private, and offline-first AI ecosystem designed for restricted corporate environments. It serves as a unified **AI Gateway**, providing an OpenAI-compatible API for internal teams while ensuring absolute data sovereignty.

---

## 🚀 Key Features

- **Unified AI Gateway:** A single endpoint for multiple local LLM backends (llama.cpp, vLLM, Ollama).
- **Maestro Architecture:** A "Maestro" model (Reasoning-focused) routes inquiries and delegates complex tasks to specialized workers (Coding/Logic-focused).
- **Enterprise Governance:** API Key management and token tracking powered by LiteLLM and Redis.
- **Offline-First Resilience:** Architecture optimized for air-gapped networks with support for manual model transfers and offline dependency management.
- **Heterogeneous Hardware Support:** Adaptive inference supporting GPU Acceleration (CUDA) or high-performance CPU/Hybrid modes.

---

## 🏗️ Architecture

The system operates in three distinct layers:
1. **Inference Layer:** Multiple inference engine instances (e.g., llama.cpp) running quantized GGUF models.
2. **Gateway Layer:** LiteLLM Proxy acting as a central router, authenticator, and request translator.
3. **Client Layer:** Integration with industry-standard tools like VS Code (Continue), Aider, and Open WebUI.

---

## 🛰️ Air-Gapped Deployment (Generic Linux)

This section covers the standard procedure for deploying Sapo AI in environments without active internet connections.

### Phase 1: Preparation (Connected Environment)
1. **Model Acquisition:** Download required `.gguf` models (e.g., Llama 3.1, Qwen 2.5) from trusted sources like Hugging Face or ModelScope.
2. **Container Sideloading:**
   - Pull the required inference engine image: `docker pull ghcr.io/ggerganov/llama.cpp:server-cuda`
   - Export the image to a portable archive: `docker save ghcr.io/ggerganov/llama.cpp:server-cuda > llama_cuda.tar`
3. **Dependency Bundling:** Collect necessary `.deb` packages for Docker, Docker Compose, and the NVIDIA Container Toolkit for the target OS version.

### Phase 2: Implementation (Target Environment)
1. **Driver Installation:** Ensure compatible NVIDIA drivers are installed using the official `.run` installer if repository access is unavailable.
2. **Service Initialization:**
   - Install Docker components: `sudo dpkg -i *.deb`
   - Load the engine image: `docker load -i llama_cuda.tar`
   - Start the gateway infrastructure: `cd infra && docker-compose up -d`
3. **Engine Launch:** Deploy the inference engine container:
   ```bash
   docker run -d --name sapo-engine --gpus all -p 8080:8080 -v /path/to/models:/models ghcr.io/ggerganov/llama.cpp:server-cuda -m /models/your-model.gguf --port 8080 --host 0.0.0.0 --n-gpu-layers 99
   ```

---

## 🛠️ Troubleshooting & Workarounds

### Restricted Network Issues
- **Problem:** Standard package managers (`apt`, `pip`) fail due to firewall restrictions.
- **Workaround:** Utilize the **Offline Sideloading** method described above. Pre-package all binaries and container images in a connected environment before transferring them via secure physical media.

### GPU Detection in Containers
- **Problem:** Docker containers fail to recognize the host GPU even with drivers installed.
- **Workaround:** Verify the installation of the **NVIDIA Container Toolkit**. Execute `nvidia-smi` inside a test container (`docker run --rm --gpus all nvidia/cuda:12.0-base-ubuntu22.04 nvidia-smi`) to confirm the passthrough is functional.

### Binary Compatibility
- **Problem:** Pre-compiled binaries fail due to missing shared libraries or GLIBC version mismatches.
- **Workaround:** Use **Docker-based Inference Engines**. Containers encapsulate the entire runtime environment, ensuring consistency across different Linux distributions regardless of the host's library versions.

---

## 📝 Implementation Note: Pop!_OS & NVIDIA Quadro
During initial prototyping, the system was validated on **Pop!_OS** using **NVIDIA Quadro** series hardware. 
- **Drivers:** Professional Quadro cards often require the stable branch of NVIDIA drivers. In air-gapped scenarios, the official `.run` installer is recommended over distribution-specific tools if the latter require internet-based dependency resolution.
- **OS Choice:** Pop!_OS provides an excellent base for AI workloads due to its native NVIDIA support and optimized kernel, though the standard ISO may require manual driver injection for certain legacy or specialized Quadro hardware.

---

## 💻 Client Configuration
*Follow standard OpenAI API integration for tools like Continue, Aider, and Open WebUI.*
