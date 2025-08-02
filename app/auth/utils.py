from passlib.context import CryptContext

from sqlmodel import Session, select, or_

from .models import UserInDB
from app.models import User as UserDB

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(username: str, db: Session):
    statement = select(UserDB).where(
    or_(UserDB.username == username, UserDB.email == username)
    )
    
    user = db.exec(statement).first()

    if user:
        return UserInDB(
            id=user.id,
            username=user.username,
            email=user.email,
            email_verified_at=user.email_verified_at,
            hashed_password=user.hashed_password,
            profile=user.profile,
            created_at = user.created_at,
            udpated_at = user.updated_at
            #mag add day dapat kog status sa user hahaha (for reminder lang para maka adjust ko sa user model)
        )

    return None


def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username, db)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user
