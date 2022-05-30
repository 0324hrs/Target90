print("welcome to tippy!!")

# 
bill = float(input("what is your total bill? \n ksh"))

tip = int(input("how much tip do you want to give? 10, 15 \n"))

people = int(input("how many people to split the bill? \n"))
# 
tip_percentage = tip/ 100
tt_tip_amount = tip_percentage * bill

total_billed = bill + tt_tip_amount
bill_per_person = float(total_billed / people)
# 
print(f"each person will pay ksh {bill_per_person}")