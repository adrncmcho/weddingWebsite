from firebase_admin import storage

bucket = storage.bucket()

def upload_file(user_id, file_name, file_content, content_type):
    blob = bucket.blob(f"uploads/{user_id}/{file_name}")
    blob.upload_from_string(file_content, content_type=content_type)
    blob.make_public()  # optional
    return blob.public_url