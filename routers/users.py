from fastapi import APIRouter, Depends

from models.user import User
from dependencies import get_current_user


router = APIRouter()


@router.get("/profile")
def get_profile(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "name": current_user.name
    }