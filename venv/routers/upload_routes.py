from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import shutil
import os
import uuid

from model import Document, User, AuditLog
from auth import get_current_user   

router = APIRouter()

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


# -------------------------
# DB Dependency
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------
# Upload PDF
# -------------------------
@router.post("/upload")
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Validate file type properly
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    # Unique filename generate karo
    unique_name = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Save document in DB
    new_doc = Document(
        filename=file.filename,
        file_path=file_path,
        uploaded_by=current_user.id
    )

    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    # Create audit log
    log = AuditLog(
        user_id=current_user.id,
        document_id=new_doc.id,
        action="upload"
    )

    db.add(log)
    db.commit()

    return {
        "message": "File uploaded successfully",
        "id": new_doc.id
    }


# -------------------------
# Get User Specific Docs
# -------------------------
@router.get("/my-documents")
def get_my_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    documents = db.query(Document).filter(
        Document.uploaded_by == current_user.id
    ).all()

    return documents