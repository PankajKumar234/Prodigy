from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #Intialize extensions
    db.init_app(app)
    JWTManager(app)

    #Import models (important for db.create_all)
    import models

    #Register blueprints
    from routes.auth_routes import auth_bp
    from routes.room_routes import room_bp
    from routes.booking_routes import booking_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(room_bp)
    app.register_blueprint(booking_bp)

    @app.route("/")
    def home():
        return{"status": "Hotel Booking API is running"}
    
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)