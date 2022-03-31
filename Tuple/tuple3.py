tup = eval(input("Enter List of Tuple: "))

list = list(tup)

for i in list:
    list.remove(i)
    i = i+2
t = tuple(list)


print(t)