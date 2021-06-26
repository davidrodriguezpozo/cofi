from ..models.Product import Product
import pytest


def test_invalid_price_1():
    """
    Test that price must be a float, and cannot be a string
    """
    with pytest.raises(TypeError):
        Product('TEST', 'Test product', 'a')


def test_invalid_price_2():
    """
    Test that price must be positive
    """
    with pytest.raises(TypeError):
        Product('TEST', 'Test product', -4)


def test_valid_product():
    """
    Test that a given product is created correctly
    """
    product = Product('TEST', 'Test product', 3.50)
    assert product.code == 'TEST'
    assert product.name == 'Test product'
    assert product.price == 3.50
