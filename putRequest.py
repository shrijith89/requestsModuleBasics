import requests

url = "https://reqres.in/api/users/2"
data = {"name":"testUpdated","job":"testJobUpdated"}

re = requests.put(url,data)
print(re.json())
