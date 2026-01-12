import art
import random

def check_answer(guess, answer):
    if guess == answer:
        print(f"You got it! The answer was {answer}")
        return 0
    elif guess > answer:
        print("Guess is higher than the number\nGuess again")
        return 1
    elif guess < answer:
        print("Guess is lower than the number\nGuess again.")
        return 1
    return 1


print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1,100)
print(f"Psst the correct answer is {answer}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("Incorrect difficulty")
    lives = 0
while lives > 0:
    print(f"You have {lives} attempts remaining to guess the answer")
    guess = int(input("Make a guess: "))
    guessed = check_answer(guess, answer)
    if guessed == 0:
        break
    else:
        lives -= 1