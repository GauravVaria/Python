# https://www.sbmp.ac.in
import re
x = 'https://www.sbmp.ac.in'
y = 'www.gaurav.com'
z = 'varia.co.in'
url = re.search(r'^([a-z]+://)?([w]{3}.)?[\w.]+.[a-z]{2,}$',x)
def checkurl(url):
    if url:
        print('Valid URL')
    else:
        print('Invalid URL')

checkurl(x)
checkurl(y)
checkurl(z)
