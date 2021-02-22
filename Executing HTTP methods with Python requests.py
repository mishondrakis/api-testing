import requests
import json

Base_URL = "https://reqres.in"
data = {"name": "morpheus",
        "job": "leader"}

responseTwo = requests.post(Base_URL + "/api/users", data=data)

print(responseTwo.json())