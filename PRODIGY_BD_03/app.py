from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from database import init_db
from auth import register, login
from routes import get_users, admin_only

app = Flask(__name__)
app.config.from_object(Config)

JWTManager(app)
init_db()

@app.route("/")
def home():
    return {
        "status": "PRODIGY_BD_03 API is running",
        "endpoints": [
            "POST /register",
            "POST /login",
            "GET /users (JWT)",
            "GET /admin (Admin only)"
        ]
    }

app.add_url_rule("/register", view_func=register, methods=["POST"])
app.add_url_rule("/login", view_func=login, methods=["POST"])
app.add_url_rule("/users", view_func=get_users, methods=["GET"])
app.add_url_rule("/admin", view_func=admin_only, methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True)