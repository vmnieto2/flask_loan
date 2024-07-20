from .validator import Validator


class Rules:
    """ Esta clase se encarga de validar los datos de entrada de la API
        y si hay un error, lanza una excepcion """

    val = Validator()

    def __init__(self, path: str, params: dict):
        path_dict = {
            "/login": self.__val_login,
            "/save_client": self.__save_client,
            "/get_all_loans": self.__get_all_loans,
            "/create_loan": self.__create_loan,
            "/show_payments": self.__show_payments,
            "/create_payment": self.__create_payment,
        }
        # Se obtiene la funcion a ejecutar
        func = path_dict.get(path, None)
        if func:
            # Se ejecuta la funcion para obtener las reglas de validacion
            validacion_dict = func(params)

            # Se valida la datas
            self.val.validacion_datos_entrada(validacion_dict)
            
    # Validate data login
    def __val_login(self, params: dict):
        validacion_dict = [
            {
                "tipo": "email",
                "campo": "email",
                "valor": params["email"],
                "obligatorio": True,
            },
            {
                "tipo": "string",
                "campo": "contraseña",
                "valor": params["passwd"],
                "obligatorio": True,
            }
        ]
        return validacion_dict

    # Validate data save a client
    def __save_client(self, params: dict):
        validacion_dict = [
            {
                "tipo": "int",
                "campo": "tipo documento",
                "valor": params["type_document"],
                "obligatorio": True,
            },
            {
                "tipo": "string",
                "campo": "documento",
                "valor": params["document"],
                "obligatorio": True,
            },
            {
                "tipo": "string",
                "campo": "primer nombre",
                "valor": params["first_name"],
                "obligatorio": True,
            },
            {
                "tipo": "string",
                "campo": "segundo nombre",
                "valor": params["second_name"],
                "obligatorio": False,
            },
            {
                "tipo": "string",
                "campo": "primer apellido",
                "valor": params["last_name"],
                "obligatorio": True,
            },
            {
                "tipo": "string",
                "campo": "segundo apellido",
                "valor": params["second_last_name"],
                "obligatorio": False,
            },
            {
                "tipo": "phone",
                "campo": "celular",
                "valor": params["cell_phone"],
                "obligatorio": False,
            },
            {
                "tipo": "email",
                "campo": "correo",
                "valor": params["email"],
                "obligatorio": True,
            }
        ]
        return validacion_dict

    # Validate data loans of a client
    def __get_all_loans(self, params: dict):
        validacion_dict = [
            {
                "tipo": "int",
                "campo": "cliente id",
                "valor": params["client_id"],
                "obligatorio": True,
            }
        ]
        return validacion_dict

    # Validate data save loan
    def __create_loan(self, params: dict):
        validacion_dict = [
            {
                "tipo": "int",
                "campo": "cliente id",
                "valor": params["client_id"],
                "obligatorio": True,
            },
            {
                "tipo": "string",
                "campo": "descripción",
                "valor": params["description"],
                "obligatorio": True,
            },
            {
                "tipo": "int",
                "campo": "total prestamo",
                "valor": params["total_loan"],
                "obligatorio": True,
            }
        ]
        return validacion_dict

    # Validate payments of a loan
    def __show_payments(self, params: dict):
        validacion_dict = [
            {
                "tipo": "int",
                "campo": "id de prestamo",
                "valor": params["loan_id"],
                "obligatorio": True,
            }
        ]
        return validacion_dict

    # Validate data for create a payment
    def __create_payment(self, params: dict):
        validacion_dict = [
            {
                "tipo": "int",
                "campo": "prestamo id",
                "valor": params["loan_id"],
                "obligatorio": True,
            },
            {
                "tipo": "int",
                "campo": "monto a pagar",
                "valor": params["pay_amount"],
                "obligatorio": True,
            }
        ]
        return validacion_dict
