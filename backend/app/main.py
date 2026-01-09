from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os

from app.api import routes_photos, routes_users

# Load environment variables from .env
load_dotenv()

app = FastAPI(
    title="Photo Upload API",
    version="1.0.0"
)

# Include your routers
app.include_router(routes_photos.router, prefix="/photos", tags=["Photos"])
app.include_router(routes_users.router, prefix="/users", tags=["Users"])

# Mount static files folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Serve favicon to prevent 404s
@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse("app/static/favicon.ico")

# Health check route
@app.get("/")
def health_check():
    return {
        "status": "okay",
        "bucket": os.getenv("FIREBASE_STORAGE_BUCKET")
    }