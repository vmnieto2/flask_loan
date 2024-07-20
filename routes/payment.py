from flask import Blueprint, request
from Class.payment import Payment
from flask_jwt_extended import jwt_required
from utils.decorator import http_decorator

payment_route = Blueprint("payment", __name__)

@payment_route.route('/show_payments', methods=["POST"])
@jwt_required()
@http_decorator
def show_payments():
    result = Payment().show_payments(request.get_json())
    return result

@payment_route.route('/create_payment', methods=["POST"])
@jwt_required()
@http_decorator
def create_payment():
    result = Payment().create_payment(request.get_json())
    return result
