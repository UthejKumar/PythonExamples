''' "Bank Application" ~ by Uthej Kumar
A simple bank application that performs basic bank operations.
For more info checkout the "bankapplication" README.txt.'''

import user_creation as user
import transaction as trans
import bank_operations as bo
from random import randint

print("*"*10,"_"*15,"*"*10,"WELCOME TO VERTIGO BANK!","*"*10,"_"*15,"*"*10,"\n")


#User creation part of the program.
print("You must create a bank account first.\n")
user_name = user.name_func()
dob = user.dob_func()
gender = user.gender_func()
address = user.address_func()
mob_no = user.phone_func()
print("\nHere is a summary of the details you gave us:")
print("Name -", user_name)
print("Date Of Birth -", dob)
print("Gender -", gender)
print("Address -", address)
print("Contact No -", mob_no)
print("""\n1. PROCEED
2. EXIT""")
while True:
    user_choice = int(input(">"))
    if 1 <= user_choice <= 2:
        if user_choice == 1:
            pass
        elif user_choice == 2:
            exit()
        break


#Creates an account and gives the user an ACCOUNT NO.
print("\nCongratulations %s your account has been SUCCESSFULLY CREATED!" % user_name)
acc_no = randint(100000000000, 999999999999)
print("Your account number is: %d\n" % acc_no)
acc_balance = 0
print("Your starting balance is: Rs.%.2f" % acc_balance)
bo.bank_operations(acc_balance)
