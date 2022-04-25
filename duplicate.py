# Python Program to move all duplicate values in a list to the end of the list.

l =eval(input('Enter a list: '))
duplicate = []
list = []

for  i in l:
    if i in duplicate:
        list.append(i)
    else:
        duplicate.append(i)
new = duplicate + list

print(new)