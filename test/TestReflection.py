import asyncio
import sys, inspect
import os

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)

# print(sys.path)
sys.path.append(PROJECT_ROOT)
from MediatP.Mediator import Mediator



#print(sys.path)

from backend.application.TodoItems.commands.CreateTodoList.CreateTodoListCommand import CreateTodoListCommand
#from MediatP.IRequestHandler import IRequestHandler

request = CreateTodoListCommand()
request.title = "Test"

from MediatP.IRequestHandler import IRequestHandler

#print(isinstance(request, IRequestHandler))
# module = inspect.getmodule(request)
# for name, obj in inspect.getmembers(module):
#     if inspect.isclass(obj):
#         print(obj)



# module = inspect.getmodule(request)
# test = inspect.getmembers(module)
# for item in test:
#     print(item)



#print(inspect.getmembers(module))

# print(inspect.getmodule(request))
# print(request.__module__)
# print("##############################################################################")

# res = inspect.getmembers(inspect.getmodule(request), lambda member: inspect.isclass(member) and member.__base__ == IRequestHandler)

# print(res)

med = Mediator()
test_cmd = CreateTodoListCommand()
test_cmd.title = "Test"
asyncio.run(med.send(test_cmd))