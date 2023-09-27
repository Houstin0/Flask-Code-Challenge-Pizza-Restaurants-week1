#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate


from .models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)

from api import routes
