#this is a simple calculator made by Abeer Choubey


#inputs
a = input("Please Enter the first number you want to calculate :-")
b = input("Please Enter the second number you want to calculate :-")
op = input("Please enter the type of operation you want to perform :-")




#calculations
def add(a,b):
    r=a+b
    print(r)
    pass
def sub(a,b):
    r=a-b
    print(r)
    pass
def mul(a,b):
    r=a*b
    print(r)
    pass
def div(a,b):
    r=a/b
    print(r)
    pass

#if statements

if op=="+":
    add(a,b)
    pass
elif op=="-":
    sub(a,b)
    pass
elif op=="*":
    mul(a,b)
    pass
elif op=="/":
    div(a,b)
    pass
else:
    print("Incorrect type of operation")
    print("Please check if you used one of the following as only those work:-")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    print("if your operation statement didn't contain one of these, then your operation syntax was wrong")
    pass
input('Press enter to exit this program')
exit()