from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from database import init_db
from auth import auth_bp
from routes import routes_bp

app = Flask(__name__)
app.config.from_object(Config)

#Initialize JWT
JWTManager(app)

#Initialize MongoDB
init_db(app)

#Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(routes_bp)

@app.route("/")
def home():
    return {
        "status": "PRODIGY_BD_04 API is running",
        "features": [
            "JWT Authentication",
            "Role-Based Authorization",
            "Redis Caching"
        ],
        "endpoints": [
            "POST /register",
            "POST /login",
            "GET /users (JWT + Cached)",
            "GET /admin (Admin only)"
        ]
    }


if __name__ == "__main__":
    app.run(debug=True)