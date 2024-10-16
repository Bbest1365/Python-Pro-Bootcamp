import art
import random

# Define the card values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_user_cards(list_user):
    """Calculate the user's cards and return the current score."""
    list_user.append(random.choice(cards))
    return (f"Your cards: {list_user}, current score: {sum(list_user)}")


def calculate_computer_cards(list_com):
    """Calculate the computer's cards."""
    list_com.append(random.choice(cards))
    return (f"Computer's first card: {list_com[0]}")


loop = True

while loop:
    play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    list_user = []
    list_com = []

    if play_or_not.lower() == 'y':
        print(art.logo)

        # Initial two cards for user and computer
        for _ in range(2):
            list_user.append(random.choice(cards))
            list_com.append(random.choice(cards))

        print(f"Your cards: {list_user}, current score: {sum(list_user)}")
        print(calculate_computer_cards(list_com))

        # Check for initial blackjack
        if sum(list_com) == 21:
            print('You lose, opponent has Blackjack 😭')
            continue
        elif sum(list_user) == 21:
            print('You win with a Blackjack! 😎')
            continue

        # User's turn to hit or stay
        while True:
            type_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if type_choice.lower() == 'y':
                print(calculate_user_cards(list_user))
                if sum(list_user) > 21:
                    print('You went over. You lose 😭')
                    break
            elif type_choice.lower() == 'n':
                print(f"Your final hand: {list_user}, final score: {sum(list_user)}")
                break

        # Computer's turn
        while sum(list_com) < 16:
            list_com.append(random.choice(cards))

        print(f"Computer's final hand: {list_com}, final score: {sum(list_com)}")

        # Determine the winner
        if sum(list_user) > 21:
            print('You went over. You lose 😭')
        elif sum(list_com) > 21 or sum(list_user) > sum(list_com):
            print('Opponent went over. You win! 😁')
        elif sum(list_user) < sum(list_com):
            print('You lose. 😭')
        else:
            print('Push, it\'s a tie!')

    elif play_or_not.lower() == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please type 'y' or 'n'.")
