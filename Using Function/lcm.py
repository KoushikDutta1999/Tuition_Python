def lcm(x,y):
    if x > y:
        p = x
    else:
        p = y
    
    while(1):
        if((p % x == 0) and (p % y == 0)):
            lcm = p
            break
        p += 1
    return lcm


print(lcm(5, 10))