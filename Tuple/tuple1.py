tup = eval(input("ENter List of Tuple: "))

list = list(tup)

l = []

for i in list:
    if i not in l:
        l.append(i)
t = tuple(l)
print("Tuple after removing duplicate: ",t)