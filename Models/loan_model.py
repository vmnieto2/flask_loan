from Database.db import BASE
from sqlalchemy import Column, BigInteger, Integer, DateTime, Text, DECIMAL
from datetime import datetime

class LoanModel(BASE):

    __tablename__= "loan"
    
    id = Column(BigInteger, primary_key=True)
    client_id = Column(BigInteger)
    description = Column(Text, nullable=True)
    total_loan = Column(DECIMAL)
    status = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)

    def __init__(self, data: dict):
        self.client_id = data['client_id']
        self.description = data['description']
        self.total_loan = data['total_loan']
    