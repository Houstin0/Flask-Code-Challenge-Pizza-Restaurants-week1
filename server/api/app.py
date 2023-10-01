#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate


from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://restaurant_pizza_db_oanm_user:lfG9ZOfdDpqkOLJWDfZei7VzVS7GdOQk@dpg-ckctqlect0pc73c1b0l0-a.ohio-postgres.render.com/restaurant_pizza_db_oanm"

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)


