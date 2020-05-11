''' "Bank Application" ~ by Uthej Kumar
A simple bank application that performs basic bank functions.
For more info checkout the "bankapplication" README.md.'''

import user_creation as user


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

print("GREAT JOB UTHEJ!!")


#Display all the final details all together before submitting the details (Confirm)
#If there is any particular change that the user wants to make, give him an option to. (per function)