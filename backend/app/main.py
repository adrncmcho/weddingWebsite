# FastAPI imports
from fastapi import FastAPI, UploadFile, File, Header, HTTPException

# Firebase Admin
import firebase_admin
from firebase_admin import credentials, auth

# Your service modules
# Relative import
from services.firestore_service import log_upload
from services.storage_service import upload_file

app = FastAPI()

@app.post("/upload")
async def upload_endpoint(file: UploadFile = File(...), authorization: str = Header(...)):
    # Verify Firebase token
    id_token = authorization.split(" ")[1]
    decoded_token = auth.verify_id_token(id_token)
    user_id = decoded_token["uid"]

    # Read file contents
    contents = await file.read()

    # Upload file
    file_url = upload_file(user_id, file.filename, contents, file.content_type)

    # Log metadata in Firestore
    log_upload(user_id, file.filename, file_url)

    return {"file_url": file_url}