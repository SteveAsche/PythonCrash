filename = 'text_files/someinfo.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
print(type(lines))

for line in lines:
    pi_string += line.rstrip()

print(lines)
print(pi_string)
print(len(pi_string))
    #contents = file_object.read()
    #for line in file_object:
     #   print(line.rstrip())
#    print(contents.rstrip())