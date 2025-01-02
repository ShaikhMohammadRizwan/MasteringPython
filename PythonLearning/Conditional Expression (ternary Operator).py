# Conditional Expression = A one-line Shortcuts for the if-statements (ternary operator)
#                             print or assign one of two values based on a condition
#                             x if condition else y


num = 5

a = 5
b = 6

age = 22
# age = 2

temp = 30
# temp = 37

user_role = 'ADMIN'
# user_role = 'John'

print('Positive' if num  > 0 else "negative")
result = 'EVEN' if num % 2 == 0 else 'ODD'
print(result)

max_num = a if a > b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

status = 'ADULT' if age >= 18 else "Your Adult"
print(status)

weather = 'HOT' if temp > 50 else "Cold"
print(weather)

access_level = 'Full Access' if user_role == 'ADMIN' else 'Not Access'
print(access_level)