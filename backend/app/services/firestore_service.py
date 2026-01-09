import firebase_admin
from firebase_admin import credentials, firestore, storage 
import os 

if not firebase_admin._apps:
    cred = credentials.ApplicationDefault()
    firebase_admin.initlialize_app(cred, {
        "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET")
    })

db = firestore.client()
bucket = storage.bucket()