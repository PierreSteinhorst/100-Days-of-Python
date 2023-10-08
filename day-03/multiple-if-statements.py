# Nested if / else
# if condition:
#    if another condition:
#       do this
#    else:
#       do this
#else:
#    do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}")
    else:
        bill = 12
        print(f"Adults tickets are ${bill}")

    want_photo = input("Do you want a photo taken? Y or N ")

    if want_photo == "Y":
        # Add $3 to the bill
        bill += 3
    print(f"Your bill is ${bill}")
else:
    print("You can't ride.")
