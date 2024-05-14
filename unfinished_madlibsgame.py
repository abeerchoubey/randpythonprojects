#Mad Libs Game
#Made by Abeer Choubey
import time
#Setting up to clear console

def cls():
    print("\n" * 500) 
    pass





#Titles

print('''
      Mad Libs by Abeer Choubey
      How to play this game:--
      
      1.You will have to choose a a series of text by the title
      2.You will have to type in some words to complete that text
      3.Replace the special characters apart from words and numbers
      
      GOOD LUCK!!!!!
      :)
      
      ''')

input("Press Enter to clear out the instructions and start the game!")
cls()

#Stories

def travel_text_1():
    text = ''' You are going to - using / while eating _.
     You visited > there and ate < .'''
    print("You will have to complete the following text\n")
    time.sleep(2)
    print("\n")
    time.sleep(4)
    cls()
    print(text, "\n")
    input1 = input("Please enter the first word denoted with '-' you want to replace >>>")
    cls()
    text = text.replace('-', input1)
    print(text, "\n")
    input2 = input("Please enter the second word denoted with '/' you want to replace >>>")
    cls()
    text = text.replace('/', input2)
    print(text, "\n")
    input3 = input("Please enter the third word denoted with '_' you want to replace >>>")
    cls()
    text =text.replace('_', input3)
    print(text, "\n")
    input4 = input("Please enter the fourth word denoted with '>' you want to replace >>>")
    cls()
    text =text.replace('>', input4)
    print(text, "\n")
    input5 = input("Please enter the fifth word denoted with '<' you want to replace >>>")
    cls()
    text = text.replace('<', input5)
    print(text, "\n")
    print("That is your FINAL PRODUCT!!")
    print("nice work")
    pass
travel_text_1()
input("press enter to exit this program")