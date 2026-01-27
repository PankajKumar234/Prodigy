import bcrypt
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from models import User

def register():
    data = request.json

    if User.objects(email=data["email"]).first():
        return jsonify({"error": "Email already exists"}), 400
    
    hashed_pw = bcrypt.hashpw(
        data["password"].encode(),
        bcrypt.gensalt()
    ).decode("utf-8")

    User(
        name=data["name"],
        email=data["email"],
        password=hashed_pw,
        role=data.get("role", "user")
    ).save()

    return jsonify({"message": "User registered successfully"}), 201


def login():
    data = request.json
    user = User.objects(email=data["email"]).first()

    if not user or not bcrypt.checkpw(
        data["password"].encode(),
        user.password.encode()
    ):
        return jsonify({"error": "Invalid credentials"}), 401
    
    token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role}
    )

    return jsonify({"access_token": token}), 200
