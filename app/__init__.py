from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials", "Access-Control-Allow-Origin", "Access-Control-Allow-Headers", "x-access-token"], supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.getcwd()+'/database.db'
db = SQLAlchemy(app)

from app.routes import *
