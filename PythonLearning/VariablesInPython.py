# Variable = A Container for a value (Strings, integers, float, boolean)
#            A variables behaves as if it was the value it contains

# To use "Formated String Literals" begin a string with 'f' or 'F' before the opening Quotation mark or triple quotation mark.
#    inside this string, you can write python expression between { and } characters that can refer to variables or literals values
# print(f"hello {first_name} "). "f" = format

# **************** STRING *********************

# Strings = String is a Series/Sequence of Character.
# They can Include the number also but we treat them as a character.

print('STRINGS')
first_name = 'John'
food = 'Pizza'
email = "John@123"
print(f"hello {first_name} ")
print(f"You like {food} ")
print(f"Your E-mail is {email}")

print(" ")
# **************** INTEGERS *********************

# An Integers is an whole number
# Integers should not be in a quotes because it is not a string
print("INTEGERS")
age = 22
quantity = 3
num_students = 30

print(f"You are {age} years old")
print(f"your are buying {quantity} items")
print(f"Your class has {num_students} students")

print(" ")
# **************** FLOATS *********************

# Float means floating point numbers
# float is a number but its contain decimals portion

print(" FLOATS ")
price = 10.99
GPA = 3.2
distance = 5.5

print(f"The Price is ${price}")
print(f"Your GPA is {GPA}")
print(f"Your Ran {distance}KM")

print(" ")
# **************** BOOLEAN *********************

# Booleans is either True or Flase
# Booleans has Only 2 values True or Flase

print('BOOLEANS')

is_student = True
# is_student = False

for_sale = True
# for_sale = False

is_online = True
# is_online = False


print(f"Are You a Student? {is_student}")
# Example

if is_student:
    print("Your a Students")
else:
    print("Your not a Students")

if for_sale:
    print("This is for Sale")
else:
    print("This is not a sale thing")

if is_online:
    print("You are Online")
else:
    print('Your not Online')


print(" ")
# Question

print('Question')
user_name = "Rizwan Shaikh"
Year = 2024
pi = 3.4
is_admin = True

print(f"My name is {user_name} and i was born on the year {Year} and the value of pi is {pi} and i'm admin {is_admin}")