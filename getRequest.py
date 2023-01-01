import requests

r = requests.get("https://reqres.in/api/users?page=2")
print(r.status_code)
print(r.json())