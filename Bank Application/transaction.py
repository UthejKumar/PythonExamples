''' "Transaction Types" module ~ by Uthej Kumar '''

import bank_operations as bo

#Function to check the user's account balance.
def balance_func(acc_balance):
    return acc_balance


#Function to deposit amount into bank account.
def deposit_func(acc_balance):
    print("\nHow much amount would you like to deposit into your account?")
    deposit_amt = int(input(">"))
    print("""\nYou have chosen to deposit Rs.%.2f into your account.
Please CONFIRM:
1. Yes
2. No""" % deposit_amt)
    while True:
        deposit_confirmation = int(input(">"))
        if 1 <= deposit_confirmation <= 2:
            if deposit_confirmation == 1:
                acc_balance += deposit_amt
                return acc_balance
            elif deposit_confirmation == 2:
                deposit_func(acc_balance)  #Check why this is not working!              
            break


#Function to withdraw amount from account.
def withdraw_func(acc_balance):
    print("\nEnter amount to withdraw:")
    withdraw_amt = int(input(">"))
    print("""\nAre you sure you want to withdraw Rs.%.2f from your account?
1. Yes
2. No""" % withdraw_amt)
    while True:
        wthdrw_dcsn = int(input(">"))
        if 1 <= wthdrw_dcsn <= 2:
            if wthdrw_dcsn == 1:
                if withdraw_amt > acc_balance:
                    print("\nYour account has insufficient funds!")
                    print("Your ACCOUNT BALANCE is: Rs.%.2f" % acc_balance)
                    print("""1. Re-enter another amount
2. Go back.""")
                    while True:
                        insufficient_dcsn = int(input(">"))
                        if 1 <= insufficient_dcsn <= 2:
                            if insufficient_dcsn == 1:
                                withdraw_func(acc_balance)
                            elif insufficient_dcsn == 2:                                                                
                                bo.bank_operations(acc_balance)
                            break
                elif withdraw_amt < acc_balance:                                       
                        acc_balance -= withdraw_amt
                        print("\nTRANSACTION SUCCESSFUL!\n")
                        print("WITHDRAWN AMOUNT: Rs.%.2f" % withdraw_amt) 
                        return acc_balance                        
            if wthdrw_dcsn == 2:
                withdraw_func(acc_balance)
            break


#Closing an exisitng user's account.
def close_func():
    print("""\nAre you sure you want to TERMINATE YOUR ACCOUNT?
1. YES
2. NO""")
    while True:
        close_dcsn = int(input(">"))
        if 1 <= close_dcsn <= 2:
            if close_dcsn == 1:
                print("\nThanks for being one of our MOST VALUABLE MEMBERS!\n")
                exit()
            elif close_dcsn == 2:
                print("\nGood decison! How can we help you?")
                return True
            break
                