# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.
# Rules: 1. Jahre sind durch 4 teilbar => Schaltjahr
#        2. Jahre sind durch 4 teilbar UND durch 100 => kein Schaltjahr
#        3. Jahre sind durch 100 teilbar UND 400 teilbar => Schaltjahr
#        4. Jahr ist durch 400 teilbar => Schaltjahr

year = int(input("Please type in the year you want to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Your year is a leap year!")
        else:
            print("Your year is not a leap year.")
    else:
        print("Your year is a leap year!")
else:
    print("Your year is not a leap year.")
