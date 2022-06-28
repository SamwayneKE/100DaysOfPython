print("Welcome to the Tip Calculator!")

bill = float(input("Enter the total bill $"))
tip = int(input("How much would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people do you wish to split the bill?\n"))

percentage_tip = tip / 100
total_tip = bill * percentage_tip
total_bill = bill + total_tip

bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")