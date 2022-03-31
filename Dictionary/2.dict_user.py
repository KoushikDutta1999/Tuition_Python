# Python Program to show a Dictionary user input

s = {}
n = int(input("ENter the number of values: "))

for i in range(0,n):
    key = input("ENter the key: ")
    value = input("ENter the value: ")
    s[key]=value
print(s)