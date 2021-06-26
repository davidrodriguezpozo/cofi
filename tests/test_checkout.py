from ..models.Checkout import Checkout
from ..models.Promotion import Promotion, promotions, PromoType
import pytest


def test_ticket_scan():
    ticket = Checkout()
    ticket.scan('NOTHING')
    assert ticket.total == 0
    assert len(ticket.products) == 0


def test_ticket_1():
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
    ticket = Checkout()

    ticket.scan('VOUCHER')
    ticket.scan('VOUCHER')
    ticket.scan('VOUCHER')
    ticket.scan('TSHIRT')
    ticket.scan('MUG')

    assert ticket.total == 30


def test_ticket_3():
    ticket = Checkout()
    ticket.scan('VOUCHER')
    ticket.scan('VOUCHER')
    ticket.scan('VOUCHER')

    promotions.append(Promotion(['VOUCHER'],
                                0, PromoType.MxN, 1, '3x1'))
    assert ticket.total == 5

    promotions.pop()

    assert ticket.total == 10
