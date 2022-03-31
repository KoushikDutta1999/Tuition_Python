from heapq import merge


# Python Program to merge two Dictionaries

s1 = {}
n = int(input("Enter the number of values: "))

for i in range(0,n):
    key = input("Enter the key: ")
    value = input("ENter the value: ")
    s1[key]=value
print(s1)

s2 = {}
n = int(input("Enter the number of values: "))

for i in range(0,n):
    key = input("Enter the key: ")
    value = input("ENter the value: ")
    s2[key]=value
print(s2)

s2.update(s1)

print(s2)