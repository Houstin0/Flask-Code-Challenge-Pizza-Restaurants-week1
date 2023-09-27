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
- GET /restaurants
- GET /restaurants/:id
- DELETE /restaurants/:id
- GET /pizzas
- POST /restaurant_pizzas

##  Author
Houstin Angwenyi

## License
This project is licensed under the [MIT License](LICENSE).