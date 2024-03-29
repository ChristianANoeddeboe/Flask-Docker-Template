

from typing import Optional
from Medipy.IRequestHandler import IRequestHandler
from backend.application.common.interfaces.IApplicationDbContext import IApplicationDbContext
from backend.domain.entities.TodoList import TodoList


class CreateTodoListCommand():

    id: int
    title: Optional[str]

class CreateTodoListCommandHandler(IRequestHandler[CreateTodoListCommand, int]):

    __context: IApplicationDbContext

    def __init__(self, context: IApplicationDbContext):
        self.__context = context

    async def handle(self, request: CreateTodoListCommand, cancellation_token=None) -> int:
        entity = self.__context.TodoLists.find(lambda x: x.id == request.id)

        entity.title = request.title

        self.__context.TodoLists.add(entity)

        await self.__context.save_changes_async(cancellation_token)

        return entity.id
