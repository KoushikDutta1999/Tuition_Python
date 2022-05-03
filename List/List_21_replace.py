# Python Program to enter a list containing numbers between 1 anad 12, then replace all of the entries in the list that are greater than 10 with 10

list = eval(input("Enter a list containing numbers between 1 and 12: "))

for i in range(len(list)):
    if list[i] > 10:
        list[i] = 10

print("New List:; ",list)