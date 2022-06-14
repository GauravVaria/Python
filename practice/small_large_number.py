# Write a python program to find the largest and smallest element from a list

lst = [10, 20, 0, 100, 5]

for i in range(4):
    if lst[i] < lst [i+1]:
        largest = lst[i+1]
        smallest = lst[i]

print("Smallest is: " + str(smallest))
print("Largest is: " + str(largest))