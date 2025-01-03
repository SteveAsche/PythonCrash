# gather the pizza toppings unti they type quit
# print the toppings one at a time

prompt = "\nPlease enter the pizza topping you'd like."
prompt += "\n(Enter 'quit' when you are finished.) "
pizzatoppinglist = []

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print("I like " + topping.title() + "!")
        pizzatoppinglist.append(topping)

toppingcount = 1

for atopping in pizzatoppinglist:
    print("Topping " + str(toppingcount) +": " + atopping.title())
    toppingcount += 1
