# tuples are immutable 
''' 
tuple1 = (0, 1, 2, 3) 
tuple1[0] = 4
print(tuple1)

Traceback (most recent call last):
  File "E:\Gaurav\College\VSC\Python\mutable.py", line 4, in <module>
    tuple1[0] = 4
TypeError: 'tuple' object does not support item assignment
'''
# strings are immutable 
  
'''message = "Welcome to GeeksforGeeks"
message[0] = 'p'
print(message)
# lists are mutable 
color = ["red", "blue", "green"]
print(color)
Traceback (most recent call last):
  File "e:\Gaurav\College\VSC\Python\mutable.py", line 15, in <module>
    message[0] = 'p'
TypeError: 'str' object does not support item assignment
'''
color = ["red", "blue", "green"]
print(color)
print(id(color))
color[0] = "pink"
color[-1] = "orange"
print(color)
print(id(color))

age = 42
print(age)
print(id(age))
age = 43
print(age)
print(id(age))
