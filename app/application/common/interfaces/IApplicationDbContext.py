from abc import ABC, abstractmethod
from app.domain.entities.TodoList import TodoList
from app.domain.entities.TodoListItem import TodoListItem


class IApplicationDbContext(ABC):

    TodoLists: set[TodoList]
    TodoListItems: set[TodoListItem]

    @abstractmethod
    async def save_changes_async(self):
        pass