# Exercise 2:- Creating Shopping Cart Program

item = input("What item would you like to buy:- ")
price = float(input("What is the Price?:- "))
quantity = int(input("How many would you like:- "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s ")
print(f"your total is:- ${total}")