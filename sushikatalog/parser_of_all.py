import requests
from bs4 import BeautifulSoup
import csv
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
           "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"}

URL = 'https://sushishop.ru/'


def get_soup(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def crawl_categories(url):
    urls_of_cats = []
    soup = get_soup(url)
    cats = soup.find('div', class_='home-app-menu__links').find_all('a')
    for cat in cats:
        url_of_cat = str(url) + cat.get('href')
        urls_of_cats.append(url_of_cat)

        title_of_cat = cat.find('span', class_='home-app-menu__item-title').text.strip()
        with open('{}.csv'.format(title_of_cat), 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            table_head = ['Title', 'price', 'weight', 'caloricity']
            writer.writerow(table_head)

    return urls_of_cats


def crawl_products(urls):
    for url in urls:
        soup = get_soup(url)
        products = soup.find('div', class_='category__items').find_all('a')
        title_of_cat = soup.find_all('div', class_='breadcrumbs__element')[-1].find('span',
                                                                                    class_='breadcrumbs__element-title').text.strip()

        for product in products:
            title = product.find('span', class_='category__item-title').text.strip()
            price = product.find('span', class_='category__item-price').text.strip()
            price_old = product.find('span', class_='category__item-price__old')
            if price_old is not None:
                # использую модуль re, чтобы отбросить ненужное значение старой цены
                # (оно находится во вложенном теге родительского,
                # которое мне не нужно, а нужно непосредственнно содержимое родительского тега)
                # пример: <класс цена><класс старая уена>300р</старая цена>200р</цена>
                price = re.split(r'\s₽', product.find('span', class_='category__item-price').text.strip(), maxsplit=1)[
                    -1]
                # или зная, сколько символов надо в строчке отнять, пользуюсь извлечением подстроки из строки:
                # price = product.find('span', class_='category__item-price').text.strip()[-5:]

            url_of_product = 'https://sushishop.ru' + product.get('href')
            soup2 = get_soup(url_of_product)
            weight = soup2.find('div', class_='item__weight').text.strip()
            caloricity = soup2.find('div', class_='caloricity-table__td caloricity-table__energy').find('span',
                                                                                                        class_='caloricity-table__td-value').text.strip()
            data = [title, price, weight, caloricity]
            with open('{}.csv'.format(title_of_cat), 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)


def main():
    urls = crawl_categories(URL)
    crawl_products(urls)


if __name__ == "__main__":
    main()
