import requests
import time
import random

# ✅ Ganti token dan chat ID dengan punyamu (sudah sesuai)
TOKEN = '7671287681:AAGHheO_e8gy-qWSpG8mOGmCby-SoIEtjkc'
CHAT_ID = '6843291533'

# ✅ Endpoint AI sinyal
API_URL = 'https://xauusd-ai-signal-production.up.railway.app/api/signal'

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        'chat_id': CHAT_ID,
        'text': msg
    }
    try:
        response = requests.post(url, data=data)
        print(f"✅ Kirim sinyal ke Telegram sukses ({response.status_code})")
    except Exception as e:
        print("❌ Gagal kirim ke Telegram:", e)

def get_signal():
    try:
        print("🔍 Minta data dari AI server...")
        response = requests.get(API_URL, timeout=10)
        print(f"📥 Status: {response.status_code}")
        print(f"📤 Data: {response.text[:100]}...")  # preview max 100 char
        return response.json().get('message')
    except Exception as e:
        print("❌ Gagal ambil sinyal AI:", e)
        return None

def main_loop():
    while True:
        print("\n🚀 Ambil sinyal terbaru...")
        signal = get_signal()
        if signal:
            send_telegram(signal)
        else:
            send_telegram("⚠️ Gagal ambil sinyal dari AI server.")
        wait = random.randint(900, 1800)  # 15–30 menit
        print(f"⏳ Tunggu {wait//60} menit sebelum request berikutnya...\n")
        time.sleep(wait)

if __name__ == "__main__":
    main_loop()
