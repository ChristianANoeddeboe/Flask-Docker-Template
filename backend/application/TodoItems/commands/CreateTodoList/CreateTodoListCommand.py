

from typing import Optional

from pydantic import BaseModel
from Medipy.IRequestHandler import IRequestHandler
from backend.application.common.interfaces.IApplicationDbContext import IApplicationDbContext
from backend.domain.entities.TodoList import TodoList


class CreateTodoListCommand(BaseModel):

    id: int
    title: Optional[str]

class CreateTodoListCommandHandler(IRequestHandler[CreateTodoListCommand, int]):

    __context: IApplicationDbContext

    def __init__(self, context: IApplicationDbContext):
        self.__context = context

    async def handle(self, request: CreateTodoListCommand, cancellation_token=None) -> int:
        entity = TodoList()

        print(request.title)

        entity.title = request.title

        self.__context.TodoLists.add(entity)

        await self.__context.save_changes_async()

        return entity.id
