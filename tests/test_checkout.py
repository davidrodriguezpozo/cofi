from ..models.Checkout import Checkout
from ..models.Promotion import Promotion, promotions, PromoType
import pytest


def test_ticket_scan_1():
    """
    Test that the scan of the ticket scans nothing if the product is not found
    """
    ticket = Checkout()
    ticket.scan('NOTHING')
    assert ticket.total == 0
    assert len(ticket.products) == 0


def test_ticket_scan_2():
    """
    Test that the scan of the ticket scans a product correctly
    """
    ticket = Checkout()
    ticket.scan('VOUCHER')
    assert len(ticket.products) == 1
    assert ticket.products[0].code == 'VOUCHER'


def test_ticket_1():
    """
    Test the total value of a given ticket
    """
    ticket = Checkout()

    ticket.scan('VOUCHER')
    ticket.scan('VOUCHER')
    ticket.scan('VOUCHER')
    ticket.scan('TSHIRT')
    ticket.scan('TSHIRT')
    ticket.scan('TSHIRT')
    ticket.scan('TSHIRT')
    ticket.scan('TSHIRT')
    ticket.scan('VOUCHER')
    ticket.scan('MUG')

    assert ticket.total == 111


def test_ticket_2():
    """
    Test the total value of a given ticket
    """
    ticket = Checkout()

    ticket.scan('VOUCHER')
    ticket.scan('VOUCHER')
    ticket.scan('VOUCHER')
    ticket.scan('TSHIRT')
    ticket.scan('MUG')

    assert ticket.total == 30


def test_ticket_3():
    """
    Test that two different promotions are applied if a new 
    promotion is added that is better than the one applied
    """
    ticket = Checkout()
    ticket.scan('VOUCHER')
    ticket.scan('VOUCHER')
    ticket.scan('VOUCHER')

    assert ticket.total == 10
    promotions.append(Promotion(['VOUCHER'],
                                0, PromoType.MxN, 1, '3x1'))
    assert ticket.total == 5

    promotions.pop()

    assert ticket.total == 10
