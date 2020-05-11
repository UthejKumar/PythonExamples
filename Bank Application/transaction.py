''' "Transaction Types" module ~ by Uthej Kumar '''

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
                pass
            if deposit_confirmation == 2:
                deposit_func
            break
    acc_balance += deposit_amt
    return acc_balance


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
                    print("Your account has insufficient funds!")
                    print("Please re-enter another amount")
                    withdraw_func(acc_balance)
                elif withdraw_amt < acc_balance:                                       
                        acc_balance -= withdraw_amt
                        print("\nTransaction Successful!\n")
                        return withdraw_amt, acc_balance                        
            if wthdrw_dcsn == 2:
                withdraw_func(acc_balance)
            break