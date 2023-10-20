# Nested decision
cover_type = input("What type of coveer does the book have?")
if cover_type == "soft":
    perfect_bound = input("\nIs the book perfect bound")
    if perfect_bound == "yes":
        print("\nSoft cover, perfect bounds books are very popular")
    else:
        print("\nSoft cover with coils or stitches are great for short books")
else:
    print("\nBooks with hard covers can be more expensive!")


# Multiple Nested Decisions
where_to_look = input("Where should I look?")
if where_to_look == "in the bedroom":
    where_in_bedroom = input("Where in the bedroom should I look?")
    if where_in_bedroom == "under the bed":
       print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")
if where_to_look == "in the bathroom":
    where_in_bathroom = input ("Where in the bathroom should I look?")
    if where_in_bathroom == "in the bathtub":
        print("Found bathroom stuff but no phone.")
if where_to_look == "in the living room":
    where_in_living_room = imput("Where in the living room should I look?")
    if where_in_living_room == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")







