PRODIGY_BD_04 – Caching with Redis

📌 Overview
PRODIGY_BD_04 focuses on improving API performance by integrating Redis caching into an existing Flask REST API that already supports:

JWT-based Authentication
Role-Based Authorization (RBAC)
MongoDB (MongoEngine) persistence

Redis is used to cache frequently accessed endpoints and reduce database load, while ensuring data consistency through cache invalidation strategies.

🛠️ Tech Stack
Backend: Python, Flask
Authentication: JWT (flask-jwt-extended)
Authorization: Role-Based Access Control (admin/user)
Database: MongoDB (MongoEngine ODM)
Caching: Redis
Security: bcrypt password hashing
Config Management: python-dotenv (.env)

📁 Project Structure

Prodigy/PRODIGY_BD_04/
        │
        ├── app.py              # Application entry point
        ├── auth.py             # User registration & login (JWT)
        ├── auth_utils.py       # Role-based authorization helpers
        ├── routes.py           # Protected & cached API routes
        ├── models.py           # MongoEngine User model
        ├── database.py         # MongoDB connection setup
        ├── cache.py            # Redis client initialization
        ├── config.py           # Environment-based configuration
        ├── .env                # Environment variables
        └── requirements.txt    # Project dependencies

⚙️ Environment Setup
1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate # Windows

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure .env
MONGO_URI=mongodb://localhost:27017/prodigy_bd_04
FLASK_ENV=development
SECRET_KEY=supersecretkey
JWT_SECRET_KEY=jwtsecretkey
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
CACHE_TTL=60

▶️ Running the Application
Make sure MongoDB and Redis are running.
python app.py

Server will start at:
http://127.0.0.1:5000/

🔐 Authentication Flow

Register User
POST /register

Login
POST /login

Returns a JWT token, which must be sent in headers for protected routes:
Authorization: Bearer <JWT_TOKEN>

⚡ Redis Caching Implementation

Cached Endpoint
GET /users
First request → Data fetched from MongoDB and cached in Redis
Subsequent requests → Served from Redis cache
Cache TTL controlled via CACHE_TTL

Cache Invalidation
Cache is automatically cleared when:

A new user is registered
Data is modified (future PUT/DELETE extensions)
redis_client.delete("users:all")

🔒 Role-Based Access Control (RBAC)

Admin-only Endpoint
GET /admin
Requires valid JWT
Requires role = admin
Normal users receive 403 Forbidden

🧪 Postman Testing Summary

Endpoint	Method	Auth Required	Description
/register	 POST	    ❌	       Create user
/login	     POST	    ❌	       Login & get JWT
/users	     GET	    ✅	       Cached user list
/admin	     GET	    ✅(Admin)   Admin-only access

📊 Performance Observation

Request	                Response Time
First /users call	    ~40–60 ms
Cached /users call	    ~2–5 ms

This demonstrates significant performance improvement using Redis caching.

✅ Key Learnings

Redis drastically improves API response times

TTL ensures cache freshness
Cache invalidation prevents stale data
Blueprint-based architecture improves scalability
Secure APIs using JWT + RBAC

🎯 Conclusion

PRODIGY_BD_04 successfully demonstrates how to integrate Redis caching into a secure Flask API, balancing performance, security, and data consistency—a common real-world backend architecture pattern.

👨‍💻 Author

Pankaj Kumar
Backend / Python Developer