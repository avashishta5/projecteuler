#!usr/bin/env python
# Project Euler problem 4
def ispalindrome(num):
    check = str(num)[::-1]
    if check == str(num):
        return True
    else:
        return False
pal = 0
a = 999
while a > 99:
    b = 999
    while b >= a:
        product = a * b
        if ispalindrome(product) and product > pal :
            pal = product
        b -= 1
    a -=1
print pal
