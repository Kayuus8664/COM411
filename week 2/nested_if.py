# Nested decision
cover_type = input("What type of coveer does the book have?")
if cover_type == "soft":
    perfect_bound = input("\nIs the book perfect bound")
    if perfect_bound == "yes":
        print ("\nSoft cover, perfect bounds books are very popular")
    else:
        print ("\nSoft cover with coils or stitches are great for short books")
else:
    print ("\nBooks with hard covers can be more expensive!")

