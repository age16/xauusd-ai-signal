import os
import requests
import time
import random

# Token dan Chat ID Telegram
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")  # Masukkan ke Railway sebagai VARIABLE
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")  # Masukkan ke Railway juga

# URL API sinyal AI kamu
AI_SIGNAL_URL = "https://xauusd-ai-signal-production.up.railway.app/api/signal"

def get_signal():
    try:
        response = requests.get(AI_SIGNAL_URL, timeout=10)
        data = response.json()
        return data.get("message", "❌ Tidak ada sinyal.")
    except Exception as e:
        print("❌ Gagal ambil sinyal AI:", e)
        return "❌ Gagal ambil sinyal AI dari server."

def send_to_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": msg
    }
    try:
        response = requests.post(url, data=payload)
        print(f"✅ Kirim sinyal ke Telegram sukses ({response.status_code})")
    except Exception as e:
        print("❌ Gagal kirim ke Telegram:", e)

# Loop utama (auto every 15–30 menit)
while True:
    print("\n🚀 Ambil sinyal terbaru...")
    message = get_signal()
    print("📤 Kirim ke Telegram...")
    send_to_telegram(message)

    delay = random.randint(900, 1800)  # 15 - 30 menit
    print(f"⏳ Tunggu {delay // 60} menit sebelum request berikutnya...")
    time.sleep(delay)