from art import logo, vs
from game_data import data
import random
score = 0
print(logo)
def rand():
    compare_A = random.choice(data)
# print(f'{compare_A['name']}, {compare_A['description']}, {compare_A['country']}')
    against_B = random.choice(data)
# print(f'{against_B['name']}, {against_B['description']}, {against_B['country']}')
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
        print(f"You're right! Current score: {score}.")
    elif compare_A['follower_count'] < against_B['follower_count'] and followers == 'B':
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        loop = False

