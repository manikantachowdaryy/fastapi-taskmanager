from sqlalchemy.orm import Session

from . import models, schemas



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

    create_activity(
        db,
        current_user_id,
        "Project Created",
        "Project",
        new_project.id,
        f"Created project '{new_project.name}'"
    )

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

    old_description = existing.description

    existing.name = project.name
    existing.description = project.description

    db.commit()
    db.refresh(existing)

    create_activity(
        db,
        existing.created_by,
        "Project Updated",
        "Project",
        existing.id,
        f"Updated project '{existing.name}'"
    )

    create_audit_log(
        db,
        "Project",
        existing.id,
        "description",
        old_description,
        existing.description,
        existing.created_by
    )

    return existing


def delete_project(
    db: Session,
    project_id: int
):
    project = get_project(db, project_id)

    if project is None:
        return None

    create_activity(
        db,
        project.created_by,
        "Project Deleted",
        "Project",
        project.id,
        f"Deleted project '{project.name}'"
    )

    db.delete(project)
    db.commit()

    return project



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

    create_notification(
        db,
        member.user_id,
        "Project Added",
        f"You were added to project '{project.name}'"
    )

    create_activity(
        db,
        project.created_by,
        "Member Added",
        "Project",
        project.id,
        f"Added {user.full_name} to project"
    )

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

    create_notification(
        db,
        task.assigned_to,
        "New Task Assigned",
        f"You have been assigned '{task.title}'"
    )

    create_activity(
        db,
        task.assigned_to,
        "Task Created",
        "Task",
        new_task.id,
        f"Task '{task.title}' created"
    )

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

    old_status = existing.status

    existing.title = task.title
    existing.description = task.description
    existing.status = task.status
    existing.priority = task.priority
    existing.due_date = task.due_date
    existing.assigned_to = task.assigned_to
    existing.project_id = task.project_id

    db.commit()
    db.refresh(existing)

    create_activity(
        db,
        existing.assigned_to,
        "Task Updated",
        "Task",
        existing.id,
        f"Updated task '{existing.title}'"
    )

    if old_status != existing.status:
        create_notification(
            db,
            existing.assigned_to,
            "Task Status Updated",
            f"Task '{existing.title}' changed from {old_status} to {existing.status}"
        )

        create_audit_log(
            db,
            "Task",
            existing.id,
            "status",
            old_status,
            existing.status,
            existing.assigned_to
        )

    return existing

def delete_task(
    db: Session,
    task_id: int
):
    task = get_task(db, task_id)

    if task is None:
        return None

    create_activity(
        db,
        task.assigned_to,
        "Task Deleted",
        "Task",
        task.id,
        f"Deleted task '{task.title}'"
    )

    db.delete(task)
    db.commit()

    return task

def create_notification(
    db: Session,
    user_id: int,
    title: str,
    message: str
):
    notification = models.Notification(
        user_id=user_id,
        title=title,
        message=message
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return notification


def get_notifications(
    db: Session,
    user_id: int
):
    return (
        db.query(models.Notification)
        .filter(models.Notification.user_id == user_id)
        .order_by(models.Notification.created_at.desc())
        .all()
    )


def get_unread_notifications(
    db: Session,
    user_id: int
):
    return (
        db.query(models.Notification)
        .filter(
            models.Notification.user_id == user_id,
            models.Notification.is_read == 0
        )
        .all()
    )


def mark_notification_read(
    db: Session,
    notification_id: int,
    user_id: int
):
    notification = (
        db.query(models.Notification)
        .filter(
            models.Notification.id == notification_id,
            models.Notification.user_id == user_id
        )
        .first()
    )

    if notification is None:
        return None

    notification.is_read = 1

    db.commit()
    db.refresh(notification)

    return notification


def mark_all_notifications_read(
    db: Session,
    user_id: int
):
    notifications = (
        db.query(models.Notification)
        .filter(models.Notification.user_id == user_id)
        .all()
    )

    for notification in notifications:
        notification.is_read = 1

    db.commit()

    return notifications


def delete_notification(
    db: Session,
    notification_id: int,
    user_id: int
):
    notification = (
        db.query(models.Notification)
        .filter(
            models.Notification.id == notification_id,
            models.Notification.user_id == user_id
        )
        .first()
    )

    if notification is None:
        return None

    db.delete(notification)
    db.commit()

    return notification

def create_activity(
    db: Session,
    user_id: int,
    action: str,
    entity_type: str,
    entity_id: int,
    description: str
):
    activity = models.ActivityLog(
        user_id=user_id,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        description=description
    )

    db.add(activity)
    db.commit()
    db.refresh(activity)

    return activity


def get_all_activities(db: Session):
    return (
        db.query(models.ActivityLog)
        .order_by(models.ActivityLog.created_at.desc())
        .all()
    )


def get_user_activities(
    db: Session,
    user_id: int
):
    return (
        db.query(models.ActivityLog)
        .filter(models.ActivityLog.user_id == user_id)
        .order_by(models.ActivityLog.created_at.desc())
        .all()
    )


def get_project_activities(
    db: Session,
    project_id: int
):
    return (
        db.query(models.ActivityLog)
        .filter(
            models.ActivityLog.entity_type == "Project",
            models.ActivityLog.entity_id == project_id
        )
        .order_by(models.ActivityLog.created_at.desc())
        .all()
    )

def create_audit_log(
    db: Session,
    entity_type: str,
    entity_id: int,
    field_name: str,
    old_value: str,
    new_value: str,
    changed_by: int
):
    audit = models.AuditLog(
        entity_type=entity_type,
        entity_id=entity_id,
        field_name=field_name,
        old_value=old_value,
        new_value=new_value,
        changed_by=changed_by
    )

    db.add(audit)
    db.commit()
    db.refresh(audit)

    return audit


def get_all_audit_logs(db: Session):
    return (
        db.query(models.AuditLog)
        .order_by(models.AuditLog.changed_at.desc())
        .all()
    )


def get_entity_audit_logs(
    db: Session,
    entity_type: str,
    entity_id: int
):
    return (
        db.query(models.AuditLog)
        .filter(
            models.AuditLog.entity_type == entity_type,
            models.AuditLog.entity_id == entity_id
        )
        .order_by(models.AuditLog.changed_at.desc())
        .all()
    )