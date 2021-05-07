
print("welcome to tip calculator!")
total=input("Enter total amount:\t")
percent=int(input("How much percent each of want to contribute 10% or 12% or 15%?\t"))
members=int(input("How many members you are?\t"))
if percent==10:
    amount=(float(total)//members)*10//100
    print(f"Each should give {amount}Rs.")
elif  percent==15:
    amount=(float(total)//members)*15//100
    print(f"Each should give {amount}Rs.")
else:
    amount=(float(total)//members)*15//100
    print(f"Each should give {amount}Rs.")