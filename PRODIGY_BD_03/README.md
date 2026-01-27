🚀 PRODIGY_BD_03

JWT-Based Authentication & Authorization API

This project implements secure authentication and authorization using JSON Web Tokens (JWT) for a RESTful API built with Flask and MongoDB. It extends previous tasks by adding user registration, login, password hashing, protected routes, and role-based access control (RBAC).


📌 Features Implemented

User Registration & Login
Password Hashing using bcrypt
JWT Token Generation on Login
Protected API Routes using JWT
Role-Based Access Control (admin, user, owner)
MongoDB Persistent Storage
Environment-Based Configuration using .env
Modern MongoEngine setup (Flask 3 compatible)


🛠️ Tech Stack

Backend: Python, Flask
Database: MongoDB
ODM: MongoEngine (standalone)
Authentication: JWT (flask-jwt-extended)
Security: bcrypt
Config Management: python-dotenv


📂 Project Structure

PRODIGY_BD_03/
│
├── app.py              # Main application entry
├── config.py           # Environment configurations
├── database.py         # MongoDB connection
├── models.py           # User schema
├── auth.py             # Register & Login logic
├── auth_utils.py       # Role-based authorization
├── routes.py           # Protected routes
├── requirements.txt
├── .env
└── venv/


⚙️ Environment Variables (.env)

FLASK_ENV=development
SECRET_KEY=supersecretkey
JWT_SECRET_KEY=jwtsecretkey
MONGO_URI=mongodb://localhost:27017/prodigy_bd_03


📦 Installation & Setup

1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
pip install flask mongoengine pymongo flask-jwt-extended bcrypt python-dotenv

3️⃣ Start MongoDB
Ensure MongoDB is running locally.

4️⃣ Run the Application
python app.py

Server will start at:
http://127.0.0.1:5000


🔐 API Endpoints
Open Postman click on New then select request type HTTP  

📝 Register User
POST /register
{
  "name": "Pankaj Kumar",
  "email": "pankaj@example.com",
  "password": "123456",
  "role": "admin"
}

🔑 Login User
POST /login
{
  "email": "pankaj@example.com",
  "password": "123456"
}

Response:
{
  "access_token": "<JWT_TOKEN>"
}


👥 Get All Users (Protected)

GET /users
Header:
Authorization: Bearer <JWT_TOKEN>

🛡️ Admin-Only Route

GET /admin
Header:
Authorization: Bearer <JWT_TOKEN>

✔ Only accessible if user role is admin.


🔒 Security Highlights

Passwords are hashed using bcrypt (one-way hashing)
Passwords cannot be decoded
JWT tokens carry role information
Role validation enforced before route execution
Sensitive routes protected using decorators


🧪 Testing with Postman

Register a user
Login and copy JWT token
Pass token in Authorization header
Test protected and admin-only routes


✅ Requirement Coverage Checklist

Requirement	                Status
User Registration & Login	 ✅
Password Hashing (bcrypt)	 ✅
JWT Token Generation	     ✅
Protected Routes	         ✅
Role-Based Access Control	 ✅
MongoDB Persistence	         ✅
Environment Variables	     ✅
Flask 3 Compatibility	     ✅


📌 Notes

Passwords are never stored in plain text
MongoDB does not require migrations
Role-based authorization is implemented using reusable decorators
Modern MongoEngine setup avoids deprecated Flask extensions


👨‍💻 Author

Pankaj Kumar
Backend / Python Developer