from flask import Blueprint, request
from Class.loan import Loan
from flask_jwt_extended import jwt_required
from utils.decorator import http_decorator

loan_route = Blueprint("loan", __name__)

@loan_route.route('/get_all_loans', methods=["POST"])
@jwt_required()
@http_decorator
def get_all_loans():
    result = Loan().get_all_loans(request.get_json())
    return result

@loan_route.route('/create_loan', methods=["POST"])
@jwt_required()
@http_decorator
def create_loan():
    result = Loan().create_loan(request.get_json())
    return result
