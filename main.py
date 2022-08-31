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

    # response = requests.get(
    #     url='https://api.rivegauche.ru/rg/v1/newRG/products/search?fields=FULL&currentPage=0&pageSize=100&categoryCode=Perfumery&tag=3959512627673786',
    #     headers={'user-agent': f'{ua.random}'}
    # )
    # with open('totalResults.json', 'w', encoding='utf-8') as file:
    #     json_data = response.json()
    #     json.dump(json_data['pagination']['totalResults'], file, indent=4, ensure_ascii=False)

    num_page = 0
    result = []
    for item in range(pages_count):
        page = item
        print(f'[+] Добавлена {page} страница')

        url = f'https://api.rivegauche.ru/rg/v1/newRG/products/search?fields=FULL&currentPage={num_page}&pageSize=100&categoryCode=Perfumery&tag=3959512627673786'
        response = requests.get(
            url=url,
            headers={'user-agent': f'{ua.random}'}
        )
        num_page += 1

        list_data = response.json()['results']
        result = result + list_data

    with open('result.json', 'w', encoding='utf-8') as file:
        json_data = response.json()
        json.dump(result, file, indent=4, ensure_ascii=False)


def main():
    collect_data()


if __name__ == '__main__':
    main()
