# Python Program to print Fibonacci Series

n = int(input("Enter the term "))
n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Enter positive")
elif n == 1:
    print("Fibonacci sequence upto ",n)
    print(n1)
else:
    print("Fibonacci sqeuence: ")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1