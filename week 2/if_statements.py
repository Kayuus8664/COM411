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
direction = input("Towards which direction should I go (up, down, left or right")
if direction == "up":
    print("I am moving in an upward direction")
elif direction == "down":
    print("I am moving in a downward direction")
elif direction == "left" or "right":
    print ("I am moving sideways")

