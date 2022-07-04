from typing import List


class TodoList(BaseAuditableEntity):

    id: str
    title: str
    items: List[TodoListItem]