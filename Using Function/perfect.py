def perfectnum(n):
    sum = 0
    for x in range(1,n):
        if n % x == 0:
            sum += x
    return sum == n

n = int(input("ENter a number: "))
print(perfectnum(n))