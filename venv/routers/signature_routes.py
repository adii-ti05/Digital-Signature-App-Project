from fastapi import APIRouter
import fitz
import base64
from io import BytesIO
import os

router = APIRouter()

@router.post("/finalize")
def finalize_signature(data: dict):

    filename = data["filename"]
    x = data["x"]
    y = data["y"]
    size = int(data["size"])
    image_data = data["image"]

    file_path = f"uploads/{filename}"

   
    doc = fitz.open(file_path)
    page = doc[0]

    rect = fitz.Rect(x, y, x + size, y + size)

  
    output = f"uploads/signed_{filename}"
    doc.save(output)

    return {"msg": "signed", "file": output}