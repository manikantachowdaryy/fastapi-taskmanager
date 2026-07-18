from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app import models, schemas, crud
from app.auth import (
    router as auth_router,
    get_current_user,
    require_admin,
    require_manager_or_admin
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Project Management API",
    description="Project Management System with RBAC",
    version="3.0.0"
)

app.include_router(auth_router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "Project Management API with RBAC",
        "docs": "/docs"
    }


# --------------------------
# PROJECTS
# --------------------------

@app.post(
    "/projects",
    response_model=schemas.ProjectResponse,
    status_code=status.HTTP_201_CREATED
)
def create_project(
    project: schemas.ProjectCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_manager_or_admin)
):
    return crud.create_project(
        db,
        project,
        current_user.id
    )


@app.get(
    "/projects",
    response_model=list[schemas.ProjectResponse]
)
def get_projects(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_projects(db)


@app.get(
    "/projects/{project_id}",
    response_model=schemas.ProjectResponse
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    project = crud.get_project(db, project_id)

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


@app.put(
    "/projects/{project_id}",
    response_model=schemas.ProjectResponse
)
def update_project(
    project_id: int,
    project: schemas.ProjectCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_manager_or_admin)
):
    updated = crud.update_project(
        db,
        project_id,
        project
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return updated


@app.delete("/projects/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_admin)
):
    deleted = crud.delete_project(
        db,
        project_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "message": "Project deleted successfully"
    }


# --------------------------
# PROJECT MEMBERS
# --------------------------

@app.post(
    "/projects/{project_id}/members",
    response_model=schemas.ProjectMemberResponse
)
def add_member(
    project_id: int,
    member: schemas.ProjectMemberCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_manager_or_admin)
):
    project_member = crud.add_member(
        db,
        project_id,
        member
    )

    if project_member is None:
        raise HTTPException(
            status_code=404,
            detail="Project or User not found"
        )

    return project_member


@app.get(
    "/projects/{project_id}/members",
    response_model=list[schemas.ProjectMemberResponse]
)
def get_members(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_project_members(
        db,
        project_id
    )


# --------------------------
# TASKS
# --------------------------

@app.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_manager_or_admin)
):
    return crud.create_task(
        db,
        task
    )


@app.get(
    "/tasks",
    response_model=list[schemas.TaskResponse]
)
def get_tasks(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_tasks(db)


@app.get(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    task = crud.get_task(
        db,
        task_id
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.put(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)
def update_task(
    task_id: int,
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    updated = crud.update_task(
        db,
        task_id,
        task
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated


@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_manager_or_admin)
):
    deleted = crud.delete_task(
        db,
        task_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }