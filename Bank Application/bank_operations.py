''' "Bank Operations" module ~ by Uthej Kumar '''

import transaction as trans

#Taking the user's action choice and performing the corresponding bank operation.
def bank_operations(acc_balance):
    print("\nPlease choose an action to perform:")
    print("""1. Check Balance
2. Deposit Amount into Account
3. Withdraw Money from Account
4. Close Your Account
5. Exit""")
    while True:
        actn_chosen = int(input(">"))
        if 1 <= actn_chosen <= 5:
            if actn_chosen == 1:
                acc_balance = trans.balance_func(acc_balance)
                print("\nYour ACCOUNT BALANCE is: Rs.%.2f" % acc_balance)                
                bank_operations(acc_balance)
            elif actn_chosen == 2:
                acc_balance = trans.deposit_func(acc_balance)
                print("\nYour UPDATED BALANCE is Rs.%.2f" % acc_balance)
                bank_operations(acc_balance)
            elif actn_chosen == 3:    
                acc_balance = trans.withdraw_func(acc_balance)    
                print("UPDATED ACCOUNT BALANCE: Rs.%.2f" % acc_balance)
                bank_operations(acc_balance)
            elif actn_chosen == 4:
                boolean = trans.close_func()
                if boolean == True:
                    bank_operations(acc_balance)            
            elif actn_chosen == 5:
                exit()
            break

