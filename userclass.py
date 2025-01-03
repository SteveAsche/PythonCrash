""" Test assignment chaper 9 Python crash course"""
class User():
    """ this class defines the attributes and methods for typical user """

    def __init__(self, first_name, last_name, age, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + " is " + str(self.age) + " years old and is in the " + self.department.title() + " department")

    def greet_user(self):
        print("Welcome " + self.first_name.title() + " " + self.last_name.title() +"!")


employee1 = User("Joe", "Smith", 25, "I.T.")
employee2 = User("jane", "doe", 44, "finance")

employee1.greet_user()

employee2.describe_user()