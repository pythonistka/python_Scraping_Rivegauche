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


def get_result():
    with open('result.json', encoding='utf-8') as file:
        products_data = json.load(file)

        products_data_information = {}
        for item in products_data:
            product_name = item.get('name')
            product_name = product_name.upper()
            product_link = item.get('url')
            product_price = item.get('price').get('value')
            product_price_base = item.get('prices')[2].get('value')
            product_price_sale = int(100 - (product_price * 100 / product_price_base))

            products_data_information[product_name] = {
                'product_link': f'https://rivegauche.ru{product_link}',
                'product_price_base': product_price_base,
                'product_price': product_price,
                'product_price_sale': f'{product_price_sale}%'
            }
        # print(products_data_information)
        with open('total_result.json', 'w', encoding='utf-8') as file:
            json.dump(products_data_information, file, indent=4, ensure_ascii=False)


def main():
    collect_data()
    get_result()


if __name__ == '__main__':
    main()
