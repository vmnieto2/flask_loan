from Database.db import session
from Models.user_model import UserModel
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from utils.tools import Tools, CustomException

class User():

    def __init__(self):
        self.session = session
        self.tools = Tools()

    # Function for login
    def login(self, data: dict):
        
        email = data["email"]
        passwd = data["passwd"]
        
        query = self.session.query(
            UserModel
        ).filter(
            UserModel.email == email, UserModel.status == 1,
        ).first()
        self.session.close()
        
        if not query:
            raise CustomException("Username or password incorrect.")
        
        enc_passwd = query.password
        if not check_password_hash(enc_passwd, passwd):
            raise CustomException("Username or password incorrect.")
        
        if query.user_type_id != 1:
            raise CustomException("User not authorized.", 401)
            
        token = create_access_token(identity={"id": query.id})
        
        response = {
            "token": token
        }
        
        return self.tools.output(200, "Login successfully", response)
