from sqlalchemy import Column, Integer, DateTime, DECIMAL
from Database.db import BASE
from datetime import datetime

class PaymentModel(BASE):
    
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, nullable=False)
    pay_amount = Column(DECIMAL, nullable=False)
    status = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)

    def __init__(self, data: dict):
        self.loan_id = data['loan_id']
        self.pay_amount = data['pay_amount']
