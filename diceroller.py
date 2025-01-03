from random import randint

class Die():
    """ a representation of a die """

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        diceroll = randint(1, self.sides)
        return diceroll
    
# sampledice = Die(6)

sideinput = int(input("How many sides on this die"))
sampledice = Die(sideinput)

for value in range(1,20):
    print("dice roll " + str(value) + " is " + str(sampledice.roll_die()))
