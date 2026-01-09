from fastapi import APIRouter, HTTPException

router = APIRouter()

# In-memory user list (replace with Firebase later)
users_db = []

@router.post("/create")
async def create_user(username: str):
    if username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db.append(username)
    return {"username": username, "message": "User created successfully"}

@router.get("/")
async def list_users():
    return {"users": users_db}
