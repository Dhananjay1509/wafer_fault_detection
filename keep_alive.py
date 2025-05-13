from flask import Flask
from threading import Thread
import time
import os

# Try to import requests, install if missing
try:
    import requests
except ImportError:
    import subprocess
    print("Installing requests module...")
    subprocess.check_call(["pip", "install", "requests"])
    import requests

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=5000)

def keep_alive():
    t = Thread(target=run)
    t.start()

def ping_self():
    while True:
        try:
            # For Replit, construct URL based on environment variables
            if os.environ.get('REPL_ID'):
                # Get the actual Replit URL from the environment
                repl_id = os.environ.get('REPL_ID')
                repl_slug = os.environ.get('REPL_SLUG', 'wafer-fault-detection')
                repl_owner = os.environ.get('REPL_OWNER', 'dhananjaypatil1')
                
                # Use the correct format for Replit URLs
                replit_url = f"https://{repl_slug}.{repl_owner}.repl.co/healthz"
                print(f"Attempting to ping {replit_url}")
                
                response = requests.get(replit_url, timeout=10)
                print(f"Pinged {replit_url} - Status: {response.status_code}")
            else:
                # For local development
                local_url = "http://localhost:5000/healthz"
                response = requests.get(local_url, timeout=5)
                print(f"Pinged {local_url} - Status: {response.status_code}")
        except Exception as e:
            print(f"Ping failed: {str(e)}")
        
        # Sleep for 5 minutes before next ping
        time.sleep(300)  # Ping every 5 minutes

if __name__ == "__main__":
    keep_alive()
    ping_thread = Thread(target=ping_self)
    ping_thread.start()






