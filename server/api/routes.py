from marshmallow_schemas import restaurant_schema,pizza_schema,restaurant_pizza_schema
from models import Pizza,Restaurant,RestaurantPizza
from models import db
from app import api
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
        db.session.add(new_restaurant)
        db.session.commit()

        response=make_response(
            restaurant_schema.dump(new_restaurant),
            201
        )
        return response
    
api.add_resource(Restaurants,'/restaurants')

class RestaurantByID(Resource):
    def get(self,id):

        restaurant=Restaurant.query.filter_by(id=id).first()
        if restaurant:
            response=make_response(
                restaurant_schema.dump(restaurant),
                200
            )
            return response
        else:
            response_dict={
                "error": "Restaurant not found"
            }
            response=make_response(
                response_dict,
                404
            )
            return response