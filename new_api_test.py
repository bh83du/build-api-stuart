"""
Test File for API

Run Flask Server on URL http://127.0.0.1:5000"

"""

import requests
import simplejson as json

BASE_URL = "http://127.0.0.1:5000"


# Use a POST request to create a new Item
response = requests.post(
    BASE_URL + "/album/EMTC103",
    {"catalogue": "EMTC103", "year": "1975", "name": "A Night at the Opera", "label": "EMI"})
print(response.text)
print("Response Status Code: " + str(response.status_code))

response = requests.post(
    BASE_URL + "/album/EMTC104", data={"catalogue": "EMTC104", "year": "1976", "label": "EMI", "name": "A Day at the Races"})
print(response.text)
print("Response Status Code: " + str(response.status_code))

response = requests.post(
    BASE_URL + "/album/EMA784", data={"catalogue": "EMA784", "year": "1977", "label": "EMI", "name": "News of the World"})
print(response.text)
print("Response Status Code: " + str(response.status_code))

response = requests.post(
    BASE_URL + "/album/EMA795", data={"catalogue": "EMA795", "year": "1980", "label": "EMI", "name": "The Game"})
print(response.text)
print("Response Status Code: " + str(response.status_code))

response = requests.post(
    BASE_URL + "/album/EMA797", data={"catalogue": "EMA797","year": "1982", "name": "Hot Space"})
print(response.text)
print("Response Status Code: " + str(response.status_code))

response = requests.post(
    BASE_URL + "/album/EMC24", data={"catalogue": "EMC24", "name": "The Works", "label": "EMI"})
print(response.text)
print("Response Status Code: " + str(response.status_code))

# GET Request to return all albums:

response = requests.get(BASE_URL)
print(response.text)
print("Response Status Code: " + str(response.status_code))

# GET Request to return Single Album

response = requests.get(BASE_URL + "/album/EMTC103")
print(response.text)
print("Response Status Code: " + str(response.status_code))

