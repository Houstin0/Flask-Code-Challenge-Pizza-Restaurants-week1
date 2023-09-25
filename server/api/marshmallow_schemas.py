from app import app
from models import Restaurant,Pizza,RestaurantPizza
from flask_marshmallow import Marshmallow

ma=Marshmallow(app)

class RestaurantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Restaurant 

restaurant_schema=RestaurantSchema()
restaurant_schema=RestaurantSchema(many=True)        

class PizzaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pizza

pizza_schema = PizzaSchema()
pizzas_schema = PizzaSchema(many=True)

class RestaurantPizzaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RestaurantPizza

restaurant_pizza_schema = RestaurantPizzaSchema()
restaurant_pizzas_schema = RestaurantPizzaSchema(many=True)