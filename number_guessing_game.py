# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 19:29:44 2025

@author: abeer_sameer
"""
import random
ran_num = random.randint(1, 20)
for i in range(1,11):
    x = int(input(f"Chance {i} , guess the number between 1 and 20:- "))
    if x==ran_num:
        print(f"Great Job! the number was {ran_num} \n You guessed the number in {i} chances")
        break
    if x>ran_num:
        print("Go Lower")
        pass
    if x<ran_num:
        print("Go higher")
        pass
    else:
        print("Try again")
        pass
    if i==10:
        print(f"Too bad. the number was {ran_num}")
        pass
    pass
