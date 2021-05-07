from simple_colors import *
print(green("Let's Count your days!:)"))
name=input("Enter your name:\t")
year_of_wish=int(input(f"How many years you want live {name} ?\t"))
age=int(input("Enter your age:\t"))
remaining_years=year_of_wish-age
days=365*remaining_years
weeks=52*remaining_years
months=12*remaining_years
print(red(f"You have left with {days} days,{weeks} weeks and {months} months to reach {year_of_wish} years!"))
print(green("Peace be upon you :)"))