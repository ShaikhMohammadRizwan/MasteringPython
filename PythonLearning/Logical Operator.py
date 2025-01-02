# Logical Operator = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both condition must be True
#                     not = inverts the condition (not False, not True)

# OR Logical Operator

# temp = 2
# is_raining = False
#
# if temp > 35 or temp < 0 or is_raining:
#     print("The event is Canceled")
# else:
#     print("The Event is Schedule")


# AND Logical Operator

temp = 300
is_sunny = True

if temp >= 35 and is_sunny:
    print(f"The Outside Temperature is {temp}")
    print(f"The Outside Sunny is Less")