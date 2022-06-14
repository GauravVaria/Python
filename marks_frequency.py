# WAP which calculates the frequency of students or the given range o marks i.e. for the marks entered for 20 students out of 100 in for loop

'''
A] 0-39 =
B] 40-59 =
C] 60-69 =
D] 70-89 =
E] 90-100 =
'''

a = b = c = d = e = 0

marks = [34,8,10,47,23,49,94,12,17,36,42,60,98,18,26,19,50,96,24,11]

for i in marks:
    if i >= 0 and i <= 39:
        a = a + 1
    elif i >= 40 and i <= 59:
        b = b + 1
    elif i >= 60 and i <= 69:
        c = c + 1
    elif i >= 70 and i <= 89:
        d = d + 1
    elif i >= 90 and i <= 100:
        e = e + 1

print(a, b, c, d, e, sep = ', ')