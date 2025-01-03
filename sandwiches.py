# Start with users that need to be confirmed then an empty list
sandwich_orders = ['pastrami', 'ham and swiss', 'bologna', 'tongue', 'brisket', 'pastrami', 'tuna', 'salami', 'pastrami']
completed_sandwiches =[]

print("\nOh fuck-a-doodle-do, we're out of pastrami.  All pastrami will be removed from the orders")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print("I am working on the " + sandwich.title() + " sandwich")
    completed_sandwiches.append(sandwich)

print("\nI have completed the following sandwiches")
for sandwich in completed_sandwiches:
    print(sandwich.title())

