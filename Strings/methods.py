spam = "Hello World"

print(spam.upper())
print(spam.lower())
print(spam.title())

print(spam.isalpha(),
spam.isdecimal(),
spam.isalnum(),
spam.isspace(),
spam.startswith('Hel'),
spam.endswith('ld'))

print(','.join(['cats','rats','bats']))

print('Hello world how are you'.split('h'))

print('Hello'.rjust(10)) # Total string length is 10
print('Hello'.ljust(10,'*'))
print('Hello'.center(20,'*'))
spam = '     Hello'
print(spam.strip()) # Removes WhiteSpaces from either side
spam.lstrip()
spam.rstrip()
spam = 'SpamSpamSpamHelloSpamHelloSpamSpam'
print(spam.strip('maSp'))
print(spam.replace('Spam','Replace'))