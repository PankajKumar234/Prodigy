# 🚀 Prodigy InfoTech – Backend Development Tasks

This repository contains all **Backend Development tasks** completed as part of the **Prodigy InfoTech Internship Program**.  
Each task is implemented as an **independent backend project** following best practices in API design, security, and documentation.

---

## 🧩 Tasks Overview

| Task ID | Project Name | Description |
|-------|-------------|-------------|
| **PRODIGY_BD_01** | Authentication System | User registration, login, JWT authentication |
| **PRODIGY_BD_02** | RESTful API | CRUD-based REST API with proper validation |
| **PRODIGY_BD_03** | Role-Based Access Control | Permissions, user roles, protected routes |
| **PRODIGY_BD_04** | Secure Backend API | JWT, password hashing, protected endpoints |
| **PRODIGY_BD_05** | Booking System API | Room booking, cancellation, conflict prevention |

Each task resides in its **own folder** with:
- Independent codebase
- Dedicated `.env` configuration
- Separate README for project-specific details

---

## 🛠 Tech Stack Used

- **Backend Framework:** Flask (Python)
- **Database:** PostgreSQL / SQLite
- **Authentication:** JWT (Flask-JWT-Extended)
- **ORM:** SQLAlchemy
- **Environment Management:** python-dotenv
- **API Testing:** Postman
- **Version Control:** Git & GitHub

---

## 📁 Repository Structure
```
Prodigy/
       └── PRODIGY_BD_01/
       ├── PRODIGY_BD_02/
       ├── PRODIGY_BD_03/
       ├── PRODIGY_BD_04/
       ├── PRODIGY_BD_05/
       └── README.md
```

> ⚠️ **Note:** All `.env` files are excluded using `.gitignore` to ensure security.

---

## ▶️ How to Run Any Task Locally

__1.__ Navigate to the task folder:  
```
cd PRODIGY_BD_05
```

__2.__ Create a virtual environment:  
```
python -m venv venv  
venv\Scripts\activate   # Windows
```

__3.__ Install dependencies:  
```
pip install -r requirements.txt
```

__4.__ Create .env file:  
```
FLASK_APP=app.py  
FLASK_ENV=development  
JWT_SECRET_KEY=your_secret_key  
DATABASE_URL=your_database_url  
```

__5.__ Run the server:  
```
python app.py
```

**🔐 Security Practices Followed**
- JWT-based authentication
- Password hashing
- Role-based access control
- Secure environment variable handling
- API-level validation and error handling

**📄 Documentation**
- Each task folder contains its own README
- API endpoints documented with request/response samples
- Postman collections used for testing

**👨‍💻 Author**

Pankaj Kumar  
Backend Developer | Python | Flask | Databases
