from flask import Blueprint, request
from Class.params import Params
from flask_jwt_extended import jwt_required
from utils.decorator import http_decorator

type_document_route = Blueprint("type_document", __name__)
type_user_route = Blueprint("type_user", __name__)

@type_document_route.route('/get_type_document', methods=["POST"])
@jwt_required()
@http_decorator
def get_type_document():
    result = Params().get_type_document()
    return result

@type_user_route.route('/get_type_user', methods=["POST"])
@jwt_required()
@http_decorator
def get_type_user():
    result = Params().get_type_user()
    return result
