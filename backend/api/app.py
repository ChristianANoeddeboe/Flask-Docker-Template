from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from Medipy.Mediator import Mediator
from backend.api.controllers import v1
from backend.api.ApplicationAPIContext import application_api_context

app = FastAPI()

application_api_context.register_application_service(app)
application_api_context.register_request_handler_service(Mediator())
application_api_context.test(3)

print(1, application_api_context.get_test())

app.include_router(v1.api_router_v1, prefix="/api/v1")

print(3, application_api_context.get_test())