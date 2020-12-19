"""
В данном коде мы парсим сайт https://news.ycombinator.com/
и получаем список новостей
"""
import requests  # requests - Отправляет запрос на сайт и получает данные
from bs4 import BeautifulSoup  # Структурно форматирует текст в html

response = requests.get('https://news.ycombinator.com/')
response_text = response.text
html = BeautifulSoup(response_text, 'lxml')
trs = html.find('body').find('center').find('table').find_all('tr')
news_tr = trs[3].find('td').find('table').find_all('tr', class_='athing')
l = []
for i in news_tr:
    l.append(
        {"title": i.find_all('td')[2].find('a').text,
         "link": i.find_all('td')[2].find('a')['href']}
    )

print(l)
