from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routers.auth_routes import router as auth_router
from routers.upload_routes import router as upload_router
from routers.signature_routes import router as signature_router


app = FastAPI()

# -----------------------------
# CORS CONFIGURATION (ADD HERE)
# -----------------------------

origins = [
    "http://localhost:3000",      # Next.js frontend
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],     # Allow all HTTP methods
    allow_headers=["*"],     # Allow all headers
)

# -----------------------------
# CREATE DATABASE TABLES
# -----------------------------
Base.metadata.create_all(bind=engine)

# -----------------------------
# INCLUDE ROUTERS
# -----------------------------
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(upload_router, prefix="/api/docs", tags=["Docs"])
app.include_router(signature_router, prefix="/api/signatures", tags=["Signature"])

# -----------------------------
# STATIC FILES
# -----------------------------
app.mount("/app", StaticFiles(directory="frontend", html=True), name="frontend")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.get("/")
def home():
    return {"msg": "API WORKING"}






