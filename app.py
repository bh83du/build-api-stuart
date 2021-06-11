""" 
Simple RESTful API
"""

from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

# Names dictionary

names = {}

## Argument Parsing ##

# Create RequestParser object
parser = reqparse.RequestParser()

# Specify mandatory arguments
parser.add_argument(
    "name", type=str, help="Name is required", required=True)
parser.add_argument(
    "age", type=int, help="Age is required", required=True)
parser.add_argument(
    "fav_colour", type=str, help="Favourite Colour", required=False)

## Resources ##
# Classes inherit from Resource

class RouteOne(Resource):
    def get(self):
        return {"data": "RouteOne: GET"}

    def post(self):
        args = parser.parse_args()
        names.update(args)
        return names

## API Routing ##
# Add RouteOne to the API and define the endpoint
api.add_resource(RouteOne, '/')

if __name__ == "__main__":
    app.run(debug=True)
