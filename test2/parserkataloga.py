import requests
from bs4 import BeautifulSoup

pages_count = 10


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def crawl_products(pages_count):
    url = 'https://parsemachine.com/sandbox/catalog/?page={page}'
    urls = []

    for page_n in range(1, pages_count + 1):
        print('page: {}'.format(page_n))
        page_url = url.format(page=page_n)
        soup = get_soup(url=page_url)
        if soup is None:
            break

        products = soup.find_all('a', class_='no-hover title')
        for product in products:
            url_of_product = str('https://parsemachine.com' + product.get('href'))
            urls.append(url_of_product)

    return urls


def parse_products(urls):
    data = []

    for url in urls:
        soup = get_soup(url=url)
        product_name = soup.find('h1', id='product_name').text.strip()
        product_amount = soup.find('big', id='product_amount').text.strip()
        print(product_name, product_amount)

        characteristics = {}
        characts = soup.find('table', id='characteristics').find('tbody').find_all('tr')
        for charact in characts:
            char = charact.find('td').text.strip()
            value = charact.find_all('td')[-1].text.strip()
            characteristics[char] = value
        print(characteristics)
        item = {
            'name': product_name,
            'amount': product_amount,
            'characters': characteristics
        }

        data.append(item)
    print(data)


def main():
    urls = crawl_products(pages_count)
    data = parse_products(urls)


if __name__ == '__main__':
    main()
