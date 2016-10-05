#!usr/bin/env python
# Project Euler problem 2
a, b = 0, 1
fib_list = []
sum_fib = 0
while a <= 4000000:
    a, b = b, a+b
    fib_list.append(a)
for i in fib_list:
    if i%2 == 0:
        sum_fib += i
print sum_fib
