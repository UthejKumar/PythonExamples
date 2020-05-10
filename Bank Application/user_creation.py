''' "New User Creation" module ~ by Uthej Kumar '''

import dob

print("You must create a bank account first.\n")


#Function to get user's name.
def name_func():
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


#DOB function and checking legal age to open bank account.
def dob_func():
    print("\nEnter your date of birth.")
    date_of_birth = dob.main()
    print("Your DOB is:",date_of_birth) 
    #Add validation > 18.


#Function to get user's gender.
def gender_func():
    print("""\nPlease select your gender:
    M - Male
    F - Female
    O - Other""")
    while True:
        gender_input = (input(">"))
        if gender_input == "M" or gender_input == "m":
            gender = "Male"
            break
        elif gender_input == "F" or gender_input == "f":
            gender = "Female"
            break
        elif gender_input == "O" or gender_input == "o":
            gender = "Other"
            break
    print("Your gender is:", gender)


#Function to get user's address.
def address_func():
    print("\nPlease enter the following details:")
    city = input("Enter CITY: ")
    state = input("Enter STATE: ")
    pin_code = int(input("Enter your PINCODE: "))
    country = input("Enter COUNTRY: ")

    print("\nYour address - %s, %s, %s - %d." % (city, state, country, pin_code))


#Function to get user's contact number.
def phone():
    print ("\nPlease enter your MOBILE NUMBER.")
    while True:
        mob_no = int(input(">"))
        if 1000000000 <= mob_no <= 9999999999:  #To check if mobile number given is valid.
            break
        else:
            print("Please enter a valid mobile number!")   
    print("\nPlease confirm your contact number:", mob_no)
    print("""1. Confirm
2. Change Mobile Number""")
    while True:
        confirm = int(input(">"))
        if 1 <= confirm <= 2:
            if confirm == 1:
                pass
            if confirm == 2:
                phone()
        else:
            print("Please select only the given options. (1/2)")


#Function for email services. (Optional)

phone()