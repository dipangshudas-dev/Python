# Question- Write A program that takes total bill amount and number of friends as input
# Calculate how much each person will pay
# also print the data type of each veriable used

totalBill = float(input("Total Bill: "))
totalFriends = int(input("Total: "))

print("Each will pay:" , totalBill/totalFriends)
print(type(totalBill))
print(type(totalFriends))