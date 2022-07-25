from abc import ABC, abstractmethod
from backend.domain.entities.TodoList import TodoList
from backend.domain.entities.TodoListItem import TodoListItem


class IApplicationDbContext(ABC):

    TodoLists: set[TodoList]
    TodoListItems: set[TodoListItem]

    @abstractmethod
    async def save_changes_async(self):
        pass