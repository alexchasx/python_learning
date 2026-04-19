import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Заголовки для имитации обычного браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/'
}

# URL сайта, который будем парсить
url = 'https://news.ycombinator.com/'


def parse_page(url):
    # Добавляем случайную задержку для имитации человеческого поведения
    time.sleep(random.uniform(1, 3))

    # Отправляем запрос
    response = requests.get(url, headers=headers)
    # Проверяем успешность запроса
    if response.status_code != 200:
        print(f"Ошибка при доступе к странице: {response.status_code}")
        return
    
    # Создаём объект BeautifulSoup для парсинга
    soup = BeautifulSoup(response.text, 'html.parser')
    # Находим все элементы с новостями
    news_items = soup.select('.athing')
    # Список для хранения результатов
    news_data = []
    # Извлекаем данные из каждой новости
    for item in news_items:
        title_element = item.select_one('.titleline > a')
        title = title_element.text
        link = title_element['href']
        news_data.append({
            'title': title,
            'link': link
        })
    return news_data 


def main():
    print("Начинаем парсинг Hacker News...")
    # Парсим первую страницу
    news_data = parse_page(url)
    # Дополнительно можно парсить следующие страницы
    next_page_url = url + 'news?p=2'
    news_data.extend(parse_page(next_page_url))

    # Преобразуем в DataFrame для дальнейшей обработки
    df = pd.DataFrame(news_data)
    print(f"Собрано {len(df)} новостей")
    # Выводим первые 5 результатов
    print(df.head())
    # Сохраняем результаты в CSV-файл
    df.to_csv('hacker_news_data.csv', index=False)
    print("Данные сохранены в hacker_news_data.csv")


if __name__ == "__main__":
    main()