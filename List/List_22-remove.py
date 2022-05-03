# Python Program to enter a list of strings then create a new list that consists of those strings with their first characters removed.

list = eval(input("Enter list of strings: "))

newlist = []

for i in range(len(list)):
    newlist.append(list[i][1:])

print("New List: ",newlist)