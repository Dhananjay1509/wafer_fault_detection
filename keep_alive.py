from flask import Flask
from threading import Thread
import time
import requests

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=8081)

def keep_alive():
    t = Thread(target=run)
    t.start()

def ping_self():
    while True:
        try:
            requests.get("YOUR_REPLIT_URL")
        except:
            pass
        time.sleep(300)  # Ping every 5 minutes

if __name__ == "__main__":
    keep_alive()
    ping_thread = Thread(target=ping_self)
    ping_thread.start()