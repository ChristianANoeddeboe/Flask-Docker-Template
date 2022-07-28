
from datetime import datetime

from fastapi import APIRouter
from Medipy.ISender import ISender
from Medipy.Mediator import Mediator
from backend.application.TodoItems.commands.CreateTodoList.CreateTodoListCommand import CreateTodoListCommand
from backend.domain.entities.TodoList import TodoList


router = APIRouter()

Mediator: ISender = Mediator()

# Get all todolists
@router.get("/")
async def get_todolists():
    return {"message": "Get all todolists"}

# Get a todolist
@router.get("/{todolist_id}")
async def get_todolist(todolist_id: int):
    todolist = TodoList(id=todolist_id, created=datetime.now(), title="TodoList 1")
    return todolist

@router.post("/")
async def create_todolist(command: CreateTodoListCommand):
    return await Mediator.send(command)