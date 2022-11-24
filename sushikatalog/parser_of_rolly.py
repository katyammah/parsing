import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://sushishop.ru/rolly'

table_head = ['Title', 'price', 'weight', 'caloricity']
with open('rolly.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(table_head)


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def crawl_products(url):
    soup1 = get_soup(url)
    products = soup1.find('div', class_='category__items').find_all('a')

    for product in products:
        title = product.find('span', class_='category__item-title').text.strip()
        price = product.find('span', class_='category__item-price').text.strip()
        price_old = product.find('span', class_='category__item-price__old')
        if price_old is not None:
            # использую модуль re, чтобы отбросить ненужное значение старой цены
            # (оно находится во вложенном теге родительского,
            # которое мне не нужно, а нужно непосредственнно содержимое родительского тега)
            price = re.split(r'\s₽', product.find('span', class_='category__item-price').text.strip(), maxsplit=1)[-1]
            # или зная, сколько символов надо в строчке отнять, пользуюсь извлечением подстроки из строки:
            # price = product.find('span', class_='category__item-price').text.strip()[-5:]

        url_of_product = 'https://sushishop.ru' + product.get('href')
        soup2 = get_soup(url_of_product)
        weight = soup2.find('div', class_='item__weight').text.strip()
        caloricity = soup2.find('div', class_='caloricity-table__td caloricity-table__energy').find('span', class_='caloricity-table__td-value').text.strip()
        data = [title, price, weight, caloricity]
        with open('rolly.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)


def main():
    crawl_products(url)


if __name__ == "__main__":
    main()
