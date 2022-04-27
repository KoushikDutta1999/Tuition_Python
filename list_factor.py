# Python Program to Find the factor of a number and store those in a List

n = int(input("Enter a number to find factor: "))

list=[]
flag = False

for i in range(1,n+1):
    if n % i == 0:
        list.append(i)
print(list)

for i in list:
        for j in range(2,i):
            if(i % j) == 0:
                flag = False
                break
            if flag == True:
                print(i,"is prime")
            else:
                print(i,"is not prime")