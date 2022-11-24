import requests
from bs4 import BeautifulSoup
import csv

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
           "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"}


def get_data(url):
    response = requests.get(url=url, headers=headers)

    with open('pythontoday.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

    with open('pythontoday.html', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')


    table = soup.find('table', id="tark40")

    data_td = table.find('thead').find('tr').find_all('td')
    table_head = []
    for dtd in data_td:
        dtd = dtd.text.strip()
        table_head.append(dtd)

    with open('file_data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            (table_head)
        )

    table_countries = table.find('tbody').find_all('tr')

    for country in table_countries:
        country_column = country.find_all('td')
        table_body = []
        for each_column in country_column:
            each_column = each_column.text.strip()
            table_body.append(each_column)

        with open('file_data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(
                (table_body)
            )


def main():
    get_data(url='https://u-karty.ru/russia/countries-europe-by-area.html')


if __name__ == "__main__":
    main()
