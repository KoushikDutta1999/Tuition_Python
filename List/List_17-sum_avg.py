# Python Program to print the sum and average of a list

list = eval(input("ENter the list: "))

print("The List: ",list)

sum = 0

for i in list:
    sum = sum +i
    avg = sum/len(list)
    
print("Sum: ",sum)
print("Avg: ",avg)