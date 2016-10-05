#!usr/bin/env python
# Project Euler problem 3
import math
def prime_check(num):
    if num > 1:
        Prime = True
        if num == 2:
            pass
        else:
            for i in range(2,num):
                if num%i == 0:
                    Prime = False
                    break
                else:
                    pass
    else:
        Prime = False
    return Prime
prime_factor_list = []
num = 600851475143
for i in range(1,int(math.sqrt(num))+1):
    if num%i == 0:
        if prime_check(i):
            prime_factor_list.append(i)
print prime_factor_list[-1]
