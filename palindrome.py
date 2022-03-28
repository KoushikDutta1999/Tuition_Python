# Python Program to find a number is Palindrome or not

num = int(input("ENter a number: "))

temp = num

rev = 0

while(num > 0):
    digit = num%10
    rev = rev*10+digit
    num = num//10
if(temp == rev):
    print("This is a Palindrome Number")
else:
    print("This is Not a Palindrome Number")