from typing import List, Tuple
from .Product import Product, default_products
from .Promotion import Promotion, promotions
from itertools import permutations


class Checkout():
    """
    Class that contains the products list. This class provides the property total
    that gives the total of the ticket, with the promotion applied.
    """

    def __init__(self):
        self.products: List[Product] = []
        self.unique_products: dict = {}

    @property
    def total(self):
        """
        Method that computes the total of the ticket, given all the promotions available. 

        1. Get all promotions that apply to the ticket. 
        2. Get all possible combinations of promotions to be applied to the ticket. 
        3. Apply them and get the best one. 
        4. Apply the discount of the best one and substract it from the total. 
        5. Return the result.
        """
        applicable_promotions = []

        for promotion in promotions:
            # For all promotions, get the ones that are valid in the current ticket.
            if promotion.is_valid(self.unique_products):
                applicable_promotions.append(promotion)

        # For all the promotions applicable in the current ticket, get all possible combinations.
        all_possible_combinations: Tuple[List[Promotion]] = list(permutations(
            applicable_promotions, len(applicable_promotions)))

        # Now that we have all the possible combinations compute the total discount on the ticket.
        ticket_discount: float = 0

        for combination in all_possible_combinations:
            remaining_products = self.unique_products.copy()
            combination_discount: float = 0

            for promotion in combination:
                # Each promotion is applied to the ticket and the products that have the promotion are removed from it
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
        else:
            print('Product not found.')
