# Python Program to find an alphabet in a string and show how many times it's there

str = input("Enter a string: ")
search = input("Enter alphabet you want to search: ")

if str.find(search):
    print("Found")

print("The alphabet was found ",str.count(search),"times")