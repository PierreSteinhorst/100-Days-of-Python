#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
# Input total bill.
bill = float(input("What was the total bill?\n$"))
# Input percentage tip.
percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15?\n%"))
percentage_tip_as_percent_number = percentage_tip / 100 + 1
# Input people to split the bill.
people = int(input("How many people to split the bill?\n"))

# Pay the bill.
total_bill = (bill * percentage_tip_as_percent_number) / people
amount_bill = "{:.2f}".format(total_bill)
# Output sentence
print(f"Each person should pay: ${amount_bill}")

