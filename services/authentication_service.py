from models.model_for_authentication import Token
from firebase_admin import auth
import logging


class AuthenticationService:
    def __init__(self):
        pass
    
    
    @staticmethod
    def authenticate(self,access_token) -> Token:
        try:
            auth.verify_id_token(access_token = access_token)
        except:
            pass
        
        return Token(access_token="asdflkjasdlkfj", token_type = "sdfsdf")