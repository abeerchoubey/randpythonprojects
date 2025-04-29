# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 18:54:33 2025

@author: abeer_sameer
"""

#Password generator by Abeer
#importing libraries
import random
import string
import os
#Creating the password
len_pass = int(input("Please enter the length of the password you want:- "))
def rand_char(leng):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for h in range(leng))
    return random_string
passw = rand_char(len_pass)
#Storing the password
file_path = "password.log"

with open(file_path, 'w') as file:
    file.write(str(passw))

print(f"The password has been saved in the file {file_path}")
input("Press enter to exit the program")
