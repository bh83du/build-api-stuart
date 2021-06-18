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
response = requests.post(
    BASE_URL + "/album/EMTC103",
    {"catalogue": "EMTC103", "year": 1975, "name": "A Night at the Opera", "label": "EMI"})
# Confirm response
print(response.text)

# Test Name is Mandatory
response = requests.post(
    BASE_URL + "/album/EMTC104", data={"catalogue": "EMTC104", "year": 1976, "label": "EMI"})
print(response.text)

#Expected Output
# "Album Name is required"

# Post Further Data

response = requests.post(
    BASE_URL + "/album/EMTC104", data={"catalogue": "EMTC104", "year": 1976, "label": "EMI", "name": "A Day at the Races"})

response = requests.post(
    BASE_URL + "/album/EMA784", data={"catalogue": "EMA784", "year": 1977, "label": "EMI", "name": "News of the World"})

response = requests.post(
    BASE_URL + "/album/EMA795", data={"catalogue": "EMA795", "year": 1980, "label": "EMI", "name": " The Game"})


# GET Data

# Returns All
response = requests.get(BASE_URL)
print(response.text)

# Return a single Album
response = requests.get(BASE_URL + "/album/EMTC104")
print(response.text)

'''
# GET Request where Catalogue ID doesn't exist.  Generates KeyError
response = requests.get(BASE_URL + "/album/EMA796")
print(response.text)

# Expected response
# KeyError : 'EMA796'
# Kills Console.  Need to restart Flask
'''


