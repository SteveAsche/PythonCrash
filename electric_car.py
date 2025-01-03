class Car():
    """ a simple attempt to represent a cer"""

    def __init__(self, make, model, year):
        """Initializes attributes of the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ return the current odometer reading for this car"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer to the parameter given"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't reduce the odometer mileage")

    def add_miles(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Representas aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """initialiase attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """prints a statement decribing battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_new_car = Car("nissan", "400Z", 2023)
my_tesla = ElectricCar('tesla','model 3', 2023)

print(my_new_car.get_descriptive_name())
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
