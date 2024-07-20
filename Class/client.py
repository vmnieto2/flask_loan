from Database.db import session
from Models.client_model import ClientModel
from Models.type_document_model import TypeDocumentModel
from utils.tools import Tools, CustomException

class Client():

    def __init__(self):
        self.session = session
        self.tools = Tools()

    # Function for have all active clients
    def get_all_clients(self, data: dict = None):

        response = list()
                
        query = self.session.query(
            ClientModel, TypeDocumentModel
        ).join(
            TypeDocumentModel,
            TypeDocumentModel.id == ClientModel.type_document
        ).filter(
            ClientModel.status == 1,
            TypeDocumentModel.status == 1
        ).all()
        self.session.close()
        
        if not query:
            return self.tools.output(200, "No data to show.", response)
        
        for client, type_document in query:
            response.append({
                "id": client.id,
                "type_document": type_document.name,
                "document": client.document,
                "full_name": client.full_name.title(),
                "cell_phone": client.cell_phone,
                "email": client.email
            })
        
        return self.tools.output(200, "Data found", response)

    # Function for save a client.
    def save_client(self, data: dict):
        
        # Get all params
        type_document = data['type_document']
        document = data['document']
        first_name = data['first_name']
        second_name = data['second_name']
        last_name = data['last_name']
        second_last_name = data['second_last_name']
        cell_phone = data['cell_phone']
        email = data['email']
        data_client_save = None
        
        # Validate if para exists
        type_document_model = TypeDocumentModel
        type_document_field = "tipo documento"
        
        """
            Structure of this funcion is
            1. model name
            2. param to find in model
            3. current field name in json
        """
        self.check_param_exists(
            type_document_model, type_document, type_document_field
        )
        
        # Validate if client exists
        self.check_if_exists_client(document)

        # concat full name
        full_name = " ".join(x for x in [first_name, second_name, last_name, second_last_name] if x)
        
        # json of cliente data to save
        data_client_save = {
            'type_document': type_document,
            'document': document,
            'first_name': first_name,
            'second_name': second_name,
            'last_name': last_name,
            'second_last_name': second_last_name,
            'full_name': full_name,
            'cell_phone': cell_phone,
            'email': email
        }
        self.insert_data_client(data_client_save)

        return self.tools.output(201, "Client created successfully.")

    # Check if client exists.
    def check_if_exists_client(self, document: str):

        client = self.session.query(
            ClientModel
        ).filter(
            ClientModel.document == document, ClientModel.status == 1
        ).first()
        self.session.close()

        if client:
            raise CustomException("Client already exists.")
        
        return

    # Inserting data for save a client.
    def insert_data_client(self, data: dict):
        
        try:
            client = ClientModel(data)
            self.session.add(client)
            self.session.commit()
            self.session.close()
        except Exception as ex:
            raise CustomException(str(ex))

    # Check if param of any model exits
    def check_param_exists(
            self, model: any, param_to_find: int, field: str
        ):
        
        query = self.session.query(
            model
        ).filter(
            model.id == param_to_find, model.status == 1
        ).first()
        self.session.close()
        
        msg = f"Field {field} doesn't exists."
        if not query:
            raise CustomException(msg)

        return
