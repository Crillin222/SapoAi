import subprocess
import os
import time
import sys

# Configuration for Sapo AI Engines
MODELS_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
ENGINES_DIR = os.path.join(os.path.dirname(__file__), "..", "engines")

# Define the models and their assigned ports
ENGINES_CONFIG = [
    {
        "name": "sapo-maestro",
        "file": "Llama-3.1-8B-Instruct-Q5_K_M.gguf",
        "port": 8080,
        "ngl": 33 # Adjust based on VRAM (6GB)
    },
    {
        "name": "sapo-general",
        "file": "qwen2.5-7b-instruct-q5_k_m.gguf",
        "port": 8081,
        "ngl": 28
    },
    {
        "name": "sapo-coder",
        "file": "qwen2.5-coder-7b-instruct-q5_k_m.gguf",
        "port": 8082,
        "ngl": 28
    }
]

def start_engine(config):
    model_path = os.path.abspath(os.path.join(MODELS_DIR, config["file"]))
    
    # Determine the executable name based on OS
    binary_name = "llama-server.exe" if os.name == "nt" else "./llama-server"
    binary_path = os.path.abspath(os.path.join(ENGINES_DIR, binary_name))

    if not os.path.exists(model_path):
        print(f"❌ Error: Model file not found: {model_path}")
        return None

    print(f"🚀 Starting {config['name']} on port {config['port']}...")
    
    cmd = [
        binary_path,
        "-m", model_path,
        "--port", str(config["port"]),
        "--n-gpu-layers", str(config["ngl"]),
        "--ctx-size", "8192",
        "--parallel", "2"
    ]

    # Start the process in the background
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )
    return process

if __name__ == "__main__":
    processes = []
    
    print("🐸 Sapo AI - Engine Orchestrator")
    print("-------------------------------")
    
    for config in ENGINES_CONFIG:
        proc = start_engine(config)
        if proc:
            processes.append(proc)
        time.sleep(2) # Give some time between starts

    print("\n✅ All engines initiated. Gateway should now be able to route traffic.")
    print("Press Ctrl+C to stop all engines.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down Sapo AI engines...")
        for p in processes:
            p.terminate()
        print("Done.")
