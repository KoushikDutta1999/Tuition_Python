# Python Program to print Armstrong or Not using Function

def arm(n):
    temp = n
    sum = 0
    """count = 0
    while temp > 0:
        count = count +1
        temp = temp // 10
        
        temp = n
        for i in range(1,temp+1):
            rem = temp % 10
            sum = sum + (rem ** count)
            temp //+ 10
        return sum

n = int(input("Enter an number: "))

if( n == arm(n)):
    print("Armstrong")
else:
    print("Not armstrong")"""

#----------------------------------------------------------------

    while temp > 0:
        digit = temp%10
        sum += digit ** 3
        temp //= 10

n = int(input("Enter an number: "))

if( n == arm(n)):
    print("Armstrong")
else:
    print("Not armstrong")
