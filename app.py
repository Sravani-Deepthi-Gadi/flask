from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Load MongoDB credentials securely
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    raise ValueError("MONGO_URI is not set in environment variables")

client = MongoClient(mongo_uri)
db = client["myDatabase"]
collection = db["users"]

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    users = list(collection.find({}))
    for user in users:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
    return jsonify(users)

# Add a new user
@app.route("/users", methods=["POST"])  # Changed route from "/user" to "/users"
def add_user():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"message": "User added successfully", "user_id": str(result.inserted_id)}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Use for deployment
