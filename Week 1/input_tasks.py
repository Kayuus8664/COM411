# Ask user to enter their name
print("What is your name?")
name = input()
print(F"It is nice to meet you {name}")

# read in user's name
name = input("What is your name?")
age = int(input("How old are you (in years)?"))
height = float(input("How tall are you (in meters)?"))
weight = float(input("how much do you weigh (in kilograms)?"))
BMI = weight/height**2
print (f"{name}, you are {age} years old and your bmi is {BMI}")



lives = int(input("Please enter the number of lives:"))
energy = int(input("please enter the energy level"))
shield = int(input("please enter the shield level"))
print(f"\nHealth has been set\nLives:\t{'♥'*lives}\nEnergy:\t{'♦'*energy}\nShield:\t{'♦'*shield}")d