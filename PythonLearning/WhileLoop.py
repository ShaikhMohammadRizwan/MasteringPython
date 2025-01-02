# While Loop = execute some code WHILE some condition remains true

# name = input("Enter a Name")
#
# if name == '':
#     print("You did not submitted")
# else:
#     print(f"Hello {name}")

# name = input("Enter the Name:- ")
#
# while name == '':
#     print("You Didn't Submitted the Name")
#     name = input("Enter the Name:- ")
# print(f"Hello {name}")

# age = int(input("Enter the age:- "))
#
# while age < 0 :
#     print("You can't add negative number")
#     age = int(input("Enter the age:- "))
#
# print(F"you are {age} years old")

# WHile Loop using Logical Operator

# food = input("Enter a Food you like (q to quite):- ")
#
# while not food == 'q':
#     print(f"you like {food}")
#     food = input("Enter a Food you like (q to quite):- ")
# print('bye')

# While loop using OR

num = int(input("Enter a number between 1 - 10:- "))

while num < 1 or num > 10 :
    print(f'{num} is not valid')
    num = int(input("Enter a number between 1 - 10:- "))

print(f'your number is {num}')