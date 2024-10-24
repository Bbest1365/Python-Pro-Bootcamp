from art import logo, vs
from game_data import data
import random
score = 0
print(logo)
compare_A = random.choice(data)
def rand():
    against_B = random.choice(data)
    same =True
    while same:
        if compare_A == against_B:
            against_B = random.choice(data)
        else:
            same =False
    print(f'Compare A: {compare_A['name']}, {compare_A['description']}, {compare_A['country']}')
    print(vs)
    print(f'Against B: {against_B['name']}, {against_B['description']}, {against_B['country']}')

    return compare_A, against_B
loop = True
while loop:
    compare_A, against_B = rand()
    followers = input("Who has more followers? Type 'A' or 'B': ").upper()

    if compare_A['follower_count'] > against_B['follower_count'] and followers == 'A':
        score += 1
        compare_A = against_B
        print(f"You're right! Current score: {score}.")
    elif compare_A['follower_count'] < against_B['follower_count'] and followers == 'B':
        score += 1
        compare_A = against_B
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        loop = False

