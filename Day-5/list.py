# Question- write a program that takes names of 3 favorite food that user and stores them in a list. 
# then print the list and its length

# case 1

food1= input("enter food1: ")
food2= input("enter food 2: ")
food3= input("eneter food 3: ")

foodList= [food1, food2, food3]
print(foodList)
print(len(foodList))

# case 2

food1= input("enter food1: ")
food2= input("enter food 2: ")
food3= input("eneter food 3: ")

foodList= []
foodList.append(food1)
foodList.append(food2)
foodList.append(food3)

print(foodList)
print(len(foodList))