from Database.db import BASE
from sqlalchemy import Column, String, BigInteger, Integer, DateTime
from datetime import datetime

class TypeUserModel(BASE):

    __tablename__= "type_user"
    
    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    status = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)
 