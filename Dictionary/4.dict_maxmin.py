# Python Program to show a maximum and minumum values in a Dictionary

dict = {'x': 100, 'y': 200, 'z':300}

for i in dict:
    ma=max(dict.values())
    mi=min(dict.values())
print(ma,mi)