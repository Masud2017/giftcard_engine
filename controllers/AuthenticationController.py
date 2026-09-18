from fastapi import APIRouter
from models.user import User
from configs.config import firebase_admin

from models.model_for_authentication import Token
from services.authentication_service import AuthenticationService

router = APIRouter()

@router.get("/test")
async def test_router():
    return "Hello world this is a test router"


@router.post("/register_user_pass")
def register_user_pass(user: User)-> bool:
    return AuthenticationService.register(email=user.username, password=user.password)

@router.get("/authenticate")
def authenticate() -> Token:
    return AuthenticationService.authenticate()

@router.get("verify")
def verify()->bool:
    return False