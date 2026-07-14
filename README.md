# Task Manager API

A simple REST API built using **FastAPI**, **SQLite**, **SQLAlchemy ORM**, and **Pydantic** for managing tasks.

## Features

- Add a new task
- View all tasks
- Update an existing task
- Delete a task
- Automatic API documentation using Swagger UI

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy ORM
- Pydantic

## Project Structure

```
fastapi-taskmanager/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/manikantachowdaryy/fastapi-taskmanager.git
```

### 2. Move into the project folder

```bash
cd fastapi-taskmanager
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Run the FastAPI server

```bash
uvicorn app.main:app --reload
```

## API Documentation

After starting the server, open:

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home endpoint |
| POST | /tasks | Create a task |
| GET | /tasks | Get all tasks |
| PUT | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |

## Sample Request

```json
{
    "title": "Complete Assignment",
    "description": "Submit FastAPI Task Manager",
    "status": "Pending"
}
```

## Author

**Manikanta Chowdary**