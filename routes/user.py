from flask import Blueprint, request, render_template
from Class.user import User
from flask_jwt_extended import jwt_required
from utils.decorator import http_decorator
import json

user_route = Blueprint("user", __name__)

@user_route.route('/login', methods=["POST", "GET"])
@http_decorator
def login():
    user = User().login(request.get_json())
    return user
    # return render_template("login.html", res="victor")

@user_route.route('/test', methods=["POST"])
@jwt_required()
@http_decorator
def test_passwd():
    user = User().test_passwd(request.get_json())
    return user
