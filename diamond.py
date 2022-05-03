# Python Program to Print Diamond Pattern

row = int(input("Enter number of row: "))
half = row//2+1
space=row-2

for i in range(1, half+1):
    for j in range(1,space-2):
        print("", end=" ")
    for j in range(1,i+1):
        print("*", end=" ")
    print()
    space-=1

space=1
h=row//2
for i in range(h,0, -1):
    for j in range(1,space+1):
        print("", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()
    space+=1