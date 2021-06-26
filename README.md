# Cofi - Checkout with promotions

## Adding and computing promotions to several items in a given ticket. 

This little project consists of several classes that allow a user to add products to a ticket, and given some promotion, obtain the total of this ticket. 

## Products

The `Product` class offers a wrapper for given product. It is a very simple class to store the code, the name and the price of a given product. 

### `products.json`

Products are loaded from a json file in the root of the project. A product in this file has the following strucure: 

```
"CODE": {
        "price": PRICE,
        "name": NAME
    },
```

