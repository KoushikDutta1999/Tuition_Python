# Python Program to read two lists num and denum which contain the numerators and denominators 
# of same fractions at the respective indexes. Then display the smallest fraction along with its index.

num = eval(input("Enter num list: "))
denum = eval(input("Enter denum list: "))

small = 0
index = 0

for i in range(len(num)):
    fraction = num[i] / denum[i]
    if fraction < small:
        index = i

frac = num[index], "/" ,denum[index]

print("Smallest Fraction = ",frac)
print("Smallest Fraction index: ",index)