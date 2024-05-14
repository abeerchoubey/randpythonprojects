#Temperature Converter

#calculating celsius to farhenight

def ctf():
    
    cel = float(input("Please Input the C* value you want to convert :-"))
    
    #calculations
    
    temp1=float(cel*9/5)
    
    if cel==0:
        temp1=0
        pass
    
    else:
        pass
    
    temp2=float(temp1+32)
    print("The F* Temperature is:-",temp2)
    pass
def ftc():
    
    far=float(input("Please Input the F* value you want to convert :-"))
    
    #calculations
    
    temp1=float(far-32)
    
    temp2=float(temp1*5/9)
    
    print("The C* Temperature is :-",temp2)
    
    pass

#taking input about what they want to convert

print("Please Enter from what and to what you want to convert")
print("Enter 1 to convert C* to F*")
print("Enter 2 to convert F* to C* \n")
operation = input("Input >>>")

if operation == '1':
    ctf()
    pass
elif operation == '2':
    ftc()
    pass
else:
    print("Invalid Operation")
    print("Please read the above statement to ensure that you chose a valid input")
    pass

input("Please press ENTER or RETURN button to exit this program")

    