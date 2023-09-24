from .marshmallow_schemas import restaurant_schema,pizza_schema,restaurant_pizza_schema
from .models import Pizza,Restaurant,RestaurantPizza
from api import db, api,app
from flask_restful import Resource
from flask import make_response,request

class Index(Resource):

    def get(self):

        response_dict = {
            "index": "Welcome to the Pizza Restaurant RESTful API",
        }

        response = make_response(
            response_dict,
            200,
        )

        return response

api.add_resource(Index, '/')

class Restaurants(Resource):

    def get(self):

        restaurants=Restaurant.query.all()

        response=make_response(
            restaurant_schema.dump(restaurants),
            200
        )
        return response
    
    def post(self):

        new_restaurant=Restaurant(
            name=request.form['name'],
            address=request.form['body']
        )
        db.session