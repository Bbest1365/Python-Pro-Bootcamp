# import art,random
# print(art.logo)
#
# print('Welcome to the Number Guessing Game!')
# print("I'm thinking of a number between 1 and 100.")
# Type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# correct_number = random.randint(1,100)
# n1 = 10
# n2 = 5
# is_gameover = True
#
#
# while is_gameover:
#     if Type == 'easy':
#         print(f'You have {n1} attempts remaining to g uess the number.')
#         guess_number = int(input('Make a guess: '))
#         n1 -= 1
#         if guess_number == correct_number:
#             print(f'You got it! The answer was {correct_number}.')
#             is_gameover = False
#         elif guess_number < correct_number:
#             print('Too low.')
#             if n1 == 0:
#                 print('You\'ve run out of guesses, you lose.')
#                 is_gameover = False
#             print('Guess again.')
#
#         elif guess_number > correct_number:
#             print('Too high.')
#             if n1 == 0:
#                 print('You\'ve run out of guesses, you lose.')
#                 is_gameover = False
#             print('Guess again.')
#
#     elif Type == 'hard':
#         print(f'You have {n2} attempts remaining to guess the number.')
#         guess_number = int(input('Make a guess: '))
#         n2 -= 1
#         if guess_number == correct_number:
#             print(f'You got it! The answer was {correct_number}.')
#             is_gameover = False
#         elif guess_number < correct_number:
#             print('Too low.')
#             if n2 == 0:
#                 print('You\'ve run out of guesses, you lose.')
#                 is_gameover = False
#             print('Guess again.')
#
#         elif guess_number > correct_number:
#             print('Too high.')
#             if n2 == 0:
#                 print('You\'ve run out of guesses, you lose.')
#                 is_gameover = False
#             print('Guess again.')
#

from random import randint
# choosing a random number between 1 and 100.
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check users' guess against actual answer
def check_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print('Too high.')
        turns -= 1
    elif user_guess <  actual_answer:
        print('Too low.')
        turns -= 1
    else:
        print(f'You got it! The answer was {actual_answer}.')

#Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS

# Let the user guess a number
print('Welcome to the Number Guessing Game!')
def game():
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f'Pssst, the correct answer is {answer}')

    turns = set_difficulty()

# Repeat the guessing functionality if they get it wrong.

    guess = 0
    while guess != answer:
        print(f'You have {turns} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        check_answer(user_guess=guess,actual_answer=answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


#track the number of turns and reduce by 1 if they get it wrong

game()