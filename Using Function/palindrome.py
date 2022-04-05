# Python Program to check Pallindrome or Not using Function

def pallindrome(n):
    temp = n
    rem = 0
    while n>0:
        a = n % 10
        rem = rem * 10 + a
        n = n // 10
    if temp == rem:
        print("Palindrome")
    else: 
        print("Not palindrome")

n = int(input("Enter a number: "))

print(pallindrome(n))