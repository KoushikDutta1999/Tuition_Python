# Python Program to find the duplicates in a list

list = eval(input("Enter the list: "))
print("The List: ",list)

l = []

for i in list:
    if i not in l:
        l.append(i)
    else:
        print("Duplicate number : ",i)