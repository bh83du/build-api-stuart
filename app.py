""" 
Simple RESTful API
"""

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import boto3
import botocore.exceptions
import simplejson as json

# Create the DynamoDB resource

dynamodb = boto3.resource('dynamodb', region_name='eu-west-2', aws_access_key_id='REMOVED', aws_secret_access_key='REMOVED')

app = Flask(__name__)
api = Api(app)

## Argument Parsing ##

# Create RequestParser object
parser = reqparse.RequestParser()

# Specify mandatory arguments
parser.add_argument(
    "name", type=str, help="Album Name is required", required=True)
parser.add_argument(
    "year", type=str, help="Release Year is required", required=True)
parser.add_argument(
    "label", type=str, help="Label is required", required=False)
parser.add_argument(
    "catalogue", type=str, help="Catalogue ID is required", required=True)

## Resources ##
# Classes inherit from Resource


class GetAlbums(Resource):
    def get(self):
        # Get Table
        try:
            TABLE = dynamodb.Table('albums')
            ALL_ALBUMS = TABLE.scan()
            print(ALL_ALBUMS)
            return ALL_ALBUMS['Items']
        except:
            return 'Error: Table Not Found'


class GetAlbum(Resource):
    def get(self, album_cat):
        # Get Specific Album from Table
        try:
            TABLE = dynamodb.Table('albums')
            ALBUM = TABLE.get_item(
                Key={
                    'catalogue': 'EMTC103'
                }
            )
            return ALBUM['Item']
        except:
            return 'Error: Album Not Found'


class NewAlbum(Resource):
    def post(self, album_cat):
        args = parser.parse_args()
        #Add Album to the table
        try:
            TABLE = dynamodb.Table('albums')
            TABLE.put_item(
                Item={
                    'catalogue': args['catalogue'],
                    'name': args['name'],
                    'year': args['year'],
                    'label': args['label']
                }
            )
            return 'Album Added'
        except:
            return 'Album Not Added'

## API Routing ##
api.add_resource(GetAlbums, '/')
api.add_resource(GetAlbum, '/album/<string:album_cat>')
api.add_resource(NewAlbum, '/album/<string:album_cat>')



if __name__ == "__main__":
    app.run(debug=True)
