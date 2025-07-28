from flask import Flask, request
import requests
import telegram

app = Flask(__name__)

TELEGRAM_TOKEN = '8488443513:AAGlagWO9mfRUIK_4-hHMTIKTASeILtq9MM'
CHAT_ID = 1050138562
bot = telegram.Bot(token=TELEGRAM_TOKEN)

last_positions = None

def get_positions():
    url = "https://api.hyperliquid.xyz/positions"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/check_positions')
def check_positions():
    global last_positions
    positions = get_positions()
    if positions and positions != last_positions:
        message = "تغییر در پوزیشن‌ها دیده شد!"
        bot.send_message(chat_id=CHAT_ID, text=message)
        last_positions = positions
        return "Message sent!"
    return "No change detected."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
