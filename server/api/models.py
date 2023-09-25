
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class Restaurant(db.Model):
    __tablename__="restaurants"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True)
    address=db.Column(db.String)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', overlaps="restaurant_pizza")

   
    def __repr__(self):
        return f'< Restaurant {self.name} | Address: {self.address}>'
    
    @validates('name')
    def check_name(self,key,name):
        if len(name) > 50:
            raise AssertionError("Name must be less than 50 words in length.")
        return name

    
class Pizza(db.Model):
    __tablename__="pizzas"    

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    ingredients=db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    def __repr__(self):
        return f'< Pizza {self.name} | Ingredients: {self.ingredients}>'
    
class RestaurantPizza(db.Model):
    __tablename__="restaurant_pizzas"

    id=db.Column(db.Integer,primary_key=True)
    pizza_id=db.Column(db.Integer,db.ForeignKey("pizzas.id"))
    restaurant_id=db.Column(db.Integer,db.ForeignKey("restaurants.id"))
    price=db.Column(db.Integer) 
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas', overlaps="restaurant_pizza")
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas', overlaps="restaurants")


    def __repr__(self):
        return f'< Restaurant Pizza Price {self.price} | Created at: {self.created_at} | Updated at: {self.updated_at} >'
    
    @validates('price')
    def check_price(self,key,price):
        if not (1<=price<=30):
            raise AssertionError("Price must be between 1 and 30.")
        return price
    

    