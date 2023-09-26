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

if height >= 120:
    print("You can ride.")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You can't ride.")