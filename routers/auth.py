from fastapi import APIRouter, HTTPException

from database import SessionLocal
from models.user import User
from schemas.user import UserLogReg
from services.auth import (
    create_access_token,
    get_password_hash,
    verify_password
)


router = APIRouter()


@router.post("/register")
def register_user(user: UserLogReg):
    hashed_password = get_password_hash(user.password)

    with SessionLocal() as session:
        session.add(User(
            name=user.name,
            hashed_password=hashed_password
        ))
        session.commit()

    return {"message": "Register Successful"}


@router.post("/login")
def login_user(user_data: UserLogReg):
    with SessionLocal() as session:
        user = session.query(User).filter(
            User.name == user_data.name
        ).first()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Incorrect username or password"
            )

        if not verify_password(user_data.password, user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="Incorrect username or password"
            )

        return {
            "access_token": create_access_token(user.id),
            "token_type": "bearer"
        }