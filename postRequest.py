import requests

url = "https://reqres.in/api/users"
data = {"name":"test","job":"testJob"}

re = requests.post(url,data)
print(re.json())
