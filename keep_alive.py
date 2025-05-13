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
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def ping_self():
    while True:
        try:
            # Get your Replit URL from environment or use a default format
            replit_url = os.environ.get('REPLIT_URL', f"https://{os.environ.get('REPL_SLUG', 'your-repl')}.{os.environ.get('REPL_OWNER', 'your-username')}.repl.co")
            requests.get(replit_url)
            print(f"Pinged {replit_url}")
        except Exception as e:
            print(f"Ping failed: {str(e)}")
        time.sleep(300)  # Ping every 5 minutes

if __name__ == "__main__":
    keep_alive()
    ping_thread = Thread(target=ping_self)
    ping_thread.start()


