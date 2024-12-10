***** What is String Concatination *****

+ sysmbol ka use hota hai String ko concatinate karana or Addition karana
jab dono side Number milte hai to wo addition karata hai
jab dono side String milte hai to wo Concatinate karata hai

ek trfh agar app string or ek trf nummber likh die to error dega

******************************


a = "hello"
b = "World"

print(a+b)
# helloWorld

print(a +" "+b)
# hello World

c = 20
print(c+30)
# 50

**** Error Case ****
print(a + c)

Output
#  TypeError: can only concatenate str (not "int") to str