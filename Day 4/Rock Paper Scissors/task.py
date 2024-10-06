import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

a = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')
b = random.randint(0, 2)

if a == '0':
    print(rock)
    if b == 2:
        print('Computer chose:')
        print(scissors)
        print('You win!')
    elif b == int(a):
        print('Computer chose:')
        print(rock)
        print("It's a draw")
    else:
        print('You lose!')

elif a == '1':

    print(paper)
    if b == 0:
        print('Computer chose:')
        print(rock)
        print('You win!')
    elif b == int(a):
        print('Computer chose:')
        print(paper)
        print("It's a draw")
    else:
        print('You lose!')

elif a == '2':

    print(scissors)
    if b == 1:
        print('Computer chose:')
        print(paper)
        print('You win!')
    elif b == int(a):
        print('Computer chose:')
        print(scissors)
        print("It's a draw")
    else:
        print('You lose!')


else:
        print('You typed invalid number, you lose!')
