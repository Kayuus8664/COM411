print("Program Started!")
standard_character = input("Please enter a standard character:")
value = ord(standard_character)
if len(standard_character) == 1:
    print(f"The ASCII code for {standard_character} is {value}.")
else:
    print("error!")

print("Program Ended!")