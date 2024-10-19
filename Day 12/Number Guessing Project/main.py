import art,random
print(art.logo)

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
Type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
correct_number = random.randint(1,100)
def select_type(Type):
    if Type == 'easy':
        n = 10
        print('You have 10 attempts remaining to guess the number.')
        guess_number = input('Make a guess: ')

    elif Type == 'hard':
        n = 5
        print('You have 5 attempts remaining to guess the number.')
        input('Make a guess: ')

 def check()
    if guess_number == correct_number:
        print()
    elif guess_number < correct_number:
        print('Too low.')
        print('Guess again.')
        select_type(guess_number)
    elif guess_number > correct_number:
        print('Too high.')
        print('Guess again.')
        print(f'You have {n - 1} attempts remaining to guess the number.')
        guess_number = input('Make a guess: ')

print(number)