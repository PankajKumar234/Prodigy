from flask import Flask, request, jsonify
import uuid
import re

app = Flask(__name__)

# In-memory storage (HashMap equivalent)
users = {}

# Email validation regex
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Helper function to validate user input
def validate_user(data):
    if not data:
        return "Request body is missing"
    
    name = data.get("name")
    email = data.get("email")
    age = data.get("age")

    if not name or not isinstance(name, str):
        return "Name is required and must be a string"
    
    if not email or not re.match(EMAIL_REGEX, email):
        return "Valid email is required"
    
    if not isinstance(age, int) or age <= 0:
        return "Age must be a positive integer"
    
    return None


#CREATE a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    error = validate_user(data)

    if error:
        return jsonify({"error": error}), 400
    
    user_id = str(uuid.uuid4())

    users[user_id] = {
        "id": user_id,
        "name": data["name"],
        "email": data["email"],
        "age": data["age"]
    }

    return jsonify(users[user_id]), 201

# READ all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values())), 200

# READ a single user
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(user), 200

#Update a user
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    error = validate_user(data)

    if error:
        return jsonify({"error": error}), 400
    
    users[user_id].update({
        "name": data["name"],
        "email": data["email"],
        "age": data["age"]
    })

    return jsonify(users[user_id]), 200

# DELETE a user
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"mesage": "Users deleted successfully"}), 200

#Something to appear at the root URL
@app.route("/")
def home():
    return jsonify({
        "message": "User CRUD API is running",
        "endpoints": {
            "POST": "/users",
            "GET": "/users",
            "GET by id": "/users/<id>",
            "PUT": "users/<id>",
            "DELETE": "/users/<id>"
        }
    }), 200

if __name__ == "__main__":
    app.run(debug=True)