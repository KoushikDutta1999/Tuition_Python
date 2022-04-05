# Python Program to find the sum of digits of a number until its a single digit number (O/P -> 129 -> 3)

n = int(input("Enter number: "))

sum = 0

while n > 0 or sum >=10:
    if n == 0:
        print(sum)
        n = sum
        sum = 0
    sum += n % 10
    n //= 10
    
print(sum)