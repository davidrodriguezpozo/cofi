from typing import List, Tuple
from .Product import Product, default_products
from .Promotion import Promotion, promotions
from itertools import permutations


class Checkout():
    def __init__(self):
        self.products: List[Product] = []
        self.unique_products: dict = {}

    @property
    def total(self):
        applicable_promotions = []

        for promotion in promotions:
            if promotion.is_valid(self.unique_products):
                applicable_promotions.append(promotion)

        all_possible_combinations: Tuple[List[Promotion]] = list(permutations(
            applicable_promotions, len(applicable_promotions)))

        # Now that we have all the possible combinations let's compute the total discount on the ticket.
        ticket_discount: float = 0

        for combination in all_possible_combinations:
            remaining_products = self.unique_products.copy()
            combination_discount: float = 0

            for promotion in combination:
                discount = promotion.compute_discount(
                    remaining_products)
                combination_discount += discount

            if combination_discount > ticket_discount:
                ticket_discount = combination_discount

        return sum([prod.price for prod in self.products]) - ticket_discount

    def scan(self, product: str):
        product = next(
            (p for p in default_products if p.code == product), None)
        if product is not None:
            self.products.append(product)
            try:
                self.unique_products[product.code] += 1
            except:
                self.unique_products[product.code] = 1
