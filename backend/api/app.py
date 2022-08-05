from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from Medipy.Mediator import Mediator
from backend.api.controllers import v1
from backend.api.ApplicationAPIContext import application_api_context

app = FastAPI()

# Setup

mediator_services = []

mediator = Mediator(mediator_services)

application_api_context.register_application_service(app)
application_api_context.register_request_handler_service(mediator)


app.include_router(v1.api_router_v1, prefix="/api/v1")
