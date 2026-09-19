from fastapi import APIRouter


gift_card_buying_router = APIRouter()

@gift_card_buying_router.get("/")
def teset():
    return {"data": "GiftCard buying controller is working"}