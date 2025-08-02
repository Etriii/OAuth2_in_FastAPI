from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int | None = None
    username: str | None = None
    email: str | None = None
    email_verified_at: datetime | None = None
    profile: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    
class UserInDB(User):
    password_hash: str
