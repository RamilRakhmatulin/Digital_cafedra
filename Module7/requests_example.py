import requests
from pprint import  pprint
response = requests.get('https://python.org')
print(response.status_code)
text = 'Python is a programming language that lets you work quickly'
print(text in response.text)

response2 = requests.post(
    "https://postman-echo.com/post",
    data = {
        'a': "test",
        'b': 2
    }
)
print(response2.status_code)
pprint(response2.json())