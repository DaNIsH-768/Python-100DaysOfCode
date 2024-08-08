print("Welcome to Tip Calculator!!!")

total = float(input("Enter the total bill: $"))
tip = int(input("Enter the tip you would like to give (10, 15, or, 20): "))
no_of_people = int(input("Enter the number of people to split: "))

print(f"Each person would pay ${round(((total + (total * tip/100)) / no_of_people), 2)}")
