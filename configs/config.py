import firebase_admin
from firebase_admin import credentials
import os

python = os.path.join(os.path.abspath(os.curdir),"firebase_config.json")

cred = credentials.Certificate(python)
firebase_admin.initialize_app(cred)

