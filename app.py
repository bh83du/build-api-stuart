""" 
Simple RESTful API
"""

from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

# Album dictionary

album = {}

## Argument Parsing ##

# Create RequestParser object
parser = reqparse.RequestParser()

# Specify mandatory arguments
parser.add_argument(
    "name", type=str, help="Album Name is required", required=True)
parser.add_argument(
    "year", type=int, help="Release Year is required", required=True)
parser.add_argument(
    "label", type=str, help="Label is required", required=True)
parser.add_argument(
    "catalogue", type=str, help="Catalogue ID is required", required=True)

## Resources ##
# Classes inherit from Resource


class GetAlbums(Resource):
    def get(self):
        return album


class GetAlbum(Resource):
    def get(self, album_cat):
        return album[album_cat]


class NewAlbum(Resource):
    def post(self, album_cat):
        args = parser.parse_args()
        album[album_cat] = args
        return album[album_cat]


## API Routing ##
api.add_resource(GetAlbums, '/')
api.add_resource(GetAlbum, '/album/<string:album_cat>')
api.add_resource(NewAlbum, '/album/<string:album_cat>')



if __name__ == "__main__":
    app.run(debug=True)
