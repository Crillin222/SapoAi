import requests
import json
import sys

# Sapo AI Gateway Settings
SAPO_URL = "http://localhost:4000"
MASTER_KEY = "sk-sapo-admin-123"

def check_gateway_health():
    """Verify if the Gateway is online and accessible."""
    print(f"🔍 Checking connection to Sapo AI Gateway at {SAPO_URL}...")
    try:
        # Standard LiteLLM endpoint to list models
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
            print(response.text)
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the Gateway. Is Docker running?")
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        check_gateway_health()
    else:
        print("🐸 Sapo AI CLI - Use 'python app/main.py check' to test the connection.")
