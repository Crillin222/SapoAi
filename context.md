# Sapo AI - Contexto do Projeto (Master)

## 🎯 Objetivo
Prover um ecossistema de IA privado, seguro e totalmente offline para uma rede de laboratório corporativa. O objetivo é contornar restrições de TI que impedem o uso de nuvem ou downloads diretos (Ollama Pull/CLI), fornecendo modelos de linguagem e uma interface de linha de comando (CLI) para a equipe interna, garantindo a soberania dos dados.

## 🛠️ Restrições Críticas (LEIA ANTES DE SUGERIR)
1.  **Ambiente Altamente Restritivo:** Sem acesso a `ollama pull`, Hugging Face ou download de bibliotecas via pip em tempo real. Tudo deve ser via transferência manual (GGUF, Wheels, instaladores offline).
2.  **Segurança de Dados:** Nenhuma informação pode sair da rede interna.
3.  **Hardware:** Testes iniciais em notebook corporativo, deploy final em servidor com 6GB VRAM.
4.  **Stack Tecnológica:**
    *   **Engine:** Ollama (modelos via `Modelfile` manual).
    *   **Gateway:** LiteLLM (Porta 4000) - Unifica múltiplos modelos em uma única API OpenAI-Compatible.
    *   **Interface:** CLI Customizada em Python (Lab-AI Hub) e VS Code + Continue.

## 📂 Estrutura de Pastas
- `/app`: Código fonte da CLI Sapo AI.
- `/infra`: Configurações do LiteLLM (Ponto central de acesso aos modelos).
- `/models`: Modelfiles para registrar modelos GGUF manualmente.
- `/scripts`: Automações de setup e gestão de dependências offline.

## 🚀 Roadmap e Fases
- **Fase 1 (Base):** Configuração do LiteLLM como hub de modelos locais.
- **Fase 2 (Distribuição):** Desenvolvimento da CLI Python para que a equipe possa interagir com os modelos sem configurações complexas.
- **Fase 3 (Casos de Uso):** Otimização para automação (Robot Framework), análise de logs e scripts XML proprietários.

## 🧠 Instruções para a IA
- **Tom:** Arquiteto de Sistemas e Facilitador de IA.
- **Padrão:** Sempre assuma que o usuário precisa de soluções que funcionem sem internet. Priorize simplicidade no setup para a equipe final.
