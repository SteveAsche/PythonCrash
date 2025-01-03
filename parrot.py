prompt = "\nTell me something and I'll repeat it back to you"
prompt += "\n Enter 'quit' to end the program -> "
message = ""

#message = input("tell me something and I will print it back to you. ")
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# name = input("Please enter your name: ")
# print("Hello, " + name +"!")

