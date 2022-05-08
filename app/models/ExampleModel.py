"""Data models."""
from sqlalchemy import func
import enum
from app.configs.DB import db
from sqlalchemy_serializer import SerializerMixin

class StatusEnum(enum.Enum):
    New = 'New'
    Operational = 'Operational'
    Error = 'Error'

class ExampleModel(db.Model, SerializerMixin):
    __tablename__ = 'examples'
    
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False, index=True)
    created = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    modified = db.Column(db.DateTime(), nullable=False, server_default=func.now(), onupdate=func.now())
    status = db.Column(db.Enum(StatusEnum), nullable=False, server_default="Init")
    children = db.relationship('ExampleChildModel', backref='parent', lazy=True)

    def __repr__(self):
        return '<ExampleModel %r>' % self.id