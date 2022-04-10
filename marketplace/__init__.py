from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'lasjkljasklfhj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:A12345$@localhost/marketdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from marketplace.roots import *


