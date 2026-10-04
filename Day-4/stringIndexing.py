# Question- write a program that takes your favourite food name as input and prints:
# the middle charecters
# the last 2 charecters

str= input("enter your favourite food: ")
l= len(str)

print(str[1:l-1])
print(str[l-2:l])