# PRODIGY_BD_02 – User CRUD REST API with MongoDB (Persistent Storage)

## 📌 Project Overview

This project extends **PRODIGY_BD_01** by replacing in-memory storage with **persistent storage using MongoDB**.

The application is a **RESTful API** built with **Flask** that performs **CRUD operations** on a User resource.  
It integrates a **NoSQL database (MongoDB)** using an **ODM (MongoEngine)** and uses **environment variables** for secure and flexible configuration.

This task demonstrates real-world backend concepts such as database integration, schema enforcement, unique constraints, and environment-based configuration.

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **MongoDB**
- **MongoEngine (ODM)**
- **python-dotenv**
- **UUID**

---

## 📁 Project Structure

Prodigy/PRODIGY_BD_02/
        ├── app.py
        ├── models.py
        ├── config.py
        ├── requirements.txt
        ├── .env
        └── README.md

---

## 👤 User Schema (MongoDB Document)

Each user has the following fields:

| Field | Type | Description |
|-----|-----|-------------|
| id | UUID (string) | Primary key |
| name | String | User's name |
| email | String | Unique email address |
| age | Integer | Must be greater than 0 |

- Email field is enforced as **unique** at the database level
- Schema is defined using **MongoEngine**

---

## 🔗 API Endpoints

### ➕ Create User
**POST** `/users`

**Request Body (JSON):**
```json
{
  "name": "Pankaj Kumar",
  "email": "pankaj.kumar@example.com",
  "age": 25
}

Response:
201 Created
400 Bad Request (invalid input or duplicate email)

📄 Get All Users
GET /users

Response: 200 OK

🔍 Get User by ID
GET /users/<id>

Response:
200 OK
404 Not Found

✏️ Update User
PUT /users/<id>

Request Body (JSON):
{
  "name": "Updated Name",
  "email": "updated@example.com",
  "age": 30
}

Response:
200 OK
400 Bad Request
404 Not Found

❌ Delete User
DELETE /users/<id>

Response:
200 OK
404 Not Found

✅ Input Validation & Error Handling

Validation Rules

Name must be a string
Email must be valid
Age must be a positive integer

Error Handling
Scenario	            HTTP Status
Invalid input	            400
Duplicate email	            500
User not found	            404
Successful creation	        201
Successful operation        200

🔐 Environment Configuration

The project uses a .env file to manage environment-specific settings.

Example .env

FLASK_ENV=development
MONGO_URI=mongodb://localhost:27017/prodigy_db

⚠️ Note:
The .env file should never be committed to version control.

🔁 Database & Connection Pooling

MongoDB handles connection pooling internally
No manual pooling configuration is required
Collections and indexes are created automatically

Unique Index

Email uniqueness is enforced via MongoDB index
Duplicate email insertions raise E11000 error

▶️ How to Run the Project

1️⃣ Start MongoDB
Ensure MongoDB service is running:
 
Type command as below in windows cmd-
mongod

or to manually start in windows
net start MongoDB

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
python app.py

Server will start at:
http://127.0.0.1:5000

🧪 Testing the API
Use Postman, Thunder Client, or curl for testing POST, PUT, and DELETE requests.

Here I've used POSTMAN.

Example:
GET http://127.0.0.1:5000/users

📝 Notes

MongoDB is a NoSQL document database
Schema is enforced at the application level using an ODM
Persistent storage ensures data survives server restarts
Database migrations are not required for MongoDB

📌 Task Status

✅ Persistent storage implemented
✅ MongoDB integrated
✅ ODM (MongoEngine) used
✅ Environment variables configured
✅ Connection pooling handled
✅ Robust validation and error handling

Short Statement:
“The REST API was extended to use MongoDB for persistent storage. MongoEngine was used as an ODM to define and enforce the user schema. Database migrations were not required as MongoDB is schema-less and collections are created automatically. Connection pooling is handled internally by MongoDB, and environment-specific configurations including database credentials were managed using .env files.”


👨‍💻 Author

Pankaj Kumar
Backend Developer – Prodigy Tasks


---