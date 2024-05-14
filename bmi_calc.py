#Body Mass Index (BMI) Calculator
#By Abeer Choubey
# :)
#Open Source Python Code by Abeer

#Importing libraries

import time

#Topics

print("Welcome to Body Mass Index (BMI) Calculator\n")
time.sleep(0.9)
print("This program was made by Abeer Choubey\n")
time.sleep(2)
print("You should input the values in decimals\n")
time.sleep(1)
# Taking Necessary inputs from the user
weight = float(input("Please enter your weight in KiloGrams >>>"))
time.sleep(1)
height = float(input("Please enter your height in Metres >>>"))
time.sleep(1)

print("\n")
#Using the Input to Calculate BMI 

square_height = float(height**2)

bmi = float(weight/square_height)

#printing out the outputs

print("Calculating")
time.sleep(1)

print(".")
time.sleep(1)
print("")

print("Your Body Mass Index (BMI) is", bmi, "\n")

input("Please press ENTER or RETURN to exit this program! ")