# Python Program to find the number of occurrences of item 50 from a tuple

tuple = (11,20,3,50,100,50,150,55)
print("Tuple: ",tuple)

occur = int(input("Enter the number you want to count: "))

count = tuple.count(occur)
print("Occurrence: ",count)