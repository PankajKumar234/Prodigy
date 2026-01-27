# PRODIGY_BD_01 – User CRUD REST API (In-Memory)

## 📌 Project Overview

This project implements a **RESTful API** to perform **basic CRUD (Create, Read, Update, Delete) operations** on a **User resource** using **Flask**.

The API uses an **in-memory data structure (Python dictionary)** to store user data and demonstrates proper REST principles, input validation, error handling, and HTTP status codes.

This task is part of the **Prodigy Backend Development series**.

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **UUID** (for unique user identification)
- **In-memory storage (HashMap equivalent)**

---

## 📁 Project Structure

Prodigy/PRODIGY_BD_01/
        ├── app.py
        ├── requirements.txt
        └── README.md

---

## 👤 User Model

Each user has the following fields:

| Field | Type | Description |
|------|------|------------|
| id | UUID (string) | Unique user identifier |
| name | String | User's name |
| email | String | User's email (validated) |
| age | Integer | User's age (must be > 0) |

---

## 🔗 API Endpoints

### ➕ Create User
**POST** `/users`

**Request Body (JSON):**
```json
{
  "name": "Pankaj Kumar",
  "email": "pankaj@gmail.com",
  "age": 25
}

Response: 201 Created

📄 Get All Users
GET /users

Response: 200 OK

🔍 Get User by ID
GET /users/<id>

Response:
200 OK (if found)
404 Not Found (if not found)

✏️ Update User
PUT /users/<id>

Request Body (JSON):
{
  "name": "Updated Name",
  "email": "updated@gmail.com",
  "age": 30
}

Response:
200 OK
404 Not Found

❌ Delete User
DELETE /users/<id>

Response:
200 OK
404 Not Found

✅ Input Validation

The API includes basic validation:
Name must be a string
Email must be in valid format
Age must be a positive integer

Invalid requests return:
400 Bad Request

⚠️ Error Handling
Scenario                 HTTP Status
Invalid input	            400
User not found	            404
Successful creation	        201
Successful operation	    200


▶️ How to Run the Project

1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the server
python app.py


Server will start at:
http://127.0.0.1:5000

🧪 Testing the API

Use Postman, Thunder Client, or curl to test POST, PUT, and DELETE requests.

Example:
GET http://127.0.0.1:5000/users

📝 Notes

This project uses in-memory storage, so all data will be lost when the server restarts.
Designed for learning and demonstration purposes.
Persistent storage is implemented in PRODIGY_BD_02.

📌 Task Status

✅ CRUD operations implemented
✅ Proper status codes used
✅ Input validation added
✅ Error handling covered

👨‍💻 Author

Pankaj Kumar
Backend Developer – Prodigy Tasks


---