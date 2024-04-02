#This code was made By Abeer Choubey.

#Do NOT use this for commercial use

print("Hello, this calculator was made by Abeer Choubey, and is very Unstable")

#takes inputs from user
print("\n")
print("\n")


p = int(input("Please put the Principal'or the starting money' here :-"))
print("\n")
r = int(input("Please put the Rate of Interest Percent without any symbol of percent here :-"))
print("\n")
t = int(input("Please enter the time for the interest in years here :-"))
print("\n")

si = p*r*t
si2 = si/100
si_final = si2

Amount = si_final + p

print("Your amount after the time period come to :-", Amount)
print("Your Simple Interest after the time period comes to :-", si_final)
print("Revision of you inputs below:-")
print("Principle :-", p)
print("Rate of Interest :-", r)
print("Time Period :-", t)

print('''
    Thank you for choosing to use my program
      Remember that this is made for personal use only.
      :)


''')

input("Press Enter to Exit this program")