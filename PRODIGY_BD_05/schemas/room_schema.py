from marshmallow import Schema, fields

class RoomCreateSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str()
    price_per_night = fields.Float(required=True)
    location = fields.Str(required=True)


    class RoomResponseSchema(Schema):
        id = fields.Int()
        title = fields.Str()
        description = fields.Str()
        price_per_night = fields.Float()
        location = fields.Str()
        owner_id = fields.Int()
        