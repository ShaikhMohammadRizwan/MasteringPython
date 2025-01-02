# String Indexing = accessing elements of a sequence using []
#                   ( indexing operator )
#                     [ start : end : step ]

credit_numb = '1234-5678-9012-1314'

# print(credit_numb[0])
# print(credit_numb[1])
# print(credit_numb[2])
# print(credit_numb[3])

print(credit_numb[0:4])

print(credit_numb[5:9])

print(credit_numb[5:])

print(credit_numb[-1])

print(credit_numb[::4])

last_digit = credit_numb[-4:]

print(f"xxxx-xxxx-xxxx-{last_digit}")

print(credit_numb[::-1])

