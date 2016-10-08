#!usr/bin/env pyhton
# Project Euler problem 5
def gcd(a,b):
    if a > b :
        g, l = a, b
    else:
        g, l = b, a
    while l != 0:
        rem = g%l
        g, l = l, rem
    return g
def lcm(a,b):
    lcm = ((a*b)/gcd(a,b))
    return lcm
final = 1
for i in range(1,21):
    final = lcm(final,i)
print final
