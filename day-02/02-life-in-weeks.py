# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# Input your age.
age = input("What is your current age?\n")

# Create variables for maximum year, month, weeks and days.
max_age = 90
max_months = max_age * 12
max_weeks = max_age * 52
max_days = max_age * 365

# Create variables for actual year, month, weeks and days.
age = int(age)
age_months = age * 12
age_weeks = age * 52
age_days = age * 365

# Calculate left time.
left_age = max_age - age
left_months = max_months - age_months
left_weeks = max_weeks - age_weeks
left_days = max_days - age_days

# Output
print(f"You have {left_age} years, {left_months} months, {left_weeks} weeks und {left_days} days left.")
