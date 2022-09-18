
from backend.infrastructure.models.Base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

class TodoList(Base):
    
    id = Column(Integer(), primary_key=True, unique=True)
    title = Column(String(255), nullable=False)
    items = relationship("TodoListItem", back_populates="parent")
    

    def __repr__(self):
        return '<ExampleModel %r>' % self.id
