#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = int(str(number)[-1])

if number < 0:
    l_digit = l_digit * -1

if l_digit > 5:
    msg = "and is greater than 5"
    print("Last digit of {} is {} {}".format(number, l_digit, msg))
elif l_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, l_digit))
else:
    msg = "and is less than 6 and not 0"
    print("Last digit of {} is {} {}".format(number, l_digit, msg))
