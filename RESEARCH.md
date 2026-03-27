# Sapo AI - Pesquisa Técnica e Referências (RESEARCH)

## ☁️ Sapo AI Cloud (Provedor de IA Universal)
A visão mudou de um simples servidor para uma **Infraestrutura de IA Privada** compatível com qualquer aplicação do mercado.

### 1. Gateway de Governança (O Cérebro da Rede)
- **Ferramenta Principal:** **LiteLLM** (ou Bifrost para alta performance).
- **Funções Críticas:**
    - **Chaves Virtuais (API Keys):** Gestão individual de acesso, limites de tokens e auditoria de uso por usuário.
    - **Semantic Routing:** O servidor identifica a tarefa (ex: Coding vs Chat) e roteia automaticamente para o modelo mais capaz disponível.
    - **Fallback Automático:** Se um modelo estiver sobrecarregado ou falhar, o gateway redireciona para um modelo secundário de forma transparente para o usuário.

### 2. Camada de Inferência (Os Motores)
- **vLLM:** Motor principal para o servidor Pop!_OS (GPU). Focado em atender múltiplos usuários simultaneamente com baixa latência.
- **llama.cpp:** Motor de contingência ou para execução local em CPU (notebooks).

### 3. Compatibilidade e Consumo
- **OpenAI Compatible API:** O servidor expõe o padrão `/v1/chat/completions`.
- **Clientes Suportados:** Aider, Continue (VS Code), Open WebUI, LibreChat, scripts Python, e qualquer ferramenta que aceite o padrão OpenAI.

### 2. Camada de Gateway (LiteLLM)
- **Papel:** Unificar APIs e gerenciar chaves de acesso.
- **Configuração:** Deve rodar na porta 4000, oferecendo endpoints OpenAI-Compatible para toda a rede.
- **Benefício:** Permite trocar o backend (Ollama -> llama.cpp) sem alterar a configuração dos clientes (VS Code, WebUI).

### 3. Camada de Interface (O Front-end)
- **VS Code + Continue:** Integração profunda com o fluxo de trabalho de desenvolvimento.
- **Open WebUI:** Interface principal para usuários não-técnicos. Suporte nativo a RAG (Retrieval Augmented Generation) e gerenciamento de documentos.
- **Sapo CLI:** Ferramenta de diagnóstico e automação rápida via terminal.

## 🛰️ Air-Gapped Deployment Strategy
Lessons learned from deploying in high-security, no-internet environments (Pop!_OS + NVIDIA Quadro):

### 1. NVIDIA Driver Sideloading (The .run Method)
- **Challenge:** NVIDIA Quadro cards in professional workstations often require specific stable drivers not found in standard "Gaming" ISOs.
- **Solution:** Use the **Official NVIDIA .run installer**.
- **Pre-requisite:** Disable the `nouveau` driver and stop the display manager (`gdm` or `gdm3`) before installation.

### 2. Pre-built Engine (The Docker Sideloading Method)
- **Challenge:** Compiling `llama.cpp` with CUDA support requires a complex toolchain (GCC, CMake, CUDA Toolkit) that is difficult to replicate offline.
- **Solution:** **Docker Save/Load**.
- **Benefit:** Docker containers bundle the exact OS, CUDA version, and pre-compiled binaries, ensuring "write once, run anywhere" performance on the server.

### 3. Dependency Management (The .deb Bundle)
- **Requirement:** The `nvidia-container-toolkit` is the bridge between Docker and the GPU. It must be downloaded as a bundle of `.deb` packages for the specific Pop!_OS version.
- **Critical:** Required for Docker to access GPU resources. Must be manually downloaded as a bundle of `.deb` packages for the specific Ubuntu/Pop!_OS version.

## 🧠 Model Strategy: The Maestro Pattern
To ensure Sapo AI is a versatile generalist assistant, we employ a delegation architecture:

1. **The Maestro (General Reasoning & Routing):** 
   - **Model:** **Llama-3.1-8B-Instruct**. 
   - **Role:** The primary interface. It handles intent classification, reasoning, and determines if a specialist worker is needed for specific tasks (recipes, jokes, code).
2. **The Specialists (Task Workers):**
   - **Qwen2.5-7B-Instruct:** For creative writing, fast chat, and general knowledge.
   - **Qwen2.5-Coder-7B-Instruct:** For technical logic, automation scripts, and structured data tasks.

## 🧠 Anti-Hallucination Strategies (Grounding)
1. **Low Temperature System Prompts:** Set `temperature: 0.0` for technical/deterministic tasks.
2. **Local RAG:** Use tools like **Docling** for document ingestion and **Qdrant** (or Open WebUI's native RAG) to provide real-world context.
3. **Chain of Thought (CoT):** Instruct the model (via System Prompt) to "think step-by-step" before providing the final answer.

## 🛠️ Complementary Tools
- **n8n (Self-hosted):** For visual agentic automation flows.
- **Claude Code / OpenCode:** For terminal command execution and automatic file editing.

## 📍 Lessons Learned & Technical Benchmarks
- **Model Size:** Do not use models < 7B for complex reasoning; they hallucinate logic patterns.
- **Task Separation:** Separate autocomplete from chat. Use ultra-light models (1.5B) for real-time text prediction to save CPU.
- **Quantization:** Q4_K_M is the "sweet spot" between intelligence and memory usage.
