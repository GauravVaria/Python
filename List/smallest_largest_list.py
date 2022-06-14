# WAP to find the largest and smallest element from a list

lst = [10, 20, 4, 2, 100]

for i in range(4):
    if lst[i] > lst[i+1]:
        smallest = lst[i+1]
    if lst[i] < lst[i+1]:
        largest = lst[i+1]

print("Smallest Number is: " + str(smallest))
print("Largest Number is: " + str(largest))