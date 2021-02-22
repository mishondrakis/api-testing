import requests
import json

BASE_Url = "https://reqres.in"

params = {'page': 2}

responseOne = requests.get(BASE_Url + "/api/users", params=params)

print(json.dumps(responseOne.json(), indent=4))
