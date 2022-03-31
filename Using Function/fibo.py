def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))
nth_term = int(input("Enter the nth term: "))

if nth_term <= 0:
    print("positive number")
else:
    for i in range(nth_term):
        print(fibo(i),end=" ")