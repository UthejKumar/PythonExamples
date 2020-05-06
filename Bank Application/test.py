print("Please enter your full name.")
full_name = input(">")
users_list = []
users_list.append(full_name)

num_of_users = len(users_list)

'''for name in full_name:
    if name == "Uthej":
        print(True)
    else:
        print(False)'''

print(users_list)

print("Number of current users are:",num_of_users)