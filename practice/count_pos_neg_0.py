# Write a python script to read n integers from user and display the count of +ve nos, -ve nos and 0s

print("Enter 5 values: ")
lst=[]

for i in range(5):
    value = int(input())
    lst.append(value)

print("Values Entered: " + str(lst))
lstpos = []
lstneg = []
lstzer = []

for i in lst:
    if i > 0 :
        lstpos.append(i)
    elif i < 0 :
        lstneg.append(i)
    else:
        lstzer.append(i)
    
countpos = len(lstpos)
countneg = len(lstneg)
countzer = len(lstzer)

print(lstpos)
print("Number of Positive Numbers: " + str(countpos))
print(lstneg)
print("Number of Negative Numbers: " + str(countneg))
print(lstzer)
print("Number of Zeros: " + str(countzer))
