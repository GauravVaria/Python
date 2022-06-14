import re
phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
mo = phoneNumRegex.search('hello my number is 123-123-123, 9819-230-384 and 1234-567-890')
print(mo.group()) 
print(phoneNumRegex.findall('9819-230-384 and 1234-567-890')) # Find every occurence of pattern