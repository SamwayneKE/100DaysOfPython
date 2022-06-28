age = input("What is your current age?  ")

# Converting age into an integer
age_in_integer = int(age)

# Get age in months, weeks, and days left from the current age,  if one lives upto 70yrs old
years_remaining = 70 - age_in_integer
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"

print(message)

