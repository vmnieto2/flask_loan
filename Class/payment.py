from Database.db import session
from Models.loan_model import LoanModel
from Models.payment_model import PaymentModel
from utils.tools import Tools, CustomException

class Payment():

    def __init__(self):
        self.session = session
        self.tools = Tools()

    # Function for show all payments of the loan
    def show_payments(self, data: dict):
        
        loan_id = data['loan_id']
        response = None

        result_loan = self.check_if_exists_loan(loan_id)
        
        total_loan = result_loan['total_loan']
        owe = result_loan['total_loan']
        
        result_payments = self.find_payments(loan_id)

        if len(result_payments) > 0:
            result_difference = self.calculate_difference(result_payments)
            owe = total_loan - result_difference

        response = {
            'payment_list': result_payments,
            'owe': owe,
        }

        return self.tools.output(200, "Data found.", response)

    # find payments by loan id
    def find_payments(self, loan_id: int):

        result = []

        pays = self.session.query(
            PaymentModel
        ).filter(
            PaymentModel.loan_id == loan_id, PaymentModel.status == 1
        ).all()
        self.session.close()

        if pays:
            for pay in pays:
                result.append({
                    "id": pay.id,
                    "pay_amount": float(pay.pay_amount),
                    "created_at": str(pay.created_at)
                })

        return result
    
    # Calculate the difference of the total loan and all payments 
    def calculate_difference(self, data: dict):

        result = 0
        for pay in data:
            result += pay['pay_amount']
        
        return result

    # Function for create a pay of the loan.
    def create_payment(self, data: dict):

        loan_id = data['loan_id']
        pay_amount = data['pay_amount']
        data_pay_save = None
        
        result_loan = self.check_if_exists_loan(loan_id)
        
        total_loan = result_loan['total_loan']

        result_payments = self.find_payments(loan_id)
        if len(result_payments) > 0:
            sum_result = self.calculate_difference(result_payments)
            
            if sum_result == total_loan:
                return self.tools.output(200, "The debt is already paid.")

        if pay_amount > total_loan:
            msg = "The amount to pay is higher than the total of loan."
            raise CustomException(msg)
        elif pay_amount <= 0:
            msg = "The amount to pay is invalid."
            raise CustomException(msg)

        data_pay_save = {
            "loan_id": loan_id,
            "pay_amount": pay_amount
        }
        self.insert_data_pay(data_pay_save)
        
        return self.tools.output(201, "Payment created successfully.")
    
    # Check if loan exists.
    def check_if_exists_loan(self, loan_id: int):

        result = None
        
        loan = self.session.query(
            LoanModel
        ).filter(
            LoanModel.id == loan_id, LoanModel.status == 1
        ).first()
        self.session.close()

        if not loan:
            raise CustomException("Loan doesn't exists.")
        
        result = {
            'id': loan.id,
            'client_id': loan.client_id,
            'description': loan.description,
            'total_loan': float(loan.total_loan)
        }
        
        return result
    
    # Inserting data for save a payment.
    def insert_data_pay(self, data: dict):
        try:
            pay = PaymentModel(data)
            self.session.add(pay)
            self.session.commit()
            self.session.close()
        except Exception as ex:
            raise CustomException(str(ex))
