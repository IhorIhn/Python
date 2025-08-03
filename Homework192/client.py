import requests
import urllib.parse

BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = "example.png"

# 1. Завантажую зображення (POST /upload)
with open(IMAGE_PATH, "rb") as img:
    files = {"image": img}
    response = requests.post(f"{BASE_URL}/upload", files=files)

if response.status_code == 201:
    image_url = response.json()["image_url"]
    print("[UPLOAD] Успішно завантажено:", image_url)
else:
    print("[UPLOAD] Помилка:", response.text)
    exit()

# 2. Достаю ім'я файлу з URL
filename = image_url.split("/")[-1]
encoded_filename = urllib.parse.quote(filename)

# 3. Отримую URL зображення
headers = {"Content-Type": "text"}
response = requests.get(f"{BASE_URL}/image/{encoded_filename}", headers=headers)
print("[GET] Відповідь сервера:", response.json())

# 4. Видаляю файл з сервера
response = requests.delete(f"{BASE_URL}/delete/{encoded_filename}")
print("[DELETE] Статус:", response.status_code)
try:
    print("[DELETE] Відповідь сервера:", response.json())
except Exception:
    print("[DELETE] Відповідь не в форматі JSON:", response.text)

