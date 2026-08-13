import firebase_admin
from firebase_admin import credentials
from firebase_admin.firestore import firestore
import os

firebase_credential_path = os.path.join(os.path.abspath(os.curdir),"firebase_config.json")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = firebase_credential_path


cred = credentials.Certificate(firebase_credential_path)
app = firebase_admin.initialize_app(cred) # keeping the instance for later use

firestore_db = firestore.Client()

