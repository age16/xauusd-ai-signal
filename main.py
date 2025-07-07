import os
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Server AI XAU/USD Aktif"

@app.route("/api/signal")
def signal():
    now = datetime.now()
    jam = now.strftime("%H:%M WIB")

    signal_data = {
        "message": f"""🤖 Sinyal SELL XAU/USD
📍 Entry: 3309.50
⛔ SL: 3314.50
🎯 TP1: 3300.00
🎯 TP2: 3288.00
📊 RSI: 47.1 – lemah, cenderung bearish
📈 MA20: 3308.7, MA50: 3310.5
📉 Pattern: Bearish Rejection (TF 30M)
📶 TF: SELL | SELL | SELL
🧠 Confidence: 91%
🕒 {jam}
📰 PS: Tekanan jual dipicu sentimen dagang AS, pelemahan demand safe-haven dorong potensi lanjut turun ke bawah 3300."""
    }

    return jsonify(signal_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)