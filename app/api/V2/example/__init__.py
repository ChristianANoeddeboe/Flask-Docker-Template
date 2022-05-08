from app.controllers.ExampleController import create_example, delete_example, get_example, get_examples, update_example
from flask import Blueprint, request, make_response
import json

example_api = Blueprint("example", __name__, url_prefix="/example")

@example_api.route('', methods=['GET'])
def api_get_examples():
    try:
        data = get_examples()
        res = []
        for item in data:
            res.append(item.to_dict())
        body = json.dumps(res)
    except BaseException as error:
        return make_response("Something went wrong on our side", 500)
    
    return make_response(body, 200)

@example_api.route('/<id>', methods=['GET'])
def api_get_example(id):
    try:
        res = get_example(id)
        body = json.dumps(res)
    except BaseException as error:
        return make_response("Something went wrong on our side", 500)
    
    return make_response(body, 200)

@example_api.route('', methods=['POST'])
def api_create_example():

    body = json.dumps(request.json)
    try:
        res = create_example(body)
        body = json.dumps(res)
    except BaseException as error:
        return make_response("Something went wrong on our side", 500)
    
    return make_response(body, 201)

@example_api.route('/<id>', methods=['PUT'])
def api_update_example(id):

    body = json.dumps(request.json)
    try:
        res = update_example(id, body)
        body = json.dumps(res)
    except BaseException as error:
        return make_response("Something went wrong on our side", 500)
    
    return make_response(body, 200)

@example_api.route('/<id>', methods=['DELETE'])
def api_delete_example(id):
    try:
        res = delete_example(id)
        body = json.dumps(res)
    except BaseException as error:
        return make_response("Something went wrong on our side", 500)
    
    return make_response(body, 200)