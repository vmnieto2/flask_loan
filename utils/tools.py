import base64
# from Utils.constants import BASE_PATH_TEMPLATE
from flask import Response
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json
import os
import smtplib


class Tools:

    """ Esta funcion permite darle formato a la respuesta de la API """
    def output(self, codigo, message, data=[]):

        response = Response(json.dumps({
            "responseCode": codigo,
            "message": message,
            "data": data,
        }), status=codigo,  content_type="application/json")
        return response

    # """ Esta funcion permite obtener el template """
    # def get_content_template(self, template_name: str):
    #     template = f"{BASE_PATH_TEMPLATE}/{template_name}"

    #     content = ""
    #     with open(template, 'r') as f:
    #         content = f.read()

    #     return content

    def result(self, msg, code=400, error="", data=[]):
        return {
            "body": {
                "statusCode": code,
                "message": msg,
                "data": data,
                "Exception": error
            }
        }
    # """ Obtener archivo"""
    # def get_file_b64(self, file_path):
    #     with open(file_path, "rb") as file:
    #         # Leer el contenido binario del archivo PDF
    #         pdf_content = file.read()

    #         # Codificar el contenido binario en base64
    #         pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')

    #         return pdf_base64

    # async def send_email_error(self, service_name, code, request, response):
    #     load_dotenv()
    #     # Obtener enviroment
    #     stage = os.getenv("STAGE")
    #     remitente = os.getenv("EMAIL_USER")
    #     destinatario = os.getenv("EMAIL_DEV")

    #     template_url = f"{BASE_PATH_TEMPLATE}/notificacion_error.html"
    #     # Preapar el asunto del correo
    #     subject = f"TOYO - Project: Error service - Stage: {stage}"
    #     # Preparar el contenido del correo
    #     data_correo = {
    #         "servicio": "TOYO",
    #         "status_code": code,
    #         "consumo": service_name,
    #         "id_gestion": "000",
    #         "url": "Toyo_dev",
    #         "request": request,
    #         "response": response
    #     }

    #     msg = MIMEMultipart()
    #     msg["Subject"] = subject
    #     msg["From"] = remitente
    #     msg["To"] = destinatario

    #     with open(template_url, 'r') as template_file:
    #         template = template_file.read()
    #         template = template.format(**data_correo)
    #     msg.attach(MIMEText(template, 'html'))

    #     # Configura la conexión al servidor SMTP de Gmail
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.starttls()
    #     server.login(remitente, os.getenv('EMAIL_PASSWORD'))

    #     # Envía el correo
    #     server.sendmail(remitente, destinatario, msg.as_string())

    #     # Cierra la conexión con el servidor SMTP
    #     server.quit()

    # async def send_email(self, recipients, subject, body, attachments=None):
    #     sender = os.getenv("EMAIL_USER")

    #     msg = MIMEMultipart()
    #     msg["Subject"] = subject
    #     msg["From"] = sender
    #     msg["To"] = recipients

    #     msg.attach(MIMEText(body, 'html'))
    #     # Agregar archivos adjuntos en formato base64 al mensaje MIME
    #     if attachments:
    #         for attachment in attachments:
    #             # Decodificar el contenido base64
    #             decoded_data = base64.b64decode(attachment["file"])

    #             # Crear un objeto MIMEBase y adjuntar el archivo decodificado
    #             attachment_part = MIMEBase('application', 'octet-stream')
    #             attachment_part.set_payload(decoded_data)
    #             encoders.encode_base64(attachment_part)

    #             # Establecer el encabezado del archivo adjunto
    #             attachment_part.add_header('Content-Disposition', f'attachment; filename={attachment["name"]}')
    #             msg.attach(attachment_part)

    #     # Configurar conexion con servidor SMTP
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.starttls()
    #     server.login(sender, os.getenv('EMAIL_PASSWORD'))
    #     server.sendmail(sender, recipients, msg.as_string())
    #     # Cerrar conexion Con servidor
    #     server.quit()


class CustomException(Exception):
    """ Esta clase hereda de la clase Exception y permite
        interrumpir la ejecucion de un metodo invocando una excepcion
        personalizada """
    def __init__(self, message="", codigo=400, data=[]):
        self.codigo = codigo
        self.message = message
        self.data = data
        self.resultado = {
            "body": {
                "statusCode": codigo,
                "message": message,
                "data": data,
                "Exception": "CustomException"
            }
        }
