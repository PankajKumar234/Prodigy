from flask import jsonify
from flask_jwt_extended import jwt_required
from models import User
from auth_utils import role_required

@jwt_required()
def get_users():
    users = User.objects()
    return jsonify([u.to_json() for u in users]), 200


@jwt_required()
@role_required("admin")
def admin_only():
    return jsonify({"message": "Welcome Admin"}), 200