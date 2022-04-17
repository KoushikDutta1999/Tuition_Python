#Python Program to print the reverse of the string and Check if string is palindrome or not

str = input("Enter a string: ")

rev = str[::-1]

print("Reverse of the string is: ",rev)

if str == rev:
    print("Palindrome")
else:
    print("Not palindrome")