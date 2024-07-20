from .tools import CustomException
from datetime import datetime
import re


class Validator:

    # Validar tipo de dato sea correcto
    def tipo_dato(self, params):
        tipo = params["tipo"]
        campo = params["campo"].lower()
        obligatorio = params["obligatorio"]
        valor = params["valor"]
        limite = params.get("limite", None)
        if "tipo_documento" in params:
            type_document = int(params["tipo_documento"])

        if (valor == "" or valor is None) and bool(obligatorio):
            message = f"El campo {campo} no puede ser vacio."
            raise CustomException(message)
        try:
            if limite and (
                    len(str(valor)) > limite["max"]
                    or len(str(valor)) < limite["min"]
                    ):
                if limite["max"] == limite["min"]:
                    message = f"El campo {campo} ({valor}) debe tener {limite['max']} caracteres."
                else:
                    message = f"El campo {campo} ({valor}) debe tener entre {limite['min']} y {limite['max']} caracteres."
                raise CustomException(message)
            elif bool(valor):
                if tipo == "int":
                    valor = int(valor)
                    if valor < 0:
                        message = f'El campo {campo} ({valor}) no puede ser negativo.'
                        raise CustomException(message)
                elif tipo == "string":
                    valor = str(valor)
                    valor = " ".join(valor.split())
                    if valor == "":
                        message = f'El campo {campo} ({valor}) tiene espacios vacios.'
                        raise CustomException(message)
                    if limite and (
                                len(str(valor)) > limite["max"]
                                or len(str(valor)) < limite["min"]
                                ):
                        if limite["max"] == limite["min"]:
                            message = f"El campo {campo} ({valor}) debe tener {limite['max']} caracteres."
                        else:
                            message = f"El campo {campo} ({valor}) debe tener entre {limite['min']} y {limite['max']} caracteres."
                        raise CustomException(message)
                elif tipo == "bool":
                    if valor not in [True, False]:
                        message = f'El campo {campo} ({valor}) no es válido.'
                        raise CustomException(message)
                elif tipo == "numeric":
                    valor = valor.isnumeric()
                elif tipo == "float":
                    valor = float(valor)
                    if valor < 0:
                        message = f'El campo {campo} ({valor}) no es válido.'
                        raise CustomException(message)
                elif tipo == "date":
                    tipo = "date (DD-MM-YYYY)"
                    valor = datetime.strptime(valor, "%d-%m-%Y")
                elif tipo == "placa":
                    regex = r"^[a-zA-Z]{3}\d{3}$|^[a-zA-Z]\d{5}$"
                    if (not re.fullmatch(regex, valor)):
                        message = f"El campo {campo} ({valor}) no es válido."
                        raise CustomException(message)
                elif tipo == "email":
                    # regex = r'\b[A-Za-z0-9]+[._%+-]*[A-Za-z0-9]+@([A-Za-z0-9][.-]*)+\.[A-Z|a-z]{2,}\b'
                    regex = r'^[a-zA-Z0-9._-]{3,}@.{2,}\..{2,}$'
                    if (not re.fullmatch(regex, valor)):
                        message = f"El campo {campo} ({valor}) no es válido."
                        raise CustomException(message)
                elif tipo == "list":
                    if not isinstance(valor, list):
                        message = f"El campo {campo} ({valor}) no es válido."
                        raise CustomException(message)
                elif tipo == "name":
                    regex = r'^[a-zA-ZáÁ-úÚ-ñÑ\s-]{2,100}$'
                    if (not re.fullmatch(regex, valor)):
                        message = f"El campo {campo} ({valor}) no es válido."
                        raise CustomException(message)
                elif tipo == "document":
                    valor = int(valor)
                    longitud = len(str(valor))
                    if ((type_document == 16 and (longitud < 5 or longitud > 12))
                       or (type_document == 17 and (longitud < 6 or longitud > 10))):
                        message = f"El campo {campo} ({valor}) no es válido."
                        raise CustomException(message)
                elif tipo == "address":
                    regex = r'^[a-zA-Z0-9-áÁ-úÚ-ñÑ\s#-]+$'
                    if (not re.fullmatch(regex, valor)):
                        message = f"El campo {campo} ({valor}) no es válido."
                        raise CustomException(message)
                elif tipo == "phone":
                    valor = int(valor)
                    if not (str(valor).startswith("3") or str(valor).startswith("6")):
                        message = f"El campo {campo} ({valor}) no es válido."
                        raise CustomException(message)
        except ValueError as ve:
            print(str(ve))
            message = f"Los datos enviados no son correctos o están incompletos. Verifique la información e inténtelo nuevamente. {campo}"
            raise CustomException(message)

    # Iterador para validar datos
    def validacion_datos_entrada(self, data):
        for rows in data:
            self.tipo_dato(rows)
