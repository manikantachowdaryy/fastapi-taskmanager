# Notification & Activity Tracking System

## Overview
This project extends the Project Management API by implementing Notifications, Activity Logs, and Audit Logs using FastAPI, SQLAlchemy ORM, JWT Authentication, and SQLite.

## Features

### Authentication
- User Signup
- User Login
- JWT Authentication
- Get Current User

### Notifications
- View Notifications
- View Unread Notifications
- Mark Notification as Read
- Mark All Notifications as Read
- Delete Notification

### Activity Logs
- Track User Activities
- View All Activities
- View User Activities
- View Project Activities

### Audit Logs
- Track Changes to Projects and Tasks
- Store Old and New Values
- View Audit Logs
- View Audit Logs by Entity

## Technologies Used

- FastAPI
- SQLAlchemy ORM
- SQLite
- JWT Authentication
- Pydantic
- Uvicorn

## API Endpoints

### Authentication
- POST /auth/signup
- POST /auth/login
- GET /auth/me

### Notifications
- GET /notifications
- GET /notifications/unread
- PUT /notifications/{id}/read
- PUT /notifications/read-all
- DELETE /notifications/{id}

### Activities
- GET /activities
- GET /activities/user/{id}
- GET /activities/project/{id}

### Audit Logs
- GET /audit-logs
- GET /audit-logs/{entity_type}/{entity_id}

## How to Run

```bash
git clone <repository-url>

cd fastapi-taskmanager

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 -m uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## Future Improvements

- Email Notifications
- WebSocket Real-Time Notifications
- Export Logs to CSV/PDF
- Notification Preferences
- Docker Support
- Unit Testing