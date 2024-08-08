print("Welcome to Python Pizza Delivery Service!!!\n")

size = input("Enter the size you would like (S, M or L): ")
xtra_ppr = input("Would you like extra pepperoni (Y or N): ")
xtra_chs = input("Would you like extra cheese (Y or N): ")

bill = 0

if size == "S":
    bill += 15
    if xtra_ppr == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if xtra_ppr == "Y":
        bill += 3
else:
    bill += 25
    if xtra_ppr == "Y":
        bill += 3

if xtra_chs == "Y":
    bill += 1

print(f"\nYour total is ${bill}")
