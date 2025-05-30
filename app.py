from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    
    return "🚀 Backend is live!"

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

@app.route("/bookings", methods=["GET"])
def get_bookings():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    conn.close()

    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)