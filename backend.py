# backend.py
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test_db'
mongo = PyMongo(app)

@app.route('/store-data', methods=['POST'])
def store_data():
    try:
        data = request.json['data']
        mongo.db.requests.insert_one({'data': data, 'timestamp': datetime.utcnow()})
        return 'Data stored successfully', 200
    except Exception as e:
        print(e)
        return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run(debug=True)
