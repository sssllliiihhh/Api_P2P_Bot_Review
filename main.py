import requests

url = "http://localhost:8000/users"

data = {
  "name": "slih",
  "link_to_git": "https://github.com/sssllliiihhh/",
  "other_id": 902134453
}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Запрос на регистрацию пользователя успешно отправлен.")
else:
    print("Ошибка при отправке запроса на регистрацию пользователя.")
print(response.text)

