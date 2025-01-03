class Dog():
    """ A simple attempt to mode a dog """

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over"""
        print(self.name.title() + " is rolling over.")


Jasper = Dog('jasper', 9)
Rudi = Dog('rudi', 9)

print("My dog's name is " + Jasper.name.title())
print("My other dog's name is " + Rudi.name.title())
print("Jasper is " + str(Jasper.age))
print("Rudi is " + str(Rudi.age))
Rudi.sit()
Rudi.roll_over()
Jasper.roll_over()