class Restaurant():
    """This clase defines the characteristics and methods of a restaurant"""

    # When you create a new class, it has to start with the method to define the properties of this class.
    def __init__(self, restaurant_name, cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print("Welcome to " + self.restaurant_name.title())
        print("We serve " + self.cuisine.title() + " cuisine.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")

    def set_number_served(self, served):
        if served >= self.number_served:
            self.number_served = served
        else:
            print("You can't reduce the number served")

    def increment_number_served(self, served):
        self.number_served += served
        print(str(served) + " customer added")

    def print_number_served(self):
        print(str(self.number_served) + " customers served.")


restaurants = []
keepgoing = True

while keepgoing:
    rname = input("Enter the restaurant name (or 'quit' to exit): ")
    if rname != 'quit':
        rcuisine = input("Enter the type of food served here: ")
        restaurants.append(Restaurant(rname, rcuisine))
    else:
        keepgoing = False

for restaurant in restaurants:
    restaurant.describe_restaurant()

print(str(len(restaurants)))

"""
myrestaurant = Restaurant("Maison Bacon", "Barbecue")

myrestaurant.describe_restaurant()
myrestaurant.open_restaurant()

myrestaurant.print_number_served()
myrestaurant.increment_number_served(100)
myrestaurant.print_number_served()
"""





