tup = eval(input("Enter List of Tuple: "))

list = list(tup)

del list[::2]
t = tuple(list)

'''for i in list:
    list.remove(i)
    i = i+2
t = tuple(list)
'''

print(t)