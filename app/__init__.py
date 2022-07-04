import os

from flask import Flask, make_response
from flask_cors import CORS
from app.api import base_api

web_app = Flask("Flask app")
CORS(web_app, max_age=86400)
web_app.register_blueprint(base_api)

@web_app.route('/api/heartbeat')
def api_healthcheck():
    # try:
    #     body = json.dumps(healthcheck())
    # except ControllerError as error:
    #     logger.error(error.__repr__())
    #     return make_response(error.message, error.status_code)
    # except BaseException as error:
    #     logger.error(error.__repr__())
    #     return make_response("Something went wrong on our side", 500)
    
    return make_response(True, 200)

# if __name__ == '__main__':
#     app.secret_key = os.urandom(24)
#     app.run(host="0.0.0.0", port=os.getenv('FLASK_PORT'), use_reloader=True)
