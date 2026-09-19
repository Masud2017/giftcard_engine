from pydantic import BaseModel
from typing import Optional

class SellerInfo(BaseModel):
    first_name:str
    second_name:str
    bank_ibn:str
    card_number:str
    pin:str
    status:Optional[str] = None