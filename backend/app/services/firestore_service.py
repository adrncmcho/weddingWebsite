from firebase_admin import firestore

db = firestore.client()

def log_upload(user_id, file_name, file_url):
    db.collection("uploads").add({
        "userId": user_id,
        "fileName": file_name,
        "fileUrl": file_url,
        "uploadedAt": firestore.SERVER_TIMESTAMP
    })