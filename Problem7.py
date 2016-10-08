#!usr/bin/env python
# Projet Euler Problem 7
import time
def isprime(num):
    if num > 1:
        Prime = True
        if num == 2:
            pass
        else:
            for i in range(2,int(num**0.5)+1):
                if num%i == 0:
                    Prime = False
                    break
                else:
                    pass
    else:
        Prime = False
    return Prime
c = 0
l = 0
prime_no = 0
start = time.time()
while c!=10001:
    if isprime(l):
        c += 1
        if c == 10001:
            prime_no = l
            break
    l += 1

print l
stop = time.time()
print "time elapsed:", stop - start
