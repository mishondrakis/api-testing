import requests
import json

BASE_Url = "https://reqres.in"




responseOne = requests.get(BASE_Url + "/api/users/2")

print(json.dumps(responseOne.json(), indent=4))