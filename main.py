from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/signal')
def signal():
    return jsonify({
        "message": "🤖 AI Signal XAU/USD\n📈 Sinyal: BUY\n💰 Harga: 3310.45\n🎯 TP: 3318.00\n⛔ SL: 3302.00\n🧠 Confidence: 92%"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
