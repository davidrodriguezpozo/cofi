import json


class Product():
    """
    This class wraps the information of a given product.
    This information is:
    - Code
    - Name
    - Price
    """

    def __init__(self, code, name, price):
        self.__name: str = name
        self.__code: str = code
        self.price: float = price

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

    @price.setter
    def price(self, value):
        if(type(value) == 'str'):
            raise TypeError('Value must be a positive number')
        if(value < 0):
            raise TypeError('Price must be positive')
        self.__price = value


with open('./products.json') as products_file:
    try:
        json_products = json.load(products_file)
    except Exception as e:
        raise Exception(
            'Products could not be loaded correctly, check JSON file')

default_products = []
for prod in json_products:
    default_products.append(
        Product(prod, json_products[prod]['name'], json_products[prod]['price']))
