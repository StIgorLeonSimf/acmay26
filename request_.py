import requests
from bs4 import BeautifulSoup


def pars(url):
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content, 'html.parser')
    name = soup.find('h1', class_='person-caption').text
    print(name)
    # pos = soup.find('span', class_='person-appointment-title').text[:-2]
    pos = soup.find('span', class_='person-appointment-title').text.replace(':','')
    print(pos)
    langs = soup.find('dl', class_='main-list large main-list-language-knowledge-level')
    langs = langs.find_all('dd')
    for l in langs:
        print(l.text)


staff = ['https://www.hse.ru/staff/allat',
         'https://www.hse.ru/org/persons/135897',
         'https://www.hse.ru/org/persons/63890353']
for s in staff:
    pars(s)
