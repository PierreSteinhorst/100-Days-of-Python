# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#
# It should tell them the interpretation of their BMI based on the BMI value.
#
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
print(bmi)
if bmi < 18.5:
    print(f"BMI: {bmi} => You are underweight")
elif bmi < 25:
    print(f"BMI: {bmi} => You have normal weight")
elif bmi < 30:
    print(f"BMI: {bmi} => You are slightly overweight")
elif bmi < 35:
    print(f"BMI: {bmi} => You have obese")
else:
    print(f"BMI: {bmi} => You have clinical obese")
