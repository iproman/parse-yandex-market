import csv

import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)


def write_csv(data):
    with open('yandex-market.csv', 'a') as f:
        writer = csv.writer(f)
        pass


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    pass


def main():
    url = ''
    get_html(url)


if __name__ == '__main__':
    main()
