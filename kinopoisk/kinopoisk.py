import requests
from bs4 import BeautifulSoup
user_id = 51389537
url = 'http://www.kinopoisk.ru/user/%d/votes/' % (user_id)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
           "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"}
r = requests.get(url, headers=headers, stream=True)



print(r.status_code)

with open('text.html', 'w', encoding='utf-8', errors='ignore') as f:
    f.write(r.text)

