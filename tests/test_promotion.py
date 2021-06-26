from ..models.Promotion import Promotion, promotions, PromoType
from ..models.Product import Product, default_products
import pytest


def test_valid_promotion():
    promo = Promotion([default_products[0].code], 10, PromoType.MxN, 1, '2x1')
    assert promo.is_valid({default_products[0].code: 2}) is True


def test_invalid_promotion():
    with pytest.raises(Exception):
        Promotion([default_products[0].code], 10, PromoType.MxN, 1, '2xa')


def test_change_promotion():
    promo = Promotion(['VOUCHER', 'TSHIRT'], 10, PromoType.COMBINATION, 1, '')
    promo.validate_promo()

    promo.products.pop()
    with pytest.raises(AssertionError):
        promo.validate_promo()
