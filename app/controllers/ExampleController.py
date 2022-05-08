from typing import List
from app.models.ExampleModel import ExampleModel
from app.configs.DB import db

def get_examples() -> List[ExampleModel]:
    examples = ExampleModel.query.all()
    return examples

def get_example(id) -> ExampleModel:
    example = ExampleModel.query.get(id)
    return example

def create_example(name, user_id):
    example = ExampleModel(name=name, user_id=user_id)
    db.session.add(example)
    return example

def update_example(id, changes):
    example = ExampleModel.query.filter_by(id=id).update(changes)
    db.session.commit()
    return example

def delete_example(id):
    example = ExampleModel.query.filter_by(id=id).delete()
    db.session.commit()
    return example