from models.model_for_authentication import Token
from firebase_admin import auth
from firebase_admin.auth import ExpiredIdTokenError,InvalidIdTokenError
import logging

import traceback



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
    
    
    @staticmethod
    def verify_auth_token(self, auth_token)-> dict:
        try:
            response = auth.verify_id_token(auth_token)
            return response
        except ExpiredIdTokenError as e:
            # Refresh the id token again
            auth.revoke_refresh_tokens()
            traceback.format_exc()
        except ValueError as e:
             traceback.format_exc()
            