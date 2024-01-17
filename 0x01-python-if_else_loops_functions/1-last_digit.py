#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    lst_nmbr = number % 10
else:
    lst_nmbr = number % -10

print(f'Last digit of {number} is {lst_nmbr}', end=' ')

if lst_nmbr > 5:
    print("and is greater than 5")
elif lst_nmbr == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
