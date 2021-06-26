# Cofi - Checkout with promotions

## Adding and computing promotions to several items in a given ticket. 

This little project consists of several classes that allow a user to add products to a ticket, and given some promotion, obtain the total of this ticket. 

***
## Products

The `Product` class offers a wrapper for given product. It is a very simple class to store the code, the name and the price of a given product. 


`products.json`

Products are loaded from a json file in the root of the project. A product in this file has the following strucure: 

```
"CODE": {
        "price": PRICE,
        "name": NAME
    },
```
And the `products.json` file has the following structure: 

```
{
    "CODE1": {
        "price": PRICE,
        "name": NAME1
    },
    "CODE2": {
        "price": PRICE,
        "name": NAME2
    },
    "CODE3": {
        "price": PRICE,
        "name": NAME3
    },
    .
    .
    .
}
```

***
## Promotions

The `Promotion` class offers a wrapper for the promotions that will be applied (or possibly applied) to the products. There are 3 types of promotions: 

1. `MxN`: Buy `M` products, pay `N`.
2. `FIXED`: Buy more than `n` items of a given product, pay `X` for each one. 
3. `COMBINATION`: Buy the products `A, B, C, ...`, pay `X` for all of them.

All promotions must be of type `PromoType` (in the `Promotion.py` file). Promotions are validated when they are created, with the method `validate_promo`.




