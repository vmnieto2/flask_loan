from Database.db import BASE
from sqlalchemy import Column, String, BigInteger, Text, Integer, DateTime
from datetime import datetime

class UserModel(BASE):

    __tablename__= "user"
    
    id = Column(BigInteger, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    second_last_name = Column(String, nullable=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(Text)
    user_type_id = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)
    
    def __init__(self, data: dict):
        self.first_name = data['first_name']
        self.second_name = data['second_name']
        self.last_name = data['last_name']
        self.second_last_name = data['second_last_name']
        self.full_name = data['full_name']
        self.email = data['email']
        self.password = data['password']
        self.user_type_id = data['user_type_id']
    