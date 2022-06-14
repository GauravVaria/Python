'''
2. Write a Python program to create a dictionary of character as a key and frequency as a value
from a given string. Sample string: 'awesome!!! Expected output: {'a': 1, 'w': 1, 'e': 2, 's': 1, 'o': 1, 'm': 1,!: 3}
'''

dictcount = {}
str1 = input("Enter a string: ")
for i in str1:
    val = str1.count(i)
    dictcount.setdefault(i, val)

print(dictcount)