# Question- write a python program that takes a numbers as input and prints
# "Positve" if number > 0
# "zero" if number == 0
# "negative" if number < 0

num= int(input("Enter a number: "))

if(num > 0):
    print("your number is positive")
elif(num == 0):
    print("your number is zero")
elif(num < 0):
    print("your number is negative")
else:
    print("please enter a valid number")
