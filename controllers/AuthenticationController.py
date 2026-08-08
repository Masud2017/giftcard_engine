from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test_router():
    return "Hello world this is a test router"