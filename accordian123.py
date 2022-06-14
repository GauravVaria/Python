'''
Write a function accordian(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements 
alternates between increasing strictly and decreasing strictly.

Here are some examples of how your function should work.

  >>> accordian([1,5,1])
  False
Explanation: Differences between adjacent elements are 5-1 = 4, 5-1 = 4, which are equal.

  >>> accordian([1,5,2,8,3])
  True
Explanation: Differences between adjacent elements are 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-3 = 5, so the differences decrease, increase and then decrease.

  >>> accordian([-2,1,5,2,8,3]) 
  True
Explanation: Differences between adjacent elements are 1-(-2) = 3, 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-3 = 5, so the differences increase, decrease, increase and then decrease.

  >>> accordian([1,5,2,8,1])
  False
Explanation: Differences between adjacent elements are 1-(-2) = 3, 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-1 = 7, so the differences increase, decrease, increase and then increase again.
'''
lst = [1,5,1]
lst2 = [1,5,2,8,3]
lst3 = [-2,1,5,2,8,3]
lst4 = [1,5,2,8,1]

def accordian(lst):
    flag = 0
    for i in range(1,(len(lst)-3), 2):
        difference1 = abs(lst[i-1] - lst[i])
        difference2 = abs(lst[i] - lst[i+1])
        if difference1 > difference2:
            flag = 1
        else:
            flag = 0
    if flag == 1:
        print(True)
    elif flag == 0:
        print(False)
accordian(lst)
accordian(lst2)
accordian(lst3)
accordian(lst4)    