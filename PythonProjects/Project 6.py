# 0. Validate user input exercise.
# 1. Username is no more 12 Characters.
# 2. username must not contain space.
# 3. username must not contain digit

username = input("Enter a Username:- ")

if len(username) > 12:
    print("Your username can't be more then 12 character")
elif not username.find(" ") == -1:
    print("your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"welcome {username}")
