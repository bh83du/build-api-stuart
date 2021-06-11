"""

Test File for API

Run Flask Server on URL http://127.0.0.1:5000"

"""

import requests

BASE_URL = "http://127.0.0.1:5000"

# GET Request to RouteOne
response = requests.get(BASE_URL)

# Check response is as expected

print(response.text)

# POST Request to RouteOne
response = requests.post(BASE_URL, data={"name": "Stuart", "age": 46, "fav_colour": "Blue"})

# Confirm response

print(response.text)

# Test Name is Mandatory
response = requests.post(BASE_URL, data={"age": 47, "fav_colour": "Green"})
print(response.text)

# Test age is integer

response = requests.post(BASE_URL, data={"name": "Ann", "age": 77})
print(response.text)

