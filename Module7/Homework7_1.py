import requests
from pprint import  pprint
ip_adress = input("Введите ip: ")
data = requests.post(
    "http://ip-api.com/json/"+ip_adress
)

if data.json()["status"] == "fail":
    print("Таĸого IP не существует")
else:
    print(data.json()["country"])
