
from datetime import datetime

from fastapi import APIRouter
from Medipy.ISender import ISender
from backend.application.TodoItems.commands.CreateTodoList.CreateTodoListCommand import CreateTodoListCommand
from backend.application.TodoLists.queries.GetTodoLists.GetTodoListsQuery import GetTodoListsQuery
from backend.domain.entities.TodoList import TodoList
from backend.api.ApplicationAPIContext import application_api_context

router = APIRouter()

Mediator: ISender = application_api_context.get_request_handler_service()

# Get all todolists
@router.get("/")
async def get_todolists():
    todolists = Mediator.send(GetTodoListsQuery())
    return todolists

# Get a todolist
@router.get("/{todolist_id}")
async def get_todolist(todolist_id: int):
    todolist = Mediator.send(GetTodoListsQuery())
    return todolist

@router.post("/")
async def create_todolist(command: CreateTodoListCommand):
    return await Mediator.send(command)