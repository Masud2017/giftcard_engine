from fastapi import APIRouter
from models.seller_info import SellerInfo
from models.card_submission_info import CardSubmissionInfo
from repositories import firebase_firestore_repository

gift_card_buying_router = APIRouter()

@gift_card_buying_router.get("/")
def teset():
    return {"data": "GiftCard buying controller is working"}

@gift_card_buying_router.post("/submit_thuis_card_info")
def submit_thuis_card_info(seller_information:SellerInfo) -> CardSubmissionInfo:
    try:
        seller_information.status = "Pending"
        firebase_firestore_repository.add_thuis_card_info(seller_info=seller_information)
        print(seller_information.model_dump_json())
        return CardSubmissionInfo(status=200)
    except Exception as e:
        import traceback; traceback.format_exc(e)
        return CardSubmissionInfo(status=404)
