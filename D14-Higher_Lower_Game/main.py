import art
import random
import game_data

# Steps to make the game
# Print the logo
# Print the first option A
# Print the vs logo
# Print the second option B
# Ask for input from them
# If correct, loop it and add to score
# If incorrect, end it and give final score


gameover = False
length = len(game_data.data)
data = game_data.data
score = 0

while not gameover:
    print(art.logo)
    if score>0:
        print(f"You're right! Current score {score}")
    a = random.randint(0, length-1)
    print(f"Compare A: {data[a]["name"]}, a {data[a]["description"]}, from {data[a]["country"]}")
    b = random.randint(0, length - 1)
    while b == a:
         b = random.randint(0, length - 1)
    print(art.vs)
    print(f"Compare B: {data[b]["name"]}, a {data[b]["description"]}, from {data[b]["country"]}")
    chosen = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n"*20)
    if chosen == "a" and int(data[a]["follower_count"]) > int(data[b]["follower_count"]):
        score += 1
    elif chosen == "b" and int(data[b]["follower_count"]) > int(data[a]["follower_count"]):
        score += 1
    else:
        print(art.logo)
        print(f"Sorry that's wrong. Final Score: {score}")
        gameover = True