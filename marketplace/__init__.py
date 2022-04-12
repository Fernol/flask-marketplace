from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from marketplace.category.category import category


app = Flask(__name__)
app.config['SECRET_KEY'] = 'lasjkljasklfhj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:A12345$@localhost/marketdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from marketplace.roots import *


