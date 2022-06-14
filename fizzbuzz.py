# WAP which iterates integers from 1 to 50. For multiples of three print 'Fuzz' and for multiples of 5 print 'Buzz'
# for multiples of both print "FizzBuzz" using while loop.

i = 1
while i < 50:

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        i = i + 1

    elif i % 3 == 0:
        print("Fuzz")
        i = i + 1

    elif i % 5 == 0:
        print("Buzz")
        i = i + 1

    print(i)
    i = i + 1
