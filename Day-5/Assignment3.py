# question- write program to check grade based on marks (A/B/C/D) using if-elif-else.

mark= int(input("Enter your marks: "))

if(mark >= 90):
    print("you got: A")
elif(mark >= 80):
    print("you got: B")
elif(mark >= 70):
    print("You got: C")
else:
    print("Sorry yoy can not pass....Fail :(")