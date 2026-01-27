from marshmallow import Schema, fields

class BookingCreateSchema(Schema):
    room_id = fields.Int(required=True)
    check_in = fields.Date(required=True)
    check_out = fields.Date(required=True)


    class BookingREsponseSchema(Schema):
        id = fields.Int()
        room_id = fields.Int()
        user_id = fields.Int()
        check_in = fields.Date()
        check_out = fields.Date()
        created_at = fields.DateTime()
        