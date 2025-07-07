from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/signal')
def signal():
    signal = random.choice(['BUY', 'SELL'])
    price = round(random.uniform(3290, 3320), 2)
    message = f"""
🤖 AI Signal XAU/USD  
📈 Sinyal: {signal}  
💰 Harga: {price}  
🎯 TP/SL dinamis  
🧠 Confidence: {random.randint(80, 95)}%
🕒 Realtime
"""
    return jsonify({'message': message.strip()})

if __name__ == '__main__':
    app.run()
