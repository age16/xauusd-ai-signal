import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Server AI XAU/USD Aktif"

@app.route("/api/signal")
def signal():
    return jsonify({
        "message": "🤖 AI Signal XAU/USD\n📈 Sinyal: BUY\n💰 Harga: 3310.45\n🎯 TP: 3318.00\n⛔ SL: 3302.00\n🧠 Confidence: 92%"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ambil port dari Railway
    app.run(host="0.0.0.0", port=port)