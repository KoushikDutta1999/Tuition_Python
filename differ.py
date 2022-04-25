# Python Program to compare two equal sized lists and print the first index where they differ.

list1 = eval(input("Enter 1st list: "))
list2 = eval(input("Enter 2nd list: "))

for i in range(len(list1)):
    if list1[i] != list2[i]:
        print("Lists differ at index: ",i)
        break;
else:
    print("List is equal.")