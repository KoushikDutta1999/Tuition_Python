# Python Program to Remove an element from a list

list = eval(input("Enter the list: "))
print("The List: ",list)

rem = int(input("Enter the element to remove: "))

for i in list:
    if i == rem:
        l = list.remove(i)
print("List after remove: ",list)