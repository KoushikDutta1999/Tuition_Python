# Python Program to print the sum of Sine Seres Expansion
#sin(x) = x+x^3/3!+x^5/5!+x^7/7!+x^9/9!.............n

from math import factorial

def sin(x,n):
    sinx=0
    for i in range(n):
        s=(-1)**i
        p=22/7
        y=x*(p/180)
        sinx=sinx+((y**(2*i+1))/factorial(2*i+1))*s
    return sinx

x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n(term): "))

print("sin(",x,") =",sin(x,n))