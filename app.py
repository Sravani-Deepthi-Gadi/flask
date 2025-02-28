from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://pravallika:pralak1@cluster1.3ipip.mongodb.net/?retryWrites=true&w=majority&appName=cluster1")
db = client["myDatabase"]
collection = db["users"]

@app.route("/users", methods=["GET"])
def get_users():
    users = list(collection.find({}, {"_id": 0}))  # Fetch all users, hide _id
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "User added successfully"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
