# Cofi - Checkout with promotions

## Adding and computing promotions to several items in a given ticket. 

This little project consists of several classes that allow a user to add products to a ticket, and given some promotion, obtain the total of this ticket. 

The project can be inported to be used in a bigger project in order to have the `Checkout` class, which can be extended, and have a promotions module.

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

This method checks that the promotion parameters are valid (for more details please see file `Promotion.py`).

***
## Checkout

The `Checkout` class is the one that contains the information about the products list. It contains the property `total` that computes the total of the ticket, with the promotions applied. 

***

# Run the code

## Install dependencies 

Run the following command to install the required dependencies of the project.

```
pip install -r requirements.txt
```

## main

Running

```
python main.py
```

Will start a new checkout session, where products can be added to an empty ticket via the terminal. The total price of the ticket can be checked in any moment while adding products. 

## tests

Running 
```
pytest tests
```

Will run all the tests in the folder `tests`



