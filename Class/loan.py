from Database.db import session
from Class.client import Client
from Models.loan_model import LoanModel
from utils.tools import Tools, CustomException

class Loan():

    def __init__(self):
        self.session = session
        self.tools = Tools()
        self.client = Client()

    # Function for have all loans of a client
    def get_all_loans(self, data: dict = None):
        
        client_id = data["client_id"]
                
        self.client.check_if_exists_client(client_id)
        
        get_loans = self.show_loans_by_client(client_id)
        
        return self.tools.output(200, "Data found", get_loans)
    
    # Function for get all loans
    def show_loans_by_client(self, client_id: int):
        
        result = list()
        
        loans = self.session.query(
            LoanModel
        ).filter(
            LoanModel.client_id == client_id, LoanModel.status == 1
        ).all()
        self.session.close
        
        if loans:
            for loan in loans:
                result.append({
                    "id": loan.id,
                    "description": loan.description,
                    "total_loan": float(loan.total_loan)
                })
                
        return result

    # Function for create a loan to an client.
    def create_loan(self, data: dict):

        client_id = data['client_id']
        description = data['description']
        total_loan = data['total_loan']
        data_loan_save = None
        
        self.client.check_if_exists_client(client_id)
        
        quantity_loans = self.validate_loan_amount(client_id)
        if quantity_loans >= 3:
            raise CustomException("Exceeds number of loans, maximum 3.")

        data_loan_save = {
            "client_id": client_id,
            "description": description.capitalize(),
            "total_loan": total_loan
        }
        self.insert_data_loan(data_loan_save)

        return self.tools.output(201, "Loan created successfully.")
    
    # Validate how many loans have the client.
    def validate_loan_amount(self, client_id: int):

        loans = self.session.query(
            LoanModel
        ).filter(
            LoanModel.client_id == client_id, LoanModel.status == 1
        ).count()
        session.close()

        return loans

    # Inserting data for save a loan of a client.
    def insert_data_loan(self, data: dict):
        try:
            loan = LoanModel(data)
            self.session.add(loan)
            self.session.commit()
            self.session.close()
        except Exception as ex:
            raise CustomException(str(ex))
