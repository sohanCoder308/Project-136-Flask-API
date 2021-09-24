from data import data
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "Success"
    }), 200

@app.route("/star")
def stars_data():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": star_data,
        "message": "Success!"
    }), 200

if __name__ == "__main__":
    app.run()