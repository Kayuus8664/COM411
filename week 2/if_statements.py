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