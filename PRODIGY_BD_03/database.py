from mongoengine import connect
from config import Config

def init_db():
    connect(
        host=Config.MONGO_URI,
        alias="default"
    )