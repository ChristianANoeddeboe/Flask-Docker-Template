

from typing import Coroutine
from backend.application.common.interfaces.IApplicationDbContext import IApplicationDbContext
from backend.application.common.interfaces.models.DbSet import DbSet
from backend.domain.entities.TodoList import TodoList
from backend.domain.entities.TodoListItem import TodoListItem


class ApplicationDbContext(IApplicationDbContext):

    TodoLists: DbSet[TodoList]
    TodoListItems: DbSet[TodoListItem]

    async def save_changes_async(self, cancellation_token=None) -> Coroutine[int, None, None]:
        pass