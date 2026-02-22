from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter()

@router.post("/upload")
def upload_pdf(file:UploadFile=File(...)):
    path=f"uploads/{file.filename}"
    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return {"msg":"uploaded"}