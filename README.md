# FastAPI Task Manager

This is a simple Task Manager API developed using Python and FastAPI as part of a backend assignment.

The application allows users to:

- Add a new task
- View all tasks
- Update an existing task
- Delete a task

The project uses SQLite as the database, SQLAlchemy as the ORM, and Pydantic for request validation.

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic

## Project Structure

```
fastapi-taskmanager
│
├── app
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

## How to Run

Clone the repository:

```bash
git clone https://github.com/manikantachowdaryy/fastapi-taskmanager.git
```

Move into the project folder:

```bash
cd fastapi-taskmanager
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

**macOS/Linux**

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
uvicorn app.main:app --reload
```

Open the browser and go to:

```
http://127.0.0.1:8000/docs
```

to test the APIs using Swagger UI.

## API Endpoints

- POST /tasks
- GET /tasks
- PUT /tasks/{task_id}
- DELETE /tasks/{task_id}

## Author

Manikanta Chowdary