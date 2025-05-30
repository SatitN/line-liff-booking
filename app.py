from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_id = data.get("userId")
    name = data.get("name")
    date = data.get("date")
    time = data.get("time")

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO bookings (userId, name, date, time)
        VALUES (?, ?, ?, ?)
    ''', (user_id, name, date, time))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)