from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from ..auth import utils, auth
from ..auth.token_schema import Token
from ..auth.models import User


from ..db import get_db

from sqlmodel import Session, select


from ..auth.utils import pwd_context


router = APIRouter(tags=["Auth"])

@router.post("/login", response_model=Token,summary="Login with email or username",
    description="Accepts either a username or email in the 'username' field and password to authenticate."
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = utils.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/profile", response_model=User)  
async def get_current_user(current_user: User = Depends(auth.get_current_user)):
    return current_user

