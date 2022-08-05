
from backend.infrastructure.models.BaseModel import BaseModel


class TodoListItemModel(BaseModel):

    __tablename__ = 'TODOLISTITEMS'
    
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    children = db.relationship('ExampleChildModel', backref='parent', lazy=True)
    list_id = db.Column(db.ForeignKey('users.id'), nullable=False, index=True)
    created = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    modified = db.Column(db.DateTime(), nullable=False, server_default=func.now(), onupdate=func.now())
    title = db.Column(db.String(255), nullable=False)
    note = db.Column(db.String(255), nullable=False)
    

    def __repr__(self):
        return '<ExampleModel %r>' % self.id
