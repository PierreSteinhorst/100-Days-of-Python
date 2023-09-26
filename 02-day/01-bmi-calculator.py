# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# Input Data weight and height
weight = input("Geben Sie bitte ihr Gewicht, in kg, ein!\n")
height = input("Geben Sie bitte ihre Größe, in m, ein!\n")

# Calculate Body Mass Index
bmi = float(weight) / float(height) ** 2
bmi_as_integer = int(bmi)

print("Dein Body Mass Index beträgt: " + str(bmi_as_integer))