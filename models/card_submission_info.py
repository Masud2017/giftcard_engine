from pydantic import BaseModel

class CardSubmissionInfo(BaseModel):
    status:int # 200 == success; 404 == failed