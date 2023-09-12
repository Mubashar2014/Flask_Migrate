from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import secrets
secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SECRET_KEY'] = secret_key

db = SQLAlchemy(app)
migrate=Migrate(app,db)
ma = Marshmallow(app)


from project import models
from project import routes

