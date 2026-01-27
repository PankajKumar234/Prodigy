from flask import Flask, request, jsonify
from models import User
from dotenv import load_dotenv
from mongoengine.errors import NotUniqueError
import re

load_dotenv()

app = Flask(__name__)


EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'


def validate_user(data):
    if not data:
        return "Requested body is missing "
    
    if not isinstance(data.get("name"), str):
        return "Name must be a string"
    
    if not re.match(EMAIL_REGEX, data.get("email", "")):
        return "Invalid email"
    
    if not isinstance(data.get("age"), int) or data["age"] <= 0:
        return "Age must be a positive integer"
    
    return None


@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    error = validate_user(data)

    if error:
        return jsonify({"error": error}), 400
    
    try:
        user = User(**data)
        user.save()
        return jsonify(user.to_mongo()), 201
    
    except NotUniqueError:
        return jsonify({"error": "Email already exists"}), 400
    
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500
    
    
@app.route("/users", methods=["GET"])
def get_users():
    users = User.objects()
    return jsonify([u.to_mongo() for u in users]), 200
    

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_mongo()), 200


@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    error = validate_user(data)
    if error:
        return jsonify({"error": error}), 400
    
    user.update(**data)
    return jsonify({"message": "User updated"}), 200


@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    user.delete()
    return jsonify({"message": "User deleted"}), 200


@app.route("/")
def home():
    return jsonify({
        "status": "PRODIGY_BD_02 API running",
        "endpoints": [
            "GET /users",
            "POST /users",
            "GET /users/<id>",
            "PUT /users/<id>",
            "DELETE /users/<id>"
        ]
    }), 200


if __name__ == "__main__":
    app.run(debug=True)