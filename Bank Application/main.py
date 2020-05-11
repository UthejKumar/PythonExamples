''' "Bank Application" ~ by Uthej Kumar
A simple bank application that performs basic bank functions.
For more info checkout the "bankapplication" README.md.'''

import user_creation as user
import transaction as trans
from random import randint

print("*"*10,"_"*15,"*"*10,"WELCOME TO NUKY BANK!","*"*10,"_"*15,"*"*10,"\n")


#User creation part of the program.
print("You must create a bank account first.\n")
user_name = user.name_func()
dob = user.dob_func()
gender = user.gender_func()
address = user.address_func()
mob_no = user.phone_func()
print("\nHere is a summary of the details you gave us:")
print("Name -", user_name)
print("Date of Birth -", dob)
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

print("\nCongratulations %s your account has been successfully created!" % user_name)
acc_no = randint(100000000000, 999999999999)
print("Your account number is: %d\n" % acc_no)
acc_balance = 0
print("Your starting balance is: Rs.%.2f\n" % acc_balance)


#Taking the user's action choice and performing the corresponding action.
print("Please choose an action to perform:")
print("""1. Check Balance
2. Deposit Amount into Account
3. Withdraw Money from Account
4. Close Your Account""")
while True:
    actn_chosen = int(input(">"))
    if 1 <= actn_chosen <= 4:
        if actn_chosen == 1:
            print(trans.balance_func(acc_balance))
        if actn_chosen == 2:
            acc_balance = trans.deposit_func(acc_balance)
            print("Your updated balance is Rs.%.2f" % acc_balance)
        if actn_chosen == 3:        
            print("""WITHDRAWN AMOUNT: Rs.%.2f. 
UPDATED ACCOUNT BALANCE: Rs.%.2f\n""" % trans.withdraw_func(acc_balance))
        if actn_chosen == 4:
            print("Close account funtion")
        break
#Need to write logic where intially acc_balance is 0 and 
#so after depositing an amt it should reflect so he can withdraw amount from that account


#If there is any particular change that the user wants to make, give him an option to. (per function)