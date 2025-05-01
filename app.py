from flask import Flask, jsonify
import boto3

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask server running.'

@app.route('/get-historical')
def get_historical_aqi():
    # Simulated static data (Plan B fallback)
    return jsonify([
        {"date": "2022-10-24 12:00", "aqi": 285, "pm2_5": 135.3, "temp": 24.5, "humidity": 62.1},
        {"date": "2022-10-24 14:00", "aqi": 310, "pm2_5": 144.1, "temp": 25.7, "humidity": 58.9},
        {"date": "2022-10-25 09:00", "aqi": 295, "pm2_5": 138.6, "temp": 23.6, "humidity": 64.3}
    ])

if __name__ == '__main__':
    app.run(debug=True)