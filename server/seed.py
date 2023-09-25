#!/usr/bin/env python3

from faker import Faker
from api.models import db, Restaurant, Pizza, RestaurantPizza
from api.app import app
import random

with app.app_context():
    fake = Faker()

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    restaurants = []
    for i in range(50):
        new_restaurant = Restaurant(
            name = fake.company(),
            address = fake.address()
        )
        restaurants.append(new_restaurant)
    db.session.add_all(restaurants)
    db.session.commit()


    pizzas = []
    for i in range(50):
        num = random.randint(0,30)
        new_pizza = Pizza(
            name = fake.name(),
            ingredients = ', '.join([' '.join(fake.words(3)) for _ in range(7)]),
        )
        pizzas.append(new_pizza)
    db.session.add_all(pizzas)
    db.session.commit()

    restaurant_pizzas = []
    for restaurant in Restaurant.query.all():
        pizza_count = random.randint(1,10)
        for i in range(pizza_count):
            new_restaurant_pizza = RestaurantPizza(
                pizza_id = random.choice(pizzas).id,
                restaurant_id = restaurant.id,
                price = random.randint(1,30)
            )
            restaurant_pizzas.append(new_restaurant_pizza)
    db.session.add_all(restaurant_pizzas)
    db.session.commit()