import random
comp_choice = random.choice(['scissors', 'rock', 'paper'])
user_choice = input(" Do you want rock paper or scissors?\n")
if comp_choice == user_choice:
    print('tie')
elif user_choice == 'rock' and comp_choice == 'scissors':
    print('win the computer had ' + comp_choice)
elif user_choice == 'paper' and comp_choice == 'rock':
    print('win the computer had ' + comp_choice)
elif user_choice == 'scissors' and comp_choice == 'paper':
    print('win the computer had ' + comp_choice)
else:
    print('Youre a loser! the computer had ' + comp_choice)


