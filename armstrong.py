# Python Program to find a number is armstrong or not

num = int(input("Enter a number"))

sum = 0

temp=num
while temp > 0:
    digit = temp%10
    sum += digit ** 3
    temp //=10
    
if num == sum:
    print("This is an Armstrong Number")
else:
    print("This is Not an Armstrong Number")