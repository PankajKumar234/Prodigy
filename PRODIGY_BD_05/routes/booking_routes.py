from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, date
from database import db
from models.booking import Booking
from models.room import Room

booking_bp = Blueprint("bookings", __name__, url_prefix="/bookings")

@booking_bp.route("", methods=["POST"])
@jwt_required()
def create_booking():
    data = request.get_json()
    user_id = get_jwt_identity()

    if not data or not data.get("room_id") or not data.get("check_in") or not data.get("check_out"):
        return {"error": "Missing required fields"}, 400
    
    try:
        check_in = datetime.strptime(data["check_in"], "%Y-%m-%d").date()
        check_out = datetime.strptime(data["check_out"], "%Y-%m-%d").date()
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD"}, 400
    
    if check_in >= check_out:
        return {"error": "Check-out must be after check-in"}, 400
    
    room = Room.query.get_or_404(data["room_id"])

    #OVERLAP CHECK
    conflict = Booking.query.filter(
        Booking.room_id == room.id,
        Booking.check_in < check_out,
        Booking.check_out > check_in
    ).first()

    if conflict:
        return { "error": "Room is already booked for these dates"}, 409
    
    booking = Booking(
        user_id=user_id,
        room_id=room.id,
        check_in=check_in,
        check_out=check_out
    )

    db.session.add(booking)
    db.session.commit()

    return {
        "message": "Booking confirmed",
        "booking_id": booking.id
    }, 201

@booking_bp.route("/my", methods=["GET"])
@jwt_required()
def my_bookings():
    user_id = get_jwt_identity()

    bookings = Booking.query.filter_by(user_id=user_id).all()

    return [
        {
            "booking_id": b.id,
            "room_id": b.room_id,
            "room_title": b.room.title,
            "check_in": b.check_in.isoformat(),
            "check_out": b.check_out.isoformat(),
            "created_at": b.created_at.isoformat()
        }
        for b in bookings
    ], 200

@booking_bp.route("/<int:booking_id>", methods=["DELETE"])
@jwt_required()
def cancel_booking(booking_id):
    user_id = get_jwt_identity()

    booking = Booking.query.get_or_404(booking_id)

    #Ownership check
    if booking.user_id != user_id:
        return {"error": "Not authorized to cancel this booking"}, 403
    
    #Prevent cancel after check-in
    if date.today() >= booking.check_in:
        return {"error": "cannot cancel booking after check-in date"}, 400
    
    booking.status = "cancelled"
    db.session.commit()

    return {"message": "Booking cancelled successfully"}, 200
