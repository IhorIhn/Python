import requests
import os

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

# Відправляю GET-запит
response = requests.get(url, params=params)

# Перевіряємо статус відповіді
if response.status_code == 200:
    data = response.json()
    photos = data['photos']

    # Створимо папку для збереження картинок
    os.makedirs('mars_photos', exist_ok=True)

    # Зробимо обмеження на кількість картинок для завантаження
    for i, photo in enumerate(photos[:5], start=1):
        img_url = photo['img_src']
        img_data = requests.get(img_url).content
        filename = f'mars_photos/mars_photo{i}.jpg'

        with open(filename, 'wb') as f:
            f.write(img_data)
        print(f'Збережено: {filename}')
else:
    print('Помилка при запиті до API:', response.status_code)
