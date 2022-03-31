def prime(n1):
    if(n1==1):
        return "not prime"
    elif(n1==2):
        return "prime"
    else:
        for x in range(2,n1):
            if(n1 % x == 0):
                return "not prime"
        return "Prime"

print(prime(9))