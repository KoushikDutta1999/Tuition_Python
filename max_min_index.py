# Python Program to display the maximum and minimum values from the specified range of indexes of list.

list = eval(input("ENter the list: "))
start = int(input("Enter the start: "))
end = int(input("Enter the end: "))

maximum = max(list[start:end])
minimun = min(list[start:end])

print("Max: ",maximum)
print("Min: ",minimun)