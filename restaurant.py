# restaurant seating application

print("Hello! Welcome to Chez Bacon\n")
name = input("What is the name of your party? ")
diners = input("And how many people are in the " + name +" party? ")
diners = int(diners)
maxdiners = 8

if diners > maxdiners:
    print("We're sorry, we can't sit more than " + str(maxdiners) +" at a table.")
else:
    print("Right this way " + name +" party!")