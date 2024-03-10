import requests
i = 1
url = f"http://127.0.0.1:8000/queue/{i}"

data = {
  "name": "slih",
  "link_to_git": "https://github.com/sssllliiihhh/",
  "other_id": 902134453
}
response = requests.get(url)

if response.status_code == 200:
    print("Запрос на регистрацию пользователя успешно отправлен.")
else:
    print("Ошибка при отправке запроса на регистрацию пользователя.")
string = response.text
print(string)
words = string.split()
text1 = words[1]  # извлекаем слово по индексу
if text1 == "Out":
    print(1+1)
if text1 == "No":
    print(1+1)
id1 = words[2]
text2 = words[3]
id2 = words[4]
print(id1, id2, text1, text2)


