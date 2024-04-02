#Heading for the program

print('''

    CURRENCY CONVERTER BY ABEER CHOUBEY

''')

# Notify user about the currently available currencies in this program

print('''
    There are currently three types of currency available:-
    1. INR
    2. USD
    3. JPY
''')
#caution

print("Please put in the input as 'INR' or 'USD' or 'JPY'")
# Takes input from the user
money = float(input("Please put the amount of money you want to convert :- "))
inp1 = str(input("Please put the currency you want to convert from :- "))
inp2 = str(input("Please put the currency you want to convert to :- "))

#Calculations
if inp1 == "INR":
    if inp2 == "USD":
        amount = money*0.011989
        print("Your total amount of money in USD from INR is :-", amount)
        pass
    elif inp2 == "JPY":
        amount = money*1.81587
        print("Your total amount from INR to JPY is :-", amount)
        pass
    pass

elif inp1 == "USD":
    if inp2 == "INR":
        amount = money*83
        print("Your total amount from USD to INR is :-", amount)
        pass
    elif inp2 == "JPY":
        amount = money*151.34500
        print("Your total amount from USD to JPY is :-", amount)
        pass
    pass

elif inp1 == "JPY":
    if inp2 == "INR":
        amount = money*0.55
        print("Your total amount from JPY to INR is :-", amount)
        pass
    elif inp2 == "USD":
        amount = money*0.0066
        print("Your total amount from JPY to USD is :-", amount)
        pass
    pass

else:
    print("Please Check your inputs again")
    pass
input("Press Enter to Exit this program")
