import click
import requests
import json
import os
import sys

# Configurações padrão
# No ambiente real, LITELLM_URL apontará para o IP do seu SERVIDOR (ex: http://192.168.1.100:4000/v1/chat/completions)
LITELLM_URL = os.environ.get("LITELLM_URL", "http://localhost:4000/v1/chat/completions")

@click.group()
def cli():
    """Sapo AI CLI - Assistente Privado de IA para Redes Restritas."""
    pass

@cli.command()
@click.option('--model', default='llama-3.2', help='Nome do modelo (llama-3.2 ou deepseek-coder)')
def check(model):
    """Verifica a conectividade com o servidor de IA."""
    click.echo(f"[*] Verificando conexão com {LITELLM_URL} usando o modelo {model}...")
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Olá, você está online?"}],
        "max_tokens": 15
    }
    
    try:
        response = requests.post(LITELLM_URL, json=payload, timeout=10)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            click.echo(f"[+] Conectado! Resposta: {content.strip()}")
        else:
            click.echo(f"[-] Erro na API (Status {response.status_code}): {response.text}")
    except Exception as e:
        click.echo(f"[-] Falha na conexão: {str(e)}")

@cli.command()
@click.option('--model', default='llama-3.2', help='Modelo para o chat')
@click.option('--system', default='Você é o Sapo AI, um assistente especializado em infraestrutura e QA.', help='Prompt de sistema')
def chat(model, system):
    """Inicia um chat interativo com a IA no servidor."""
    click.secho(f"--- Sapo AI Chat (Modelo: {model}) ---", fg='green', bold=True)
    click.echo("Digite 'sair' ou 'exit' para encerrar.\n")
    
    messages = [{"role": "system", "content": system}]
    
    while True:
        user_input = click.prompt(click.style("Você", fg='cyan', bold=True))
        
        if user_input.lower() in ['sair', 'exit', 'quit']:
            break
            
        messages.append({"role": "user", "content": user_input})
        
        payload = {
            "model": model,
            "messages": messages,
            "stream": False # Podemos implementar stream depois para ficar mais 'vivo'
        }
        
        try:
            with click.progressbar(length=100, label='Sapo está pensando...') as bar:
                response = requests.post(LITELLM_URL, json=payload)
                bar.update(100)
                
            if response.status_code == 200:
                reply = response.json()['choices'][0]['message']['content']
                click.secho(f"\nSapo AI: ", fg='green', bold=True, nl=False)
                click.echo(reply + "\n")
                messages.append({"role": "assistant", "content": reply})
            else:
                click.secho(f"\n[!] Erro: {response.text}", fg='red')
        except Exception as e:
            click.secho(f"\n[!] Falha de conexão: {str(e)}", fg='red')

if __name__ == '__main__':
    cli()
