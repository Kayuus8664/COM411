print("What type of book is this")
book_type = input()
if book_type == "adventure":
    print("I like adventure books!")
print("Finished reading book.")
activity = input("please enter activity")
if activity == "calculate":
    print("\nPerforming calculations...")
else:
    print("\nPerforming activity...")
print("\nActivity completed!")
direction = input("Towards which direction should I go (up, down, left or right)")
if direction == "up":
    print("I am moving in an upward direction")
elif direction == "down":
    print("I am moving in a downward direction")
elif (direction == "left" or direction == "right"):
    print ("I am moving sideways")
else:
    print()

number = int(input("Please enter a whole number"))
if number % 2 == 0:
    print(f"The number {number} is an even number")
else:
    print(f"The number {number} is an odd number")


# comparison operators
first_number = int(input("Please enter first number."))
second_number = int(input("Please enter second number"))
if first_number < second_number:
    print ("The first number is the smallest")
else:
    print ("\nThe second number is the smallest")

# counter
first_whole_number = int(input("Please enter the first whole number"))
second_whole_number = int(input("please enter the second whole number"))
third_whole_number = int(input("Please enter the third whole number"))
even_numbers = 0
odd_numbers = 0
if first_whole_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if second_whole_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if third_whole_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
print (f"\nThere were {even_numbers} even numbers and {odd_numbers} odd numbers")

