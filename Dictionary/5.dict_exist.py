# Python Program to show an element key exist or not in a Dictionary

s = {}
n = int(input("Enter the number of data: "))

for i in range(0,n):
    key = input("ENter the key: ")
    value = input("ENter the value: ")
    s[key]=value
print(s)

n = input("Enter the element you want to find: ")

for i in s.keys():
    if i == n:
        print("Element exist")
    else:
        print("Element dosenot exist")