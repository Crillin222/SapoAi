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

## 🧠 Estratégias Anti-Alucinação (Grounding)
1. **System Prompts de Baixa Temperatura:** Configurar `temperature: 0.0` para tarefas técnicas e de código.
2. **RAG Local:** Uso de ferramentas como **Docling** para ingestão de documentos e **Qdrant** ou o RAG nativo do Open WebUI para fornecer contexto real à IA.
3. **Chain of Thought (CoT):** Instruir o modelo (via System Prompt) a "pensar passo a passo" antes de fornecer a resposta final.

## 🛠️ Ferramentas Complementares
- **n8n (Self-hosted):** Para criar fluxos de automação agêntica visual (ex: IA lê log -> identifica erro -> abre ticket).
- **Claude Code / OpenCode:** Para execução de comandos de terminal e correções automáticas de arquivos.

## 📍 Lições Aprendidas dos Vídeos
- **Não use modelos < 7B para tarefas complexas:** Eles alucinam demais em lógica.
- **Separe o Autocomplete do Chat:** Use modelos ultra-leves (1.5B) para predição de texto em tempo real para não sobrecarregar o CPU.
- **Quantização é sua amiga:** Q4_K_M é o "sweet spot" entre inteligência e consumo de memória.
