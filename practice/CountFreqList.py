# Write a Python function CountFreqList(l) that takes as input a list of integers and returns a pair of the form (minfreqlist,maxfreqlist) 
# where minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order ,
# maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending
lst1 = [10, 20, 20, 30, 30, 30, 40, 40, 50, 50, 50, 50] # 10:1 20:2 30:3 40:2 50:5 
def CountFreqList(l):
    for i in l:
        count = l.count(i)
        

    tup1 = (minfreqlist,maxfreqlist)
    return tup1

CountFreqList(lst1)
