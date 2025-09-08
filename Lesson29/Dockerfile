# Базовий образ Python
FROM python:3.11-slim

# Робоча директорія
WORKDIR /app

# Копіюємо requirements
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код
COPY . .

# Команда запуску застосунку
CMD ["python", "app.py"]
