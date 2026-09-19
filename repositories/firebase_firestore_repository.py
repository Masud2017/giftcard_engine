from configs.config import firestore_db
from models.seller_info import SellerInfo
import traceback


def add_thuis_card_info(seller_info:SellerInfo):
    try:
        firestore_db.collection("thuis_card_collection").add({
                "card_number": seller_info.card_number,
                "card_pin": seller_info.pin,
                "first_name": seller_info.first_name,
                "second_name": seller_info.second_name,
                "ibn": seller_info.bank_ibn,
                "status":seller_info.status
                })
        
        # firestore_db.collection("thuis_card_collection").add(seller_info.model_dump_json())
        
    except Exception as e:
        print(traceback.format_exc())