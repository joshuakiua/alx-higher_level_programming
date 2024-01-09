#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = int(str(number)[-1])
msg = "last digit of"
if number < 0:
    l_digit = l_digit * -1

if l_digit > 5:
    print("{} {} is {} and is greater than 5".format(msg, number, l_digit))
elif l_digit == 0:
    print("{} {} is {} and is 0".format(msg, number, l_digit))
else:
    ld = l_digit
    print("{} {} is {} and is less than 6 and not 0".format(msg, number, ld))
