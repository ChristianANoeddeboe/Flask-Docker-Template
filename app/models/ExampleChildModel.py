"""Data models."""
from sqlalchemy import func
import enum
from app.configs.DB import db
from sqlalchemy_serializer import SerializerMixin

class ExampleChildModel(db.Model, SerializerMixin):
    __tablename__ = 'children'
    
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    value = db.Column(db.Integer())
    parent_id = db.Column(db.ForeignKey('examples.id'), nullable=False, index=True)
    created = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    modified = db.Column(db.DateTime(), nullable=False, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return '<ExampleChildModel %r>' % self.id