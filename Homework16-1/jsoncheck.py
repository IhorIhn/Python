import json
import logging

# Налаштування логера
log_file = "json__Ignatenko.log"
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding='utf-8'
)

# Список JSON-файлів для перевірки
json_files = ["json1.json", "json2.json", "login.json", "swagger.json"]

# Перевірка кожного файлу
for file in json_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            json.load(f)  # спроба прочитати JSON
    except json.JSONDecodeError as e:
        logging.error(f"Файл '{file}' невалідний JSON: {e}")

print(f"Файли перевірені. Лог помилок у файлі: {log_file}")
