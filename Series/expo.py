# Python Program to print the sum of Exponential Seres Expansion
# 1+x/1!+x/2!+x/3!+x/4!..............n

from math import factorial

x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n(term): "))
sum = 0

for i in range(0,n):
    sum+=pow(x,i)/factorial(i)
    
print(sum)