from sqlalchemy.orm import Session

from . import models, schemas


# -----------------------------
# PROJECTS
# -----------------------------

def create_project(
    db: Session,
    project: schemas.ProjectCreate,
    current_user_id: int
):
    new_project = models.Project(
        name=project.name,
        description=project.description,
        created_by=current_user_id
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


def get_projects(db: Session):
    return db.query(models.Project).all()


def get_project(
    db: Session,
    project_id: int
):
    return (
        db.query(models.Project)
        .filter(models.Project.id == project_id)
        .first()
    )


def update_project(
    db: Session,
    project_id: int,
    project: schemas.ProjectCreate
):
    existing = get_project(db, project_id)

    if existing is None:
        return None

    existing.name = project.name
    existing.description = project.description

    db.commit()
    db.refresh(existing)

    return existing


def delete_project(
    db: Session,
    project_id: int
):
    project = get_project(db, project_id)

    if project is None:
        return None

    db.delete(project)
    db.commit()

    return project


# -----------------------------
# PROJECT MEMBERS
# -----------------------------

def add_member(
    db: Session,
    project_id: int,
    member: schemas.ProjectMemberCreate
):
    project = get_project(db, project_id)

    if project is None:
        return None

    user = (
        db.query(models.User)
        .filter(models.User.id == member.user_id)
        .first()
    )

    if user is None:
        return None

    project_member = models.ProjectMember(
        project_id=project_id,
        user_id=member.user_id
    )

    db.add(project_member)
    db.commit()
    db.refresh(project_member)

    return project_member


def get_project_members(
    db: Session,
    project_id: int
):
    return (
        db.query(models.ProjectMember)
        .filter(
            models.ProjectMember.project_id == project_id
        )
        .all()
    )


# -----------------------------
# TASKS
# -----------------------------

def create_task(
    db: Session,
    task: schemas.TaskCreate
):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        due_date=task.due_date,
        assigned_to=task.assigned_to,
        project_id=task.project_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_tasks(db: Session):
    return db.query(models.Task).all()


def get_task(
    db: Session,
    task_id: int
):
    return (
        db.query(models.Task)
        .filter(models.Task.id == task_id)
        .first()
    )


def update_task(
    db: Session,
    task_id: int,
    task: schemas.TaskCreate
):
    existing = get_task(db, task_id)

    if existing is None:
        return None

    existing.title = task.title
    existing.description = task.description
    existing.status = task.status
    existing.priority = task.priority
    existing.due_date = task.due_date
    existing.assigned_to = task.assigned_to
    existing.project_id = task.project_id

    db.commit()
    db.refresh(existing)

    return existing


def delete_task(
    db: Session,
    task_id: int
):
    task = get_task(db, task_id)

    if task is None:
        return None

    db.delete(task)
    db.commit()

    return task