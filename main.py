
# IMPORTS
from models.Product import default_products
from models.Checkout import Checkout


if __name__ == '__main__':

    ticket = Checkout()
    print('Current products loaded from json file:')
    print([str(prod) for prod in default_products])
    next_product = True
    while next_product:
        product = input(
            'Choose a product (Product code). Press Enter to get the total or exit to end the checkout. \n')
        if(product == ''):
            print('Current ticket total:')
            print(ticket.total)
        elif(product == 'exit'):
            next_product = False
        else:
            ticket.scan(product)

    print('--------------------')
    print('PRODUCTS in ticket:')
    print([str(prod) for prod in ticket.products])
    print('--------------------')
    print('TICKET TOTAL')
    print(ticket.total)
