from sqlalchemy.orm import validates
from server.app.app import db,



class Restaurant(db.Model):
    __tablename__="restaurants"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True)
    address=db.Column(db.String)

    restaurant_pizza=db.relationship('RestaurantPizza',backref='restaurant')
    # pizzas=db.association_proxy('restaurant_pizzas','pizza',creator=lambda us: RestaurantPizza(pizza=us))

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

    restaurant_pizza=db.relationship('RestaurantPizza',backref='pizza')
    # pizzas=db.association_proxy('restaurant_pizzas','restaurant',creator=lambda gm: RestaurantPizza(restaurant=gm))

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

    pizza=db.relationship('Pizza',backref='restaurant_pizzas')
    restaurant=db.relationship('Restaurant',backref='restaurant_pizzas')

    def __repr__(self):
        return f'< Restaurant Pizza Price {self.price} | Created at: {self.created_at} | Updated at: {self.updated_at} >'
    
    @validates('price')
    def check_price(self,key,price):
        if not (1<=price<=30):
            raise AssertionError("Price must be between 1 and 30.")
        return price
    

    