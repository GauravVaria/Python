lst = [1, 5, 1]  # False
lst2 = [1, 5, -2, 8, 3]  # True
lst3 = [-2, 1, 5, 2, 8, 3]  # True
ch = []

def accordian(l):
    l_length = len(l)
    for i in range(0, l_length - 2):
        difference1 = abs(l[i+1] - l[i])
        difference2 = abs(l[i + 2] - l[i + 1])
        if difference1 < difference2:
            flag = 1
        elif difference1 == difference2:
            flag = 2
        else:
            flag = 0
            ch.append(flag)
    for k in range(len(ch)-1):
        if k == 2:
            break
        if ch[0] == ch[1]:
            return False
        else:
            return True
print(accordian(lst))
print(accordian(lst2))
print(accordian(lst3))