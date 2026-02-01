# 🏨 Hotel Booking Platform – Backend API
**PRODIGY_BD_05 (Mini Project)**
---
A RESTful backend API for a Hotel Booking Platform built using Flask, PostgreSQL, and JWT authentication.
This project supports user authentication, hotel room listings, availability filtering, and secure room bookings with overlap prevention.

# 🚀 Features
**🔐 Authentication & Authorization**
- User registration & login
- JWT-based secure authentication
- Protected routes
- Owner-based permissions

**🏠 Room Management**

- Create, update, delete hotel rooms (owner only)
- Public room listing
- Fetch single room details
- Duplicate room prevention

**🔎 Search & Availability**

- Filter available rooms by:
    - Check-in date
    - Check-out date
    - Location
- Prevents showing rooms with overlapping bookings

**📅 Booking System**

- Book available rooms
- Prevent overlapping bookings
- View logged-in user’s bookings
- Cancel booking (not allowed after check-in date)

**🛡️ Data Safety**

- Input validation
- Proper HTTP status codes
- Centralized error handling
- Secure password hashing

## 🧱 Tech Stack

|Layer      |        Technology|
|-----------|------------------|
|Backend    |             Flask|
|Database   |        POstgreSQL|
|ORM        |        SQLAlchemy|
|Auth       |Flask-JWT-Extended|
|Validation | Custom Validators|
|ApiTesting |           Postman|

## 📁 Project Structure
```
PRODIGY_BD_05/
│
├── app.py
├── config.py
├── database.py
│
├── models/
│   ├── user.py
│   ├── room.py
│   └── booking.py
│
├── routes/
│   ├── auth_routes.py
│   ├── room_routes.py
│   └── booking_routes.py
│
├── schemas/
│   ├── user_schema.py
│   ├── room_schema.py
│   └── booking_schema.py
│
├── utils/
│   ├── auth_utils.py
│   └── validators.py
│
├── requirements.txt
├── README.md
├── .env   ❌ (excluded from GitHub)
└── venv/
```

## ⚙️ Environment Setup

**1️⃣ Clone the repository**
```
git clone https://github.com/your-username/PRODIGY_BD_05.git 

cd PRODIGY_BD_05
```

**2️⃣ Create virtual environment**
```
python -m venv venv
venv\Scripts\activate   # Windows
```

**3️⃣ Install dependencies**
```
pip install -r requirements.txt
```

**4️⃣ Create .env file**
```
FLASK_ENV=development
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=hotel_booking_db
```
>⚠️ .env is ignored via .gitignore

**🗄️ Database Initialization**
```
flask shell
```
```
Python

from app import app
from database import db
with app.app_context():
     db.create_all()
```

**▶️ Run the Application**
```
python app.py
```
Server runs at:
```
http://127.0.0.1:5000
```

# 🧪 API Testing (Postman)
**🔑 Auth Endpoints**

|Method  |Endpoint        |Description|
|--------|----------------|-----------|
|POST    |/auth/register  |Register user
|POST    |/auth/login     |Login & get JWT
|GET     |/auth/me        |Get logged-in user

**🏠 Room Endpoints**

|Method  |Endpoint            |Access|
|--------|--------------------|------|
POST     |/rooms              |Auth (Owner)
GET      |/rooms              |Public
GET      |/rooms/<room id>    |Public
PUT      |/rooms/<room id>    |Owner only
DELETE   |/rooms/<room id>    |Owner only
GET      |/room/available     |Public

**📅 Booking Endpoints**

|Method     |Endpoint            |Access|
|-----------|-----------------|------|
POST    |/bookings           |Auth
GET     |/bookings/my        |Auth
DELETE  |/bookings/<room id> |Auth


**🔒 Security Highlights**

- Password hashing with Werkzeug
- JWT expiration handling
- Ownership-based authorization
- Booking overlap prevention
- Cancel booking restriction after check-in

**📌 Learning Outcomes**

- REST API design
- Flask Blueprints
- JWT authentication
- SQLAlchemy relationships
- Date overlap logic
- Production-grade project structure

**🏆 Task Completion**

✅ PRODIGY Internship – 

Backend Development
Task 05: Hotel Booking Platform Backend API

**👨‍💻 Author**

Pankaj Kumar

Backend Developer | Python | Flask | PostgreSQL
