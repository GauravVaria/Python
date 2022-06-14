# gauravvaria93@gmail.com
import re
x = 'gauravvaria93@gmail.com'
email = re.search(r'^\w+\@[a-z]+\.[a-z]+$',x)
def checkemail(email):
    if email:
        print(True)
    else:
        print(False)

checkemail(email)
