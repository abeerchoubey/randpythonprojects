#Square root Calculator by Abeer Choubey
import math
import time
print("The Number must be greater or eqeal than 0")
print("The number should be a positive number ")
time.sleep(5)
inp = float(input("Please enter the Number you want the square root of >>>"))
time.sleep(1)
if inp>=0:
    calculations = float(math.sqrt(inp))
    print("The square root of", inp, "is", calculations)
    pass
else:
    print("You have violated the only rule of this program")
    print("Please exit this program and run it again")
    print("Pay attention to the text Shown when the program starts")
    pass
time.sleep(5)
print("")
print("")
input("Please press ENTER on your keyboard to exit this program  ")