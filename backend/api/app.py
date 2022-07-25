from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.api.controllers import v1


app = FastAPI()

app.include_router(v1.api_router_v1, prefix="/api/v1")
