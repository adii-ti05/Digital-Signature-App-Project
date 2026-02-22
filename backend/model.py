from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


# ================= USER MODEL =================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    documents = relationship(
        "Document",
        back_populates="owner",
        cascade="all, delete"
    )

    signatures = relationship(
        "Signature",
        back_populates="user",
        cascade="all, delete"
    )

    logs = relationship(
        "AuditLog",
        back_populates="user",
        cascade="all, delete"
    )


# ================= DOCUMENT MODEL =================

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    status = Column(String, default="pending")  # pending / signed
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    uploaded_by = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="documents")

    signatures = relationship(
        "Signature",
        back_populates="document",
        cascade="all, delete"
    )

    logs = relationship(
        "AuditLog",
        back_populates="document",
        cascade="all, delete"
    )


# ================= SIGNATURE MODEL =================

class Signature(Base):
    __tablename__ = "signatures"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(Integer, ForeignKey("documents.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    x_position = Column(Float)       # Signature X coordinate
    y_position = Column(Float)       # Signature Y coordinate
    page_number = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)

    document = relationship("Document", back_populates="signatures")
    user = relationship("User", back_populates="signatures")


# ================= AUDIT LOG MODEL =================

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    document_id = Column(Integer, ForeignKey("documents.id"))

    action = Column(String)  # upload / sign / download
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="logs")
    document = relationship("Document", back_populates="logs")