# Your first job is to build an automatic pizza order program.
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    elif extra_cheese == "Y":
        bill += 1
    print(f"Your bill: ${bill}")
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    elif extra_cheese == "Y":
        bill += 1
    print(f"Your bill: ${bill}")
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    elif extra_cheese == "Y":
        bill += 1
    print(f"Your bill: ${bill}")
else:
    print("Wrong input! Please choose S, M or L pizza size")
