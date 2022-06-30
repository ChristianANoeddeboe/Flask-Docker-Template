from typing import List
from app.core.common.BaseAuditableEntity import BaseAuditableEntity
from app.core.entities.TodoListItem import TodoListItem


class TodoList(BaseAuditableEntity):

    id: str
    title: str
    items: List[TodoListItem]