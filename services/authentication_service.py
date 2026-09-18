from models.model_for_authentication import Token
from firebase_admin import auth
import logging

class AuthenticationService:
    def __init__(self):
        pass
    
    @staticmethod
    def register(email:str,  password:str) -> bool:
        try:
            auth.create_user(email = email, password = password)
            link = auth.generate_email_verification_link(email=email)
            logging.info(link)
            print("Printing the stuff: ", link)
            return True
        except:
            return False
    @staticmethod
    def authenticate(self,user:str, password:str) -> Token:
        userid = auth.get_user_by_email(user = user)
        
        return Token(access_token="asdflkjasdlkfj", token_type = "sdfsdf")