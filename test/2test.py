from bs4 import BeautifulSoup

#soup1 = BeautifulSoup('<a></b></a>', 'lxml')
#soup2 = BeautifulSoup('<a></b></a>', 'html.parser')
#print(soup1)
#print(soup2)

with open ('page.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup)