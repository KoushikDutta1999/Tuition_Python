#Python Program to create two lists with even and odd numbers from a list

list = eval(input("Enter List Element: "))

print("list elements: ",list)

odd = []
even = []

for num in list:
	if num%2 == 0:
		even.append(num)
	else:
		odd.append(num) 

print("even elements: ", even)
print("odd elements:  ", odd)
