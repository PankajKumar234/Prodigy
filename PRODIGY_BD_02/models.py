from mongoengine import Document, StringField, IntField, EmailField, connect
import uuid
import os

connect(host=os.getenv("MONGO_URI"))

class User(Document):
    id = StringField(primary_key=True, default=lambda: str(uuid.uuid4()))
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    age = IntField(required=True, min_value=1)

    meta = {
        "collection" : "users"
    }