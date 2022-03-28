# Python Program to find the second largest number in a list

list = eval(input("Enter the List: "))

print("The List: ",list)

list.sort()

print("The Second largest number in a list is: ",list[-2])