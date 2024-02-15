import requests

url = "http://localhost:8000/users"

data = {
  "name": "slih",
  "age": 17,
  "other_id": 90213445
}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Запрос на регистрацию пользователя успешно отправлен.")
else:
    print("Ошибка при отправке запроса на регистрацию пользователя.")
print(response.text)

