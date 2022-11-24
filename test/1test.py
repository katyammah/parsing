print('Hello')

import requests
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
          "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"}

#query = {'search_query':'весна'}

#r = requests.get('https://httpbin.org/get', headers=headers, params=query)
#r = requests.get('https://www.youtube.com/results', headers=headers, params=query)

#print(r.status_code)
#print(r.headers)
#print(r.text)


# data = {
#     "custemail": "kat.mahova96@mail.ru",
#     "custname": "123",
#     "custtel": "1-34-56",
#     "size": "small",
#     "topping": "bacon"
# }
#
# r = requests.post('https://httpbin.org/post', headers=headers, data=data)
#
# print(r.json()['form']['topping'])

url = 'https://www.shutterstock.com/shutterstock/videos/1054727690/preview/stock-footage-beautiful-summer-morning-in-the-forest-sun-rays-break-through-the-foliage-of-magnificent-green.webm'

r = requests.get(url, headers=headers, stream=True) #stream=потоковое чтение
# print(r.raw.read(10))

#with open('1.webm', 'wb') as fd:
#    for chunk in r.iter_content(chunk_size=1024*100):
#        fd.write(chunk)
#        print('Write chunk 1ookb')

print(r.__dict__)