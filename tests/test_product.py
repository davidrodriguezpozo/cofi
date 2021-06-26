from ..models.Product import Product
import pytest


def test_invalid_price():
    with pytest.raises(ValueError):
        product = Product('TEST', 'Test product', 'a')


def test_valid_product():
    product = Product('TEST', 'Test product', 3.50)
    assert product.code == 'TEST'
    assert product.name == 'Test product'
    assert product.price == 3.50
