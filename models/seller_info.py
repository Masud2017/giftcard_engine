from pydantic import BaseModel

class SellerInfo(BaseModel):
    first_name:str
    second_name:str
    bank_ibn:str
    card_number:str
    pin:str