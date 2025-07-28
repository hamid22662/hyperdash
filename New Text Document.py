import requests
import time
import telegram

TELEGRAM_TOKEN = '8488443513:AAGlagWO9mfRUIK_4-hHMTIKTASeILtq9MM'
CHAT_ID = 1050138562

bot = telegram.Bot(token=TELEGRAM_TOKEN)

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

last_positions = None

while True:
    positions = get_positions()
    if positions and positions != last_positions:
        message = "تغییر در پوزیشن‌ها دیده شد!"
        bot.send_message(chat_id=CHAT_ID, text=message)
        last_positions = positions
    time.sleep(3)
