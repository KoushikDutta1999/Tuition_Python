# Python Program to find a number is Perfect or not

n = int(input("ENter a number: "))

sum = 0

for i in range(1, n):
    if(n%i == 0):
        sum = sum+i
if(sum == n):
    print("This is a Perfect Number")
else:
    print("This is Not a Perfect Number")