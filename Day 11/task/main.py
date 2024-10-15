import art, random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def calculate_list_user(list_user):
    list_user.append(random.choice(cards))
    return (f"Your cards: {list_user}, current score: {sum(list_user)}")
def claculate_list_com(list_com):
    list_com.append(random.choice(cards))
    return (f"Computer's first card: {sum(list_com)}")
loop = True
while loop:
    play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    list_user = []
    list_com = []
    if play_or_not == 'y':
        print(art.logo)
        for i in range(2):
            list_user.append(random.choice(cards))
        list_com.append(random.choice(cards))
        print(f"Your cards: {list_user}, current score: {sum(list_user)}")
        print(f"Computer's first card: {sum(list_com)}")

        if sum(list_com) == 21:
            print('You lose Blackjack😭')
        elif sum(list_user) == 21:
            print('Win with a Blackjack 😎')

        if sum(list_user) > 21:
            Ace = 1
        Ace = 1
        type = input("Type 'y' to get another card, type 'n' to pass: ")
        if type == 'y':
            print(calculate_list_user(list_user))
            print(f"Computer's first card: {sum(list_com)}")
        elif type == 'n':
            print(f"Your cards: {list_user}, current score: {sum(list_user)}")
            print(f"Computer's first card: {sum(list_com)}")
            list_com.append(random.choice(cards))

            print(f'Your final hand: {list_user}, final score: {sum(list_user)}')
            print(f'Computer\'s final hand: {list_com}, final score: {sum(list_com)}')

        if sum(list_user) > sum(list_com):
            if sum(list_user) > 21:
                print('You went over. You lose 😭')
            else:
                print('Opponent went over. You win 😁')
        elif sum(list_user) == sum(list_com):
            print('Push equal')
        else:
            print('You went over. You lose 😭')
    else:
        pass