from flask_jwt_extended import get_jwt_identity

def is_owner(resource_owner_id):
    return resource_owner_id == get_jwt_identity()
# This removes duplicate ownership checks everywhere