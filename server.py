from flask import Flask, request, jsonify
import os
import json


app = Flask(__name__)
JSON_FILE ='data.json'

def read_json():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def write_json(data):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/data', methods=['GET'])
def get_data():
    data = read_json()
    return jsonify(data)

@app.route('/data', methods=['POST'])
def update_data():
    new_data = request.json
    write_json(new_data)
    return jsonify(new_data)

if __name__ == '__main__':
    app.run(debug=True) 
