# Python Program to Replace an element from a list if found

list = eval(input("Enter the List: "))
print("The List: ",list)

rep = int(input("Enter the element to find: "))

for i in list:
    if i == rep:
        rem = int(input("Enter the number to replace: "))
        list[i] = rem
print(list)