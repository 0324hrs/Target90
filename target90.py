age = input("what is your age? \n")
# convert age string into an integer
age_int = int(age)

# logic
years_remaining = 90 - age_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

# 
print(f"Hello there Kelvin, you're currently {age_int}.You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months and {years_remaining} years remaining to get to 90..enjoy while you're still young")