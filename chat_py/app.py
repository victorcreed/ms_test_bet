
from flask import Flask
from pymongo import MongoClient

from bson import json_util
import os

from flask import jsonify, request

app = Flask(__name__)

client = MongoClient(os.environ.get('MONGO_HOST'), os.environ.get('MONGO_PORT'))

db = client.flask_db
chats = db.chats

@app.route("/", methods=["GET"])
def index():
    data = chats.find()
    return json_util.dumps(data)

@app.route("/create_post", methods=["POST"])
def create():
    content = json.loads(request.data)["message"]

    chat = chats.insert_one({"message": content})
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
