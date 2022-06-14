# Write a function that takes a single int as input and returns sum of integers from 0 to input parameter

def sum(n):
    sum1 = 0
    for i in range(n+1):
        sum1 += i
    return sum1

abc = sum(10)
print(abc)