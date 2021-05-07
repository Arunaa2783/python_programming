import math
from simple_colors import *
print(green(r"Let's calculate Your Body Mass Index!",["bold",'underlined']))
print("Welcome",input("Enter your name:"))
weight=int(input("Enter you weight ig kg :\t"))
height=int(input("Enter you height in cm :\t"))
height=height/100   #converting cm to meter
# formula=kg/(meter)^2
BMI=weight/math.pow(height,2)
# print(BMI)
if BMI<18.5:
    print("Underweight")
elif 18.5<BMI<24.9:
    print("Normal weight")
elif 25.0<BMI<29.9:
    print("Pre-obesity")
elif 30.0<BMI<34.9:
    print("Obesity class")
elif 35.0<BMI<39.9:
    print("Obesity class II")
elif BMI>40:
    print("Obesity class lll")
else:
    pass