import json


class Product():
    def __init__(self, code, name, price):
        self.__name: str = name
        self.__code: str = code
        self.__price: float = float(price)

    def __str__(self):
        return f'Product name: {self.name}. Product code: {self.code}. Price: {self.price} €'

    @property
    def name(self) -> str:
        return self.__name

    @property
    def code(self) -> str:
        return self.__code

    @property
    def price(self) -> float:
        return self.__price


with open('./products.json') as products_file:
    json_products = json.load(products_file)

default_products = []
for prod in json_products:
    default_products.append(
        Product(prod, json_products[prod]['name'], json_products[prod]['price']))
