from mongoengine import connect
from config import Config

def init_db(app=None):
    connect(
        db=None,
        host=Config.MONGO_URI,
        alias="default",
        maxPoolSize=50,
        serverSelectionTimeoutMS = 5000
    )