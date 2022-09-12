from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from Medipy.Mediator import Mediator

from backend.api.ApplicationAPIContext import application_api_context
from backend.infrastructure.persistence.ApplicationDBContext import ApplicationDbContext

app = FastAPI()

# Setup
mediator_services = [
    ApplicationDbContext()
]

mediator = Mediator(mediator_services)

application_api_context.register_application_service(app)
application_api_context.register_request_handler_service(mediator)
print(application_api_context.get_request_handler_service())
print(application_api_context.test)

from backend.api.controllers import v1
app.include_router(v1.api_router_v1, prefix="/api/v1")
