from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr



class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: Literal["Admin", "Manager", "Member"]


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True




class ProjectCreate(BaseModel):
    name: str
    description: str


class ProjectResponse(ProjectCreate):
    id: int
    created_by: int
    created_at: datetime

    class Config:
        from_attributes = True




class ProjectMemberCreate(BaseModel):
    user_id: int


class ProjectMemberResponse(BaseModel):
    id: int
    project_id: int
    user_id: int

    class Config:
        from_attributes = True



class TaskCreate(BaseModel):
    title: str
    description: str
    status: Literal["Pending", "In Progress", "Completed"]
    priority: Literal["Low", "Medium", "High"]
    due_date: datetime
    assigned_to: int
    project_id: int


class TaskResponse(TaskCreate):
    id: int

    class Config:
        from_attributes = True


class NotificationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    message: str
    is_read: int
    created_at: datetime

    class Config:
        from_attributes = True




class ActivityLogResponse(BaseModel):
    id: int
    user_id: int
    action: str
    entity_type: str
    entity_id: int
    description: str
    created_at: datetime

    class Config:
        from_attributes = True



class AuditLogResponse(BaseModel):
    id: int
    entity_type: str
    entity_id: int
    field_name: str
    old_value: str | None = None
    new_value: str | None = None
    changed_by: int
    changed_at: datetime

    class Config:
        from_attributes = True