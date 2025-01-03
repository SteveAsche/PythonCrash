def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

message=""
prompt = "\nProvide your pet type or type quit: "
prompt2 = "\nProvide your pet name: "


# pets = ['dog', 'cat', 'goat', 'goldfish', 'ferret', 'gerbil', 'horse', 'cat', 'donkey', 'cat']

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        pet_type = message
        pet_name = input(prompt2)
        if pet_type == "":
            describe_pet(pet_name)
        else:
            describe_pet(pet_name, pet_type)
