''' "Bank Application" ~ by Uthej Kumar
    A simple bank application that performs basic bank functions.
    For more info checkout the "bankapplication" README.md.'''

#Segregate each operation into a different module
#create a separate module for user 
#import it here by calling the respective functions of the module

print("*"*10,"_"*15,"*"*10,"WELCOME TO NUKY BANK!","*"*10,"_"*15,"*"*10,"\n")


print("You must create a bank account first.\n")
print("First enter your full name.")
user_name = input(">")


print("\nPlease confirm your name:")
print('"%s"' % user_name)
print("""1. Correct
2. Incorrect""")
while True:
    verification = int(input(">"))
    if 1<= verification <= 2:
        break


if verification == 1:
    pass
elif verification == 2:
    print("\nPlease enter your name again. This is your final attempt!")
    user_name = input(">")
    print('\nYour name is "%s", you cannot change your name again!' % user_name)


#take DOB and check age > 18

#gender
print("""Please select your gender:
M - Male
F - Female
O - Other""")
gender_input = (input(">")

if gender_input == "M":
    gender = "Male"



#city, state, country
print("\nPlease enter the following details:")
city = input("Enter CITY: ")
state = input("Enter STATE: ")
country = input("Enter COUNTRY: ")

print("\nAddress - %s,%s,%s." % (city, state, country))

#phone number (must be 10 digits)

#function to confirm all the above details are correct otherwise make changes 
#(create funcitons for each field.)