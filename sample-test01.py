import requests
import json

BASE_Url = "https://reqres.in"

params = {'page': 2}

responseOne = requests.get(BASE_Url + "/api/users", params=params)

# print(json.dumps(responseOne.json(), indent=4))
resp = responseOne.json()
#  import ipdb; ipdb.set_trace()

first_names = [d['first_name'] for d in resp["data"]]
print(first_names)