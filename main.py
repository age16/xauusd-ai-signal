import requests
import time
import random

TOKEN = '7671287681:AAGHheO_e8gy-qWSpG8mOGmCby-SoIEtjkc'
CHAT_ID = '6843291533'
API_URL = 'https://xauusd-ai-signal-production.up.railway.app/api/signal'

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        'chat_id': CHAT_ID,
        'text': msg
    }
    try:
        requests.post(url, data=data)
        print("✅ Kirim sinyal ke Telegram sukses")
    except Exception as e:
        print("❌ Gagal kirim Telegram:", e)

def get_signal():
    try:
        r = requests.get(API_URL, timeout=10)
        return r.json().get('message')
    except Exception as e:
        print("❌ Gagal ambil sinyal AI:", e)
        return None

def main_loop():
    while True:
        print("🚀 Ambil sinyal terbaru...")
        signal = get_signal()
        if signal:
            send_telegram(signal)
        else:
            send_telegram("⚠️ Gagal ambil sinyal AI.")
        wait_time = random.randint(900, 1800)  # 15-30 menit random
        print(f"⏳ Tunggu {wait_time//60} menit sebelum request berikutnya...\n")
        time.sleep(wait_time)

if __name__ == "__main__":
    main_loop()
