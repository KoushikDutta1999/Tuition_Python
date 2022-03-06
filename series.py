# x + x^2/2 + x^3/3 + ........ x^n/n

n = int(input("Enter the number of terms: "))
x = int(input("Enter the value: "))
sum = 0

for i in range (1, n+1):
    p = pow(x,i)
    sum = sum+(p/i)
    
print(sum)