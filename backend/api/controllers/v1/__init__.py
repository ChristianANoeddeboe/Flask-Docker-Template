from fastapi import APIRouter
from backend.api.controllers.v1 import TodoListController

api_router_v1 = APIRouter()
api_router_v1.include_router(TodoListController.router, prefix="/todolists", tags=["todolists"])
