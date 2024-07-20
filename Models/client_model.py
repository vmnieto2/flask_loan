from Database.db import BASE
from sqlalchemy import Column, String, BigInteger, Integer, DateTime
from datetime import datetime

class ClientModel(BASE):

    __tablename__= "client"
    
    id = Column(BigInteger, primary_key=True)
    type_document = Column(Integer, nullable=True)
    document = Column(String, nullable=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    second_last_name = Column(String, nullable=True)
    full_name = Column(String, nullable=False)
    cell_phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    status = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime(), default=datetime.now(), nullable=True)

    def __init__(self, data: dict):
        self.type_document = data['type_document']
        self.document = data['document']
        self.first_name = data['first_name']
        self.second_name = data['second_name']
        self.last_name = data['last_name']
        self.second_last_name = data['second_last_name']
        self.full_name = data['full_name']
        self.cell_phone = data['cell_phone']
        self.email = data['email']
    