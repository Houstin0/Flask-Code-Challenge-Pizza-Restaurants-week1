from api.models import Pizza,Restaurant,RestaurantPizza
from api.models import db
from api.app import api
from flask_restful import Resource, reqparse
from flask import make_response,request,jsonify



class Index(Resource):

    def get(self):

        response_dict = {
            "index": "Welcome to the Pizza Restaurant RESTful API",
        }

        response = make_response(
            jsonify(response_dict),
            200,
        )

        return response

api.add_resource(Index, '/')

class Restaurants(Resource):
    def get(self):
        restaurants_dicts = []
        for restaurant in Restaurant.query.all():
            restaurant_dict = restaurant.to_dict()
            restaurants_dicts.append(restaurant_dict)

        response = make_response(
            jsonify(restaurants_dicts),
            200
        )
        return response

api.add_resource(Restaurants, '/restaurants')

class RestaurantByID(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            response_dict = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": [pizza.to_dict() for pizza in restaurant.pizzas]
            }
            response = make_response(
                jsonify(response_dict),
                200
            )
            return response
        else:
            response_dict = {
                "error": "Restaurant not found"
            }
            response = make_response(
                jsonify(response_dict),
                404
            )
            return response
        
    def delete(self, id):
        restaurant = Restaurant.query.get(id)
        if restaurant:

            for restaurant_pizza in restaurant.restaurant_pizzas:
                db.session.delete(restaurant_pizza)
            db.session.delete(restaurant)
            db.session.commit()

            response = make_response('', 204) 
            return response
        else:
            response_dict = {
                "error": "Restaurant not found"
            }
            response = make_response(
                jsonify(response_dict),
                404
            )
            return response

api.add_resource(RestaurantByID, '/restaurants/<int:id>')

class Pizzas(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        pizzas_dicts = [pizza.to_dict() for pizza in pizzas]
        response = make_response(
            jsonify(pizzas_dicts),
            200
        )
        return response

api.add_resource(Pizzas, '/pizzas')

class RestaurantPizzas(Resource):
    def post(self):
        data=request.get_json()
        new_restaurant_pizza=RestaurantPizza(
            price=data.get('price'),
            pizza_id= data.get("pizza_id"),
            restaurant_id= data.get("restaurant_id"),
        ) 
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        response = make_response(
            new_restaurant_pizza.to_dict(),
            201 
        )
        return response



api.add_resource(RestaurantPizzas, '/restaurant_pizzas')