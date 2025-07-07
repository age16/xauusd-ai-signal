from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/api/signal', methods=['GET'])
def get_signal():
    # Simulasi data analisis (ganti dengan real prediksi kalau sudah)
    direction = random.choice(["BUY", "SELL"])
    entry = round(random.uniform(3300, 3315), 2)
    sl = round(entry - 8, 2) if direction == "BUY" else round(entry + 8, 2)
    tp1 = round(entry + 7, 2) if direction == "BUY" else round(entry - 7, 2)
    tp2 = round(tp1 + 10, 2) if direction == "BUY" else round(tp1 - 12, 2)
    rsi = round(random.uniform(40, 60), 1)
    ma20 = round(entry + random.uniform(-1, 1), 1)
    ma50 = round(entry + random.uniform(-1.5, 1.5), 1)
    pattern = random.choice(["Bullish Engulfing", "Bearish Rejection", "Doji", "Pin Bar"])
    tf = f"{direction} | {direction} | {direction}"
    confidence = random.randint(85, 96)
    now = datetime.now().strftime("%H:%M WIB")
    ps_note = "Sentimen pasar sedang mendukung arah " + ("naik" if direction == "BUY" else "turun") + " berdasarkan berita ekonomi terbaru."

    message = f"""🤖 Sinyal {direction} XAU/USD
📍 Entry: {entry}
⛔ SL: {sl}
🎯 TP1: {tp1}
🎯 TP2: {tp2}
📊 RSI: {rsi} – {"kuat" if rsi > 50 else "lemah"}, cenderung {"bullish" if rsi > 50 else "bearish"}
📈 MA20: {ma20}, MA50: {ma50}
📉 Pattern: {pattern} (TF 30M)
📶 TF: {tf}
🧠 Confidence: {confidence}%
🕒 {now}
📰 PS: {ps_note}
"""

    return jsonify({'message': message})

if __name__ == '__main__':
    app.run()
