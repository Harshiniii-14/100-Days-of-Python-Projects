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

userNumber = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

game_images = [rock, paper, scissors]
if userNumber>=0 and userNumber<=2:
    print(game_images[userNumber])

computerNumber = random.randint(0,2)

print(f"Computer chose:\n")
print(game_images[computerNumber])

# if userNumber == 0 and computerNumber == 2:
#     print("You win!")
# elif computerNumber == 0 and userNumber == 2:
#     print("You lose!")
# elif computerNumber > userNumber:
#     print("You lose!")
# elif userNumber > computerNumber and userNumber<=2:
#     print("You win!")
# elif computerNumber == userNumber:
#     print("It's a draw!")
# else:
#     print("You typed an invalid number. You lose!")
# This is redundant code, so it can be replaced by using modulo arithmetic logic,

if userNumber not in [0, 1, 2]:
    print("You typed an invalid number. You lose!")
elif userNumber == computerNumber:
    print("It's a draw!")
elif (userNumber - computerNumber) % 3 == 1:
    print("You win!")
else:
    print("You lose!")
