import requests
import json
import sys

# Sapo AI Gateway Settings
SAPO_URL = "http://localhost:4000"
MASTER_KEY = "sk-sapo-123"

def check_gateway_health():
    """Verify if the Gateway is online and accessible."""
    print(f"🔍 Checking connection to Sapo AI Gateway at {SAPO_URL}...")
    try:
        response = requests.get(
            f"{SAPO_URL}/v1/models",
            headers={"Authorization": f"Bearer {MASTER_KEY}"},
            timeout=5
        )
        
        if response.status_code == 200:
            models = response.json().get('data', [])
            print("✅ Connection established successfully!")
            print(f"📦 Configured models: {[m['id'] for m in models]}")
            return True
        else:
            print(f"❌ Authentication error: Status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def chat_with_maestro(prompt):
    """Send a prompt to the Maestro model through the Gateway."""
    print(f"🐸 Sapo Maestro is thinking...")
    
    payload = {
        "model": "sapo-maestro",
        "messages": [
            {"role": "system", "content": "You are Sapo Maestro, a highly intelligent and helpful generalist AI. Answer in English."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }
    
    try:
        response = requests.post(
            f"{SAPO_URL}/v1/chat/completions",
            headers={"Authorization": f"Bearer {MASTER_KEY}"},
            json=payload,
            stream=False # Set to True later for real-time streaming
        )
        
        if response.status_code == 200:
            answer = response.json()['choices'][0]['message']['content']
            print(f"\n🤖 Maestro: {answer}\n")
        else:
            print(f"❌ API Error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "check":
            check_gateway_health()
        elif command == "chat":
            if len(sys.argv) > 2:
                chat_with_maestro(" ".join(sys.argv[2:]))
            else:
                print("Usage: python app/main.py chat 'Your question here'")
    else:
        print("🐸 Sapo AI CLI")
        print("Commands: check | chat 'prompt'")
