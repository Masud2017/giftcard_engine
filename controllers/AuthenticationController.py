from fastapi import APIRouter
from models.user import User
from configs.config import firebase_admin

router = APIRouter()

@router.get("/test")
async def test_router():
    return "Hello world this is a test router"


@router.post({"register_user_pass"})
def register_user_pass(user: User):
    pass