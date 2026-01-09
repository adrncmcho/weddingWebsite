from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

# Example in-memory storage route (replace with Firebase later)
photos_storage = []

@router.post("/upload")
async def upload_photo(file: UploadFile = File(...)):
    # Just store filename for now
    if not file.filename.lower().endswith((".jpg", ".jpeg", ".png")):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    photos_storage.append(file.filename)
    return {"filename": file.filename, "message": "Photo uploaded successfully"}

@router.get("/")
async def list_photos():
    return {"photos": photos_storage}
