print("Program Started!")
code = int(input("Please enter an ASCII code:"))
if code in range(32,127):
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is {character}.")


print("program ended!")