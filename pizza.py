def make_pizza(size, *toppings):
    '''Takes two arguements - integer size and a dynamic list of strings that define the toppings'''
    print("\nMaking a " + str(size) + " pizza with the following toppings:")
    for topping in toppings:
        print(" - " + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'pepperoni', 'olive', 'sausage', 'onions')