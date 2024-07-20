from flask import Flask
from routes.user import user_route
from routes.client import client_route
from routes.params import type_document_route, type_user_route
from routes.loan import loan_route
from routes.payment import payment_route
from flask_jwt_extended import JWTManager
import os
from datetime import timedelta

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("MY_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)
app.register_blueprint(user_route)
app.register_blueprint(client_route)
app.register_blueprint(type_document_route)
app.register_blueprint(type_user_route)
app.register_blueprint(loan_route)
app.register_blueprint(payment_route)

if __name__ == '__main__':
    app.run(debug=True)
