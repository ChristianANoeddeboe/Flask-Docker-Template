from flask import Blueprint
from app.api.V2.example import example_api

api_v2 = Blueprint('api_v2', __name__, url_prefix='/V2')
api_v2.register_blueprint(example_api)

DEFAULT_PATH = "V2.py"