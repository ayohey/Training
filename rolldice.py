import random
roll = random.randint(1,6)
guess = int(input('Guess the dice roll:\n'))
if guess == roll:
    print('correct they rolled a ' + str(roll))
else:
    print('Wrong, they rolled a ' + str(roll))
