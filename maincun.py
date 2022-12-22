import time
import requests

print('Hello, world')
c = 0
while c != 2:
    print('Privet mir')
    c+= 1
    print('null')
api_url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(response.text)
    print(response.status_code)
else:
    print(response.status_code)    # При другом коде ответа выводим этот код
