print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
firstDecision = input("You stand at a cross road in front of a dense forest, will you go 'right' or 'left': ")
if firstDecision == "left":
    secondDecision = input("You made a wise choice traveller... now you stumble across a large lake, do you want to 'swim' or 'wait': ")
    if secondDecision == "wait":
        print("You've made it so far! Now a final choice stands before you, you are so close to the treasure.")
        thirdDecision = input("You find a house with three doors, which color do you pick? 'red', 'yellow' or 'blue': ")
        if thirdDecision == "red":
            print("You were burned by a witch! Game over.")
        elif thirdDecision == "blue":
            print("You were eaten by wolves! Game over.")
        elif thirdDecision == "yellow":
            print("You win! Congratulations! You found the treasure... a spoon!")
        else:
            print("You picked a choice outside the three doors. You get lost forever. Game over.")
    else:
        print("You were attacked by an alligator! You died!")
else:
    print("You fell into a hole! Game over.")