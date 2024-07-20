from flask import Blueprint, request
from Class.client import Client
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.decorator import http_decorator

client_route = Blueprint("client", __name__)

@client_route.route('/get_all_clients', methods=["POST"])
@jwt_required()
@http_decorator
def get_all_clients():
    result = Client().get_all_clients()
    return result

@client_route.route('/save_client', methods=["POST"])
@jwt_required()
@http_decorator
def save_client():
    result = Client().save_client(request.get_json())
    return result
