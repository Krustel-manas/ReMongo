from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
bigchain = client['bigchain']
assets = bigchain.assets
metadata = bigchain.metadata
transactions = bigchain.transactions

@app.route("/findoneasset")
def index():
	return jsonify(assets.find_one())

if __name__ == '__main__':
    app.run(debug=True)