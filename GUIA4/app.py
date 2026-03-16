import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuración
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///default.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'clave-insegura')


from models import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


db.init_app(app)

migrate = Migrate(app, db)  
jwt = JWTManager(app)      


if __name__ == '__main__':

    puerto = int(os.getenv('PORT', 5000))
    modo_debug = os.getenv('FLASK_DEBUG', 'False') == 'True'

    app.run(port=puerto, debug=modo_debug)
