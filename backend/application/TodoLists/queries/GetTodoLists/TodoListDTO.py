
from backend.application.TodoLists.queries.GetTodoLists.TodoListItemDTO import TodoListItemDTO


class TodoListDTO():

    id: int
    title: str
    items: list[TodoListItemDTO] = []