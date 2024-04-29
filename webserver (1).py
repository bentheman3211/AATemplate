from flask import Flask, jsonify
from threading import Thread
import requests

app = Flask('')

# JSON URL from the pastebin
json_url = 'https://pastebin.com/raw/TRMFu91F'

# Function to fetch JSON data
def fetch_json_data():
    response = requests.get(json_url)
    data = response.json()
    return data

@app.route('/')
def home():
    json_data = fetch_json_data()

    status_text = json_data.get('status', {}).get('text', 'No status available')
    
    update_logs = json_data.get('update_log', [])
    update_log_messages = [log['message'] for log in update_logs]

    response = f"Status: {status_text}\n\nUpdate Log:\n"
    response += "\n".join(update_log_messages)

    return response

def run():
    app.run(host='0.0.0.0', port=8000)


def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
