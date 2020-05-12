=================================="BANK APPLICATION GUIDE"==================================

The USER can perform basic bank application operations like:
    
    1. Creating a bank account for a new customer.  
    2. Depositing amount into an account.
    3. Withdrawing amount from an account.
    4. Checking the balance of an account.
    5. Closing an existing customer's bank account.


Python Modules Hierarchy:

main.py (Run this file)
    |____1.user_creation.py
                |____1.1dob.py (import)
    |____2.transaction.py
                |____2.1bank_operations.py (import)
    |____3.bank_operations.py
                |____3.1transaction.py (import)
    |____4.randint (Default python module)


Run only the "main.py" file.
*   To get started, the user must create a bank account
    every time they run the program.

*   Once the user is finished creating a bank account, 
    the user will get prompted to choose an operation 
    that they would like to perform.

*   The user can choose from the given list of options 
    to carry out an operation of their choice.
