print("Welcome to the tip calculator!")
billAmount = input("What was the total bill? $")
tipPercent = input("How much tip % would you like to give? 10, 12, or 15? ")
numberPeople = input("How many people to split the bill? ")
tipAmount = (float(billAmount) * float(tipPercent)) / 100
billAmount = float(billAmount) + tipAmount
eachPersonAmount = billAmount / float(numberPeople)
print(f"Each person should pay: ${eachPersonAmount}")