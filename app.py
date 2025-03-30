from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv('7542408750:AAH5df9bHzlaBJSSuHwC95NGVH86nEGZlHo')         # Token bot Telegram dari environment
CHAT_ID = os.getenv('-4796523227')             # Chat ID grup Telegram

@app.route('/', methods=['GET'])
def index():
    return 'Webhook Aktif'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    msg = data.get('message', 'Pesan kosong dari alert')
    
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': f"[Alert TradingView]\n{msg}"
    }
    requests.post(telegram_url, data=payload)
    
    return 'ok', 200