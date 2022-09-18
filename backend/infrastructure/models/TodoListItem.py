
from backend.infrastructure.models.Base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, Boolean
from sqlalchemy.orm import relationship

class TodoListItemModel(Base):
    
    id = Column(Integer(), primary_key=True, unique=True)
    list = relationship('TodoList', back_populates="children")
    list_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    created = Column(DateTime(), nullable=False, server_default=func.now())
    modified = Column(DateTime(), nullable=False, server_default=func.now(), onupdate=func.now())
    title = Column(String(255), nullable=False)
    note = Column(Boolean(), nullable=False)
    is_done: bool

    def __repr__(self):
        return '<ExampleModel %r>' % self.id
