from fastapi import APIRouter
from models.seller_info import SellerInfo
from models.card_submission_info import CardSubmissionInfo


gift_card_buying_router = APIRouter()

@gift_card_buying_router.get("/")
def teset():
    return {"data": "GiftCard buying controller is working"}

@gift_card_buying_router.post("/submit_thuis_card_info")
def submit_thuis_card_info(seller_information:SellerInfo) -> CardSubmissionInfo:
    return CardSubmissionInfo(status=200)