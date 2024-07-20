from Database.db import session
from Models.type_document_model import TypeDocumentModel
from Models.user_type_model import TypeUserModel
from utils.tools import Tools

class Params():

    def __init__(self):
        self.session = session
        self.tools = Tools()

    # Function for have all type documents
    def get_type_document(self, data: dict = None):

        response = list()
                
        query = self.session.query(
            TypeDocumentModel
        ).filter(
            TypeDocumentModel.status == 1
        ).all()
        self.session.close()
        
        if not query:
            return self.tools.output(200, "No data to show.", response)
        
        for key in query:
            response.append({
                "id": key.id,
                "name": key.name,
                "description": key.description
            })
        
        return self.tools.output(200, "Data found", response)
    
    # Function for have all type users
    def get_type_user(self, data: dict = None):

        response = list()
                
        query = self.session.query(
            TypeUserModel
        ).filter(
            TypeUserModel.status == 1
        ).all()
        self.session.close()
        
        if not query:
            return self.tools.output(200, "No data to show.", response)
        
        for key in query:
            response.append({
                "id": key.id,
                "name": key.name
            })
        
        return self.tools.output(200, "Data found", response)
