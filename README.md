# Flask-Code-Challenge-Pizza-Restaurants-week1
this repository contains a Pizza Restaurant domain with a flask api containing three models Restaurant,Pizza and RestaurantPizza.

##  Project Setup
1. Clone the repository to your local machine using git clone.
2. Navigate to the repository's directory.
3. Create pipenv environment and Install dependencies using pipenv install
4. Activate environment using pipenv shell
5. Navigate into the server directory using cd server/
6. Run the backend api  using python3 run.py or flask run

## Packages used
- flask-restful 
- flask 
- flask-migrate 
- flask-sqlalchemy
- sqlalchemy-serializer
- faker 

## Routes
- GET /restaurants - returns all the restaurants in the database.
- GET /restaurants/:id - returns a specified single restaurant in the database.
- DELETE /restaurants/:id - deletes a specified single restaurant in the database.
- GET /pizzas - returns all the pizzas in the database.
- POST /restaurant_pizzas - posts a restaurant_pizza to the database .

##  Author
Houstin Angwenyi

## License
This project is licensed under the [MIT License](LICENSE).