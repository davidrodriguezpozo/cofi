from .Product import Product, default_products
from enum import Enum
from typing import List
import numpy as np


class PromoType(Enum):
    COMBINATION = 0  # Combination of products for which you get a discount
    MxN = 1          # Promotion like 2x1, 3x2...
    FIXED = 2        # Promotion with fixed price (more than 3 -> 19€)


class Promotion():
    """
    This class wraps the promotions of the system. A promotion is a kind of discount that a customer
    can get if they buy certain amount or combination of products.
    """
    all_products = default_products

    def __init__(self, promo_products: List[str], discount: int, type: PromoType, min_quantity: int = 0, getMpayN: str = ''):
        self.products: List[Product] = self.add_products(
            promo_products)
        self.type: PromoType = type
        self.min_quantity: int = min_quantity
        self.discount: int = discount
        self.getMpayN: str = getMpayN
        self.validate_promo()

    def __str__(self):
        return f"Promotion products : {[str(prod) for prod in self.products]}. Promotion type: {self.type.name}"

    def validate_promo(self):
        """
        Checks if the promotion is valid. A promotion is valid if: 

        FIXED: min_quantity is informed, and there is only one product in the list of products
        MxN: M and N are both valid integers, and there is only one product (unique) in the list

        """
        if(self.type == PromoType.FIXED):
            assert self.min_quantity is not None
            assert len(np.unique([prod.code for prod in self.products])) == 1

        elif(self.type == PromoType.MxN):
            [m, n] = self.getMpayN.split('x')
            assert int(m) > 0 and int(n) > 0
            assert len(np.unique([prod.code for prod in self.products])) == 1

        elif(self.type == PromoType.COMBINATION):
            assert self.min_quantity is not None
            assert len(np.unique([prod.code for prod in self.products])) > 1

        else:
            raise TypeError('Type of promotion is not valid')

    def add_products(self, product_codes: List[str]):
        """
        Args:
        product_codes: list of the product codes to add to the promotion

        Example:
        ['VOUCHER', 'TSHIRT', 'MUG'] <- To add a promotion of type COMBINATION
        """
        products_list = []
        for product_code in product_codes:
            # Find the product in the products list and add it to the promo products.
            p = next(
                (prod for prod in default_products if prod.code == product_code), None)

            if p is not None:
                products_list.append(p)
            else:
                raise Exception('Product not found!')

        return products_list

    def is_valid(self, unique_products: dict):
        """
        Args:
            unique_products: dictionary containing the product codes and the quantities of the list of products
            that wants to be checked.  


        Checks if a promotion can be applied for a given list of products.
        A promotion is valid if:
        MxN: The list of products contains at least M products of the promotion product (self.product)
        FIXED and COMBINATION: The list of products contains at least self.min_quantity of all the products
                               in self.products
        """
        if (self.type == PromoType.MxN):
            [m, n] = self.getMpayN.split('x')
            if(self.products[0].code in unique_products and unique_products[self.products[0].code] >= int(m)):
                return True
            return False

        else:
            for prod in self.products:
                if prod.code not in unique_products:
                    return False
                elif unique_products[prod.code] < self.min_quantity:
                    return False
            return True

    def compute_discount(self, unique_products: dict) -> float:
        """
        Given a list of products, compute the total discount applied by this promotion, in absolute value. 

        Example: 
            self.type = PromoType.MxN -> 2x1
            unique_products: { "VOUCHER" : 4 }

            returns 10, given that the product VOUCHER costs 5€

        """
        if(self.type == PromoType.MxN):
            [m, n] = self.getMpayN.split('x')
            items = unique_products[self.products[0].code]

            # How many packs of m items can one make from the products
            packs = items // int(m)
            # The remaining products that cannot be packed
            remaining = items % int(m)

            price_without_discount = items * self.products[0].price
            price_with_discount = packs * \
                self.products[0].price * \
                int(n) + remaining * self.products[0].price

            discount = price_without_discount - price_with_discount

            # Remove the products that are in the promotion from the list
            unique_products[self.products[0].code] -= packs * int(m)
            return discount

        elif(self.type == PromoType.COMBINATION):

            # The number of packs that we can make is the minimum of all the products
            # of the promo, present in the products list.
            packs = min([unique_products[prod.code]
                         for prod in self.products if prod.code in unique_products])

            price_without_discount = sum(
                [prod.price * packs for prod in self.products])
            price_with_discount = packs * self.discount

            discount = price_without_discount - price_with_discount

            # Remove the products from the products list
            for prod in self.products:
                if(prod.code in unique_products):
                    unique_products[prod.code] -= packs
            return discount

        elif (self.type == PromoType.FIXED):
            # The number of products is the total number of products of the promotion
            # present in the products list.
            items = unique_products[self.products[0].code]

            price_without_discount = sum(
                [prod.price * items for prod in self.products])
            price_with_discount = items * self.discount

            discount = price_without_discount - price_with_discount

            # Remove the products from the product list
            for prod in self.products:
                if prod.code in unique_products:
                    unique_products[prod.code] -= items

            return discount


promotions = [Promotion(['VOUCHER'], 0, PromoType.MxN, 0, '2x1'), Promotion(
    ['TSHIRT'], 19, PromoType.FIXED, 3), Promotion(['VOUCHER', 'TSHIRT', 'MUG'], 25, PromoType.COMBINATION)]
