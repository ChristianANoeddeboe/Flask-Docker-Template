from typing import Optional
from Medipy.IRequestHandler import IRequestHandler
from backend.application.common.interfaces.IApplicationDbContext import IApplicationDbContext
from backend.domain.entities.TodoList import TodoList


from backend.application.TodoLists.queries.GetTodoLists.TodoListsVM import TodoListsVM


class GetTodoListsQuery(TodoListsVM):
    
    def __init__(self) -> None:
        super().__init__()

class GetTodoListsQueryHandler(IRequestHandler[GetTodoListsQuery, TodoListsVM]):

    __context: IApplicationDbContext

    def __init__(self, context: IApplicationDbContext):
        self.__context = context

    async def handle(self, request: GetTodoListsQuery, cancellation_token=None) -> TodoListsVM:
        res = TodoListsVM()
        res.lists = self.__context.TodoLists.to_list()
        return res