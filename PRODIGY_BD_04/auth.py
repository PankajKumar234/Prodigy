import bcrypt
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User
from cache import redis_client

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    if not data or not all(k in data for k in ("name", "email", "password")):
        return jsonify({"error": "MIssing required fields"}), 400

    if User.objects(email=data["email"]).first():
        return jsonify({"error": "Email already exists"}), 400
    
    hashed_pw = bcrypt.hashpw(
        data["password"].encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    User(
        name=data["name"],
        email=data["email"],
        password=hashed_pw,
        role=data.get("role", "user")
    ).save()

    # Cache invalidation (important for BD_4
    redis_client.delete("users: all")

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    if not data or not all(k in data for k in ("email", "password")):
        return jsonify({"error": "Missing credentials"}), 400
    
    user = User.objects(email=data["email"]).first()

    if not user or not bcrypt.checkpw(
        data["password"].encode("utf-8"),
        user.password.encode("utf-8")
    ):
        return jsonify({"error": "Invalid credentials"}), 401
    
    token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role}
    )

    return jsonify({"access_token": token}), 200
