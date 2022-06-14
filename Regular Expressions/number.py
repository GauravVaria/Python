import re
num = '9819230384'
def check(number):
    valid = re.search(r'^((\+)?91(\s?))?(\s)?(\d{10})$', number)
    if valid:
        print(True)
    else:
        print(False)
check(num)