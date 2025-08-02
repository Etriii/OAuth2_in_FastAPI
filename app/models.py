from sqlmodel import Field, SQLModel
from sqlalchemy import Column,  String, DateTime
from datetime import datetime
from typing import Optional

class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column(String(255), unique=True, index=True))
    email: str = Field(sa_column=Column(String(255), unique=True, index=True))
    email_verified_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )
    password_hash: str = Field(sa_column=Column(String(1024)))
    profile: str = Field(sa_column=Column(String(255), nullable=True))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )
    updated_by: int = Field(foreign_key="users.id", index=True, nullable=True)
