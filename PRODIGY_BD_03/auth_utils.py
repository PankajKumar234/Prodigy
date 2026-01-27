from flask_jwt_extended import get_jwt
from flask import jsonify
from functools import wraps

def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            claims = get_jwt()
            if claims.get("role") != role:
                return jsonify({"error": "Access forbidden"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper