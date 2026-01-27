from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from database import db
from models.room import Room
from datetime import datetime
from sqlalchemy import and_, not_
from models.booking import Booking
from schemas.room_schema import RoomCreateSchema

room_bp = Blueprint("rooms", __name__, url_prefix="/rooms")

#Create Room (Owner)
@room_bp.route("", methods=["POST"])
@jwt_required()
def create_room():
    try:
        data = RoomCreateSchema().load(request.get_json())
    except ValidationError as err:
        return {"error": err.messages}, 400
    user_id = get_jwt_identity()
    
#API level duplicate check
    existing_room = Room.query.filter_by(
        title=data["title"],
        location=data["location"],
        owner_id=user_id
    ).first()

    if existing_room:
        return {"error": "You already created this room at this location"}, 409

    room = Room(
        title=data["title"],
        description=data.get("description"),
        price_per_night=data["price_per_night"],
        location=data["location"],
        owner_id=get_jwt_identity()
    )

    db.session.add(room)
    db.session.commit()

    return {"message": "Room created successfully"}, 201


#Get All Rooms (Public)
@room_bp.route("", methods=["GET"])
def get_rooms():
    rooms = Room.query.all()

    return [
        {
            "id": r.id,
            "title": r.title,
            "price_per_night": r.price_per_night,
            "location": r.location,
            "owner_id": r.owner_id
        }
        for r in rooms
    ], 200

# Get Single Room (Public)
@room_bp.route("/<int:room_id>", methods=["GET"])
def get_room(room_id):
    room = Room.query.get_or_404(room_id)

    return {
        "id": room.id,
        "title": room.title,
        "description": room.description,
        "price_per_night": room.price_per_night,
        "location": room.location,
        "owner_id": room.owner_id
    }, 200

#Search Rooms
@room_bp.route("/search", methods=["GET"])
def search_rooms():
    location = request.args.get("location")
    min_price = request.args.get("min_price", type=int)
    max_price = request.args.get("max_price", type=int)

    query = Room.query

    if location:
        query = query.filter(Room.location.ilike(f"%{location}%"))

    if min_price is not None:
            query = query.filter(Room.price_per_night >= min_price)

    if max_price is not None:
        query = query.filter(Room.price_per_night <= max_price)

    
    rooms = query.all()

    return [
        {
            "id": r.id,
            "title": r.title,
            "price_per_night": r.price_per_night,
            "location": r.location
        }
        for r in rooms
    ], 200

#Available Rooms
@room_bp.route("/available", methods=["GET"])
def available_rooms():
    check_in = request.args.get("check_in")
    check_out = request.args.get("check_out")

    if not check_in or not check_out:
        return {"error": "check_in and check_out required"}, 400
    
    try:
        check_in = datetime.strptime(check_in, "%Y-%m-%d").date()
        check_out = datetime.strptime(check_out, "%Y-%m-%d").date()
    except ValueError:
        return {
            "error": "Invalid date format. Use YYYY-MM-DD"
        }, 400

    #Subquery for booked rooms
    booked_rooms = db.session.query(Booking.room_id).filter(
        and_(
            Booking.check_in < check_out,
            Booking.check_out < check_in,

        )
    )

    rooms = Room.query.filter(
        ~Room.id.in_(booked_rooms)
    ).all()

    return [
        {
            "id": r.id,
            "title": r.title,
            "price_per_night": r.price_per_night,
            "location": r.location
        }
        for r in rooms
    ], 200

    
#Update Room (Only Owner)
@room_bp.route("/<int:room_id>", methods=["PUT"])
@jwt_required()
def update_room(room_id):
    user_id = int(get_jwt_identity())
    room = Room.query.get_or_404(room_id)

    print("JWT user_id:", user_id)
    print("Room owner_id:", room.owner_id)

    if room.owner_id != user_id:
        return {"error": "Unauthorized"}, 403
    
    data = request.get_json()
    room.title = data.get("title", room.title)
    room.description = data.get("description", room.description)
    room.price_per_night = data.get("price_per_night", room.price_per_night)
    room.location = data.get("location", room.location)

    db.session.commit()
    return {"message": "Room updated successfully"}, 200

#Delete Room (Only Owner)
@room_bp.route("/<int:room_id>", methods=["DELETE"])
@jwt_required()
def delete_room(room_id):
    user_id = get_jwt_identity()
    room = Room.query.get_or_404(room_id)

    if room.owner_id != user_id:
        return {"error": "Unauthorized"}, 403
    
    db.session.delete(room)
    db.session.commit()
    return {"message": "Room deleted successfully"}, 200

