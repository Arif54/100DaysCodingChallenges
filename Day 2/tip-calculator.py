print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15%?\n"))
people = int(input("How many people to split the bill?\n"))
total = round(bill * (1 + tip/100), 2)
share = round(total / people, 2)
each_person_pay = f"Each Person should pay: ${share}"
print(each_person_pay)