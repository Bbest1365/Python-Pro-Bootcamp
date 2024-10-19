import art,random
print(art.logo)

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
Type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
correct_number = random.randint(1,100)
n1 = 10
n2 = 5
is_gameover = True


while is_gameover:
    if Type == 'easy':
        print(f'You have {n1} attempts remaining to guess the number.')
        guess_number = int(input('Make a guess: '))
        n1 -= 1
        if guess_number == correct_number:
            print(f'You got it! The answer was {correct_number}.')
            is_gameover = False
        elif guess_number < correct_number:
            print('Too low.')
            if n1 == 0:
                print('You\'ve run out of guesses, you lose.')
                is_gameover = False
            print('Guess again.')

        elif guess_number > correct_number:
            print('Too high.')
            if n1 == 0:
                print('You\'ve run out of guesses, you lose.')
                is_gameover = False
            print('Guess again.')

    elif Type == 'hard':
        print(f'You have {n2} attempts remaining to guess the number.')
        guess_number = int(input('Make a guess: '))
        n2 -= 1
        if guess_number == correct_number:
            print(f'You got it! The answer was {correct_number}.')
            is_gameover = False
        elif guess_number < correct_number:
            print('Too low.')
            if n2 == 0:
                print('You\'ve run out of guesses, you lose.')
                is_gameover = False
            print('Guess again.')

        elif guess_number > correct_number:
            print('Too high.')
            if n2 == 0:
                print('You\'ve run out of guesses, you lose.')
                is_gameover = False
            print('Guess again.')

