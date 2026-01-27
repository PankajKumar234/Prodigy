from mongoengine import Document, StringField, EmailField


class User(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(default='user', choices=["admin", "user", "owner"])

    def to_json(self):
        return{
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            "role": self.role
        }