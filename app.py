""" 
Simple RESTful API
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

## Resources ##
# Classes inherit from Resource

class RouteOne(Resource):
    def get(self):
        return {"data": "RouteOne: GET"}

    def post(self):
        return {"data": "RouteOne: POST"}

## API Routing ##
# Add RouteOne to the API and define the endpoint
api.add_resource(RouteOne, '/')

if __name__ == "__main__":
    app.run(debug=True)
