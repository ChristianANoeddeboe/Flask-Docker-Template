"""Data models."""
from app.configs.DB import db
from sqlalchemy.sql import func
import enum
from sqlalchemy_serializer import SerializerMixin

class RoleEnum(enum.Enum):
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'
    USER = 'USER'

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, unique=True)
    username = db.Column(db.String(16), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(500), nullable=False)
    created = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    modified = db.Column(db.DateTime(), nullable=False, server_default=func.now(), onupdate=func.now())
    active = db.Column(db.Boolean(), nullable=False, server_default=True)
    role = db.Column(db.Enum(RoleEnum), server_default="USER")