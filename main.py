import math

from fake_useragent import UserAgent
# установим fake-useragent для генерации рандомных юзер агентов
import requests
import random
import json

# получаем юзерагент
ua = UserAgent()


# print(ua.random)


def collect_data():
    s = requests.Session()
    response = s.get(
        'https://api.rivegauche.ru/rg/v1/newRG/products/search?fields=FULL&currentPage=0&pageSize=100&categoryCode=Perfumery&tag=3959512627673786',
        headers={'user-agent': f'{ua.random}'}).json()
    total_items = response.get('pagination').get('totalResults')
    # print(total_items)

    if total_items is None:
        return '[!] нет товаров :('

    pages_count = math.ceil(total_items / 100)
    print(pages_count)

def main():
    collect_data()


if __name__ == '__main__':
    main()
