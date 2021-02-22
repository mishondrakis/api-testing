import requests
import json

BASE_Url = "https://reqres.in"

response = requests.get(BASE_Url + "/api/users?page=2")

print(response)
print(response.json())
print(json.dumps(response.json(), indent=4))
