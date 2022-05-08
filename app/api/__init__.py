from flask import Blueprint
from app.api.V2 import api_v2

base_api = Blueprint('base_api', __name__, url_prefix='/api')
base_api.register_blueprint(api_v2)