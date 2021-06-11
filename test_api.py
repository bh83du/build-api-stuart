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
response = requests.post(BASE_URL)

# Confirm response

print(response.text)


