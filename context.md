# Sapo AI - Contexto do Projeto (Master)

## 🎯 Objetivo
Prover um ecossistema de IA **Agêntico**, privado, seguro e totalmente offline. O Sapo AI não é apenas um chat, mas um assistente capaz de interpretar problemas, propor soluções e executar tarefas (via ferramentas integradas), garantindo a soberania dos dados em ambientes restritos.

## 🧠 Product Vision (Maestro Agent Architecture)
Sapo AI is designed as a **Universal Local AI Provider** using a Master/Worker pattern:
1.  **Maestro Mode:** A central "Brain" (Llama 3.1) receives all general inquiries. It interprets the user's intent—whether it's a joke, a recipe, or a complex logic problem.
2.  **Delegation:** For specialized tasks (like deep coding or data analysis), the Maestro or the Gateway routes the request to dedicated worker models (e.g., Qwen 2.5 Coder).
3.  **Tool Integration:** Seamless compatibility with Aider, Continue, and WebUIs via a standard OpenAI-compatible API.

## 🛠️ Critical Constraints & Architecture

1.  **Ambiente Air-Gapped:** Sem `pip install` ou `ollama pull` em tempo real. Tudo via `.whl` e modelos GGUF manuais.
2.  **Hardware & Performance:**
    *   **Foco em CPU:** Para notebooks corporativos sem GPU, priorizar `llama.cpp` com quantização avançada (GGUF) para reduzir alucinações e aumentar a velocidade de inferência em relação ao Ollama padrão.
3.  **Stack Tecnológica:**
    *   **Motores:** Ollama (agilidade) ou `llama.cpp` (precisão em CPU).
    *   **Gateway (LiteLLM):** Abstrai o motor. Se o motor mudar de Ollama para llama.cpp, as interfaces (VS Code, CLI) não quebram.
    *   **Interface:** CLI Sapo AI (Python), VS Code + Continue, e planejado Open WebUI.

## 📂 Estrutura de Pastas
- `/app`: Lógica da CLI e definições de System Prompts para os agentes.
- `/infra`: Configurações do LiteLLM (Ponto central de acesso).
- `/models`: Modelfiles e binários GGUF selecionados por qualidade/inteligência.
- `/scripts`: Gestão de dependências offline e automação de setup do motor.

## 🚀 Roadmap Evolutivo
- **Fase 1 (Base):** Configuração do LiteLLM e estabilização do motor (Ollama/llama.cpp) em CPU.
- **Fase 2 (Cérebro):** Refinamento de System Prompts para reduzir alucinações e implementação de RAG simples para documentos locais.
- **Fase 3 (Agente):** Integração total com VS Code + Continue para automação de código e scripts XML.

## 📍 Onde Paramos (Sessão 24/03/2026)
1.  **Arquitetura Sapo AI Cloud:** Implementação do Gateway LiteLLM com persistência em Redis via Docker Compose.
2.  **Estratégia de Modelos:** Foco em Qwen 2.5 Coder (7B-32B) e Llama 3.1 (8B-70B) via vLLM ou llama.cpp (abandonando DeepSeek por instabilidade).
3.  **Próximo Passo:** Validar a subida dos containers Docker e iniciar a CLI de conexão em `app/main.py`.

## 🛠️ Stack Consolidada
- **Gateway:** LiteLLM Proxy (Porta 4000) with Master Key.
- **Banco de Dados:** Redis (Persistência de chaves e logs).
- **Motor de Inferência:** llama.cpp (CPU/Híbrido) ou vLLM (GPU Pop!_OS).
- **Orquestração:** Docker Compose.

## 🗣️ Communication Preference
- **Language:** Conversation is in Brazilian Portuguese.
- **Project Files:** Code, documentation, and technical configs are in English.

