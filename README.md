# Project Management API with Role-Based Access Control (RBAC)

## Overview

This project is a backend REST API developed using FastAPI that provides secure project and task management with JWT Authentication and Role-Based Access Control (RBAC).

The application allows users to create projects, manage project members, assign tasks, and perform role-based operations based on their permissions.

---

## Features

### Authentication

- User Signup
- User Login
- JWT Authentication
- Current User API (/auth/me)

### User Roles

- Admin
- Manager
- Member

### Project Management

- Create Project
- View All Projects
- View Project by ID
- Update Project
- Delete Project

### Project Members

- Add Users to Projects
- View Project Members

### Task Management

- Create Task
- View All Tasks
- View Task by ID
- Update Task
- Delete Task

### Role-Based Access Control

#### Admin

- Create Projects
- Update Projects
- Delete Projects
- Manage Users
- View All Projects
- View All Tasks

#### Manager

- Create Projects
- Assign Tasks
- Reassign Tasks
- Update Projects
- Add Members to Projects

#### Member

- View Assigned Projects
- View Assigned Tasks
- Update Task Status

---

## Technologies Used

- FastAPI
- Python 3
- SQLAlchemy ORM
- SQLite
- Pydantic
- JWT Authentication
- Uvicorn

---

## Project Structure

```
fastapi-taskmanager/

│── app/
│   ├── auth.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── screenshots/
├── task_manager.db
├── requirements.txt
└── README.md
```

---

## Database Tables

### Users

- id
- full_name
- email
- hashed_password
- role
- created_at

### Projects

- id
- name
- description
- created_by
- created_at

### Project Members

- id
- project_id
- user_id

### Tasks

- id
- title
- description
- status
- priority
- due_date
- assigned_to
- project_id

---

## API Endpoints

### Authentication

| Method | Endpoint |
|---------|----------|
| POST | /auth/signup |
| POST | /auth/login |
| GET | /auth/me |

### Projects

| Method | Endpoint |
|---------|----------|
| POST | /projects |
| GET | /projects |
| GET | /projects/{id} |
| PUT | /projects/{id} |
| DELETE | /projects/{id} |

### Project Members

| Method | Endpoint |
|---------|----------|
| POST | /projects/{id}/members |
| GET | /projects/{id}/members |

### Tasks

| Method | Endpoint |
|---------|----------|
| POST | /tasks |
| GET | /tasks |
| GET | /tasks/{id} |
| PUT | /tasks/{id} |
| DELETE | /tasks/{id} |

---

## Installation

Clone the repository

```bash
git clone https://github.com/manikantachowdaryy/fastapi-taskmanager.git
```

Go to the project directory

```bash
cd fastapi-taskmanager
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python3 -m uvicorn app.main:app --reload
```

Open Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Authentication

The application uses JWT Authentication.

1. Register a new user.
2. Login using email and password.
3. Copy the access token.
4. Click **Authorize** in Swagger.
5. Authenticate and access protected APIs.

---

## Testing

The APIs were tested using:

- Swagger UI
- Postman

---

## Screenshots

Swagger documentation screenshots are available in the **screenshots** folder.

---

## Author

**Manikanta Kancheti**

Backend Developer Assignment

FastAPI | SQLAlchemy | JWT | RBAC