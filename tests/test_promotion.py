from ..models.Promotion import Promotion, PromoType
from ..models.Product import default_products
import pytest


def test_valid_promotion():
    """
    Test that a promotion is valid for a simple ticket
    """
    promo = Promotion([default_products[0].code], 10, PromoType.MxN, 1, '2x1')
    assert promo.is_valid({default_products[0].code: 2}) is True


def test_invalid_promotion():
    """
    Test that a promotion gives an error if wrong values are inserted when creating it
    """
    with pytest.raises(Exception):
        Promotion([default_products[0].code], 10, PromoType.MxN, 1, '2xa')


def test_change_promotion():
    """
    Test that a combination promotion gives an error if it only contains 
    one item, after creating it with more items. 
    """
    promo = Promotion(['VOUCHER', 'TSHIRT'], 10, PromoType.COMBINATION, 1, '')
    promo.validate_promo()

    promo.products.pop()
    with pytest.raises(AssertionError):
        promo.validate_promo()


def test_invalid_type():
    """
    Test that a random promotion type is not valid. 
    """
    with pytest.raises(TypeError):
        Promotion([default_products[0].code], 10, 'Non-valid type', 1, '2xa')
