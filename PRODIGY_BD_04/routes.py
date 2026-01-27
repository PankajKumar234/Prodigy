import json 
import time
import os
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models import User
from cache import redis_client
from auth_utils import role_required

routes_bp = Blueprint("routes", __name__)

CACHE_KEY = "users:all"

# Get all users (cached)
@routes_bp.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    start = time.time()


    cached_data = redis_client.get(CACHE_KEY)
    if cached_data:
        response = json.loads(cached_data)
        response["cached"] = True
        response["response_time_ms"] = round((time.time() - start) * 1000, 2)
        return jsonify(response), 200
    
    users = User.objects()
    users_list = [u.to_json() for u in users]

    redis_client.setex(
        CACHE_KEY,
        int(os.getenv("CACHE_TTL", 60)),
        json.dumps({"users": users_list})
    )

    return jsonify({
        "users": users_list,
        "cached": False,
        "response_time_ms": round((time.time() - start) * 1000, 2)
    }), 200

# Admin-only route
@routes_bp.route("/admin", methods=["GET"])
@jwt_required()
@role_required("admin")
def admin_only():
    return jsonify({"message": "Welcome Admin"}), 200