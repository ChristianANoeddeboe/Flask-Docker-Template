from backend.domain.common.BaseAuditableEntity import BaseAuditableEntity
from backend.domain.entities.TodoListItem import TodoListItem


class TodoList(BaseAuditableEntity):

    id: str
    title: str
    items: list[TodoListItem] = []
    
