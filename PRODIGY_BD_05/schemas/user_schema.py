from marshmallow import Schema, fields, validate

class UserRegisteredSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))


    class UserResponseSchema(Schema):
        id = fields.Int()
        name = fields.Str()
        email = fields.Email()
        created_at = fields.DateTime()