''' 1.
To count frequency of range of marks using dictionary. i.e., marks would be entered out of 100 for n number of students. 
The program should display the frequency count of the following marks range.0-39 40-60 61-80 81-100
'''
stud_num = int(input("Enter number of students: "))
list1 = []
list2 = []
list3 = []
list4 = []
marks = {"0-39": 0,
         "40-60": 0,
         "61-80": 0,
         "81-100": 0}
for i in range(stud_num):
    mark = int(input(f"Enter Mark {i+1}/{stud_num}: "))
    if mark <= 39:
        list1.append(mark)
    elif mark >= 40 and mark <= 60:
        list2.append(mark)
    elif mark >= 61 and mark <= 80:
        list3.append(mark)
    elif mark >= 81 and mark <= 100:
        list4.append(mark)
    marks.update({"0-39": len(list1),"40-60": len(list2), "61-80": len(list3), "81-100": len(list4)})
print(marks)
 