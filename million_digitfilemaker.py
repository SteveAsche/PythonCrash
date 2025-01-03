"""Creates a text file that writes a million digits in a file """
from random import randint

million_file = 'million_digits.txt'

with open(million_file, 'w') as file_object:
   file_object.write('3.1415934538')
   for linecount in range(1,100000):
       pi_line = ''
       for pidigit in range(0,10):
           pi_line += str(randint(0,9))
       file_object.write(pi_line)

with open(million_file) as file_object:
    lines = file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string += line.strip()

print(pi_string[:52])
print(len(pi_string))

birthday = input('Enter your birthday in the form mmddyy: ')

if birthday in pi_string:
    print("Your birthday is in Pi")
else:
    print("Wah wah")