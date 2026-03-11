# Lab-AI Hub - Kit de Migração Offline

Este diretório contém todos os arquivos necessários para o setup de um servidor de IA Privado em ambiente corporativo restrito.

## Estrutura do Projeto
- `app/`: Código fonte da CLI customizada (Python).
- `infra/`: Configurações do LiteLLM (Proxy) e Ollama.
- `models/`: Arquivos GGUF e Modelfiles para o Ollama.
- `scripts/`: Scripts para download de dependências (Wheels) e setup.

## Checklist de Migração (Offline)
- [ ] Baixar Ollama Installer (Windows/Linux).
- [ ] Baixar LiteLLM Python Wheels.
- [ ] Baixar GGUF: DeepSeek-Coder-V2-Lite-GGUF (Q4_K_M ou inferior para 6GB VRAM).
- [ ] Baixar GGUF: Llama-3.2-3B-Instruct-GGUF.
- [ ] Extensão VS Code (.vsix): Continue.

## Comandos Úteis
### 1. Injetar Modelo no Ollama
`ollama create llama-3.2 -f ./models/Llama3.2.Modelfile`

### 2. Rodar LiteLLM Proxy
`litellm --config ./infra/litellm_config.yaml`
